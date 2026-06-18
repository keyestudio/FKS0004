### Project 08: Anti-theft Alarm

#### 1. Overview

When the smart anti-theft alarm detects that the anti-theft box has been moved, the speaker on the micro:bit board will alarm and the red LED will flash.

#### 2. Components

| ![Img](./media/A850.png) |              ![Img](./media/A858.png)              | ![Img](./media/A906.png) |
| :---------------------: | :-----------------------------------------------: | :---------------------: |
|   micro:bit board *1    |        micro:bit T-type expansion board *1        |   micro USB cable *1    |
| ![Img](./media/A937.png) |              ![Img](./media/A944.png)              | ![Img](./media/A950.png) |
|       red LED *1        |                 220Ω resistor *1                  |      jump wire *2       |
| ![Img](./media/A017.png) |              ![Img](./media/A024.png)              | ![Img](./media/A952.png) |
|      breadboard *1      |battery holder *1 <br> (<span style="color: rgb(255, 76, 65);">self-provided AA batteries *2</span>)|      alarm card *1      |

#### 3. Components Knowledge

**Accelerometer**

![Img](./media/A026.png)

The micro:bit board boasts a built-in LSM303AGR acceleration sensor (we called accelerometer) which includes standard, fast, plus and high-speed mode (100 kHz, 400 kHz, 1 MHz and 3.4 MHz) of I2C serial bus interface and SPI serial standard interface for external communication, with resolution of 8/10/12 bits and range of ±2g, ±4g, or ±8g. 

When the micro:bit board is at rest or in uniform motion, the accelerometer only detects the acceleration of gravity. If it is slightly swung, the detected acceleration is much less than the that of gravity, so the difference can be ignored. Therefore, we mainly detect the change of gravitational acceleration on x, y, and z axes.

#### 4. Wiring Diagram

![Img](./media/A219.png)

<span style="color: rgb(255, 76, 65);">The board control pin of LED is P1 (the pin of T-type expansion board is digital 1).</span>

#### 5. Code Flow

![Img](./media/A4434.png)

#### 6. Test Code

The code file is provided in folder Project 08：Burglar Alarm, file Project-08-Burglar-Alarm\.py.

![Img](./media/A3743.png)

**Complete code:** 

<span style="color: rgb(255, 76, 65);">**After importing the code, if the buzzer keeps sounding even though the breadboard is not moved; it may be caused by geographical factors. You can modify the threshold in the condition -60 and 50 according to actual conditions.**</span>

```python
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
```

#### 7. Test Result

Click “<span style="color: rgb(255, 76, 65);">Flash</span>” to load the code to the micro:bit board.

![Img](./media/A3757.png)

After downloading the code to the board, **power on via micro USB cable or external power supply(turn the DIP switch to ON)**, and press the reset button on the board.

![Img](./media/A455.png)

After downloading the code to the board, move the breadboard. If the acceleration value x＜-60 or x＞50, the speaker on the board alarms and the LED flashes, and the micro:bit LED matrix shows ![Img](./media/A706.png). Otherwise, the speaker makes no sound and LED is off, and the micro:bit LED matrix shows ![Img](./media/A720.png).

<span style="color: rgb(255, 76, 65);">**ATTENTION:** If the wiring is correct but you cannot see the results, press the reset button on the back of the board.</span>

![Img](./media/A936.gif)
