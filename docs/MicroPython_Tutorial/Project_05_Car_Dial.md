### Project 05: Car Dial

#### 1. Overview

In this project, we combine an adjustable potentiometer, a servo and a beautiful dial card to make a simple car dial model.

#### 2. Components

| ![Img](./media/A850.png)  |              ![Img](./media/A858.png)              | ![Img](./media/A906.png) |
| :----------------------: | :-----------------------------------------------: | :---------------------: |
|    micro:bit board *1    |        micro:bit T-type expansion board *1        |   micro USB cable *1    |
| ![Img](./media/A350.png)  |              ![Img](./media/A309.png)              | ![Img](./media/A950.png) |
|     potentiometer *1     |                     servo *1                      |       jump wires        |
| ![Img](./media/A017.png)  |              ![Img](./media/A024.png)              | ![Img](./media/A233.png) |
|      breadboard *1       |battery holder *1 <br> (<span style="color: rgb(255, 76, 65);">self-provided AA batteries *2</span>)|  potentiometer card *1  |
| ![Img](./media/A1326.png) |                                                   |                         |
|     car dial card*1      |                                                   |                         |

#### 3. Components Knowledge

**potentiometer**

![Img](./media/A350.png)

A potentiometer is also a resistor element with three contacts, whose resistance value can be adjusted according to some regularity.

They come in all shapes, sizes and values, but they all have the followings in common:

① Three terminals (or connection points).

② A movable knob or slider that can change the resistance between the intermediate terminal and any external terminal.

③ As the knob is moved, the resistance between the intermediate terminal and any external terminal varies from 0Ω to its maximum.

The circuit symbol of potentiometer:

![Img](./media/A654.png)

(1)\. As a voltage divider

The potentiometer is a continuously adjustable resistor. When you rotate its slider, the moving contact slides across the resistor. At this point, a voltage can be output according to the voltage applied to potentiometer and the angle or stroke of rotation of the movable slider.

(2)\. As a variable resistor

When potentiometer is used as a variable resistor, connect its intermediate terminal to one of two additional terminals in the circuit. In this way, you can obtain a steady and continuously varying resistance value within the range of it.

(3)\. As a current controller

When it is used as a current controller, the moving contact must be connected as one of the output terminals.

#### 4. Wiring Diagram

![Img](./media/A812.png)

<span style="color: rgb(255, 76, 65);">**When using the servo, we must connect an external power supply and turn the DIP switch to ON.**</span>

![Img](./media/A902.png)

![Img](./media/A836.png)

#### 5. Code Flow

![Img](./media/A0854.png)

#### 6. Test Code

The code file is provided in folder Project 05：Car Dial, file Project-05-Car-Dial\.py.

![Img](./media/A3438.png)

**Complete code:**

```python
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
```

#### 7. Test Result

Click “<span style="color: rgb(255, 76, 65);">Flash</span>” to load the code to the micro:bit board.

![Img](./media/A3457.png)

After downloading the code to the board, **power on via micro USB cable or external power supply(turn the DIP switch to ON)**, and press the reset button on the board.

![Img](./media/A455.png)

Rotate the knob on potentiometer and the servo moves the pointer on the dial.

<span style="color: rgb(255, 76, 65);">**ATTENTION:** If the wiring is correct but you cannot see the results, press the reset button on the back of the board.</span>

![Img](./media/A706.gif)
