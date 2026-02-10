from machine import UART, ADC
import time

light = ADC(28)
uart = UART(1, baudrate = 9600, tx=4, rx=5)

while True:
    raw_light = light.read_u16()
    uart.write(f"LIGHT: {raw_light}\n")
    time.sleep(.2)
    
    