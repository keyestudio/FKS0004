### Project 01: Small Lamp with Button

#### 1. Overview

There are two programmable buttons on the front of the micro:bit board (A and B). We combine them with a red LED and a lamp card to build a small desk lamp. When the button A is pressed, the red LED lights up; when B is pressed, it goes off.

#### 2. Components

| ![Img](./media/A850.png) |              ![Img](./media/A858.png)              | ![Img](./media/A906.png) |
| :---------------------: | :-----------------------------------------------: | :---------------------: |
|   micro:bit board *1    |        micro:bit T-type expansion board *1        |   micro USB cable *1    |
| ![Img](./media/A937.png) |              ![Img](./media/A944.png)              | ![Img](./media/A950.png) |
|       red LED *1        |                 220Ω resistor *1                  |      jump wire *2       |
| ![Img](./media/A017.png) |              ![Img](./media/A024.png)              | ![Img](./media/A920.png) |
|      breadboard *1      | battery holder *1 <br> (<span style="color: rgb(255, 76, 65);">self-provided AA batteries *2</span>) |      lamp card *1       |

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

4- and 5-band resistors are commonly used.

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

<span style="color: rgb(255, 76, 65);">**Note that the top and bottom holes are horizontally connected, while the rest of the holes are vertically connected.**</span>

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

<span style="color: rgb(255, 76, 65);">**The board control pin of LED is P0 (the pin of T-type expansion board is digital 0).**</span>

#### 5. Code Flow

![Img](./media/A4323.png)

#### 6. Test Code

The code file is provided in folder Project 01：Small Lamp with Button, file Project-01-Small-Lamp-with-Button\.py.

![Img](./media/A100.png)

**Complete code:**

```python
'''
Function: microbit on-board buttons A&B control LED
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import microbit related libraries
from microbit import *

display.show(Image.HEART) # LED matrix displays ❤
pin0.write_digital(0) # set P0 pin to low

while True:
    if button_a.is_pressed():     # if A is pressed
        pin0.write_digital(1)     # P0 is high
        display.show(Image.HAPPY) # LED matrix displays a smile face
    elif button_b.is_pressed():   # or else B is pressed
        pin0.write_digital(0)     # P0 is low
        display.show(Image.SAD)   # LED matrix displays a crying face
```

#### 7. Test Result

Click “<span style="color: rgb(255, 76, 65);">Flash</span>” to load the code to the micro:bit board.

![Img](./media/A2156.png)

After downloading the code to the board, **power on via micro USB cable or external power supply(turn the DIP switch to ON)**, and press the reset button on the board.

![Img](./media/A455.png)

We can see the phenomenon：5x5 LED matrix shows ![Img](./media/A512.png). Press button A, and 5x5 LED matrix shows ![Img](./media/A518.png), LED turns on. Press button B, 5x5 LED matrix shows ![Img](./media/A527.png), LED goes off. Does it look like a mini lamp?

<span style="color: rgb(255, 76, 65);">**ATTENTION:** If the wiring is correct but you cannot see the results, press the reset button on the back of the board again.</span>

![Img](./media/A359.gif)

<span style="color: rgb(255, 76, 65);">When powering on via external power supply, turn the DIP switch to ON.</span>

![Img](./media/A904.png)
