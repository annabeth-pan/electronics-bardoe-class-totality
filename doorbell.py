from machine import Pin, PWM
import time

button = Pin(21, Pin.IN, Pin.PULL_UP)
LED = Pin(16, Pin.OUT)
peizo = PWM(Pin(15))

peizo.freq(1000)
peizo.duty_u16(0)
LED.value(0)

def buzz_doorbell(dur):
    peizo.duty_u16(30000)
    LED.value(1)
    time.sleep(dur)
    LED.value(0)
    peizo.duty_u16(0)

while True:
    if button.value() == 0:
        buzz_doorbell(.5)
    time.sleep(.1)
