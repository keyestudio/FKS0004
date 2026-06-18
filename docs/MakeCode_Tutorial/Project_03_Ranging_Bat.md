### Project 03: Ranging Bat

#### 1. Overview

Based on an ultrasonic sensor, the ranging bat detects the distance of obstacles and displays it in real time on an OLED. When it is less than 10cm, the speaker alarms.

#### 2. Components

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit board *1 | micro:bit T-type expansion board *1 | micro USB cable *1 |
| ![Img](./media/A356.png)| ![Img](./media/A406.png)| ![Img](./media/A415.png) |
| ultrasonic sensor *1 | OLED module *1 | DuPont wires |
|![Img](./media/A017.png) | ![Img](./media/A950.png) | ![Img](./media/A024.png) |
|breadboard *1 | jump wires |battery holder *1 <br> (<span style="color: rgb(255, 76, 65);">self-provided AA batteries *2</span>)|
|![Img](./media/A315.png)|![Img](./media/A557.png) | |
|bat card *1| OLED card *1 | |

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

#### 5. Code Flow

![Img](./media/A924.png)

#### 6. Test Code

The code file is provided in folder Project 03：Ranging Bat, file Project-03-Ranging-Bat.hex.

![Img](./media/A955.png)

**Load code blocks:** <span style="color: rgb(255, 76, 65);">The threshold in the condition 10 can be modified according to actual conditions.</span>

![Img](./media/A022.png)

#### 7. Test Result

For Windows 10 App, click “<span style="color: rgb(255, 76, 65);">Download</span>” . For browsers, send the downloaded “<span style="color: rgb(255, 76, 65);">.hex</span>” file to the micro:bit board.

After downloading the code to the board, <span style="color: rgb(255, 76, 65);">power on via external power supply and turn the DIP switch to ON</span>, and the OLED displays the distance between the ultrasonic sensor and the obstacle in real time. When the distance value is less than 10cm, the speaker on micro:bit board alarms.

<span style="color: rgb(255, 76, 65);"><span style="color: rgb(255, 76, 65);">**ATTENTION:** If the wiring is correct but you cannot see the results, press the reset button on the back of the board.</span></span>

![Img](./media/A605.gif)
