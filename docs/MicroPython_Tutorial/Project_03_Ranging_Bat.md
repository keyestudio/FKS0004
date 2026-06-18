### Project 03: Ranging Bat

#### 1. Overview

Based on an ultrasonic sensor, the ranging bat detects the distance of obstacles and displays it in real time on an OLED. When it is less than 10cm, the speaker alarms.

#### 2. Components

| ![Img](./media/A850.png) |       ![Img](./media/A858.png)       |              ![Img](./media/A906.png)              |
| :---------------------: | :---------------------------------: | :-----------------------------------------------: |
|   micro:bit board *1    | micro:bit T-type expansion board *1 |                micro USB cable *1                 |
| ![Img](./media/A356.png) |       ![Img](./media/A406.png)       |              ![Img](./media/A415.png)              |
|  ultrasonic sensor *1   |           OLED module *1            |                   DuPont wires                    |
| ![Img](./media/A017.png) |       ![Img](./media/A950.png)       |              ![Img](./media/A024.png)              |
|      breadboard *1      |             jump wires              | battery holder *1 <br> (<span style="color: rgb(255, 76, 65);">self-provided AA batteries *2</span>)|
| ![Img](./media/A315.png) |       ![Img](./media/A557.png)       |                                                   |
|       bat card *1       |            OLED card *1             |                                                   |

#### 3. Components Knowledge

**ultrasonic sensor**

Ultrasonic waves bounce back when they hit an obstacle. We measure the distance by calculating the time interval between sending and receiving the waves. Since the propagation speed of sound in air is a constant v=340m/s, we calculate the distance between the sensor and the obstacle: s=vt/2.

![Img](./media/A846.png)

The HC-SR04 ultrasonic module integrates a transmitter and receiver. The former converts electrical signals (electric energy) into high frequency (beyond human hearing) sound waves (mechanical energy), while the latter does the opposite.

The schematic diagram of the HC SR04:

![Img](./media/A642.png)

**Pin definition:**

![Img](./media/A702.png)

**Parameters:**

- Operating voltage: 5V
- Operating current: 12mA
- Minimum measuring distance: 2cm
- Maximum measuring distance: 200cm

**Working principle:**

A high level pulse lasting at least 10us is output on the Trig pin, and the module starts transmitting ultrasonic waves. At the same time, the Echo pin is pulled up. When the module receives an ultrasonic wave back when it encounters an obstacle, the Echo pin will be pulled down. The duration of the high level of the Echo pin is the total time of wave from sending to receiving: s=vt/2.

![Img](./media/A728.png)

**OLED module**

OLED technology features rich color performance, high contrast and wide perspective, providing clear and vivid pictures, especially outstanding in black. 

Each pixel of the OLED display emits light itself without backlight, so it consumes relatively low power. With small size, high resolution and low power consumption, the 0.9-inch OLED display is very suitable for wearable devices.

![Img](./media/A636.png)

<span style="color: rgb(255, 76, 65);">**In this project, the OLED display module connects the SDA interface to pin P20 and SCL to pin P19.**</span>

**Parameters:**

- Operating voltage: DC 3.3V-5V

- Operating current: 30mA

- Interface: Pin ports with a spacing of 2.54mm

- Communication mode: I2C

- Internal driver chip: SSD1306

- Resolution: 128*64

- Viewing Angle: greater than 150°

#### 4. Wiring Diagram

![Img](./media/A1849.png)

<span style="color: rgb(255, 76, 65);">**When using the OLED display and ultrasonic sensor, we must connect an external power supply and turn the DIP switch to ON.**</span>

![Img](./media/A902.png)

![Img](./media/A1906.png)

#### 5. Import Library

If you haven’t added the required library files yet (oled_ssd1306), please import it referring to [How Mu Import Library to Micro:bit](https://docs.keyestudio.com/projects/FKS0004/en/latest/docs/MicroPython_Tutorial/MicroPython_Tutorial.html#how-mu-import-library-to-micro-bit).

#### 6. Code Flow

![Img](./media/A924.png)

#### 7. Test Code

The code file is provided in folder Project 03：Ranging Bat, file Project-03-Ranging-Bat\.py.

![Img](./media/A302.png)

**Complete code:** <span style="color: rgb(255, 76, 65);">**The threshold in the condition 10 can be modified according to actual conditions.**</span>

```python
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
```

#### 8. Test Result

Click “<span style="color: rgb(255, 76, 65);">Flash</span>” to load the code to the micro:bit board.

![Img](./media/A3323.png)

After downloading the code to the board, **power on via micro USB cable or external power supply(turn the DIP switch to ON)**, and press the reset button on the board.

![Img](./media/A455.png)

The OLED displays the distance between the ultrasonic sensor and the obstacle in real time. When the distance value is less than 10cm, the speaker on micro:bit board alarms.

<span style="color: rgb(255, 76, 65);"><span style="color: rgb(255, 76, 65);">**ATTENTION:** If the wiring is correct but you cannot see the results, press the reset button on the back of the board.</span></span>

![Img](./media/A605.gif)
