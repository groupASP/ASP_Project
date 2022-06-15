from pyfirmata import Arduino, SERVO
from time import sleep

port = "COM7"
pin = 9
pos = 0
board = Arduino(port)

board.digital[pin].mode = SERVO


def servo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.01)


while True:
    for pos in range(0):
        servo(pin, pos)
        sleep(0.01)
    sleep(2)
    for pos in range(0, 90, 1):
        servo(pin, pos)
        sleep(0.01)
        print("0 - 90")
    sleep(5)
    for pos in range(90, 0, -1):
        servo(pin, pos)
        sleep(0.01)
        print("90 - 0, -1.2")
    break
