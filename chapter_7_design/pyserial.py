'''
pyserial.py

Quick intro to serial ports and communication.
Per the pyserial documentation:
http://pyserial.readthedocs.io/en/latest/shortintro.html
'''
import serial

# simple example of opening serial port and closing it 
ser = serial.Serial()
ser.baudrate = 19200
ser.port = 'COM1'
print(ser)
ser.open()
print(ser.is_open) 
# write some data 
ser.write(b'hello')
ser.close()
print(ser.is_open) # False 
