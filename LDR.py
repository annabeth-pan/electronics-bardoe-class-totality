from machine import Pin, ADC, PWM
import time
import math

sensor = ADC(27)
led = Pin(15, Pin.OUT)
led_pwm = PWM(led)
led_pwm.freq(1000)

threshold = 58000

while True:
    light_val = sensor.read_u16()
    print(f"value: {light_val}")
    
    if light_val > threshold:
        led_pwm.duty_u16(0)
    else:
        led_pwm.duty_u16(math.floor(1-(((light_val-20000)/45000)*65535))) # light value, mapped 0-1 based on a range of 20k to 65k
        # then inverted (1-that) and mapped to a range of 0-65535 for the pwm
        print((light_val/60000)*65535)
        
    time.sleep(.1)
    
# reads ~59,000 in a lit room
# ~13,000 when covered by hands, more realistically 15k because of wires tho
# 63k with phone light 
# im not allowed to have my phone so idk ab that one ijbol