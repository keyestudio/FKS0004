### Project 02: Traffic Lights

#### 1. Overview

In this project, we adopt three LEDs( red, yellow and green), a speaker on micro:bit board and 5x5 LED matrix to make a model of traffic lights.

#### 2. Components

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit board *1 | micro:bit T-type expansion board *1 | micro USB cable *1 |
| ![Img](./media/A937.png)| ![Img](./media/A5652.png) | ![Img](./media/A658.png) |
| red LED *1 | yellow LED *1 | green LED *1 |
| ![Img](./media/A944.png) | ![Img](./media/A950.png) |![Img](./media/A017.png) |
| 220Ω resistor *3 | jump wires |breadboard *1 |
|  ![Img](./media/A024.png) |  ![Img](./media/A020.png) |  |
| battery holder *1 <br> (<span style="color: rgb(255, 76, 65);">self-provided AA batteries *2</span>) | traffic lights card *1 | |

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

The code file is provided in folder Project 02：Traffic Lights, file Project-02-Traffic-Lights.hex.

![Img](./media/A0017.png)

**Load code blocks:**

![Img](./media/A605.png)

#### 7. Test Result

For Windows 10 App, click “<span style="color: rgb(255, 76, 65);">Download</span>” . For browsers, send the downloaded “<span style="color: rgb(255, 76, 65);">.hex</span>” file to the micro:bit board.

After downloading the code to the board, the green LED turns on and the 5×5 LED matrix counts down 6 seconds. After the green LED is off, the yellow LED flashes and the matrix counts down 3s with speaker sounding. At last, the red LED is on with a countdown of 6s. These actions repeat.

<span style="color: rgb(255, 76, 65);">**ATTENTION:** If the wiring is correct but you cannot see the results, press the reset button on the back of the board.</span>

![Img](./media/A459.gif)

<span style="color: rgb(255, 76, 65);">**When powering on via external power supply, turn the DIP switch to ON.**</span>

![Img](./media/A904.png)
