#这个程序是为了测试你的serial组件能否正常运作，需要另外的串口监视软件
import serial

#设置串口为com3且波特率为57600，这个可以根据实际情况调整
ser = serial.Serial('com3', 57600)
print(ser.portstr)
ser.write(b'hello_world')
#应当可以在监视软件里看到hello_world的信息
