'''
Function: microbit on-board buttons A&B control LED
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import microbit related libraries
from microbit import *

display.show(Image.HEART) # LED matrix displays ❤
pin0.write_digital(0) # set P0 pin to low

while True:
    if button_a.is_pressed():     # if A is pressed
        pin0.write_digital(1)     # P0 is high
        display.show(Image.HAPPY) # LED matrix displays a smile face
    elif button_b.is_pressed():   # or else B is pressed
        pin0.write_digital(0)     # P0 is low
        display.show(Image.SAD)   # LED matrix displays a crying face
