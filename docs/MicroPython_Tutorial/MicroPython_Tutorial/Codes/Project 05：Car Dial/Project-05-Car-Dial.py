'''
Function: The potentiometer controls the servo to simulate the car dial
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import microbit related libraries
from microbit import *

display.show(Image.HAPPY)  # LED matrix displays a smile face
pin0.write_analog(25.6)    # set P0 pin analog to 25.6, servo initial angle to 0°
sleep(200)

# map function
def map(value,fromLow,fromHigh,toLow,toHigh):
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow

while True:
    value=pin2.read_analog()    # Read the analog value of the potentiometer (ADC value)
    pin0.set_analog_period(20)  # set servo frequency
    pin0.write_analog(map(value,0,1023,25.6,128))  # Map the analog value of the potentiometer to that of the servo
    sleep(20)
