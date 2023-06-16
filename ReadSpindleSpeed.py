from ctypes import *


class ODBACT2(Structure):
    class U(Union):
        _fields_ = [
            ('cdata', c_char),
            ('idata', c_short),
            ('ldata', c_long)]

    _anonymous_ = ('u',)  # 通过该设置，可以像iodbpmc.cdata那样访问。它比iodbpmc.u.cdata更快。

    _fields_ = [
        ('dummy', c_short),
        ('data', c_long),
        ('u', U)]


"""class ODBACT(Structure):
    pass
    _fields_ = [
        ('dummy', c_short),
        ('data', c_long),
        ]"""


mylib = windll.LoadLibrary('./Fwlib64.dll')
mylib.cnc_allclibhndl3.argtypes = c_char_p, c_ushort, c_long, POINTER(c_ushort)
mylib.cnc_allclibhndl3.restype = c_ushort

handle = c_ushort()
odbact = ODBACT2()  # 读取主轴转速数据结构体
ret = mylib.cnc_allclibhndl3(b'192.168.1.10', 8193, 10, byref(handle))
# print(type(ret))
# print(ret)
# print(handle)
if ret == 0:
    print("Connection successful!")
else:
    print("connection failed!")
mylib.cnc_acts(byref(handle), odbact)
# print(type(odbact))
spindlespeed = odbact.u.ldata  # spindle speed
print(spindlespeed)

mylib.cnc_freelibhndl(byref(handle))
if mylib.cnc_freelibhndl(byref(handle)):
    print("disconnect!")
