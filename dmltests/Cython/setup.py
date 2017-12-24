from distutils.core import setup
from Cython.Build import cythonize		# type: ignore

setup(ext_modules=cythonize('fib.pyx'))
