"""
made by el,

fell free to modify it and share

todo all types
todo containers
todo remove game language
todo add test
todo add examples

"""

from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR
from threading import Thread
import socketEvents.types as _Type


class Event:
    def __init__(self, conn, name, **kargs):
        """the object that holds event data"""
        self.conn = conn
        self.event_name = name

        for i, j in kargs.items():
            self.__setattr__(i, j)

    def __repr__(self):
        return "<Event: " + ", ".join([i + "=" + str(j) for i, j in self.__dict__.items()]) + ">"


class Connection:
    def __init__(self, conn, addr, auth=False):
        self.conn = conn
        self.addr = addr
        self.auth = auth

    def __repr__(self):
        return "<Connection " + str(self.addr) +">"

    def send(self):
        pass


class Structure:
    def __init__(self, name, **kargs):
        """defines the possible events,
        where the key is the event attribute and the argument is the event type.
        the argument must be a builtin type, a type from socketEvents.type, or a custom type that can be serialized
        """
        self._ID = None
        self.name = name
        self._format = [_Type.UInt2Type]
        self._keys = []
        self._size = 0
        self._sizes = [2]

        size = True
        for i in sorted(kargs.keys()):
            item = kargs[i]
            if _Type.TypeBace not in item.__bases__:

                if item not in _Type.alias:
                    raise Exception("type not supported", i)
                item = _Type.alias[item]

            if item.len and size:
                self._size += item.len
            else:
                size = False

            self._sizes.append(item.len)

            self._format.append(item)
            self._keys.append(i)


class Client:
    def __init__(self, *args):
        """the class to send and receive data from a server
        the args must be "Structure"s defining the event types
        """
        self.ip = 'localhost'
        self.port = 5555
        self._socket = None

        for i, j in enumerate(args):
            j._ID = i

        self.__struct_size = [i._size for i in args]
        self.__struct = args

        self.__len = len(self.__struct)
        self.__run = True
        self.__events = []
        self.self = None

    def start(self):
        """try to connect to the server
        returns true if successfully connected
        """
        if self._socket:
            self._socket.close()
        try:
            self._socket = socket(AF_INET, SOCK_STREAM)
            self._socket.connect((self.ip, self.port))

        except ConnectionRefusedError:
            return False
        self.__run = True
        self.self = Connection(self._socket, None)
        Thread(target=self._conn_thread, args=(self._socket, self.self)).start()
        return True

    def stop(self):
        """stop the connection"""
        self.__len = False

    def send(self, type, **kargs):
        """send the event "type" to the server.
        'type' must be a Structure.
        and the data must be given where the key is the event attribute and the argument is the data to be sent

        return false if no connection is established
        """
        data = bytes()
        data += type._format[0].to_bytes(type._ID)
        for i, j in zip(type._format[1:], type._keys):
            data += i.to_bytes(kargs[j])
        try:
            self._socket.send(data)
        except BrokenPipeError:
            self.__events.insert(0, Event(self.self, "quit", why="unknown"))
            return False
        return True

    def events(self):
        """a generator that returns the received events"""
        while self.__events:
            yield self.__events.pop()

    def add_event(self, event):
        """push an event to the event loop"""
        if type(event) is Event:
            self.__events.insert(0, event)
        else:
            raise Exception(type(event), "is not Event")


    def _conn_thread(self, conn, player):
        """the thread that gets the data from the server and adds its it to the event loop"""

        data = bytes()
        while self.__run:
            try:
                data = data + conn.recv(2048)  # get update

            except ConnectionResetError:
                self.__events.insert(0, Event(player, "quit", why="socket fail"))
                return

            if not data:
                self.__events.insert(0, Event(player, "quit", why="user closed"))
                return

            while len(data) >= 2:
                event_id = _Type.UInt2Type.from_bytes(data[0:2])
                if event_id < self.__len:
                    event_struct = self.__struct[event_id]

                    l = len(data)
                    offset = 0
                    for i in event_struct._sizes:
                        if i:
                            offset += i
                        else:
                            if offset+3 > l:
                                break
                            offset += _Type.UInt2Type.from_bytes(data[offset:offset+2]) + 2
                        if offset > l:
                            break
                    else:
                        event, data = data[:offset], data[offset:]
                        args = []
                        for i, j in zip(event_struct._sizes, event_struct._format):
                            if not i:
                                h = _Type.UInt2Type.from_bytes(event[:2])
                                event = event[2:]
                                args.append(j.from_bytes(event[:h]))
                                event = event[h:]
                            else:
                                args.append(j.from_bytes(event[:i]))
                                event = event[i:]

                        d = {}
                        for i, j in zip(event_struct._keys, args[1:]):
                            d[i] = j

                        self.__events.insert(0, Event(player, event_struct.name, **d))



                else:
                    self.__events.insert(0, Event(player, "quit", why="bad packet"))
                    #print(data, " bad pack")
                    return
                    #  raise Exception("invalid packet id", num)

class Server(Client):
    def __init__(self, *args):
        """
        the class for creating a server confection that clients can connect to
        """
        Client.__init__(self, *args)
        self.conns = []
        with socket(AF_INET, SOCK_DGRAM) as s: # todo stop annoying google
            s.connect(('google.com', 80))
            self.ip = s.getsockname()[0]
    def send(self):
        pass # todo add

    def send_to(self, type, to, **kargs):
        """send data to a specific client
        send the event "type" to the server.
        to must be the client, you can get this from event.player
        type must be a Structure.
        and the data must be given where the key is the event attribute and the argument is the data to be sent
        """
        data = bytes()
        data += type._format[0].to_bytes(type._ID)
        for i, j in zip(type._format[1:], type._keys):
            data += i.to_bytes(kargs[j])

        to.conn.send(data)

    def start(self):
        """start the server"""
        self._socket = socket(AF_INET, SOCK_STREAM)
        self._socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self._socket.bind((self.ip, self.port))
        self._socket.listen()

        self.__run = True

        Thread(target=self.__join_loop).start()

    def __join_loop(self):
        """look for clients to join"""
        while self.__run:
            conn, addr = self._socket.accept()
            player = Connection(conn, addr)
            #self.conns[addr[1]] = conn
            self.conns.append(player)
            self.add_event(Event(player, "join"))
            Thread(target=self._conn_thread, args=(conn, player)).start()

    def kick(self, player):
        """close the confection from player"""
        player.conn.close()
        self.conns.remove(player)
        pass

    def ban(self, player):
        """close the confection from player and block them from joining again,
        if authorisation is not set up players may be abel to join again """
        self.kick(player) # todo add auth
        pass
