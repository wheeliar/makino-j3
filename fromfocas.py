import ctypes


class SpeedElmT(ctypes.Structure):
    _fields_ = (('data', ctypes.c_long),  # Speed data
                ('dec', ctypes.c_short),  # decimal point
                ('unit', ctypes.c_short),  # unit
                ('disp', ctypes.c_short),  #
                ('name', ctypes.c_char),  # C code had char not char*
                ('suff', ctypes.c_char))  # ditto

    def __repr__(self):
        return f'SpeedElemT({self.data},{self.dec},{self.unit},{self.disp},{self.name},{self.suff})'


class ODBSpeed_T(ctypes.Structure):
    _fields_ = (('actf', SpeedElmT),
                ('acts', SpeedElmT))

    def __repr__(self):
        return f'ODBSpeed_T({self.actf!r},{self.acts!r})'


mylib = ctypes.WinDLL('./Fwlib32.dll')

mylib.cnc_rdspeed.argtypes = ctypes.c_ushort, ctypes.c_short, ctypes.POINTER(ODBSpeed_T)
mylib.cnc_rdspeed.restype = ctypes.c_short


speed = ODBSpeed_T()  # Create an instance
r = mylib.cnc_rdspeed(ctypes.c_ushort(speed), 1, ctypes.byref(speed))  # pass instance by reference
print(r)
print(speed)
