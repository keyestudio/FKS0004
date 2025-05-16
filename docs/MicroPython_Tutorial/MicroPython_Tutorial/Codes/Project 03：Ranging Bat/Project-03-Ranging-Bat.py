'''
Function: bat ranging
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from microbit import *
import ustruct
import machine
from time import sleep_us
import oled_ssd1306 as oled
import music

display.show(Image.HAPPY) # LED matrix displays a smile face
distance = 0              # set variable distance initial value to 0
lastEchoDuration = 0      # set variable lastEchoDuration initial value to 0

# initialize and clear oled
oled.initialize()
oled.clear_oled()

while True:
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
    oled.clear_oled()          # clear OLED
    oled.add_text(1, 0, str(distance) + 'cm')  # Display distance in the corresponding position of OLED
    sleep(200)
    if distance < 10:       # if distance < 10cm
        music.play("C4:4")  # speaker plays C4 tone
        sleep(200)          # delay 
        music.reset()       # no tone
        sleep(200)




