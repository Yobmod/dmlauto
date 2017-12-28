try:
	from setuptools import setup		# type: ignore
except ImportError:
	from distutils.core import setup
from Cython.Build import cythonize		# type: ignore

setup(
	ext_modules=cythonize('LOC_count.pyx'))
