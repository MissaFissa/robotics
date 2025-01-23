from pyfirmata import Arduino, SERVO
from time import sleep, time
from serial import Serial
import numpy as np
import threading

arduino = Serial(port = "/dev/cu.usbmodem101", baudrate = 57600)
port = '/dev/cu.usbmodem101'
board = Arduino(port)
servo1 = 5

cw = np.arange(0, 91, 1)
ccw = np.arange(90, 181, 1)
u_led = [i / 100 for i in range(101)]

led1 = board.get_pin('d:3:p')

board.digital[servo1].mode = SERVO
board.digital[servo1].write(90)

def speed(pin, v):

    board.digital[pin].write(v)
    sleep(0.015)

def decode_bytes(data, start, stop):

    return data[start : stop + 1].decode("utf-8", errors = 'ignore').rstrip("\r\n")

def data():

    while True:   

        data = arduino.readline()
        decoded_data = int(decode_bytes(data, 0, 4))
    
        if decoded_data <= 10 and not pause.is_set():
        
            print(decoded_data)

            pause.set()
            move_servo()

def move_servo():

    sleep(1)

    for i in cw:

        speed(servo1, i)

        led1.write(u_led[i])

    for i in ccw:

        speed(servo1, i)

        led1.write(u_led[i - 90])
    
    speed(servo1, 90)
    pause.clear()

    return



pause = threading.Event()
scan = threading.Thread(target = data)
scan.start()
pause.clear()


    
    # if decoded_data <= 10:

    #     move_servo()
    #     n += 1

    #     sleep(1)


# while True:

#     data = arduino.readline()
#     decoded_data = int(decode_bytes(data, 0, 4))
#     print(decoded_data)

#     if decoded_data == 10:

#         move_servo()
        
#         decoded_data = int(decode_bytes(data, 2, 4))


# led1.write(0)

# n = 0

# while n != 5:

#     data = arduino.readline()
#     decoded_data_1 = decode_bytes(data, 0, 4)

#     print(decoded_data_1)
#     x = input("input: ")

#     if x == "1":

#         n += 1
        
#         for i in range(0, 91):

#             speed(servo1, i)
#             led1.write(u_led[i])
#             print(i)

#     if x == "2":

#         n += 1

#         for i in range(90, 181):

#             speed(servo1, i)

#             led1.write(u_led[i - 90])
#             print(i)

#         speed(servo1, 90)
    
# led1.write(0)