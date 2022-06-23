import serial
import time
arac_arduino = serial.Serial(port="COM3",baudrate = 115200)
kumanda_arduino = serial.Serial(port="COM9",baudrate = 115200)
while True:
    x = kumanda_arduino.readline()
    if x is not None:
        arac_arduino.write(bytes(str(x), 'utf-8'))
        print(x)
            
