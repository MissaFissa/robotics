from pyfirmata import Arduino, SERVO
from time import sleep
import numpy as np

port = '/dev/cu.usbmodem101'
board = Arduino(port)
servo1 = 5

u_led = [i / 100 for i in range(101)]

led1 = board.get_pin('d:3:p')

board.digital[servo1].mode = SERVO
board.digital[servo1].write(90)

def speed(pin, v):

    board.digital[pin].write(v)
    sleep(0.015)

n = 0

cw = np.arange(0, 91, 1)
ccw = np.arange(90, 181, 1)

while n != 5:

    x = input("input: ")

    if x == "1":

        n += 1
        
        for i in cw:

            speed(servo1, i)
            led1.write(u_led[i])
            print(i)

    if x == "2":

        n += 1

        for i in ccw:

            speed(servo1, i)

            led1.write(u_led[i - 90])
            print(i)
        
        speed(servo1, 90)


# while n != 1:

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


led1.write(0)