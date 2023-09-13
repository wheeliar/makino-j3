from ctypes import *

from pandocfilters import Math


class ODBPOS(Structure):
    class U(Union):
        _fields_ = [
            ('cdata', c_char),
            ('idata', c_short),
            ('ldata', c_long)]

    _anonymous_ = ('u',)  # 通过该设置，可以像iodbpmc.cdata那样访问。它比iodbpmc.u.cdata更快。

    _fields_ = [
        ('dummy', c_short),
        ('type', c_short),
        ('u', U)]


mylib = windll.LoadLibrary('./Fwlib64.dll')
mylib.cnc_allclibhndl3.argtypes = c_char_p, c_ushort, c_long, POINTER(c_ushort)
mylib.cnc_allclibhndl3.restype = c_ushort

handle = c_ushort()
odbpos = ODBPOS()
ret = mylib.cnc_allclibhndl3(b'10.100.126.40', 8193, 10, byref(handle))
# print(type(ret))
# print(ret)
# print(handle)
if ret == 0:
    print("Connection successful!")
else:
    print("connection failed!")
mylib.cnc_rdposition(byref(handle), 1, 8, odbpos)

# xposact = (odbpos.p1.abs.data * Math.Pow(10, -odbpos.p1.abs.dec)).ToString()
xposact = odbpos.u.ldata
print(xposact)

mylib.cnc_freelibhndl(byref(handle))
if mylib.cnc_freelibhndl(byref(handle)):
    print("disconnect!")
