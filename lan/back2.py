from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR
from threading import Thread
from struct import pack, unpack, calcsize

CHAR = 0
BYTE = 1
UBYTE = 2
SHORT = 3
USHORT = 4
INT = 5
UINT = 6
LONG = 7
ULONG = 8
LONGLONG = 9
ULONGLONG = 10

Id = [(CHAR, "c"),
      (int, "q"),
      (float, "f"),
      (bool, "?"),
      (str, "{}B"),
      (),
      (),
      (),
      (),
      (),
      (),
      (),
      (),
      ()]
ID = {
        CHAR: "c",
        BYTE: "b",
        UBYTE: "B",
        bool: "?",
        SHORT: "h",
        USHORT: "H",
        INT: "i",
        UINT: "I",
        LONG: "l",
        ULONG: "L",
        LONGLONG: "q",
        int: "q",
        ULONGLONG: "Q",
        float: "f",
        str: "{}B"

    }

class TypeBace:
    def __init__(self):
        self.__len = 0

    def to_bytes(self, x):
        raise Exception("must impalement 'to_bytes'")

    def from_bytes(self, x):
        raise Exception("must impalement 'from_bytes'")



class IntType(TypeBace):
    def __init__(self):
        self.__len = 8
        self.__children = []

    def to_bytes(self, x):
        if x is int:
            return int.to_bytes(self.__len, signed=True)
        else:
            raise Exception("invalid type")

    def from_bytes(self, x):
        return int.from_bytes(self.__len, signed=True)

class UInt2Type(TypeBace):
    def __init__(self):
        self.__len = 2

    def to_bytes(self, x):
        if x is int:
            return int.to_bytes(self.__len, signed=False)
        else:
            raise Exception("invalid type")

    def from_bytes(self, x):
        return int.from_bytes(self.__len, signed=False)

class StrType(TypeBace):
    def __init__(self):
        self.__len = 0

    def to_bytes(self, x):
        if x is str:
            B = "".encode('utf-8')
            return UInt2Type.to_bytes(len(B)) + B
        else:
            raise Exception("invalid type")

    def from_bytes(self, x):
        return str(x, 'utf-8')

class Event:
    def __init__(self, player, name, **kargs):
        self.player = player
        self.event_name = name
        for i, j in kargs.items():
            self.__setattr__(i, j)

    def __repr__(self):
        return "<Event: " + ", ".join([i + "=" + str(j) for i, j in self.__dict__.items()]) + ">"


class Structure:
    def __init__(self, name, **kargs):
        self._ID = None
        self.name = name
        self._format = "!H"
        self._keys = []
        while kargs:
            key, item = kargs.popitem()
            for i, j in Id:
                if i == item:
                    self._keys.append(key)
                    self._format += j
                    break
            else:
                print(item, "err")
        if "{" in self._format:
            self._size = 0
        else:
            self._size = calcsize(self._format)

        self._name = []
        temp = []
        for i, j in kargs.items():
            self._name.append(i)
            temp.append(j)

        self._name = kargs.keys()


class client:
    def __init__(self, *args):
        self.ip = 'localhost'
        self.port = 5555
        self._socket = None

        for i, j in enumerate(args):
            j._ID = i

        self.__struct_size = [i._size for i in args]
        self.__struct = args
        print(args)
        self.__len = len(self.__struct)
        self.__run = True
        self.__events = []

    def start(self):
        if self._socket:
            self._socket.close()
        self._socket = socket(AF_INET, SOCK_STREAM)
        self._socket.connect((self.ip, self.port))
        Thread(target=self._conn_thread, args=(self._socket, (0, 0),)).start()

    def stop(self):
        self.__len = False

    def send(self, type, *args):
        data = pack(type._format, type._ID, *args)
        self._socket.send(data)

    def events(self):
        while self.__events:
            yield self.__events.pop()

    def _conn_thread(self, conn, addr):
        # join event
        id = addr[1]
        self.__events.insert(0, Event(id, "join"))
        data = bytes()
        while self.__run:
            try:
                data = data + conn.recv(2048)  # get update
            except ConnectionResetError:
                self.__events.insert(0, Event(id, "quit", why="socket fail"))
                return

            if not data:
                self.__events.insert(0, Event(id, "quit", why="user closed"))
                return

            while len(data) >= 2:
                event_id = unpack("!H", data[0:2])[0]
                if event_id < self.__len:
                    event_struct = self.__struct[event_id]
                    if not event_struct._size:
                        _format = event_struct._format.replace("{}", " ")
                        print(_format)
                        sizes = []
                        offset = 0
                        for i in _format[1:]:
                            print(offset )
                            if offset+2 > len(data):
                                break
                            if i == " ":

                                sizes.append(unpack("!H", data[offset:offset+2])[0])
                                offset += 2
                                offset += sizes[-1]
                                #continue
                            else:
                                offset += calcsize("!" + i)
                        if offset <= len(data):
                            f = event_struct._format
                            f = f.format(*["H" + str(x) for x in sizes])
                            print(f, sizes, offset, data)
                            event, data = data[:offset], data[offset:]
                            print(event, len(event))
                            args = unpack(f, event)

                            d = {}
                            for i, j in zip(event_struct._keys, args[1:]):
                                d[i] = j

                            self.__events.insert(0, Event(id, self.__struct[event[1]].name, **d))

                        """
                        temp = []
                        offset = 0
                        for i in _format:
                            if offset > len(data):
                                break 
                            if "}" == i[0]:
                                temp.append(i[:2])
                                offset += data[offset:offset+2]
                                if i[2:]:
                                    temp.append(i[2:])
                                    offset += calcsize("!" + temp[-1])
                            else:
                                temp.append(i)
                                offset += calcsize("!" + temp[-1])
                        temp.remove("")
                        print(temp, _format )
                        """



                    else:  # need more data?

                        event, data = data[:self.__struct_size[event_id]], data[self.__struct_size[event_id]:]
                        args = unpack(event_struct._format, event)

                        d = {}
                        for i, j in zip(event_struct._keys, args[1:]):
                            d[i] = j

                        self.__events.insert(0, Event(id, self.__struct[event[1]].name, **d))

                else:
                    self.__events.insert(0, Event(id, "quit", why="bad packet"))
                    print(data, " bad pack")
                    return
                    #  raise Exception("invalid packet id", num)

class Server(client):
    def __init__(self, *args):
        """

        :param port:
        """
        client.__init__(self, *args)
        self.conns = {}
        with socket(AF_INET, SOCK_DGRAM) as s:
            s.connect(('google.com', 80))
            self.ip = s.getsockname()[0]

    def send_to(self, type, to, *args):
        fo = "!H"
        f = type._format[2:]
        i = 0
        out = []
        for i in args:
            if f[0] == "{":
                fo += "H" + str(len(i)) + f[2]

                f = f[2:]
                out.append(len(i))
                out.extend(i)
            else:
                fo += f[0]
                f = f[1:]
                out.append(i)
        print(fo, out)

        data = pack(fo, type._ID, *out)
        self.conns[to].send(data)

    def start(self):
        self._socket = socket(AF_INET, SOCK_STREAM)
        self._socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self._socket.bind((self.ip, self.port))
        self._socket.listen()

        self.__run = True

        Thread(target=self.__join_loop).start()

    def __join_loop(self):
        while self.__run:
            conn, addr = self._socket.accept()
            self.conns[addr[1]] = conn
            Thread(target=self._conn_thread, args=(conn, addr,)).start()


    def kick(self, player):
        pass

    def ban(self, player):
        pass


class c2(Server):
    def __init__(self):
        self.move = Structure(
            "move",
            x=int,
            y=int
        )

        self.str = Structure(
            "str",
            s=str
        )

        Server.__init__(self, self.move, self.str)


if __name__ == "__main__":
    s = c2()
    s.ip = 'localhost'
    print(s.start(), "s")

    while True:

        for i in s.events():
            print(i)

            s.send_to(s.str, i.player, b"test")
"""

ccc{}cccccc{}ccccc
ccc }cccccc }ccccc
ccc{}lic



"""