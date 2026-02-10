from machine import Pin, SPI
import time
import max7219
import framebuf

spi = SPI(0, baudrate = 1000000, polarity = 0, phase = 0, sck = Pin(18), mosi = Pin(19))

cs = Pin(17, Pin.OUT)

display = max7219.Matrix8x8(spi, cs, 1)

text = "APPLE"
x = 0
y = 0
fbuf = framebuf.FrameBuffer(bytearray(8 * 8), 8, 8, framebuf.MONO_VLSB)

while True:
    fbuf.fill(0) # Clear buffer
    fbuf.text(text, x, y) # Draw text
    
    display.blit(fbuf, 0, 0)
    display.show()
    
    x -= 1
    time.sleep(.1)
    #if x >= len(text)*8+16:
    if x <= -len(text)*12+16:
        x = 8