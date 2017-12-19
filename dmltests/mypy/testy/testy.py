
from typing import Union
import cython
from ctypes import c_int


#reveal_type(cython.long) #-> int
#reveal_type(cython.int) #-> int
#reveal_type(cython.char) #-> int
#reveal_type(cython.short) #-> int
#reveal_type(cython.longlong) #-> int

#reveal_type(cython.float) #-> float
#reveal_type(cython.double) #-> float

#reveal_type(cython.bint) #-> bool
#reveal_type(cython.gs) #-> Dict[str, Any]
#reveal_type(cython.void) #-> Type alias? / Union[None]

#reveal_type(c_int) #-> c_int


"""
useful:     mypy,typeshed,
            stubgen.py (create .pyi from annotated .py),
            retype(integrates .pyi into .py),
            PyAnnotate(add inferred types to .py),
            cython, shedskin,
            CFFI, ctypes
            pyinstaller
"""




def testy(a: cython.int, b: cython.int) -> str:
    a = a + 12
    x: int
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
