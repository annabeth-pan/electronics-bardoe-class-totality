from machine import Pin, I2C
import ssd1306
import utime
import random
from array import array

clk = Pin(16, Pin.IN, Pin.PULL_UP)
dt = Pin(17, Pin.IN, Pin.PULL_UP)
i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 400_000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

last_state = array('b', [0])
position = array('i', [0])
delta = array('i', [0])
REVERSE = False

last_irq_us = array('I', [0])
DEBOUNCE_US = 0

TRANS = (
    0, -1, 1, 0,
    1, 0, 0, -1,
    -1, 0, 0, 1,
    0, 1, -1, 0
    )

def read_state():
    return (clk.value() << 1) | dt.value() # 01 or 10 or 00 or whatever

def on_change(pin):
    now = utime.ticks_us()
    if utime.ticks_diff(now, last_irq_us[0]) < DEBOUNCE_US:
        return
    last_irq_us[0] = now
    
    old = last_state[0]
    new = read_state()
    last_state[0] = new
    
    step = TRANS[(old << 2) | new] # bitwise or
    if step: # nonzero
        if REVERSE:
            step = -step
        delta[0] += step
    
# interrupt requests are sent, running the on_change function, whenever the voltage changes on clk/dt
clk.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler = on_change)
dt.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler = on_change)

def draw_screen(val):
    oled.fill(0)
    oled.text(f"encoder: {val}", 0, 0)
    oled.rect(0, 40, 128, 10, 1)
    if val > 0:
        if val > 128:
            oled.fill_rect(0, 40, 128, 10, 1)
        else:
            oled.fill_rect(0, 40, val, 10, 1)
    oled.show()

draw_screen(0)
last_draw = -1

while True:
    d = delta[0]
    if d:
        delta[0] = 0
        position[0] += d
    
    if position[0] != last_draw:
        draw_screen(position[0])
        last_draw = position[0]
        
    utime.sleep(.002)


# oled.fill(0)
# oled.text("absolutely mean-", 0, 0)
# oled.text("-ingless bar:", 0, 10)
# oled.rect(0, 40, 128, 10, 1)
# len = 0
# oled.show()
# 
# while True:
#     if len < 128:
#         len += 1
#     oled.fill_rect(0, 40, len, 10, 1)
#     oled.show()
#     myrand = random.random()
#     time.sleep(myrand/5)