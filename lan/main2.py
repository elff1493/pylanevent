"""
made by el,

fell free to modify it and share


"""
from locale import k
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR
from threading import Thread
from struct import pack, unpack


class TypeBace:
    """the bace type for defining structures
     to make a new type inherit TypeBace and override two static methods,
     'to_bytes' and 'from_bytes'.

     if type has a fixed length set "len" to the number of byte
     of the type when converted in to bytes, else set "len" to 0 (defaults to 0).

     if len if 0 then the first two bytes must be the length of the object in bytes (big ended/UInt2Type)

     if the object is a container then its content must be stored in self.children

     """
    len = 0
    def __init__(self):
        self.children = []

    @staticmethod
    def to_bytes(x):
        """takes argument and returns it as bytes,
        if len=0 then the first two bytes(UInt2Type) must be the length of the type """
        raise Exception("must impalement 'to_bytes'")

    @staticmethod
    def from_bytes(x):
        """takes bytes and return an object"""
        raise Exception("must impalement 'from_bytes'")

class IntType(TypeBace):  # replace
    """an int in the range -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807"""
    len = 8
    @staticmethod
    def to_bytes(x):
        if type(x) is int:
            return x.to_bytes(IntType.len, byteorder='big', signed=True)
        else:
            raise Exception("invalid type", type(x))

    @staticmethod
    def from_bytes(x):
        return int.from_bytes(x, byteorder='big', signed=True)

class UInt1Type(TypeBace):
    len=1
    @staticmethod
    def to_bytes(x):
        return pack(b"!B", x)

    @staticmethod
    def from_bytes(x):
        return unpack(b"!B", x)[0]

class UInt2Type(TypeBace):#
    len=2
    @staticmethod
    def to_bytes(x):
        return pack(b"!H", x)
    @staticmethod
    def from_bytes(x):
        return unpack(b"!H", x)[0]

class UInt3Type(TypeBace):
    @staticmethod
    def from_bytes(x):
        """takes bytes and return an object"""
        raise Exception("must impalement 'from_bytes'")
    @staticmethod
    def to_bytes(x):
        """takes argument and returns it as bytes,
        if len=0 then the first two bytes(UInt2Type) must be the length of the type """
        raise Exception("must impalement 'to_bytes'")
class UInt4Type(TypeBace):
    @staticmethod
    def to_bytes(x):
        """takes argument and returns it as bytes,
        if len=0 then the first two bytes(UInt2Type) must be the length of the type """
        raise Exception("must impalement 'to_bytes'")

    @staticmethod
    def from_bytes(x):
        """takes bytes and return an object"""
        raise Exception("must impalement 'from_bytes'")
class UInt5Type(TypeBace):
    @staticmethod
    def to_bytes(x):
        """takes argument and returns it as bytes,
        if len=0 then the first two bytes(UInt2Type) must be the length of the type """
        raise Exception("must impalement 'to_bytes'")

    @staticmethod
    def from_bytes(x):
        """takes bytes and return an object"""
        raise Exception("must impalement 'from_bytes'")
class UInt6Type(TypeBace):
    @staticmethod
    def to_bytes(x):
        """takes argument and returns it as bytes,
        if len=0 then the first two bytes(UInt2Type) must be the length of the type """
        raise Exception("must impalement 'to_bytes'")

    @staticmethod
    def from_bytes(x):
        """takes bytes and return an object"""
        raise Exception("must impalement 'from_bytes'")
class UInt7Type(TypeBace):
    @staticmethod
    def to_bytes(x):
        """takes argument and returns it as bytes,
        if len=0 then the first two bytes(UInt2Type) must be the length of the type """
        raise Exception("must impalement 'to_bytes'")

    @staticmethod
    def from_bytes(x):
        """takes bytes and return an object"""
        raise Exception("must impalement 'from_bytes'")
class UInt8Type(TypeBace):
    @staticmethod
    def to_bytes(x):
        """takes argument and returns it as bytes,
        if len=0 then the first two bytes(UInt2Type) must be the length of the type """
        raise Exception("must impalement 'to_bytes'")

    @staticmethod
    def from_bytes(x):
        """takes bytes and return an object"""
        raise Exception("must impalement 'from_bytes'")
class Int1Type(TypeBace):
    @staticmethod
    def to_bytes(x):
        """takes argument and returns it as bytes,
        if len=0 then the first two bytes(UInt2Type) must be the length of the type """
        raise Exception("must impalement 'to_bytes'")

    @staticmethod
    def from_bytes(x):
        """takes bytes and return an object"""
        raise Exception("must impalement 'from_bytes'")
class Int2Type(TypeBace):
    @staticmethod
    def to_bytes(x):
        """takes argument and returns it as bytes,
        if len=0 then the first two bytes(UInt2Type) must be the length of the type """
        raise Exception("must impalement 'to_bytes'")

    @staticmethod
    def from_bytes(x):
        """takes bytes and return an object"""
        raise Exception("must impalement 'from_bytes'")
class Int3Type(TypeBace):
    @staticmethod
    def to_bytes(x):
        """takes argument and returns it as bytes,
        if len=0 then the first two bytes(UInt2Type) must be the length of the type """
        raise Exception("must impalement 'to_bytes'")

    @staticmethod
    def from_bytes(x):
        """takes bytes and return an object"""
        raise Exception("must impalement 'from_bytes'")
class Int4Type(TypeBace):
    @staticmethod
    def to_bytes(x):
        """takes argument and returns it as bytes,
        if len=0 then the first two bytes(UInt2Type) must be the length of the type """
        raise Exception("must impalement 'to_bytes'")

    @staticmethod
    def from_bytes(x):
        """takes bytes and return an object"""
        raise Exception("must impalement 'from_bytes'")
class Int5Type(TypeBace):
    @staticmethod
    def to_bytes(x):
        """takes argument and returns it as bytes,
        if len=0 then the first two bytes(UInt2Type) must be the length of the type """
        raise Exception("must impalement 'to_bytes'")

    @staticmethod
    def from_bytes(x):
        """takes bytes and return an object"""
        raise Exception("must impalement 'from_bytes'")
class Int6Type(TypeBace):
    @staticmethod
    def to_bytes(x):
        """takes argument and returns it as bytes,
        if len=0 then the first two bytes(UInt2Type) must be the length of the type """
        raise Exception("must impalement 'to_bytes'")

    @staticmethod
    def from_bytes(x):
        """takes bytes and return an object"""
        raise Exception("must impalement 'from_bytes'")
class Int7Type(TypeBace):
    @staticmethod
    def to_bytes(x):
        """takes argument and returns it as bytes,
        if len=0 then the first two bytes(UInt2Type) must be the length of the type """
        raise Exception("must impalement 'to_bytes'")

    @staticmethod
    def from_bytes(x):
        """takes bytes and return an object"""
        raise Exception("must impalement 'from_bytes'")
class Int8Type(TypeBace):
    @staticmethod
    def to_bytes(x):
        """takes argument and returns it as bytes,
        if len=0 then the first two bytes(UInt2Type) must be the length of the type """
        raise Exception("must impalement 'to_bytes'")

    @staticmethod
    def from_bytes(x):
        """takes bytes and return an object"""
        raise Exception("must impalement 'from_bytes'")
class StrType(TypeBace):
    len = 0
    @staticmethod
    def to_bytes(x):
        if type(x) is str:
            b = x.encode('utf-8')
            return UInt2Type.to_bytes(len(b)) + b
        else:
            raise Exception("invalid type", type(x))

    @staticmethod
    def from_bytes(x):
        return str(x, 'utf-8')
class ListType(TypeBace):
    len = 0
    def __init__(self, *children):
        self.children = children

    @staticmethod
    def to_bytes(x):
        """takes argument and returns it as bytes,
        if len=0 then the first two bytes(UInt2Type) must be the length of the type """
        raise Exception("must impalement 'to_bytes'")

    @staticmethod
    def from_bytes(x):
        """takes bytes and return an object"""
        raise Exception("must impalement 'from_bytes'")
class TupleType(TypeBace):
    pass
class FloatType(TypeBace):
    pass

class BoolType(TypeBace):
    len = 1
    @staticmethod
    def to_bytes(x):
        if x:
            return bytes([1])
        return bytes([0])

    @staticmethod
    def from_bytes(x):
        return bool(x)
class BytesType(TypeBace):
    pass

class DictType(TypeBace):
    pass

alias = {
        int: IntType,
        str: StrType,
        list: ListType,
        tuple: TupleType,
        float: FloatType,
        bool: BoolType,
        bytes: BytesType,
        dict: DictType
         }


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
        self._format = [UInt2Type]
        self._keys = []
        self._size = 0
        self._sizes = [2]

        size = True
        for i in sorted(kargs.keys()):
            item = kargs[i]
            if TypeBace not in item.__bases__:

                if item not in alias:
                    raise Exception("type not supported", i)
                item = alias[item]

            if item.len and size:
                self._size += item.len
            else:
                size = False

            self._sizes.append(item.len)

            self._format.append(item)
            self._keys.append(i)

class client:
    def __init__(self, *args):
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

    def start(self):
        if self._socket:
            self._socket.close()
        self._socket = socket(AF_INET, SOCK_STREAM)
        self._socket.connect((self.ip, self.port))
        self.__run = True
        Thread(target=self._conn_thread, args=(self._socket, (0, 0),)).start()

    def stop(self):
        self.__len = False

    def send(self, type, **kargs):
        data = bytes()
        data += type._format[0].to_bytes(type._ID)
        for i, j in zip(type._format[1:], type._keys):
            data += i.to_bytes(kargs[j])
        self._socket.send(data)

    def events(self):
        while self.__events:
            yield self.__events.pop()

    def add_event(self, event):
        if type(event) is Event:
            self.__events.insert(0, event)
        else:
            raise Exception(type(event), "is not Event")


    def _conn_thread(self, conn, addr):
        # join event

        id = addr[1]
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
                event_id = UInt2Type.from_bytes(data[0:2])  # unpack("!H", data[0:2])[0]
                if event_id < self.__len:
                    event_struct = self.__struct[event_id]
                    if not event_struct._size or True:

                        l = len(data)
                        offset = 0
                        for i in event_struct._sizes:

                            if i:
                                offset += i

                            else:
                                if offset+3 > l:
                                    break

                                offset += UInt2Type.from_bytes(data[offset:offset+2]) + 2

                            if offset > l:
                                break


                        else:

                            event, data = data[:offset], data[offset:]
                            args = []
                            for i, j in zip(event_struct._sizes, event_struct._format):
                                if not i:
                                    h = UInt2Type.from_bytes(event[:2])
                                    event = event[2:]
                                    args.append(j.from_bytes(event[:h]))
                                    event = event[h:]
                                else:
                                    args.append(j.from_bytes(event[:i]))
                                    event = event[i:]

                            d = {}
                            for i, j in zip(event_struct._keys, args[1:]):
                                d[i] = j

                            self.__events.insert(0, Event(id, event_struct.name, **d))

                    else:  # need more data?
                        pass


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

    def send_to(self, type, to, **kargs):
        data = bytes()
        data += type._format[0].to_bytes(type._ID)
        for i, j in zip(type._format[1:], type._keys):
            data += i.to_bytes(kargs[j])

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
            self.add_event(Event(addr[1], "join"))
            Thread(target=self._conn_thread, args=(conn, addr,)).start()


    def kick(self, player):
        pass

    def ban(self, player):
        pass


class c2(Server):
    def __init__(self):
        self.guess = Structure("guess",
                               str=str
                               )
        self.guessed = Structure("guessed",
                               guess=UInt1Type,
                                word=str,
                                 who=str
                               )
        self.end = Structure("end",
                             win=bool,
                             winner=str
        )

        Server.__init__(self, self.guess, self.guessed, self.end)

    def go(self):
        self.ip = 'localhost'
        self.start()
        word = "testword"
        letter = []
        win = False
        players = {}
        w = "".join([x if x in letter else "-" for x in word])
        while not win:

            for event in self.events():
                print(event)
                if event.event_name == "join":
                    players[event.player] = 5

                elif event.event_name == "guess":
                    if players[event.player]:
                        if event.str[0] not in word:
                            players[event.player] -= 1
                        letter.append(event.str[0])
                        w = "".join([x if x in letter else "-" for x in word])
                        self.send_to(self.guessed, event.player, guess=players[event.player], word=w,
                                     who=str(event.player))


                        if "-" not in w:
                            self.send_to(win, event.player, True, str(event.player))
                            win = False


                #print(i)
                #self.send_to(s.str, i.player, "test")
                #self.send_to(s.gg, i.player, 2, 999, "", "12345")


if __name__ == "__main__":
    s = c2()
    s.go()
"""

ccc{}cccccc{}ccccc
ccc }cccccc }ccccc
ccc{}lic



"""