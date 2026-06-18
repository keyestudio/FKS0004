### Project 02: Traffic Lights

#### 1. Overview

In this project, we adopt three LEDs( red, yellow and green), a speaker on micro:bit board and 5x5 LED matrix to make a model of traffic lights.

#### 2. Components

|              ![Img](./media/A850.png)              |       ![Img](./media/A858.png)       | ![Img](./media/A906.png) |
| :-----------------------------------------------: | :---------------------------------: | :---------------------: |
|                micro:bit board *1                 | micro:bit T-type expansion board *1 |   micro USB cable *1    |
|              ![Img](./media/A937.png)              |      ![Img](./media/A5652.png)       | ![Img](./media/A658.png) |
|                    red LED *1                     |            yellow LED *1            |      green LED *1       |
|              ![Img](./media/A944.png)              |       ![Img](./media/A950.png)       | ![Img](./media/A017.png) |
|                 220Ω resistor *3                  |             jump wires              |      breadboard *1      |
|              ![Img](./media/A024.png)              |       ![Img](./media/A020.png)       |                         |
| battery holder *1 <br> (<span style="color: rgb(255, 76, 65);">self-provided AA batteries *2</span>)|       traffic lights card *1        |                         |

#### 3. Components Knowledge

**Speaker**

![Img](./media/A833.png)

Micro: bit comes with a speaker, which makes it easy to make sound in your project.

#### 4. Wiring Diagram

![Img](./media/A908.png)

<span style="color: rgb(255, 76, 65);">**Note:** the micro:bit board needs to be inserted into the T-type expansion board as shown below. The micro:bit board LED matrix should be on the same side with the logo of the expansion board.</span>

![Img](./media/A940.png)

#### 5. Code Flow

![Img](./media/A5956.png)

#### 6. Test Code

The code file is provided in folder Project 02：Traffic Lights, file Project-02-Traffic-Lights\.py.

![Img](./media/A250.png)

**Complete code:** 

```python
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
```

#### 7. Test Result

Click “<span style="color: rgb(255, 76, 65);">Flash</span>” to load the code to the micro:bit board.

![Img](./media/A353.png)

After downloading the code to the board, **power on via micro USB cable or external power supply(turn the DIP switch to ON)**, and press the reset button on the board.

![Img](./media/A455.png)

The green LED turns on and the 5×5 LED matrix counts down 6 seconds. After the green LED is off, the yellow LED flashes and the matrix counts down 3s with speaker sounding. At last, the red LED is on with a countdown of 6s. These actions repeat.

<span style="color: rgb(255, 76, 65);">**ATTENTION:** If the wiring is correct but you cannot see the results, press the reset button on the back of the board.</span>

![Img](./media/A459.gif)

<span style="color: rgb(255, 76, 65);">**When powering on via external power supply, turn the DIP switch to ON.**</span>

![Img](./media/A904.png)
