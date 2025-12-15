from machine import Pin, ADC, PWM

import time

#enable_pin = Pin(13, Pin.OUT)
in1_pin = Pin(14, Pin.OUT)
in2_pin = Pin(15, Pin.OUT)

enable_pin = PWM(Pin(13))
enable_pin.freq(10000)

pot_pin = ADC(26)

def stop_motors():
    enable_pin.value(0)
    motor_pwm.duty_u16(0)

try:
    enable_pin.duty_u16(65535)

    while True:
#         pot = pot_pin.read_u16()
#         print(pot_pin.read_u16())
        pot=65535
        in1_pin.value(1)
        in2_pin.value(0)
        
        enable_pin.duty_u16(pot)
        time.sleep_ms(10)
    
except KeyboardInterrupt:
    print("KeyboardInterrupt; stopping motors")

finally:
    stop_motors()