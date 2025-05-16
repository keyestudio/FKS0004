'''
Function: traffic lights with countdowns and buzzes
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import microbit related libraries
from microbit import *

pin1.write_digital(0) # set P1 pin to low
pin2.write_digital(0) # set P2 pin to low
pin8.write_digital(0) # set P8 pin to low

import music # import music libraries

while True:
   pin1.write_digital(1)  # P1 pin to high
   display.show('6')  # LED matrixs shows 6
   sleep(1000)        # delay 1s
   display.show('5')
   sleep(1000)
   display.show('4')
   sleep(1000)
   display.show('3')
   sleep(1000)
   display.show('2')
   sleep(1000)
   display.show('1')
   sleep(1000)
   display.show('0')
   sleep(1000)
   pin1.write_digital(0)
   pin2.write_digital(1)
   music.play("C4:4")    # speaker plays C4 tone
   display.show('2')
   sleep(500)
   pin2.write_digital(0)
   music.reset()         # no tone
   sleep(500)
   pin2.write_digital(1)
   music.play("C4:4")
   display.show('1')
   sleep(500)
   pin2.write_digital(0)
   music.reset()
   sleep(500)
   pin2.write_digital(1)
   music.play("C4:4")
   display.show('0')
   sleep(500)
   pin2.write_digital(0)
   music.reset()
   sleep(500)
   pin8.write_digital(1)
   display.show('6')
   sleep(1000)
   display.show('5')
   sleep(1000)
   display.show('4')
   sleep(1000)
   display.show('3')
   sleep(1000)
   display.show('2')
   sleep(1000)
   display.show('1')
   sleep(1000)
   display.show('0')
   sleep(1000)
   pin8.write_digital(0)
