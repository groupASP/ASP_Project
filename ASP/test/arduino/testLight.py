from pyfirmata import Arduino, SERVO
from time import sleep

redLED = 13

port = "COM7"

on = 1
off = 0

try:
    board = Arduino(port)
    print("Connected to Arduino")
except:
    print("Failed to connect to Arduino")

while True:
    board.digital[redLED].write(on)
    sleep(1)
    board.digital[redLED].write(off)
    sleep(1)
