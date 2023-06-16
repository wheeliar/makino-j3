from ctypes import *

MAX_AXIS = 48


class IODBPSD_U(Union):
    _fields_ = [
        ('cdata', c_char),
        ('idata', c_short),
        ('ldata', c_long),
        ('cdatas', c_char * MAX_AXIS),
        ('idatas', c_short * MAX_AXIS),
        ('ldatas', c_long * MAX_AXIS)
    ]


class IODBPSD(Structure):
    _fields_ = [
        ('datano', c_short),
        ('type', c_short),
        ('u', IODBPSD_U)
    ]


facos = windll.LoadLibrary('./Fwlib64.dll')


class Facos(object):

    def __init__(self, ip, port, timeout=10):
        if isinstance(ip, str):
            ip = ip.encode()
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.handler = c_short()

    def connect(self):
        handler = c_ushort()
        res = facos.cnc_allclibhndl3(c_char_p(self.ip), c_ushort(self.port), c_long(self.timeout), byref(self.handler))
        return res == 0

    def disconnect(self):
        res = facos.cnc_freelibhndl(byref(self.handler))
        return res == 0

    @property
    def products(self):
        """
        生产件数
        :return: 生产件数
        """
        iodbpsd = IODBPSD()
        facos.cnc_rdparam(byref(self.handler), 6711, 0, 4 + MAX_AXIS, iodbpsd)
        return iodbpsd.u.ldata

    def __enter__(self):
        if self.connect():
            return self
        raise Exception("Connection failed")

    def __exit__(self, type, value, traceback):
        self.disconnect()


if __name__ == "__main__":
    with Facos("192.168.1.10", 8193) as f:
        print("生产件数:", f.products)
