# MakeCode_Tutorial

## 1. Programming On MakeCode

The following instructions are applied for Windows system but can also serve as a reference if you are using a different system.

#### 1.1. Fast Start

**Step 1 Connect to micro:bit**

Connect the board to computer via USB cable. 

![Img](./media/A800.png)

If the red LED on the back of the board is on, that means the board is powered. When your computer communicates with the main board via the USB cable, the yellow LED on it will flashes. For example, it will flash when you burn a “.hex” file.

Then Micro: bit main board will appear on your computer as a driver named “MICROBIT”. Please note that it is not an ordinary USB disk as shown below.

![Img](./media/A849.png)

**Step 2 Write heartbeat program**

Enter the link：[online version of Makecode](https://makecode.microbit.org/)

Click “<span style="color: rgb(255, 76, 65);">New Project</span>” and you will see a “<span style="color: rgb(255, 76, 65);">Creating a project</span>”, fill it with “<span style="color: rgb(255, 76, 65);">heartbeat</span>” and click “<span style="color: rgb(255, 76, 65);">Create √</span>”.

<span style="color: rgb(255, 76, 65);">Here we write programs on Google Chrome.</span>

![Img](./media/A021.png)

Let’s write a micro:bit code. 

You can drag some Blocks to the editing area and then run your program in Simulator as shown below. Here we demonstrate how to edit <span style="color: rgb(255, 76, 65);">heartbeat</span> program. 

Operation video guide:

![Img](./media/A100.png)

**Step3 Download codes**

Generally, for Windows 10 APP ([Get Windows 10 App](https://apps.microsoft.com/detail/9pjc7sv48lcx?hl=zh-CN&gl=CN#activetab=pivot:overviewtabdocx))(Click), simply clicking the  “<span style="color: rgb(255, 76, 65);">Download</span>” will directly download the code to the micro:bit board without any additional steps.

Yet for browsers, please:

Click “<span style="color: rgb(255, 76, 65);">Download</span>” in the editor. This will download a “hex” file, which is a format that the micro:bit board can read. After that, copy it to your micro:bit board just like you would copy a file to a USB drive. On Windows, you can also right-click on the “<span style="color: rgb(255, 76, 65);">.hex</span>” file and select “**Send to → MICROBIT**” to copy the file to the micro:bit board.

![Img](./media/A319.png)

![Img](./media/A449.png)

Or, you may directly drag the “<span style="color: rgb(255, 76, 65);">.hex</span>” file into MICROBIT.

![Img](./media/A341.png)

![Img](./media/A345.png)

During copying the “<span style="color: rgb(255, 76, 65);">.hex</span>” file to the Micro: bit, the yellow LED on the back of the board flashes. When the duplication is completed, the LED will stop flashing and remain on.

**Step 4 Run porgram**

After the program is uploaded to the Micro: bit, you can power it via USB cable or an external power. Then the 5 x 5 LED dot matrix displays a heartbeat pattern.

![Img](./media/A425.png)

<span style="color: rgb(255, 76, 65);">**Caution:**</span> When you programs each time, the driver of Micro: bit will automatically eject and return so the hex files will disappear. The board only has access to hex files rather than save them.

#### 1.2. MakeCode

Enter [Makecode Google Chrome online version](https://makecode.microbit.org/) . Here is its main interface.

![Img](./media/A637.png)

There are blocks “**on start**” and “**forever**”in the code editing area. <span style="color: rgb(255, 76, 65);">After powering on, codes in “on start” only executes once, while those in “forever” runs cyclically.</span>

Click “**JS JavaScript**” language:

![Img](./media/A754.png)

Switch it to “**Python**” language:

![Img](./media/A814.png)


#### 1.3. Introduction to WebUSB Functions

As mentioned before, if your computer is Windows 10 and you have downloaded the APP MakeCode, you can quickly download codes to the board by “<span style="color: rgb(255, 76, 65);">Download</span>” button. We use the webUSB of **<span style="color: rgb(255, 76, 65);">Google Chrome</span>** to access the hardware device connected by USB. 

**Devices Pairing:**

1\. Connect the board to computer via USB cable.

![Img](./media/A951.png)

2\. Click “<span style="color: rgb(255, 76, 65);">Download</span>” -> “<span style="color: rgb(255, 76, 65);">...</span>” , and “<span style="color: rgb(255, 76, 65);">Connect device</span>”.

![Img](./media/A028.png)

3\.  “<span style="color: rgb(255, 76, 65);">Next</span>”.

![Img](./media/A046.png)

4\.  “<span style="color: rgb(255, 76, 65);">Pair</span>” .

![Img](./media/A104.png)

5\. Then select the corresponding device and  “<span style="color: rgb(255, 76, 65);">Connect</span>” . 

![Img](./media/A127.png)

6\. “<span style="color: rgb(255, 76, 65);">Done</span>”.

![Img](./media/A144.png)

**Download Program:**

After connection, click “<span style="color: rgb(255, 76, 65);">Download</span>” and you will see the ![Img](./media/A212.png) becomes ![Img](./media/A220.png). The program is downloaded to the micro:bit board. 

![Img](./media/A232.png)

If no device shows up for selection, please refer to [Troubleshooting downloads with WebUSB](https://makecode.microbit.org/device/usb/webusb/troubleshoot). Browse [the user guide](https://microbit.org/guide/firmware/) to know how to update micro:bit firmware. 

#### 1.4. MakeCode Extensions Library

**3.4.1 Import Library Extensions**

Open makecode to enter a certain project, click ![Img](./media/A806.png) to choose “**Extensions**”.

![Img](./media/A842.png)

Or click “**Extensions**”  above the Advanced.

![Img](./media/A900.png)

Search the library you want.

![Img](./media/A909.png)

We provide the code files for each project containing everything you need to run a project, so you can load it directly. If you want to build code blocks by yourself, remember to add the following three extensions.

<span style="color: rgb(0, 209, 0);">**OLED Extension:**</span>

1\. Click “**Extensions**” to add library extensions.

![Img](./media/A236.png)

2\. Search “**OLED**” and click ![Img](./media/A3257.png).

![Img](./media/A306.png)

Click the first **oled-ssd1306** and wait for it to be added.

![Img](./media/A3316.png)

3\. Add successful:

![Img](./media/A335.png)

<span style="color: rgb(0, 209, 0);">**Ultrasonic sensor extension:**</span>

1\. Click “**Extensions**” to add library extensions.

![Img](./media/A236.png)

2\. Search “**sonar**” and click![Img](./media/A3257.png) to find and load “sonar”.

![Img](./media/A506.png)

3\. Add successful:

![Img](./media/A522.png)

<span style="color: rgb(0, 209, 0);">**DHT11 sensor extension:**</span>

1\. Click “**Extensions**” to add library extensions.

![Img](./media/A236.png)

2\. Search “**DHT11**” and click ![Img](./media/A3257.png) to find and load “DHT11_DHT22”.

![Img](./media/A616.png)

3\. Add successful:

![Img](./media/A645.png)

**3.4.2 Update/Delete Extensions**

1\. Click “**JavaScript**” to switch to text code.

![Img](./media/A724.png)

2\. Click “**Explorer**”.

![Img](./media/A749.png)

3\. Find the “**OLED**” library and click ![Img](./media/A813.png) to delete it.

![Img](./media/A824.png)

4\.  “**Remove it**”.

![Img](./media/A727.png)

It is removed.

#### 1.5. How to Import Codes to MakeCode

Let’s take the “**heatbeat**” project as an example to show how to load the code. 

1\. Open the Web version of Makecode or the Windows 10 App Makecode, and click “<span style="color: rgb(255, 76, 65);">Import</span>” .

![Img](./media/A956.png)

2\. “<span style="color: rgb(255, 76, 65);">Import File...</span>”

![Img](./media/A042.png)

3\. “<span style="color: rgb(255, 76, 65);">Choose File</span>”  to import the file you want to load.

![Img](./media/A06.png)

4\. Here we load “<span style="color: rgb(255, 76, 65);">heartbeat.hex</span>” .

![Img](./media/A28.png)

5\. “<span style="color: rgb(255, 76, 65);">Go ahead √</span>”

![Img](./media/A149.png)

In addition to the above method, you can also drag the the test code into the code editing area, as shown below:

![Img](./media/A202.png)

Wait for loading.

![Img](./media/A217.png)

## 2. Projects

### Project 01: Small Lamp with Button

#### 1. Overview

There are two programmable buttons on the front of the micro:bit board (A and B). We combine them with a red LED and a lamp card to build a small desk lamp. When the button A is pressed, the red LED lights up; when B is pressed, it goes off.

#### 2. Components

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit board *1 | micro:bit T-type expansion board *1 | micro USB cable *1 |
| ![Img](./media/A937.png)| ![Img](./media/A944.png) | ![Img](./media/A950.png) |
| red LED *1 | 220Ω resistor *1 | jump wire *2 |
| ![Img](./media/A017.png) | ![Img](./media/A024.png) | ![Img](./media/A920.png)  |
| breadboard *1 |battery holder *1 <br> (<span style="color: rgb(255, 76, 65);">self-provided AA batteries *2</span>) | lamp card *1 |

#### 3. Components Knowledge

**Buttons**

Buttons can control the circuit on and off. When a button is connected to a circuit, the circuit is opened when the button is not pressed; the circuit will be closed after pressing the button. 

There are three buttons on the micro:bit board: a reset button on its back and two programmable buttons (A and B) on its front.

![Img](./media/A230.png)

**Resistors**

![Img](./media/A248.png)

A resistor is an electronic component that limits the current in a branch circuit. The resistance of a fixed resistor cannot be adjusted, while that of a potentiometer or a variable resistor can.

Here are two common circuit symbols for resistors. If you see these symbols in a circuit, they represent a resistor.

![Img](./media/A303.png)

Ω is the unit of resistance, including Ω, KΩ, MΩ, etc. They can be expressed as: 1 MΩ=1000 KΩ, 1 KΩ =1000 Ω. In general, some resistances are marked on the surface.

When using a resistor, we first need to know its resistance. There are two ways: observe the color band on it, or measure its resistance by a multimeter. Obviously, the former one is more convenient and faster.

![Img](./media/A317.png)

As shown in the resistor card, each color represents a number.

![Img](./media/A3335.png)

4-band and 5-band resistors are commonly used.

Often, when you get a resistor, you may find it difficult to decide where to start reading the color.

**Therefore, you can observe the gap between the two bands at one end of it; if it is wider than any other band gap, read from the opposite end.**

<span style="color: rgb(255, 76, 65);">**Note that the gap between the 4th and 5th bands (the 3rd and 4th) is relatively wide in a 5-band (4-band) resistor.**</span>

Let’s see how to read the resistance of a 5-band resistor, as shown below:

![Img](./media/A426.png)

For this resistor, the resistance should be read from left to right. The value should be: 1st band 2nd band 3rd band x 10^multiplier(Ω), ±tolerance%. 

Therefore, the resistance of this resistor is 2(red) 2(red) 0(black) × 10^0 (black)Ω = 220Ω, ±1%(brown). Learn more about [resistor from Wiki](https://en.wikipedia.org/wiki/Resistor).

**LED**

LED, fully called “light-emitting diode”, which is an electronic device made of semiconductor materials (silicon, selenium, germanium, etc.). It is polar, with a positive pole - the long pin connected to VCC (V or 3.3V or 5V or +), and a negative pole - the short pin connected to GND (G or-). The current flows from the positive to the negative, in a one-way flow.

Electronic and graphic symbol of LED:

![Img](./media/A515.png)

LED in various sizes and colors:

![Img](./media/A525.png)

Red, yellow, blue, green and white are the most common colors of LED, which is same as their appearance colors. We rarely use transparent LED, and the light emitted may not be white. There are four sizes of LED: 3mm, 5mm(most common), 8mm and 10mm.

![Img](./media/A535.png)

Forward voltage needs to be used when the LED is on. It is a very important parameter to know when using an LED, as it determines how much power you use and how large the current limiting resistor should be. For most red, yellow, orange and light green LED, they typically use a voltage between 1.9V and 2.1V.

![Img](./media/A548.png)

According to Ohm's law, the current through the circuit decreases as the resistance increases, causing the LED to dim.

I = (VP-Vl)/R

In order to make the LED safe and have the right brightness, how much resistance should we use in the circuit?

For 99% of 5mm LED, the recommended current is 20mA, which can be seen from the conditions column in its data sheet:

![Img](./media/A613.png)

Now convert the above formula to the following:

R = (VP-Vl)/I

If VP = 5V, Vl (forward voltage) = 2V, and I = 20mA, we can tell R is 150Ω. Therefore, we can make the LED brighter by reducing the resistance, but the resistance should not be below 150Ω (this value may not be accurate because the provided LED varies).

The forward voltage and wavelength of different colors of LED are shown below for your reference:

![Img](./media/A629.png)

<span style="color: rgb(255, 76, 65);">**Do not connect a resistor with very low resistance directly to the two poles of the power supply, or the electronic components may be damaged due to excessive current. Resistors are non-polar.**</span>

**Breadboard**

Before completing any circuit, a breadboard is used for quickly designing and testing circuits. There are many holes on a breadboard that can be inserted with circuit components (say, resistors). A typical breadboard is shown below:

![Img](./media/A655.png)

A breadboard has many metal strips under it to connect to the holes at the top. They are arranged as shown below.

<span style="color: rgb(255, 76, 65);">Note that the top and bottom holes are horizontally connected, while the rest of the holes are vertically connected.</span>

![Img](./media/A723.png)

The first two rows(top) and the last two(bottom) of the breadboard are used for the positive(+) and negative(-) poles of the power supply, respectively. The conductive layout diagram is shown below:

![Img](./media/A730.png)

When connecting DIP(Dual In-line Packages) components, such as integrated circuits, microcontrollers, chips, etc., the groove isolates the two parts. Therefore, DIP components can be connected as shown below:

![Img](./media/A740.png)

![Img](./media/A747.png)

**Jump wire and DuPont wire**

Jump wires and DuPont wires connect two terminals. There are various types of them, but here we focus on those used in breadboard. They transmit electrical signals from anywhere on the breadboard to the input/output pins of a microcontroller.

When using, insert “two pins” of the wires into the breadboard without soldering. Several sets of parallel boards are arranged under the surface of the breadboard, so wires only need to be inserted in specific holes in a particular prototype.

There are three types of DuPont wires: F-F, M-M and M-F. On the wire, the pin is called male end(M), while the hole is female(F).

![Img](./media/A811.png)

More than one type can be used in a project. Although the colors of wires are different, they serve the same purpose. Colors are used to distinguish circuits.

#### 4. Wiring Diagram

<span style="color: rgb(255, 76, 65);">Note: the micro:bit board needs to be inserted into the T-type expansion board as shown below. The micro:bit board LED matrix should be on the same side with the logo of the expansion board.</span>

![Img](./media/A156.png)

<span style="color: rgb(255, 76, 65);">The board control pin of LED is P0 (the pin of T-type expansion board is digital 0).</span>

#### 5. Code Flow

![Img](./media/A4323.png)

#### 6. Test Code

The code file is provided in folder Project 01：Small Lamp with Button, file Project-01-Small-Lamp-with-Button.hex.

![Img](./media/A357.png)

**Load code blocks:**

![Img](./media/A440.png)

#### 7. Test Result

For Windows 10 App, click “<span style="color: rgb(255, 76, 65);">Download</span>” . For browsers, send the downloaded “<span style="color: rgb(255, 76, 65);">.hex</span>” file to the micro:bit board.

After downloading the code to the board, 5x5 LED matrix shows ![Img](./media/A512.png) icon. Press button A, and 5x5 LED matrix shows ![Img](./media/A518.png) icon, LED turns on. Press button B, 5x5 LED matrix shows ![Img](./media/A527.png) icon, LED goes off. Does it look like a mini lamp?

<span style="color: rgb(255, 76, 65);">**ATTENTION:** If the wiring is correct but you cannot see the results, press the reset button on the back of the board.</span>

![Img](./media/A359.gif)

<span style="color: rgb(255, 76, 65);">**When powering on via external power supply, turn the DIP switch to ON.**</span>

![Img](./media/A904.png)

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

### Project 05: Car Dial

#### 1. Overview

In this project, we combine an adjustable potentiometer, a servo and a beautiful dial card to make a simple car dial model.

#### 2. Components

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit board *1 | micro:bit T-type expansion board *1 | micro USB cable *1 |
| ![Img](./media/A350.png)| ![Img](./media/A309.png)| ![Img](./media/A950.png) |
| potentiometer *1 | servo *1 | jump wires |
|![Img](./media/A017.png)  | ![Img](./media/A024.png) |![Img](./media/A233.png) |
|breadboard *1 |battery holder *1 <br> (<span style="color: rgb(255, 76, 65);">self-provided AA batteries *2</span>)| potentiometer card *1 |
|![Img](./media/A1326.png) |  |  |
|car dial card*1| |  |

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

<span style="color: rgb(255, 76, 65);">When using the servo, we must connect an external power supply and turn the DIP switch to ON.</span>

![Img](./media/A902.png)

![Img](./media/A836.png)

#### 5. Code Flow

![Img](./media/A0854.png)

#### 6. Test Code

The code file is provided in folder Project 05：Car Dial, file Project-05-Car-Dial.hex.

![Img](./media/A922.png)

**Load code blocks:**

![Img](./media/A942.png)

#### 7. Test Result

After downloading the code to the board, rotate the knob on potentiometer and the servo moves the pointer on the dial.

<span style="color: rgb(255, 76, 65);">**ATTENTION:** If the wiring is correct but you cannot see the results, press the reset button on the back of the board.</span>

![Img](./media/A706.gif)

### Project 06: Music Party

![Img](./media/A1317.png)

#### 1. Overview

When we clap our hands, the microphone on the board picks up sound signals, and the speaker plays a cheerful birthday song while the RGB LED emits dazzling light.

#### 2. Components

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit board *1 | micro:bit T-type expansion board *1 | micro USB cable *1 |
| ![Img](./media/A500.png)| ![Img](./media/A944.png) | ![Img](./media/A950.png) |
| red LED *1 | 220Ω resistor *3 | jump wire *2 |
| ![Img](./media/A017.png) | ![Img](./media/A024.png) | ![Img](./media/A621.png)  |
| breadboard *1 |battery holder *1 <br> (<span style="color: rgb(255, 76, 65);">self-provided AA batteries *2</span>)| RGB card *1 |

#### 3. Components Knowledge

**Microphone**

A high-quality digital microphone is integrated on the front side of the micro:bit V2 board to detect sound and audio signals. The chip that controls and processes the microphone is on its back.

![Img](./media/A1317.png)

The microphone is in a small round hole on the front of the board, which is convenient to capture surrounding sound signals. Just place the micro:bit board face up when using. Next to the hole is a microphone LED indicator. When the micro:bit measures sound levels, the indicator will light up.

![Img](./media/A116.png)

**RGB LED**

![Img](./media/A2127.png)

RGB LED is imaged in the intersection of three primary colors (RGB): red, green and blue. Most colors can be synthesized by RGB in different proportions. The red, green and blue LEDs are packaged in a transparent plastic case to emit colors of light by changing the input voltage of R, G and B pins.

![Img](./media/A137.png)

**Trichromatic theory:**

![Img](./media/A150.png)

RGB LED can be divided into two types: common anode and common cathode:

In a common cathode RGB LED, the three LEDs share a negative connection (cathode);

In a common anode RGB LED, the three LEDs share a positive connection (anode).

![Img](./media/A209.png)

<span style="color: rgb(255, 76, 65);">**Note: Herein, we provide a common cathode RGB LED.**</span>

**RGB LED pins:**

RGB LED boasts 4 pins: GND(the longest one), R(red), G(green) and B(blue). Place the RGB LED as shown below, pins from left to right are red, GND, green and blue.

![Img](./media/A239.png)

#### 4. Wiring Diagram

![Img](./media/A308.png)

![Img](./media/A325.png)

#### 5. Code Flow

![Img](./media/A343.png)

#### 6. Test Code

The code file is provided in folder Project 06：Music Party, file Project-06-Music-Party.hex.

![Img](./media/A423.png)

**Load code blocks:**

![Img](./media/A445.png)

#### 7. Test Result

After downloading the code to the board, when we clap our hands, the microphone on the board picks up sound signals, and the speaker plays a cheerful birthday song while the RGB LED emits dazzling light. Isn’t the music party in a happy and joyful atmosphere?

<span style="color: rgb(255, 76, 65);">**ATTENTION:** If the wiring is correct but you cannot see the results, press the reset button on the back of the board.</span>

![Img](./media/A757.gif)

### Project 07: Environment Monitoring

#### 1. Overview

On the OLED, the smart environment monitoring system displays the temperature and humidity values detected by the DHT11 sensor in real time, as well as the brightness level value of ambient light detected by the on-board light sensor.

#### 2. Components

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit board *1 | micro:bit T-type expansion board *1 | micro USB cable *1 |
| ![Img](./media/A2637.png)| ![Img](./media/A406.png)| ![Img](./media/A415.png) |
| XHT11 temperature and humidity sensor *1 | OLED module *1 | DuPont wires |
|![Img](./media/A017.png) | ![Img](./media/A950.png) | ![Img](./media/A024.png) |
|breadboard *1 | jump wires |battery holder *1 <br> (<span style="color: rgb(255, 76, 65);">self-provided AA batteries *2</span>)|
|![Img](./media/A0715.png) |![Img](./media/A557.png)  | |
|cloud card *1| OLED card *1 | |

#### 3. Components Knowledge

**XHT11 temperature and humidity sensor**

![Img](./media/A2637.png)

XHT11 temperature and humidity sensor is a composite sensor with calibrated digital signal output, which can detect the humidity and temperature in the air. 

**Accuracy**: humidity ±5%RH, temperature ±2℃

**Detection range**: humidity 5%RH ~ 95%RH, temperature -25℃ ~ +60℃

The sensor uses special digital module acquisition and temperature and humidity sensing technology to ensure extremely high reliability and excellent long-term stability. It includes a resistive humidity sensing element and an NTC temperature sensing element, which is very suitable for measurement with relatively low accuracy and real-time requirements.

**XHT11 communication mode:**

Single bus communication is adopted. It means that there is only one data line for data exchange and control in the system.

- Definition of data bits transmitted by single bus:

Single bus data format: 40 bits of data are transmitted at a time, with the high bit coming first.

8bit humidity integer + 8bit humidity decimal + 8bit temperature integer + 8bit temperature decimal + 8bit parity bit (The decimal part of the humidity is 0)

- Definition of parity bit

8bit humidity integer + 8bit humidity decimal + 8bit temperature integer + 8bit temperature decimal. 8bit parity bit = the last 8 bits of the obtained result

- Data timeline:

After the user host (MCU) sends a starting signal, the XHT11 switches from low power mode to high speed mode. After the starting signal, XHT11 sends a response signal and 40bit data, and triggers a signal acquisition.

- The signal transmission is shown in the figure:

![Img](./media/A229.png)

 **Parameters**

- Operating voltage: DC 3.3V to 5V

- Operating current: 2.1mA

- Maximum power: 0.0105W

- Temperature range: -25℃ ~ +60℃ (± 2℃)

- Humidity range: 5%RH ~ 95%RH (accuracy ±5%RH under around 25 ° C)

**Microbit Light Sensor**

![Img](./media/A0335.png)

A light sensor is an input device that measures the brightness of external light. The micro:bit board does not include a built-in light sensor. It detects and senses ambient brightness by an LED matrix that repeatedly convert the light intensity into a value input, and then the voltage attenuation time is sampled. In this way, <span style="color: rgb(255, 76, 65);">the detected brightness level is a relative value</span>.

#### 4. Wiring Diagram

![Img](./media/A409.png)

<span style="color: rgb(255, 76, 65);">When using the OLED display, we must connect an external power supply and turn the DIP switch to ON.</span>

![Img](./media/A904.png)

![Img](./media/A554.png)

#### 5. Code Flow

![Img](./media/A638.png)


#### 6. Test Code

The code file is provided in folder Project 07：Environment Monitoring, file Project-07-Environment-Monitoring.hex.

![Img](./media/A656.png)

**Load code blocks:**

![Img](./media/A715.png)

#### 7. Test Result

After downloading the code to the board, the OLED displays the temperature and humidity values and the light brightness level in real time.

<span style="color: rgb(255, 76, 65);">**ATTENTION:** If the wiring is correct but you cannot see the results, press the reset button on the back of the board.</span>

![Img](./media/A838.gif)

### Project 08: Anti-theft Alarm

#### 1. Overview

When the smart anti-theft alarm detects that the anti-theft box has been moved, the speaker on the micro:bit board will alarm and the red LED will flash.

#### 2. Components

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit board *1 | micro:bit T-type expansion board *1 | micro USB cable *1 |
| ![Img](./media/A937.png)| ![Img](./media/A944.png) | ![Img](./media/A950.png) |
| red LED *1 | 220Ω resistor *1 | jump wire *2 |
| ![Img](./media/A017.png) | ![Img](./media/A024.png) | ![Img](./media/A952.png)  |
| breadboard *1 |battery holder *1 <br> (<span style="color: rgb(255, 76, 65);">self-provided AA batteries *2</span>)| alarm card *1 |

#### 3. Components Knowledge

**Accelerometer**

![Img](./media/A026.png)

The micro:bit board boasts a built-in LSM303AGR acceleration sensor (we called accelerometer) which includes standard, fast, plus and high-speed mode (100 kHz, 400 kHz, 1 MHz and 3.4 MHz) of I2C serial bus interface and SPI serial standard interface for external communication, with resolution of 8/10/12 bits and range of ±2g, ±4g, or ±8g. 

When the micro:bit board is at rest or in uniform motion, the accelerometer only detects the acceleration of gravity. If it is slightly swung, the detected acceleration is much less than the that of gravity, so the difference can be ignored. Therefore, we mainly detect the change of gravitational acceleration on x, y, and z axes.

#### 4. Wiring Diagram

![Img](./media/A219.png)

<span style="color: rgb(255, 76, 65);">**The board control pin of LED is P1 (the pin of T-type expansion board is digital 1).**</span>

#### 5. Code Flow

![Img](./media/A4434.png)

#### 6. Test Code

The code file is provided in folder Project 08：Burglar Alarm, file Project-08-Burglar-Alarm.hex.

![Img](./media/A4518.png)

**Load code blocks:** 

<span style="color: rgb(255, 76, 65);">**After importing the code, if the buzzer keeps sounding even though the breadboard is not moved; it may be caused by geographical factors. You can modify the threshold in the condition -60 and 50 according to actual conditions.**</span>

![Img](./media/A611.png)

#### 7. Test Result

After downloading the code to the board, move the breadboard. If the acceleration value x＜-60 or x＞50, the speaker on the board alarms and the LED flashes, and the micro:bit LED matrix shows ![Img](./media/A706.png). Otherwise, the speaker makes no sound and LED is off, and the micro:bit LED matrix shows ![Img](./media/A720.png).

<span style="color: rgb(255, 76, 65);">**ATTENTION:** If the wiring is correct but you cannot see the results, press the reset button on the back of the board.</span>

![Img](./media/A936.gif)

## 3. Troubleshooting

#### MAINTENANCE: Code fails to download to Micro:bit

**1. Problem**

Recently, many users encounter the issue that Micro:bit board doesn’t respond when download code.

If the way you operate is correct, maybe you accidentally press the reset button and enter the Maintenance mode or the firmware is lost due to mis-operation.

Plug in Micro:bit board, the “<span style="color: rgb(255, 76, 65);">MAINTENANCE</span>” drive appears, which means the program can’t be downloaded. 

![Img](./media/A158.png)

**2. Solutions**

(1) Download the <span style="color: rgb(255, 76, 65);">.hex</span> file from this page to your computer. 

Download [the latest micro:bit firmware-0255](https://www.microbit.org/get-started/user-guide/firmware/). If you do not want to download from this website, we also provide it in our tutorial.

(2) After the latest firmware is downloaded, then drag Firmware for V2.20_V2.21 into the “<span style="color: rgb(255, 76, 65);">MAINTENANCE</span>” to make Micro:bit back to normal mode. 

<span style="color: rgb(255, 76, 65);">We install different firmwares according to micro:bit board models. Here it is Firmware for V2.20_V2.21.</span>

![Img](./media/A326.png)

![Img](./media/A331.png)

**3. Avoid to enter “MAINTENANCE”**

(1) Make sure the Reset button is not pressed when plugging the board by USB cable.

![Img](./media/A228.png)

(2) Don't unplug the cable suddenly during downloading micro:bit program, otherwise, the firmware will be lost and micro:bit will enter “MAINTENANCE” mode.

(3) In the experiment, wrong wiring also cause a short circuit or firmware lost.

#### Troubleshooting Downloads with WebUSB

Clink：[Troubleshooting Downloads with WebUSB](https://makecode.microbit.org/device/usb/webusb/troubleshoot)

Having issues pairing your micro:bit with WebUSB? Let’s try to figure out why!

**Step 1: Check your cable**

Make sure that your micro:bit is connected to your computer with a micro USB cable. For example, in Windows Explorer you should see a **MICROBIT** drive appear when it’s connected.

![Img](./media/A321.png)

If you can see the MICROBIT drive go to step 2. If you can’t see the drive:

(1) Make sure that the USB cable is working. 

Does the cable work on another computer? If not, find a different cable to use. Some cables may only provide a power connection and don’t actually transfer data.

(2) Try another USB port on your computer. 

Is the cable good but you still can’t see the MICROBIT drive? Hmm, you might have a problem with your micro:bit. 

Try the additional steps described in the [fault finding page at microbit.org](https://support.microbit.org/support/solutions/articles/19000024000-fault-finding-with-a-micro-bit). If this doesn’t help, you can [create a support ticket](https://support.microbit.org/support/tickets/new) to notify the Micro:bit Foundation of the problem. Skip the remaining troubleshooting steps. 

**Step 2: Check your firmware version**

If your downloads still aren’t working, it’s possible that the firmware version on the micro:bit needs an update. Let’s check:

1. Go to the **MICROBIT** drive;

2. Open the <span style="color: rgb(255, 76, 65);">DETAILS.TXT</span> file;

![Img](./media/A0452.png)

3. Find the firmware version number; Look for a line in the file that says the version number. It should say Version:

![Img](./media/A501.png)

If the version is 0234, 0241, 0243 you NEED to update the firmware on your micro:bit. Go to Step 3 and follow the upgrade instructions.

If the version is 0249, 0250 or higher, you have the right firmware go to step 4.

**Step 3: Upgrade the firmware**

(1) Put your micro:bit into MAINTENANCE Mode. 

To do this, unplug the USB cable from the micro:bit and then reconnect the USB cable while you hold down the reset button. Once you insert the cable, you can release the reset button. 

You should now see a MAINTENANCE drive instead of the MICROBIT drive like before. Also, a yellow LED light will stay on next to the reset button.

![maintenance](./media/maintenance.gif)

(2) Download the [firmware .hex file](https://microbit.org/guide/firmware/). 

<span style="color: rgb(255, 76, 65);">We install different firmwares according to micro:bit board models. Here it is Firmware for V2.20_V2.21.</span>

![Img](./media/A0629.png)

(3) Drag and drop that file onto the **MAINTENANCE** drive. 

(4) Look for the flashing LED.

The yellow LED will flash while the HEX file is copying. When the copy finishes, the LED will go off and the micro:bit resets. The MAINTENANCE drive now changes back to MICROBIT. 

(5) Upgrade complete.

The upgrade is complete! You can open the <span style="color: rgb(255, 76, 65);">DETAILS.TXT</span> file to check and see that the firmware version changed to the match the version of the HEX file you copied. 

If you want to know more about connecting the board, MAINTENANCE Mode, and upgrading the firmware, read about it in the [Firmware guide](https://microbit.org/guide/firmware/).

**Step 4: Check your browser version**

WebUSB is a fairly new feature and may require you to update your browser. Check that your browser version matches one of those below: Browser versions for Android, Chrome OS, Linux, macOS, and Chrome 65+ for Windows 10.

**Step 5: Pair device**

Once you’ve updated the firmware, open the Chrome Browser, go to the editor and click on Pair Device in the gearwheel menu. See [WebUSB(/device/usb/webusb)](https://microbit.org/get-started/user-guide/web-usb/) for pairing instructions. 

Enjoy fast downloads!
