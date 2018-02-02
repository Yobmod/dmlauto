import cffi


ffi = cffi.FFI()
ffi.cdef("C-like declarations")
lib = ffi.dlopen("libpath")


# ffibuilder = cffi.FFI()
# ffibuilder.set_source("package._foo", None)
# ffibuilder.cdef("C-like declarations")
#
# if __name__ == "__main__":
#     ffibuilder.compile()
