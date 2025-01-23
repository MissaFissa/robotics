from pyfirmata import Arduino
from time import sleep
from serial import Serial

arduino = Serial(port="/dev/cu.usbmodem101", baudrate=57600, timeout=0.1)

def decode_bytes(data, start, stop):

    return data[start : stop + 1].decode("utf-8", errors = 'ignore').rstrip("\r\n")

n = 0

while True:

    n += 1
    data = arduino.readline()
    decoded_data_1 = decode_bytes(data, 0, 4)

    if n > 21:

        print(decoded_data_1)