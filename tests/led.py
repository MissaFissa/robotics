from pyfirmata import Arduino
from time import sleep

port = '/dev/cu.usbmodem101'
board = Arduino(port)

pin_led = board.get_pin('d:3:p')

x = [i for i in range(1024)]

for i in x:

    pin_led.write(i)
    value = pin_led.read()
    print(value)
    sleep(.1)

pin_led.write(0)