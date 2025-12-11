from machine import Pin, ADC
from servo import Servo
import time

pot = ADC(26)
servo = Servo(pin_id=16)

def map_range(x, in_min, in_max, out_min, out_max):
    return (x-in_min)*(out_max-out_min) / (in_max-in_min) + out_min

while True:
    print(pot.read_u16())
    servo.write(int(map_range(pot.read_u16(), 0, 65535, 0, 180)))
    #print(map_range(pot, 0, 65535, 0, 180))
    time.sleep_ms(10)