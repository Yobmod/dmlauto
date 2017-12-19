import redis    #type: ignore
from typing import Union, List

r = redis.StrictRedis(host='localhost', port=6379, db=0)
"""methods:
.keys()     list keys
.set()      set key and value, returns True
.get()      get value from key
.delete     del key and value, returns 1 for success
.incr()     increments value of key by b"1" / adds a key with value b"1"
.sadd()
"""


r.set('foo', 'bar')
r.set('poop', 'queef')

def getter(rkey: str) -> str:
    byteout: bytes = r.get(rkey)
    #stringout: str = byteout.decode("utf-8")
    stringout: str = str(byteout, "utf-8")
    print(stringout)
    return stringout

getter('foo')

a: List[bytes] = r.keys()
print(a)

c: List[str] = []
key: bytes
for key in a:
    b: str = key.decode("UTF-8")
    c.append(b)
print(c)


r.incr('que')
getter('que')
r.delete('que')
