from ctypes import *  # ctypes库，调用c


class SpeedElmT(Structure):
    _fields_ = [('data', c_long),  # speed data
                ('dec', c_short),  # place of decimal point
                ('unit', c_short),  # unit
                ('disp', c_short),  #
                ('name', c_char),  # C code had char not char， name *
                ('suff', c_char)]  # ditto， subscript of name

    def __repr__(self):
        return f'SpeedElemT({self.data},{self.dec},{self.unit},{self.disp},{self.name},{self.suff})'


class ODBSpeedT(Structure):  # 进给速度 主轴速度
    _fields_ = [('actf', SpeedElmT),
                ('acts', SpeedElmT)]

    def __repr__(self):
        return f'ODBSpeed_T({self.actf!r},{self.acts!r})'


mylib = windll.LoadLibrary('./Fwlib64.dll')
mylib.cnc_allclibhndl3.argtypes = c_char_p, c_ushort, c_long, POINTER(c_ushort)
mylib.cnc_allclibhndl3.restype = c_ushort

handle = c_ushort()
ret = mylib.cnc_allclibhndl3(b'192.168.1.10', 8193, 10, byref(handle))

if ret == 0:
    print("Connection successful!")
else:
    print("connection failed!")

mylib.cnc_rdspeed.argtypes = c_ushort, c_short, POINTER(ODBSpeedT)
mylib.cnc_rdspeed.restype = c_short

speed = ODBSpeedT()  # Create an instance
result = mylib.cnc_rdspeed(handle, -1, byref(speed))  # pass instance by reference
print(result)
print(speed)


