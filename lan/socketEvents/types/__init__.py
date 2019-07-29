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
    len = 3
    @staticmethod
    def to_bytes(x):
        if type(x) is int:
            return x.to_bytes(UInt3Type.len, byteorder='big', signed=False)
        else:
            raise Exception("invalid type", type(x))

    @staticmethod
    def from_bytes(x):
        return int.from_bytes(x, byteorder='big', signed=False)

class UInt4Type(TypeBace):
    len = 2
    @staticmethod
    def to_bytes(x):
        return pack(b"!I", x)

    @staticmethod
    def from_bytes(x):
        return unpack(b"!I", x)[0]

class UInt5Type(TypeBace):
    len = 5
    @staticmethod
    def to_bytes(x):
        if type(x) is int:
            return x.to_bytes(UInt5Type.len, byteorder='big', signed=False)
        else:
            raise Exception("invalid type", type(x))

    @staticmethod
    def from_bytes(x):
        return int.from_bytes(x, byteorder='big', signed=False)

class UInt6Type(TypeBace):
    len = 5
    @staticmethod
    def to_bytes(x):
        if type(x) is int:
            return x.to_bytes(UInt6Type.len, byteorder='big', signed=False)
        else:
            raise Exception("invalid type", type(x))

    @staticmethod
    def from_bytes(x):
        return int.from_bytes(x, byteorder='big', signed=False)

class UInt7Type(TypeBace):
    len = 7
    @staticmethod
    def to_bytes(x):
        if type(x) is int:
            return x.to_bytes(UInt7Type.len, byteorder='big', signed=False)
        else:
            raise Exception("invalid type", type(x))

    @staticmethod
    def from_bytes(x):
        return int.from_bytes(x, byteorder='big', signed=False)

class UInt8Type(TypeBace):
    len = 7
    @staticmethod
    def to_bytes(x):
        if type(x) is int:
            return x.to_bytes(UInt8Type.len, byteorder='big', signed=False)
        else:
            raise Exception("invalid type", type(x))

    @staticmethod
    def from_bytes(x):
        return int.from_bytes(x, byteorder='big', signed=False)


class Int1Type(TypeBace):
    len = 1

    @staticmethod
    def to_bytes(x):
        return pack(b"!b", x)

    @staticmethod
    def from_bytes(x):
        return unpack(b"!b", x)[0]


class Int2Type(TypeBace):  #
    len = 2
    @staticmethod
    def to_bytes(x):
        return pack(b"!h", x)

    @staticmethod
    def from_bytes(x):
        return unpack(b"!h", x)[0]


class Int3Type(TypeBace):
    len = 3
    @staticmethod
    def to_bytes(x):
        if type(x) is int:
            return x.to_bytes(Int3Type.len, byteorder='big', signed=False)
        else:
            raise Exception("invalid type", type(x))

    @staticmethod
    def from_bytes(x):
        return int.from_bytes(x, byteorder='big', signed=False)


class Int4Type(TypeBace):
    len = 2
    @staticmethod
    def to_bytes(x):
        return pack(b"!i", x)

    @staticmethod
    def from_bytes(x):
        return unpack(b"!i", x)[0]


class Int5Type(TypeBace):
    len = 5

    @staticmethod
    def to_bytes(x):
        if type(x) is int:
            return x.to_bytes(Int5Type.len, byteorder='big', signed=False)
        else:
            raise Exception("invalid type", type(x))

    @staticmethod
    def from_bytes(x):
        return int.from_bytes(x, byteorder='big', signed=False)


class Int6Type(TypeBace):
    len = 5

    @staticmethod
    def to_bytes(x):
        if type(x) is int:
            return x.to_bytes(UInt6Type.len, byteorder='big', signed=False)
        else:
            raise Exception("invalid type", type(x))

    @staticmethod
    def from_bytes(x):
        return int.from_bytes(x, byteorder='big', signed=False)


class Int7Type(TypeBace):
    len = 7

    @staticmethod
    def to_bytes(x):
        if type(x) is int:
            return x.to_bytes(Int7Type.len, byteorder='big', signed=False)
        else:
            raise Exception("invalid type", type(x))

    @staticmethod
    def from_bytes(x):
        return int.from_bytes(x, byteorder='big', signed=False)


class Int8Type(TypeBace):
    len = 7

    @staticmethod
    def to_bytes(x):
        if type(x) is int:
            return x.to_bytes(Int8Type.len, byteorder='big', signed=False)
        else:
            raise Exception("invalid type", type(x))

    @staticmethod
    def from_bytes(x):
        return int.from_bytes(x, byteorder='big', signed=False)


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
    len = 0
    def __init__(self, *children):
        self.children = children

    def to_bytes(self, x):
        temp = bytes()
        for i in self.children:
            temp += i.to_bytes()
        return bytes([len(temp)]) + temp

    def from_bytes(self, x):
        return

class FloatType(TypeBace):
    len = 8
    @staticmethod
    def to_bytes(x):
        return pack("!d", x)

    @staticmethod
    def from_bytes(x):
        return unpack("!d", x)[0]

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

