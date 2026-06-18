### Project 04: Smart Paeking

#### 1. Overview

Smart parking lots are everywhere. Can we also create a smart parking lot? Of course. We can use ultrasonic sensor to detect if there are vehicles ahead. When a vehicle (or thing) is detected approaching, we control servo to raise the lift rod; If it is detected to be moving away, the servo will lower the lift rod.

#### 2. Components

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit board *1 | micro:bit T-type expansion board *1 | micro USB cable *1 |
| ![Img](./media/A356.png)| ![Img](./media/A309.png)| ![Img](./media/A415.png) |
| ultrasonic sensor *1 | servo *1 | DuPont wires |
|![Img](./media/A017.png) | ![Img](./media/A950.png) | ![Img](./media/A024.png) |
|breadboard *1 | jump wires |battery holder *1 <br> (<span style="color: rgb(255, 76, 65);">self-provided AA batteries *2</span>)|
|![Img](./media/A336.png) |![Img](./media/A131.png) | |
|bat card *1 |lift rod card *1| |

#### 3. Components Knowledge

**Servo**

Servo is a position driver. We can use servo to control the exact position or output high torque. Usually, it is used in robots, remote control cars, and even aircraft models. There are many specifications, but all servos comes with three wires: signal(orange), positive(red) and negative(brown). The color will vary from servo brands.

![Img](./media/A5525.png)

**Internal structure diagram:**

![Img](./media/A5534.png)

① Signal: receives control signals from the microcontroller;

② potentiometer: The position of the output shaft can be measured, which belongs to the feedback part of the whole servo;

③ Internal controller: The embedded board processes signals from external control, drives the motor and feedback position signals, which is the core of the whole servo;

④ DC motor: It is as an actuator to output speed, torque, position;

⑤ Transmission / servo mechanism: The mechanism zooms in the stroke output by the motor to the final output angle according to a certain transmission ratio.

**Drive the servo**

Send PWM signals to the servo signal line to control its output. The duty cycle of PWM directly determines the position of the output shaft. The period is usually 20 milliseconds and is typically set to generate pulses at a frequency of 50Hz.

<span style="color: rgb(255, 0, 0);">For example (180° servo):</span>

When we send a pulse width of 1.5 milliseconds (ms) to the 180° servo, the output shaft of the servo will move to the middle position (90 degrees);

If the pulse width is 0.5ms, the output shaft will move to 0 degree;

If the pulse width is 2.5ms, the output shaft will move to 180 degree;

![Img](./media/A5545.png)

**Parameters:**

- Operating voltage: DC 3.3V~5V

- Operating temperature: -10°C ~ +50°C

- Dimensions: 32.25mm x 12.25mm x 30.42mm

- Interface: 3pin interface with a spacing of 2.54mm

#### 4. Wiring Diagram

![Img](./media/A606.png)

<span style="color: rgb(255, 76, 65);">**When using the ultrasonic sensor and servo, we must connect an external power supply and turn the DIP switch to ON.**</span>

![Img](./media/A902.png)

![Img](./media/A701.png)

#### 5. Code Flow

![Img](./media/A716.png)

#### 6. Test Code

The code file is provided in folder Project 04：Smart-Parking, file Project-04-Smart-Parking.hex.

![Img](./media/A758.png)

**Load code blocks:** <span style="color: rgb(255, 76, 65);">**The threshold in the condition 10 can be modified according to actual conditions.**</span>

![Img](./media/A832.png)

#### 7. Test Result

After downloading the code to the board, when the ultrasonic sensor detect a vehicle (or thing) approaching, the servo controls the lift rod to raise; If the sensor detects it moving away, the servo will lower the lift rod.

<span style="color: rgb(255, 76, 65);">**ATTENTION:** If the wiring is correct but you cannot see the results, press the reset button on the back of the board.</span>

![Img](./media/A021.gif)
