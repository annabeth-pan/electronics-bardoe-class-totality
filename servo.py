import time
from servo import Servo

my_servo = Servo(pin_id=16)

while True:
    my_servo.write(90)
    time.sleep_ms(1000)
    my_servo.write(0)
    time.sleep_ms(1000)
    my_servo.write(180)
    time.sleep_ms(1000)