# makino-j3
这是使用FANUC FOCAS库与Makio J3系列机床通信的Python的程序样例。

在Windows环境中，通过使用专用的库运行。

将此做为在你自己的环境中进行运行的提示。

## 实现的功能
- 读取和写入D和R寄存器的值
- NC中的目录搜索和文件操作（读、写、删）。
## 参考信息
### 需要以下dll
- fwlibe64.dll
### 库函数文档
- [使用文档1](http://alvarestech.com/temp/mtconnect/mtconnect-adapter-f9e4039ec1e48cd3f2de9b4a58309d69247a97f5/GE%20Fanus%20Focas%20Lib%202.5/GE%20Fanus%20Focas%20Lib%202.5/Document/SpecJ/FWLIB32.HTM)

- [使用文档2](https://www.woody.vip/fanuc/)
# 使用方法
```
# Open connection
j3 = J3.get_connection('192.168.1.10:8193')

# D寄存器的操作
j3.write_dev('D11600', 255)
j3.read_dev('D11600') # -> 255

j3.write_dev('D11600', 256, size=2)
j3.read_dev('D11600', size=2) # -> 256
j3.read_dev('D11600') # -> 0
j3.read_dev('D11601') # -> 1
j3.read_dev('D11602') # -> 0

# R寄存器的操作
j3.write_dev('R6653.0',1)
j3.write_dev('R6653.1',0)
j3.write_dev('R6653.2',1)
j3.write_dev('R6653.3',0)
j3.write_dev('R6653.4',1)
j3.write_dev('R6653.5',0)
j3.write_dev('R6653.6',1)
j3.write_dev('R6653.7',0)
j3.read_dev('R6653') # -> 85

# 对加工程序文件进行操作。（read・write・delete）
data = b'O8990\nG4 X10.\nM30\n%'
j3.write_file('//CNC_MEM/USER/LIBRARY/O8990', data)
j3.read_file('//CNC_MEM/USER/LIBRARY/O8990')
j3.delete_file('//CNC_MEM/USER/LIBRARY/O8990')

# Close connection
j3.close()
```
