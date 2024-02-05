from machine import Pin
from servo import Servo
from time import sleep

sensor = Pin(15,Pin.IN)
servo = Servo(pin_id=13)

while True:
    ir_value = sensor()
    print("IR Sensor Value:", ir_value)
    sleep(0.5)
    if ir_value:
        servo.write(50)
    else:
        servo.write(0)
    sleep(0.5)