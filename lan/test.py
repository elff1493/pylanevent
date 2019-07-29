from struct import pack, unpack
from time import time

l = 10000000
print(2.6/2.2)
t = time()
for i in range(l):
    x = i.to_bytes(4, byteorder="big", signed=False)
    int.from_bytes(x, byteorder="big", signed=False)


print(t - time())

t = time()
for i in range(l):
    x = pack(b"i", i)
    unpack(b"i", x)

print(t-time())

t = time()
for i in range(l):
    x = pack(b"=i", i)
    unpack(b"=i", x)

print(t-time())

t = time()
for i in range(l):
    x = pack("i", i)
    unpack("i", x)

print(t-time())

