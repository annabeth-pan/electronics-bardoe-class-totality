from machine import Pin
import time

tilt = Pin(15, Pin.IN, Pin.PULL_UP)

while True:
    print(tilt.value())
    time.sleep(.02)