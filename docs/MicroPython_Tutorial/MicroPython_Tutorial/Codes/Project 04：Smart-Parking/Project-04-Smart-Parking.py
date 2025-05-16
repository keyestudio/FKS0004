'''
Function: smart parking
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from microbit import *
import ustruct
import machine
from time import sleep_us

distance = 0              # set variable distance initial value to 0
lastEchoDuration = 0      # set variable lastEchoDuration initial value to 0

val = Image("09990:""09090:""09990:""09000:""09000")  # set iamge
display.show(val)        # LED matrix shows image
pin0.write_analog(25.6)    # set P0 pin analog to 25.6, servo angle to 0°
sleep(200)

while True:
    pin0.set_analog_period(20) # set servo frequency
    # Ultrasonic sensor sends and receives signals
    pin1.write_digital(0)
    sleep_us(2)
    pin1.write_digital(1)
    sleep_us(15)
    pin1.write_digital(0)

    # measure the time interval between "when rising edge detected from the pin2" and "until the pin becomes low again"
    # unit is μs. Assign the interval to variable t.
    t = machine.time_pulse_us(pin2, 1, 35000)

    # a conditional statement, used to check whether the values of two variables t and lastechoduration satisfy specific conditions.
    # If both conditions are met, the block of code under the condition statement is executed.
    if (t <= 0 and lastEchoDuration >= 0):
        t = lastEchoDuration   # variable t = variable lastechoduration
    else:
        lastEchoDuration = t
    distance = int(t * 0.017)  # calculate distance
    if distance < 10:          # if distance < 10cm
       pin0.write_analog(77)   # servo rotate to 90°
       sleep(2000)
    else:  # or
       sleep(2000)
       pin0.write_analog(25.6)
       sleep(2000)
