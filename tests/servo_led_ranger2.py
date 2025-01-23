from serial import Serial
from time import sleep

port = '/dev/cu.usbmodem101'
arduino = Serial(port = port, baudrate = 9600)

def decode_bytes(data, start, stop):

    return data[start : stop + 1].decode("utf-8", errors = 'ignore').rstrip("\r\n")

n = 0

while True:

    data = arduino.readline()
    decoded_data = decode_bytes(data, 0, 4)
    print(decoded_data)
    n += 1

    if n == 100:

        break

arduino.close()