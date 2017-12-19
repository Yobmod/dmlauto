
from typing import Union
import cython
from ctypes import c_int

def testy(a: c_int, b: cython.int) -> str:
    a = a + 12
    x: cython.int
    for x in range(a):
        c: int = a
        print(str(c))
    d = str(a * b)
    return d


def testy2(a: int, b: str) -> Union[str, int]:
    if a > 7:
        d: int = a
        return d
    else:
        e: str = b
        return e
