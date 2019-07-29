from builtins import print
from socket import *
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
      (),
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
        str: "{}c"

    }


class Event:
    def __init(self, args, names, player=None):
        self.player = player
        self.__args = args
        for i, j in zip(args, names):
            if j:
                self.__setattr__(i, j)


class Structure:
    def __init__(self, *args, **kargs):
        self._ID = None
        if args:
            self._type = 1
            self._callback = args[0]
            self._format = "!H" + "".join([ID[i] for i in args[1:]])
            if "{" in self._format:
                self._size = 0
            else:
                self._size = calcsize(self._format)
        else: # add
            self._type = 0
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
        self.__len = len(self.__struct)
        self.__run = True
        self.__events = []

    def start(self):
        print(self._socket)
        self._socket = socket(AF_INET, SOCK_STREAM)
        self._socket.connect((self.ip, self.port))
        print(self._socket)
        Thread(target=self._conn_thread, args=(self._socket, 0,)).start()


    def send(self, type, *args):
        data = pack(type._format, type._ID, *args)
        print(self._socket)
        self._socket.send(data)

    def events(self):
        while self.__events:
            event = self.__events.pop()
            if not self.__struct[event[1]]._type:
                yield Event(event[2:], self.__struct[event[1]])
            else:
                self.__struct[event[1]]._callback(*event[2:])

    def _conn_thread(self, conn, addr):
        # join event
        id = addr
        data = bytes()
        while self.__run:
            try:
                data = data + conn.recv(1024)  # get update
            except ConnectionResetError:
                # event quit
                return  # self.quit()

            if not data:
                return

                # quit event

            while data:
                num = unpack("!H", data[0:2])[0]
                if num < self.__len:
                    if  not self.__struct_size[num]:
                        # custom sizes
                        pass
                    elif self.__struct_size[num] <= len(data):  # need more data?
                        # default sizes
                        event, data = data[:self.__struct_size[num]], data[self.__struct_size[num]:]
                        args = unpack(self.__struct[num]._format, event)
                        print(args)
                        self.__events.append((id, *args))

                        #print(self.__struct_size[num], len(data))
                else:
                    raise Exception("invalid packet id")

class Server(client):
    def __init__(self, *args):
        """

        :param port:
        """
        super(client, self).__init__(*args)

        with socket(AF_INET, SOCK_DGRAM) as s:
            s.connect(('google.com', 80))
            self.ip = s.getsockname()[0]



    def start(self):
        self._socket = socket(AF_INET, SOCK_STREAM)
        self._socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self._socket.bind((self.ip, self.port))
        self._socket.listen()

        self.__run = True

        Thread(target=self.__join_loop).start()
        #return self._socket
        #  Thread(target=self.__event_loop).start()

    def __join_loop(self):
        while self.__run:
            conn, addr = self._socket.accept()
            Thread(target=self._conn_thread, args=(conn, addr,)).start()
            print("join")
        print("e")


class c2(Server):
    def __init__(self):
        self.st = Structure(
            self.print,
            int,
            int
        )
        super(Server, self).__init__(self.st)



    def print(self, *args):
        print(*args, "aend")
        print(self)
        self.send(self.st, 2, 3)


if __name__ == "__main__":
    s = c2()
    s.ip = 'localhost'
    print(s.start(), "s")
    while True:
        for i in s.events():
            if i:
                print(i)
