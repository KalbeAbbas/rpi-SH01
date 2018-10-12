import smbus2 as smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)
addr = 0x28
# I2C address of the device

class SH01():
	def __init__(self):
		bus.write_byte_data(addr,0x27, 0x00)
		bus.write_byte_data(addr,0x21, 0x39)
		bus.write_byte_data(addr,0x00, 0x00)
	
	def read_button(self):
		data = bus.read_i2c_block_data(addr, 0x02, 1)
                response = ''
                if data[0] == 0x01: 
		    button = bus.read_i2c_block_data(addr, 0x03, 1)
                    if button[0] == 0x01:
                        response = 'Triangle'
                    if button[0] == 0x20:
                        response = 'Circle'
                    if button[0] == 0x08:
                        response = 'Cross'
                    if button[0] == 0x10:
                        response = 'Square'
                    time.sleep(.200) #debounce...
		    bus.write_byte_data(addr,0x00, 0x00)
                    return response
                if data[0] == 0x05:
                    response = 'Many'
                    time.sleep(.200) #debounce...
		    bus.write_byte_data(addr,0x00, 0x00)
                    return response
                else:
                    pass
		
		return ""

from SH01 import SH01
SH01 = SH01()

while True:
	btn = SH01.read_button()
	print ("%s button touched..." % btn)
	time.sleep(1)
