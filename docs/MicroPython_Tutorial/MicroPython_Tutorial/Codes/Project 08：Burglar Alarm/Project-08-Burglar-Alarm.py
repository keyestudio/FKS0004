'''
Function: The accelerometer controls a buzzer and LED to simulate a anti-theft alarm
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from microbit import *
import music

display.show(Image.HAPPY) # LED matrix displays a smile face

while True:
    if accelerometer.get_x()<-60 or accelerometer.get_x()>50: # If the value of the accelerometer in the X direction is less than -60 or greater than 50
       music.play("C4:4")      # speaker plays C4 tone
       pin1.write_digital(1)   # P1 pin value is high, LED on
       sleep(200)
       pin1.write_digital(0)   # P1 pin value is low, LED off
       sleep(200)
       display.show(Image.NO)  # LED matrix shows X
    else:  # or
        display.show(Image.HAPPY) # LED matrix displays a smile face
        pin1.write_digital(0)
        music.reset()             # no tone







