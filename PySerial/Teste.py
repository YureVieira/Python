 
import serial
 
ser = serial.Serial('/dev/ttyUSB0', 9600)
##ser.write('5')
#ser.write(b'5') #Prefixo b necessario se estiver utilizando Python 3.X
while(True):
     data = ser.readline()
     print data
     
     
