.. _MicroPython_Tutorial:

MicroPython_Tutorial
====================

.. _1.-About-Mu-Software:

1. About Mu Software
--------------------

.. _1.1.-Install-MU:

1.1. Install MU
~~~~~~~~~~~~~~~

Click to visit `Mu software official website <https://codewith.mu/>`__.

Mu is a Python code editor for beginner programmers, like teachers and
students. We can get it by the official installer for Windows, Mac OSX
or Linux (Mu no longer supports 32-bit Windows). The recommended version
is Mu 1.2.0.

**Step 1 - Make sure your OS so then download Mu Installer**

First find out your computer operating system (Windows or Mac OSX). Open
“\ **This PC**\ ” to see “\ **Properties**\ ”.

.. image:: ./media/A225.png
   :alt: Img

Check the system type: 64-bit or 32-bit.

.. image:: ./media/A253.png
   :alt: Img

`Download MU <https://codewith.mu/en/download>`__. Download the version
according to your computer operating system.

.. image:: ./media/A348.png
   :alt: Img

Here we take the Windows system as an example, which can be a reference
for Mac OSX and Linux.

.. image:: ./media/A422.png
   :alt: Img

**Step 2 - Run the installer**

Double-click the installer (it is probably in your Downloads folder) to
run it.

.. image:: ./media/A440.png
   :alt: Img

We’ve outlined the extra steps needed to help Windows install Mu for
Windows 10. Other versions will be similar.

`Mu installer for
MacOS <https://codewith.mu/en/howto/1.1/install_macos>`__.

`Mu installer for Linux
system <https://codewith.mu/en/howto/1.2/install_linux>`__.

For Windows 10, the Defender will pop up with a warning message. You
should click on the “\ **More info**\ ” link.

.. image:: ./media/A615.png
   :alt: Img

The message will change giving you more information about the installer
and display a “\ **Run anyway**\ ” button. Click “\ **Run anyway**\ ”.

.. image:: ./media/A626.png
   :alt: Img

**Step 3 - License Agreement**

Review the license, select the check box and click “\ **Install**\ ” .

.. image:: ./media/A1716.png
   :alt: Img

**Step 4 - Installing**

Go make a cup of coffee as Mu installs on your computer.

.. image:: ./media/A1740.png
   :alt: Img

**Step 5 - Complete**

The installation has completed successfully, click “\ **Finish**\ ” to
close the installer.

.. image:: ./media/A817.png
   :alt: Img

**Step 6 - Start Mu**

You can start Mu by clicking on the icon in the Start menu or by typing
“Mu” into the search box (both highlighted below). On first start, this
may take some time.

.. image:: ./media/A852.png
   :alt: Img

Here’s what it looks like:

.. image:: ./media/A909.png
   :alt: Img

.. _1.2.-Using-Modes-&-Menu-Bar:

1.2. Using Modes & Menu Bar
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set “Mode” to BBC micro:bit .

On the menu, click “\ **Mode**\ ” to set it to “\ **BBC micro：bit**\ ”.
The micro:bit mode understands how to interact with and connect to a
micro:bit.

.. image:: ./media/A022.png
   :alt: Img

Click to `Start with Mu <https://codewith.mu/en/tutorials/1.1/start>`__.

For more tutorials on using Mu, please visit:
https://codewith.mu/en/tutorials/

.. _1.3.-Program-on-Mu:

1.3. Program on Mu
~~~~~~~~~~~~~~~~~~

Here we load the “heartbeat.py” to Mu. Find it in the folder “Heart
beat” we provided.

.. image:: ./media/A200.png
   :alt: Img

**Method one:**

Open the Mu and click “Load” to choose the path where you downloaded the
code.

.. image:: ./media/A341.png
   :alt: Img

.. image:: ./media/A345.png
   :alt: Img

Loaded successfully, as shown below:

.. image:: ./media/A354.png
   :alt: Img

**Method two:**

Click “new” |Img|\ to create a new program and drag “heartbeat.py” into
it:

.. image:: ./media/A521.png
   :alt: Img

Loaded successfully, as shown below:

.. image:: ./media/A533.png
   :alt: Img

The same is true for adding other codes.

.. _1.4.-Download-Code-to-Mciro:bit:

1.4. Download Code to Mciro:bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect the board to computer via USB cable.

.. image:: ./media/A252.png
   :alt: Img

Click “Flash” to download the code to the micro:bit board.

.. image:: ./media/A3728.png
   :alt: Img

After that, power on by the micro USB cable or external power supply
(turn DIP switch to ON). You will see the on-board 5×5 LED matrix
repeatedly shows |image1| and then |image2|.

Note that if there is an error in your code, it can also be able to
download yet it will not work properly.For example, the function sleep()
is written as sleeps() in the code. Click “\ Flash\ ” to load code to
micro:bit. However, the 5×5 LED matrix shows messy icons.

.. image:: ./media/A4003.png
   :alt: Img

In this case, click “\ **REPL**\ ” and press the reset button on the
board on its back. The error message will be displayed in the REPL
interface, as shown below:

.. image:: ./media/A029.png
   :alt: Img

.. image:: ./media/A033.png
   :alt: Img

Click “\ **REPL**\ ” again to close REPL. And then click “Flash”.

To ensure that the code is correct, click “Check” after completing, and
Mu will point out the error in the code.

.. image:: ./media/A119.png
   :alt: Img

Modify the code according to the error message, and click “Check” again.
Mu does not show an error.

.. image:: ./media/A134.png
   :alt: Img

See `more tutorials explaining specific aspects of
Mu <https://codewith.mu/en/tutorials/>`__.

.. _2.-How-Mu-Import-Library-to-Micro:bit:

2. How Mu Import Library to Micro:bit
-------------------------------------

Before importing libraries, we need to upload a .py code (empty code is
also ok) to the micro:bit board. Here we take an empty code as an
example.

Connect the board to computer via USB cable. Open the Mu and click
“Flash” to upload the .py code (empty code) to the board.

.. image:: ./media/A252.png
   :alt: Img

In this tutorial, OLED and DHT11 modules are used. Therefore, the
“oled_ssd1306.py” and “DHT11.py” library files need to be imported into
the micro:bit board.

The default directory for Mu to save files is “mu_code”in the root
directory of the user’s directory.

References link: https://codewith.mu/en/tutorials/1.0/files

**Instructions for importing libraries:**

1. Search for the “mu_code” folder on the Disk(C:).

.. image:: ./media/A543.png
   :alt: Img

.. image:: ./media/A550.png
   :alt: Img

2. Open “mu_code”.

.. image:: ./media/A628.png
   :alt: Img

3. Copy and paste the library files “oled_ssd1306.py” and “DHT11.py” to
“Libraries”.

.. image:: ./media/A4716.png
   :alt: Img

4. As shown below:

.. image:: ./media/A735.png
   :alt: Img

5. Open the Mu and click “Files”. Here we drag “DHT11.py” library into
micro:bit.

.. image:: ./media/A816.png
   :alt: Img

.. image:: ./media/A820.png
   :alt: Img

6. After importing “DHT11.py”, you'll see it in the box on the left.

.. image:: ./media/A841.png
   :alt: Img

7. Let’s do the same thing to the “oled_ssd1306.py”.

.. image:: ./media/A916.png
   :alt: Img

.. image:: ./media/A4920.png
   :alt: Img

Note that when you upload other files to the micro:bit, they will
overwrite the original content so you need to re-import it for the next
time you use.

.. _3.-Projects:

3. Projects
-----------

.. _Project-01:-Small-Lamp-with-Button:

Project 01: Small Lamp with Button
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _1.-Overview:

1. Overview
^^^^^^^^^^^

There are two programmable buttons on the front of the micro:bit board
(A and B). We combine them with a red LED and a lamp card to build a
small desk lamp. When the button A is pressed, the red LED lights up;
when B is pressed, it goes off.

.. _2.-Components:

2. Components
^^^^^^^^^^^^^

.. container:: table-wrapper

   +-----------------------+-----------------------+-----------------------+
   | |image3|              | |image4|              | |image5|              |
   +=======================+=======================+=======================+
   | micro:bit board \*1   | micro:bit T-type      | micro USB cable \*1   |
   |                       | expansion board \*1   |                       |
   +-----------------------+-----------------------+-----------------------+
   | |image6|              | |image7|              | |image8|              |
   +-----------------------+-----------------------+-----------------------+
   | red LED \*1           | 220Ω resistor \*1     | jump wire \*2         |
   +-----------------------+-----------------------+-----------------------+
   | |image9|              | |image10|             | |image11|             |
   +-----------------------+-----------------------+-----------------------+
   | breadboard \*1        | battery holder \*1    | lamp card \*1         |
   |                       | (self-provided AA     |                       |
   |                       | batteries \*2)        |                       |
   +-----------------------+-----------------------+-----------------------+

.. _3.-Components-Knowledge:

3. Components Knowledge
^^^^^^^^^^^^^^^^^^^^^^^

**Buttons**

Buttons can control the circuit on and off. When a button is connected
to a circuit, the circuit is opened when the button is not pressed; the
circuit will be closed after pressing the button.

There are three buttons on the micro:bit board: a reset button on its
back and two programmable buttons (A and B) on its front.

.. image:: ./media/A230.png
   :alt: Img

**Resistors**

.. image:: ./media/A248.png
   :alt: Img

A resistor is an electronic component that limits the current in a
branch circuit. The resistance of a fixed resistor cannot be adjusted,
while that of a potentiometer or a variable resistor can.

Here are two common circuit symbols for resistors. If you see these
symbols in a circuit, they represent a resistor.

.. image:: ./media/A303.png
   :alt: Img

Ω is the unit of resistance, including Ω, KΩ, MΩ, etc. They can be
expressed as: 1 MΩ=1000 KΩ, 1 KΩ =1000 Ω. In general, some resistances
are marked on the surface.

When using a resistor, we first need to know its resistance. There are
two ways: observe the color band on it, or measure its resistance by a
multimeter. Obviously, the former one is more convenient and faster.

.. image:: ./media/A317.png
   :alt: Img

As shown in the resistor card, each color represents a number.

.. image:: ./media/A3335.png
   :alt: Img

4- and 5-band resistors are commonly used.

Often, when you get a resistor, you may find it difficult to decide
where to start reading the color.

**Therefore, you can observe the gap between the two bands at one end of
it; if it is wider than any other band gap, read from the opposite
end.**

Note that the gap between the 4th and 5th bands (the 3rd and 4th) is
relatively wide in a 5-band (4-band) resistor.

Let’s see how to read the resistance of a 5-band resistor, as shown
below:

.. image:: ./media/A426.png
   :alt: Img

For this resistor, the resistance should be read from left to right. The
value should be: 1st band 2nd band 3rd band x 10^multiplier(Ω),
±tolerance%.

Therefore, the resistance of this resistor is 2(red) 2(red) 0(black) ×
10^0 (black)Ω = 220Ω, ±1%(brown). Learn more about `resistor from
Wiki <https://en.wikipedia.org/wiki/Resistor>`__.

**LED**

LED, fully called “light-emitting diode”, which is an electronic device
made of semiconductor materials (silicon, selenium, germanium, etc.). It
is polar, with a positive pole - the long pin connected to VCC (V or
3.3V or 5V or +), and a negative pole - the short pin connected to GND
(G or-). The current flows from the positive to the negative, in a
one-way flow.

Electronic and graphic symbol of LED:

.. image:: ./media/A515.png
   :alt: Img

LED in various sizes and colors:

.. image:: ./media/A525.png
   :alt: Img

Red, yellow, blue, green and white are the most common colors of LED,
which is same as their appearance colors. We rarely use transparent LED,
and the light emitted may not be white. There are four sizes of LED:
3mm, 5mm(most common), 8mm and 10mm.

.. image:: ./media/A535.png
   :alt: Img

Forward voltage needs to be used when the LED is on. It is a very
important parameter to know when using an LED, as it determines how much
power you use and how large the current limiting resistor should be. For
most red, yellow, orange and light green LED, they typically use a
voltage between 1.9V and 2.1V.

.. image:: ./media/A548.png
   :alt: Img

According to Ohm's law, the current through the circuit decreases as the
resistance increases, causing the LED to dim.

I = (VP-Vl)/R

In order to make the LED safe and have the right brightness, how much
resistance should we use in the circuit?

For 99% of 5mm LED, the recommended current is 20mA, which can be seen
from the conditions column in its data sheet:

.. image:: ./media/A613.png
   :alt: Img

Now convert the above formula to the following:

R = (VP-Vl)/I

If VP = 5V, Vl (forward voltage) = 2V, and I = 20mA, we can tell R is
150Ω. Therefore, we can make the LED brighter by reducing the
resistance, but the resistance should not be below 150Ω (this value may
not be accurate because the provided LED varies).

The forward voltage and wavelength of different colors of LED are shown
below for your reference:

.. image:: ./media/A629.png
   :alt: Img

Do not connect a resistor with very low resistance directly to the two
poles of the power supply, or the electronic components may be damaged
due to excessive current. Resistors are non-polar.

**Breadboard**

Before completing any circuit, a breadboard is used for quickly
designing and testing circuits. There are many holes on a breadboard
that can be inserted with circuit components (say, resistors). A typical
breadboard is shown below:

.. image:: ./media/A655.png
   :alt: Img

A breadboard has many metal strips under it to connect to the holes at
the top. They are arranged as shown below.

Note that the top and bottom holes are horizontally connected, while the
rest of the holes are vertically connected.

.. image:: ./media/A723.png
   :alt: Img

The first two rows(top) and the last two(bottom) of the breadboard are
used for the positive(+) and negative(-) poles of the power supply,
respectively. The conductive layout diagram is shown below:

.. image:: ./media/A730.png
   :alt: Img

When connecting DIP(Dual In-line Packages) components, such as
integrated circuits, microcontrollers, chips, etc., the groove isolates
the two parts. Therefore, DIP components can be connected as shown
below:

.. image:: ./media/A740.png
   :alt: Img

.. image:: ./media/A747.png
   :alt: Img

**Jump wire and DuPont wire**

Jump wires and DuPont wires connect two terminals. There are various
types of them, but here we focus on those used in breadboard. They
transmit electrical signals from anywhere on the breadboard to the
input/output pins of a microcontroller.

When using, insert “two pins” of the wires into the breadboard without
soldering. Several sets of parallel boards are arranged under the
surface of the breadboard, so wires only need to be inserted in specific
holes in a particular prototype.

There are three types of DuPont wires: F-F, M-M and M-F. On the wire,
the pin is called male end(M), while the hole is female(F).

.. image:: ./media/A811.png
   :alt: Img

More than one type can be used in a project. Although the colors of
wires are different, they serve the same purpose. Colors are used to
distinguish circuits.

.. _4.-Wiring-Diagram:

4. Wiring Diagram
^^^^^^^^^^^^^^^^^

Note: the micro:bit board needs to be inserted into the T-type expansion
board as shown below. The micro:bit board LED matrix should be on the
same side with the logo of the expansion board.

.. image:: ./media/A156.png
   :alt: Img

The board control pin of LED is P0 (the pin of T-type expansion board is
digital 0).

.. _5.-Code-Flow:

5. Code Flow
^^^^^^^^^^^^

.. image:: ./media/A4323.png
   :alt: Img

.. _6.-Test-Code:

6. Test Code
^^^^^^^^^^^^

The code file is provided in folder Project 01：Small Lamp with Button,
file Project-01-Small-Lamp-with-Button.py.

.. image:: ./media/A100.png
   :alt: Img

**Complete code:**

.. code:: python

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

.. _7.-Test-Result:

7. Test Result
^^^^^^^^^^^^^^

Click “Flash” to load the code to the micro:bit board.

.. image:: ./media/A2156.png
   :alt: Img

After downloading the code to the board, **power on via micro USB cable
or external power supply(turn the DIP switch to ON)**, and press the
reset button on the board.

.. image:: ./media/A455.png
   :alt: Img

We can see the phenomenon：5x5 LED matrix shows |image12|. Press button
A, and 5x5 LED matrix shows |image13|, LED turns on. Press button B, 5x5
LED matrix shows |image14|, LED goes off. Does it look like a mini lamp?

ATTENTION: If the wiring is correct but you cannot see the results,
press the reset button on the back of the board again.

.. image:: ./media/A359.gif
   :alt: Img

When powering on via external power supply, turn the DIP switch to ON.

.. image:: ./media/A904.png
   :alt: Img

.. _Project-02:-Traffic-Lights:

Project 02: Traffic Lights
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _1.-Overview:

1. Overview
^^^^^^^^^^^

In this project, we adopt three LEDs( red, yellow and green), a speaker
on micro:bit board and 5x5 LED matrix to make a model of traffic lights.

.. _2.-Components:

2. Components
^^^^^^^^^^^^^

.. container:: table-wrapper

   +-----------------------+-----------------------+-----------------------+
   | |image15|             | |image16|             | |image17|             |
   +=======================+=======================+=======================+
   | micro:bit board \*1   | micro:bit T-type      | micro USB cable \*1   |
   |                       | expansion board \*1   |                       |
   +-----------------------+-----------------------+-----------------------+
   | |image18|             | |image19|             | |image20|             |
   +-----------------------+-----------------------+-----------------------+
   | red LED \*1           | yellow LED \*1        | green LED \*1         |
   +-----------------------+-----------------------+-----------------------+
   | |image21|             | |image22|             | |image23|             |
   +-----------------------+-----------------------+-----------------------+
   | 220Ω resistor \*3     | jump wires            | breadboard \*1        |
   +-----------------------+-----------------------+-----------------------+
   | |image24|             | |image25|             |                       |
   +-----------------------+-----------------------+-----------------------+
   | battery holder \*1    | traffic lights card   |                       |
   | (self-provided AA     | \*1                   |                       |
   | batteries \*2)        |                       |                       |
   +-----------------------+-----------------------+-----------------------+

.. _3.-Components-Knowledge:

3. Components Knowledge
^^^^^^^^^^^^^^^^^^^^^^^

**Speaker**

.. image:: ./media/A833.png
   :alt: Img

Micro: bit comes with a speaker, which makes it easy to make sound in
your project.

.. _4.-Wiring-Diagram:

4. Wiring Diagram
^^^^^^^^^^^^^^^^^

.. image:: ./media/A908.png
   :alt: Img

Note: the micro:bit board needs to be inserted into the T-type expansion
board as shown below. The micro:bit board LED matrix should be on the
same side with the logo of the expansion board.

.. image:: ./media/A940.png
   :alt: Img

.. _5.-Code-Flow:

5. Code Flow
^^^^^^^^^^^^

.. image:: ./media/A5956.png
   :alt: Img

.. _6.-Test-Code:

6. Test Code
^^^^^^^^^^^^

The code file is provided in folder Project 02：Traffic Lights, file
Project-02-Traffic-Lights.py.

.. image:: ./media/A250.png
   :alt: Img

**Complete code:**

.. code:: python

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

.. _7.-Test-Result:

7. Test Result
^^^^^^^^^^^^^^

Click “Flash” to load the code to the micro:bit board.

.. image:: ./media/A353.png
   :alt: Img

After downloading the code to the board, **power on via micro USB cable
or external power supply(turn the DIP switch to ON)**, and press the
reset button on the board.

.. image:: ./media/A455.png
   :alt: Img

The green LED turns on and the 5×5 LED matrix counts down 6 seconds.
After the green LED is off, the yellow LED flashes and the matrix counts
down 3s with speaker sounding. At last, the red LED is on with a
countdown of 6s. These actions repeat.

ATTENTION: If the wiring is correct but you cannot see the results,
press the reset button on the back of the board.

.. image:: ./media/A459.gif
   :alt: Img

When powering on via external power supply, turn the DIP switch to ON.

.. image:: ./media/A904.png
   :alt: Img

.. _Project-03:-Ranging-Bat:

Project 03: Ranging Bat
~~~~~~~~~~~~~~~~~~~~~~~

.. _1.-Overview:

1. Overview
^^^^^^^^^^^

Based on an ultrasonic sensor, the ranging bat detects the distance of
obstacles and displays it in real time on an OLED. When it is less than
10cm, the speaker alarms.

.. _2.-Components:

2. Components
^^^^^^^^^^^^^

.. container:: table-wrapper

   +-----------------------+-----------------------+-----------------------+
   | |image26|             | |image27|             | |image28|             |
   +=======================+=======================+=======================+
   | micro:bit board \*1   | micro:bit T-type      | micro USB cable \*1   |
   |                       | expansion board \*1   |                       |
   +-----------------------+-----------------------+-----------------------+
   | |image29|             | |image30|             | |image31|             |
   +-----------------------+-----------------------+-----------------------+
   | ultrasonic sensor \*1 | OLED module \*1       | DuPont wires          |
   +-----------------------+-----------------------+-----------------------+
   | |image32|             | |image33|             | |image34|             |
   +-----------------------+-----------------------+-----------------------+
   | breadboard \*1        | jump wires            | battery holder \*1    |
   |                       |                       | (self-provided AA     |
   |                       |                       | batteries \*2)        |
   +-----------------------+-----------------------+-----------------------+
   | |image35|             | |image36|             |                       |
   +-----------------------+-----------------------+-----------------------+
   | bat card \*1          | OLED card \*1         |                       |
   +-----------------------+-----------------------+-----------------------+

.. _3.-Components-Knowledge:

3. Components Knowledge
^^^^^^^^^^^^^^^^^^^^^^^

**ultrasonic sensor**

Ultrasonic waves bounce back when they hit an obstacle. We measure the
distance by calculating the time interval between sending and receiving
the waves. Since the propagation speed of sound in air is a constant
v=340m/s, we calculate the distance between the sensor and the obstacle:
s=vt/2.

.. image:: ./media/A846.png
   :alt: Img

The HC-SR04 ultrasonic module integrates a transmitter and receiver. The
former converts electrical signals (electric energy) into high frequency
(beyond human hearing) sound waves (mechanical energy), while the latter
does the opposite.

The schematic diagram of the HC SR04:

.. image:: ./media/A642.png
   :alt: Img

**Pin definition:**

.. image:: ./media/A702.png
   :alt: Img

**Parameters:**

-  Operating voltage: 5V
-  Operating current: 12mA
-  Minimum measuring distance: 2cm
-  Maximum measuring distance: 200cm

**Working principle:**

A high level pulse lasting at least 10us is output on the Trig pin, and
the module starts transmitting ultrasonic waves. At the same time, the
Echo pin is pulled up. When the module receives an ultrasonic wave back
when it encounters an obstacle, the Echo pin will be pulled down. The
duration of the high level of the Echo pin is the total time of wave
from sending to receiving: s=vt/2.

.. image:: ./media/A728.png
   :alt: Img

**OLED module**

OLED technology features rich color performance, high contrast and wide
perspective, providing clear and vivid pictures, especially outstanding
in black.

Each pixel of the OLED display emits light itself without backlight, so
it consumes relatively low power. With small size, high resolution and
low power consumption, the 0.9-inch OLED display is very suitable for
wearable devices.

.. image:: ./media/A636.png
   :alt: Img

In this project, the OLED display module connects the SDA interface to
pin P20 and SCL to pin P19.

**Parameters:**

-  Operating voltage: DC 3.3V-5V

-  Operating current: 30mA

-  Interface: Pin ports with a spacing of 2.54mm

-  Communication mode: I2C

-  Internal driver chip: SSD1306

-  Resolution: 128*64

-  Viewing Angle: greater than 150°

.. _4.-Wiring-Diagram:

4. Wiring Diagram
^^^^^^^^^^^^^^^^^

.. image:: ./media/A1849.png
   :alt: Img

When using the OLED display and ultrasonic sensor, we must connect an
external power supply and turn the DIP switch to ON.

.. image:: ./media/A902.png
   :alt: Img

.. image:: ./media/A1906.png
   :alt: Img

.. _5.-Import-Library:

5. Import Library
^^^^^^^^^^^^^^^^^

If you haven’t added the required library files yet (oled_ssd1306),
please import it referring to `How Mu Import Library to
Micro:bit <https://docs.keyestudio.com/projects/FKS0004/en/latest/docs/MicroPython_Tutorial/MicroPython_Tutorial.html#how-mu-import-library-to-micro-bit>`__.

.. _6.-Code-Flow:

6. Code Flow
^^^^^^^^^^^^

.. image:: ./media/A924.png
   :alt: Img

.. _7.-Test-Code:

7. Test Code
^^^^^^^^^^^^

The code file is provided in folder Project 03：Ranging Bat, file
Project-03-Ranging-Bat.py.

.. image:: ./media/A302.png
   :alt: Img

**Complete code:** The threshold in the condition 10 can be modified
according to actual conditions.

.. code:: python

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

.. _8.-Test-Result:

8. Test Result
^^^^^^^^^^^^^^

Click “Flash” to load the code to the micro:bit board.

.. image:: ./media/A3323.png
   :alt: Img

After downloading the code to the board, **power on via micro USB cable
or external power supply(turn the DIP switch to ON)**, and press the
reset button on the board.

.. image:: ./media/A455.png
   :alt: Img

The OLED displays the distance between the ultrasonic sensor and the
obstacle in real time. When the distance value is less than 10cm, the
speaker on micro:bit board alarms.

ATTENTION: If the wiring is correct but you cannot see the results,
press the reset button on the back of the board.

.. image:: ./media/A605.gif
   :alt: Img

.. _Project-04:-Smart-Paeking:

Project 04: Smart Paeking
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _1.-Overview:

1. Overview
^^^^^^^^^^^

Smart parking lots are everywhere. Can we also create a smart parking
lot? Of course. We can use ultrasonic sensor to detect if there are
vehicles ahead. When a vehicle (or thing) is detected approaching, we
control servo to raise the lift rod; If it is detected to be moving
away, the servo will lower the lift rod.

.. _2.-Components:

2. Components
^^^^^^^^^^^^^

.. container:: table-wrapper

   +-----------------------+-----------------------+-----------------------+
   | |image37|             | |image38|             | |image39|             |
   +=======================+=======================+=======================+
   | micro:bit board \*1   | micro:bit T-type      | micro USB cable \*1   |
   |                       | expansion board \*1   |                       |
   +-----------------------+-----------------------+-----------------------+
   | |image40|             | |image41|             | |image42|             |
   +-----------------------+-----------------------+-----------------------+
   | ultrasonic sensor \*1 | servo \*1             | DuPont wires          |
   +-----------------------+-----------------------+-----------------------+
   | |image43|             | |image44|             | |image45|             |
   +-----------------------+-----------------------+-----------------------+
   | breadboard \*1        | jump wires            | battery holder \*1    |
   |                       |                       | (self-provided AA     |
   |                       |                       | batteries \*2)        |
   +-----------------------+-----------------------+-----------------------+
   | |image46|             | |image47|             |                       |
   +-----------------------+-----------------------+-----------------------+
   | bat card \*1          | lift rod card \*1     |                       |
   +-----------------------+-----------------------+-----------------------+

.. _3.-Components-Knowledge:

3. Components Knowledge
^^^^^^^^^^^^^^^^^^^^^^^

**Servo**

Servo is a position driver. We can use servo to control the exact
position or output high torque. Usually, it is used in robots, remote
control cars, and even aircraft models. There are many specifications,
but all servos comes with three wires: signal(orange), positive(red) and
negative(brown). The color will vary from servo brands.

.. image:: ./media/A5525.png
   :alt: Img

**Internal structure diagram:**

.. image:: ./media/A5534.png
   :alt: Img

① Signal: receives control signals from the microcontroller;

② potentiometer: The position of the output shaft can be measured, which
belongs to the feedback part of the whole servo;

③ Internal controller: The embedded board processes signals from
external control, drives the motor and feedback position signals, which
is the core of the whole servo;

④ DC motor: It is as an actuator to output speed, torque, position;

⑤ Transmission / servo mechanism: The mechanism zooms in the stroke
output by the motor to the final output angle according to a certain
transmission ratio.

**Drive the servo**

Send PWM signals to the servo signal line to control its output. The
duty cycle of PWM directly determines the position of the output shaft.
The period is usually 20 milliseconds and is typically set to generate
pulses at a frequency of 50Hz.

For example (180° servo):

When we send a pulse width of 1.5 milliseconds (ms) to the 180° servo,
the output shaft of the servo will move to the middle position (90
degrees);

If the pulse width is 0.5ms, the output shaft will move to 0 degree;

If the pulse width is 2.5ms, the output shaft will move to 180 degree;

.. image:: ./media/A5545.png
   :alt: Img

**Parameters:**

-  Operating voltage: DC 3.3V~5V

-  Operating temperature: -10°C ~ +50°C

-  Dimensions: 32.25mm x 12.25mm x 30.42mm

-  Interface: 3pin interface with a spacing of 2.54mm

.. _4.-Wiring-Diagram:

4. Wiring Diagram
^^^^^^^^^^^^^^^^^

.. image:: ./media/A606.png
   :alt: Img

When using the ultrasonic sensor and servo, we must connect an external
power supply and turn the DIP switch to ON.

.. image:: ./media/A902.png
   :alt: Img

.. image:: ./media/A701.png
   :alt: Img

.. _5.-Code-Flow:

5. Code Flow
^^^^^^^^^^^^

.. image:: ./media/A716.png
   :alt: Img

.. _6.-Test-Code:

6. Test Code
^^^^^^^^^^^^

The code file is provided in folder Project 04：Smart-Parking, file
Project-04-Smart-Parking.py.

.. image:: ./media/A3345.png
   :alt: Img

**Complete code:** The threshold in the condition 10 can be modified
according to actual conditions.

.. code:: python

   '''
   Function: smart parking
   Compiling IDE: MU 1.2.0
   Author: https://docs.keyestudio.com
   '''
   # import related libraries
   from microbit import *
   import ustruct
   import machine
   from time import sleep_us

   distance = 0              # set variable distance initial value to 0
   lastEchoDuration = 0      # set variable lastEchoDuration initial value to 0

   val = Image("09990:""09090:""09990:""09000:""09000")  # set iamge
   display.show(val)        # LED matrix shows image
   pin0.write_analog(25.6)    # set P0 pin analog to 25.6, servo angle to 0°
   sleep(200)

   while True:
       pin0.set_analog_period(20) # set servo frequency
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
       if distance < 10:          # if distance < 10cm
          pin0.write_analog(77)   # servo rotate to 90°
          sleep(2000)
       else:  # or
          sleep(2000)
          pin0.write_analog(25.6)
          sleep(2000)

.. _7.-Test-Result:

7. Test Result
^^^^^^^^^^^^^^

Click “Flash” to load the code to the micro:bit board.

.. image:: ./media/A3400.png
   :alt: Img

After downloading the code to the board, **power on via micro USB cable
or external power supply(turn the DIP switch to ON)**, and press the
reset button on the board.

.. image:: ./media/A455.png
   :alt: Img

When the ultrasonic sensor detect a vehicle (or thing) approaching, the
servo controls the lift rod to raise; If the sensor detects it moving
away, the servo will lower the lift rod.

ATTENTION: If the wiring is correct but you cannot see the results,
press the reset button on the back of the board.

.. image:: ./media/A021.gif
   :alt: Img

.. _Project-05:-Car-Dial:

Project 05: Car Dial
~~~~~~~~~~~~~~~~~~~~

.. _1.-Overview:

1. Overview
^^^^^^^^^^^

In this project, we combine an adjustable potentiometer, a servo and a
beautiful dial card to make a simple car dial model.

.. _2.-Components:

2. Components
^^^^^^^^^^^^^

.. container:: table-wrapper

   +-----------------------+-----------------------+-----------------------+
   | |image48|             | |image49|             | |image50|             |
   +=======================+=======================+=======================+
   | micro:bit board \*1   | micro:bit T-type      | micro USB cable \*1   |
   |                       | expansion board \*1   |                       |
   +-----------------------+-----------------------+-----------------------+
   | |image51|             | |image52|             | |image53|             |
   +-----------------------+-----------------------+-----------------------+
   | potentiometer \*1     | servo \*1             | jump wires            |
   +-----------------------+-----------------------+-----------------------+
   | |image54|             | |image55|             | |image56|             |
   +-----------------------+-----------------------+-----------------------+
   | breadboard \*1        | battery holder \*1    | potentiometer card    |
   |                       | (self-provided AA     | \*1                   |
   |                       | batteries \*2)        |                       |
   +-----------------------+-----------------------+-----------------------+
   | |image57|             |                       |                       |
   +-----------------------+-----------------------+-----------------------+
   | car dial card*1       |                       |                       |
   +-----------------------+-----------------------+-----------------------+

.. _3.-Components-Knowledge:

3. Components Knowledge
^^^^^^^^^^^^^^^^^^^^^^^

**potentiometer**

.. image:: ./media/A350.png
   :alt: Img

A potentiometer is also a resistor element with three contacts, whose
resistance value can be adjusted according to some regularity.

They come in all shapes, sizes and values, but they all have the
followings in common:

① Three terminals (or connection points).

② A movable knob or slider that can change the resistance between the
intermediate terminal and any external terminal.

③ As the knob is moved, the resistance between the intermediate terminal
and any external terminal varies from 0Ω to its maximum.

The circuit symbol of potentiometer:

.. image:: ./media/A654.png
   :alt: Img

(1). As a voltage divider

The potentiometer is a continuously adjustable resistor. When you rotate
its slider, the moving contact slides across the resistor. At this
point, a voltage can be output according to the voltage applied to
potentiometer and the angle or stroke of rotation of the movable slider.

(2). As a variable resistor

When potentiometer is used as a variable resistor, connect its
intermediate terminal to one of two additional terminals in the circuit.
In this way, you can obtain a steady and continuously varying resistance
value within the range of it.

(3). As a current controller

When it is used as a current controller, the moving contact must be
connected as one of the output terminals.

.. _4.-Wiring-Diagram:

4. Wiring Diagram
^^^^^^^^^^^^^^^^^

.. image:: ./media/A812.png
   :alt: Img

When using the servo, we must connect an external power supply and turn
the DIP switch to ON.

.. image:: ./media/A902.png
   :alt: Img

.. image:: ./media/A836.png
   :alt: Img

.. _5.-Code-Flow:

5. Code Flow
^^^^^^^^^^^^

.. image:: ./media/A0854.png
   :alt: Img

.. _6.-Test-Code:

6. Test Code
^^^^^^^^^^^^

The code file is provided in folder Project 05：Car Dial, file
Project-05-Car-Dial.py.

.. image:: ./media/A3438.png
   :alt: Img

**Complete code:**

.. code:: python

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

.. _7.-Test-Result:

7. Test Result
^^^^^^^^^^^^^^

Click “Flash” to load the code to the micro:bit board.

.. image:: ./media/A3457.png
   :alt: Img

After downloading the code to the board, **power on via micro USB cable
or external power supply(turn the DIP switch to ON)**, and press the
reset button on the board.

.. image:: ./media/A455.png
   :alt: Img

Rotate the knob on potentiometer and the servo moves the pointer on the
dial.

ATTENTION: If the wiring is correct but you cannot see the results,
press the reset button on the back of the board.

.. image:: ./media/A706.gif
   :alt: Img

.. _Project-06:-Music-Party:

Project 06: Music Party
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./media/A1317.png
   :alt: Img

.. _1.-Overview:

1. Overview
^^^^^^^^^^^

When we clap our hands, the microphone on the board picks up sound
signals, and the speaker plays a cheerful birthday song while the RGB
LED emits dazzling light.

.. _2.-Components:

2. Components
^^^^^^^^^^^^^

.. container:: table-wrapper

   +-----------------------+-----------------------+-----------------------+
   | |image58|             | |image59|             | |image60|             |
   +=======================+=======================+=======================+
   | micro:bit board \*1   | micro:bit T-type      | micro USB cable \*1   |
   |                       | expansion board \*1   |                       |
   +-----------------------+-----------------------+-----------------------+
   | |image61|             | |image62|             | |image63|             |
   +-----------------------+-----------------------+-----------------------+
   | red LED \*1           | 220Ω resistor \*3     | jump wire \*2         |
   +-----------------------+-----------------------+-----------------------+
   | |image64|             | |image65|             | |image66|             |
   +-----------------------+-----------------------+-----------------------+
   | breadboard \*1        | battery holder \*1    | RGB card \*1          |
   |                       | (self-provided AA     |                       |
   |                       | batteries \*2)        |                       |
   +-----------------------+-----------------------+-----------------------+

.. _3.-Components-Knowledge:

3. Components Knowledge
^^^^^^^^^^^^^^^^^^^^^^^

**Microphone**

A high-quality digital microphone is integrated on the front side of the
micro:bit V2 board to detect sound and audio signals. The chip that
controls and processes the microphone is on its back.

.. image:: ./media/A1317.png
   :alt: Img

The microphone is in a small round hole on the front of the board, which
is convenient to capture surrounding sound signals. Just place the
micro:bit board face up when using. Next to the hole is a microphone LED
indicator. When the micro:bit measures sound levels, the indicator will
light up.

.. image:: ./media/A116.png
   :alt: Img

**RGB LED**

.. image:: ./media/A2127.png
   :alt: Img

RGB LED is imaged in the intersection of three primary colors (RGB):
red, green and blue. Most colors can be synthesized by RGB in different
proportions. The red, green and blue LEDs are packaged in a transparent
plastic case to emit colors of light by changing the input voltage of R,
G and B pins.

.. image:: ./media/A137.png
   :alt: Img

**Trichromatic theory:**

.. image:: ./media/A150.png
   :alt: Img

RGB LED can be divided into two types: common anode and common cathode:

In a common cathode RGB LED, the three LEDs share a negative connection
(cathode);

In a common anode RGB LED, the three LEDs share a positive connection
(anode).

.. image:: ./media/A209.png
   :alt: Img

Note: Herein, we provide a common cathode RGB LED.

**RGB LED pins:**

RGB LED boasts 4 pins: GND(the longest one), R(red), G(green) and
B(blue). Place the RGB LED as shown below, pins from left to right are
red, GND, green and blue.

.. image:: ./media/A239.png
   :alt: Img

.. _4.-Wiring-Diagram:

4. Wiring Diagram
^^^^^^^^^^^^^^^^^

.. image:: ./media/A308.png
   :alt: Img

.. image:: ./media/A325.png
   :alt: Img

.. _5.-Code-Flow:

5. Code Flow
^^^^^^^^^^^^

.. image:: ./media/A343.png
   :alt: Img

.. _6.-Test-Code:

6. Test Code
^^^^^^^^^^^^

The code file is provided in folder Project 06：Music Party, file
Project-06-Music-Party.py.

.. image:: ./media/A3523.png
   :alt: Img

**Complete code:**

.. code:: python

   '''
   Function: Clap your hands, the microbit microphone receives the sound signal, the music sounds, and the RGB emits a dazzling light to simulate a musical party
   Compiling IDE: MU 1.2.0
   Author: https://docs.keyestudio.com
   '''
   # import related libraries
   from microbit import *
   import music

   display.clear() # clear LED matrix

   while True:
       if microphone.current_event() == SoundEvent.LOUD:  # If the microphone picks up a loud signal
          music.play(["G3:4", "G3", "A4"]) # the speaker plays some tones
          pin1.write_analog(1023)      # P1 analog value is 1023,RGB is red
          pin2.write_analog(0)
          # pin3.write_analog(0)
          sleep(100)
          music.play(["G4:4", "C5", "B4"])
          pin1.write_analog(0)         # P1 analog value is 0,RGB is not red
          pin2.write_analog(1023)      # P2 analog value is 1023,RGB is green
          # pin3.write_analog(0)
          sleep(100)
          pin1.write_analog(10)
          pin2.write_analog(10)
          # pin3.write_analog(1023)      # P3 analog value is 1023,RGB is blue
          sleep(100)
          music.play(["G4:4", "D5", "C5"])
          pin1.write_analog(123)
          pin2.write_analog(123)
          # pin3.write_analog(0)
          sleep(100)
          music.play(["G4:4", "D5", "C5"])
          pin1.write_analog(1023)
          pin2.write_analog(400)
          # pin3.write_analog(1023)
          sleep(100)
          music.play(["G3:4", "G3", "G4"])
          pin1.write_analog(10)
          pin2.write_analog(1023)
          # pin3.write_analog(1023)
          sleep(100)
          pin1.write_analog(1023)
          pin2.write_analog(1023)
          # pin3.write_analog(1023)
          sleep(100)
          music.play(["E5:4", "C5", "B4", "A4"])
          pin1.write_analog(32)
          pin2.write_analog(184)
          # pin3.write_analog(336)
          sleep(100)
          pin1.write_analog(640)
          pin2.write_analog(328)
          # pin3.write_analog(180)
          sleep(100)
          music.play(["F5:4", "F5", "E5"])
          pin1.write_analog(552)
          pin2.write_analog(172)
          # pin3.write_analog(904)
          sleep(100)
          pin1.write_analog(1020)
          pin2.write_analog(796)
          # pin3.write_analog(560)
          sleep(100)
          music.play(["C5:4", "D5", "C5"])
          pin1.write_analog(136)
          pin2.write_analog(560)
          # pin3.write_analog(140)
          sleep(100)
          pin1.write_analog(0)
          pin2.write_analog(0)
          # pin3.write_analog(0)
          sleep(100)
   if microphone.current_event() == SoundEvent.QUIET:  # If the microphone picks up a quie signal
          pin1.write_analog(0)
          pin2.write_analog(0)

.. _7.-Test-Result:

7. Test Result
^^^^^^^^^^^^^^

Click “Flash” to load the code to the micro:bit board.

.. image:: ./media/A3540.png
   :alt: Img

After downloading the code to the board, **power on via micro USB cable
or external power supply(turn the DIP switch to ON)**, and press the
reset button on the board.

.. image:: ./media/A455.png
   :alt: Img

When we clap our hands, the microphone on the board picks up sound
signals, and the speaker plays a cheerful birthday song while the RGB
LED emits dazzling light. Isn’t the music party in a happy and joyful
atmosphere?

ATTENTION: If the wiring is correct but you cannot see the results,
press the reset button on the back of the board.

.. image:: ./media/A757.gif
   :alt: Img

.. _Project-07:-Environment-Monitoring:

Project 07: Environment Monitoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _1.-Overview:

1. Overview
^^^^^^^^^^^

On the OLED, the smart environment monitoring system displays the
temperature and humidity values detected by the DHT11 sensor in real
time, as well as the brightness level value of ambient light detected by
the on-board light sensor.

.. _2.-Components:

2. Components
^^^^^^^^^^^^^

.. container:: table-wrapper

   +-----------------------+-----------------------+-----------------------+
   | |image67|             | |image68|             | |image69|             |
   +=======================+=======================+=======================+
   | micro:bit board \*1   | micro:bit T-type      | micro USB cable \*1   |
   |                       | expansion board \*1   |                       |
   +-----------------------+-----------------------+-----------------------+
   | |image70|             | |image71|             | |image72|             |
   +-----------------------+-----------------------+-----------------------+
   | XHT11 temperature and | OLED module \*1       | DuPont wires          |
   | humidity sensor \*1   |                       |                       |
   +-----------------------+-----------------------+-----------------------+
   | |image73|             | |image74|             | |image75|             |
   +-----------------------+-----------------------+-----------------------+
   | breadboard \*1        | jump wires            | battery holder \*1    |
   |                       |                       | (self-provided AA     |
   |                       |                       | batteries \*2)        |
   +-----------------------+-----------------------+-----------------------+
   | |image76|             | |image77|             |                       |
   +-----------------------+-----------------------+-----------------------+
   | cloud card \*1        | OLED card \*1         |                       |
   +-----------------------+-----------------------+-----------------------+

.. _3.-Component-Knowledge:

3. Component Knowledge
^^^^^^^^^^^^^^^^^^^^^^

**XHT11 temperature and humidity sensor**

.. image:: ./media/A2637.png
   :alt: Img

XHT11 temperature and humidity sensor is a composite sensor with
calibrated digital signal output, which can detect the humidity and
temperature in the air.

**Accuracy**: humidity ±5%RH, temperature ±2℃

**Detection range**: humidity 5%RH ~ 95%RH, temperature -25℃ ~ +60℃

The sensor uses special digital module acquisition and temperature and
humidity sensing technology to ensure extremely high reliability and
excellent long-term stability. It includes a resistive humidity sensing
element and an NTC temperature sensing element, which is very suitable
for measurement with relatively low accuracy and real-time requirements.

**XHT11 communication mode:**

Single bus communication is adopted. It means that there is only one
data line for data exchange and control in the system.

-  Definition of data bits transmitted by single bus:

Single bus data format: 40 bits of data are transmitted at a time, with
the high bit coming first.

8bit humidity integer + 8bit humidity decimal + 8bit temperature integer
+ 8bit temperature decimal + 8bit parity bit (The decimal part of the
humidity is 0)

-  Definition of parity bit:

8bit humidity integer + 8bit humidity decimal + 8bit temperature integer
+ 8bit temperature decimal. 8bit parity bit = the last 8 bits of the
obtained result

-  Data timeline:

After the user host (MCU) sends a starting signal, the XHT11 switches
from low power mode to high speed mode. After the starting signal, XHT11
sends a response signal and 40bit data, and triggers a signal
acquisition.

-  The signal transmission is shown in the figure:

.. image:: ./media/A229.png
   :alt: Img

**Parameters**

-  Operating voltage: DC 3.3V to 5V

-  Operating current: 2.1mA

-  Maximum power: 0.0105W

-  Temperature range: -25℃ ~ +60℃ (± 2℃)

-  Humidity range: 5%RH ~ 95%RH (accuracy ±5%RH under around 25 ° C)

**Microbit Light Sensor**

.. image:: ./media/A0335.png
   :alt: Img

A light sensor is an input device that measures the brightness of
external light. The micro:bit board does not include a built-in light
sensor. It detects and senses ambient brightness by an LED matrix that
repeatedly convert the light intensity into a value input, and then the
voltage attenuation time is sampled. In this way, the detected
brightness level is a relative value.

.. _4.-Wiring-Diagram:

4. Wiring Diagram
^^^^^^^^^^^^^^^^^

.. image:: ./media/A409.png
   :alt: Img

When using the OLED display, we must connect an external power supply
and turn the DIP switch to ON.

.. image:: ./media/A904.png
   :alt: Img

.. image:: ./media/A554.png
   :alt: Img

.. _5.-Import-Library:

5. Import Library
^^^^^^^^^^^^^^^^^

If you haven’t added the required library files yet (DHT11 and
oled_ssd1306), please import it referring to `How Mu Import Library to
Micro:bit <https://docs.keyestudio.com/projects/FKS0004/en/latest/docs/MicroPython_Tutorial/MicroPython_Tutorial.html#how-mu-import-library-to-micro-bit>`__.

.. _6.-Code-Flow:

6. Code Flow
^^^^^^^^^^^^

.. image:: ./media/A638.png
   :alt: Img

.. _7.-Test-Code:

7. Test Code
^^^^^^^^^^^^

The code file is provided in folder Project 07：Environment
Monitoring中找文件Project-07-Environment-Monitoring.py.

.. image:: ./media/A3641.png
   :alt: Img

**Complete code:**

.. code:: python

   '''
   Function: OLED displays temperature and humidity values and brightness level values in real time to simulate intelligent environment detection
   Compiling IDE: MU 1.2.0
   Author: https://docs.keyestudio.com
   '''
   # import related libraries
   import oled_ssd1306 as oled
   from microbit import *
   from DHT11 import *

   val = Image("90900:""09090:""90009:""90009:""99999")  # Set pattern
   display.show(val)   # LED matrix displays the set pattern

   #initialize and clear oled
   oled.initialize()
   oled.clear_oled()

   sensor = DHT11(pin1)  # set temperature and humidity pins

   while True:
       oled.clear_oled() # clear oled
       sensor.read()     # read the temperature and humidity values
       T = sensor.temp   # store the temperature values in T
       H = sensor.humid  # store the humidity values in H
       L = display.read_light_level()  # read the brightness level value of the light and store it in L
       oled.add_text(1, 0, 'T:' + str(T) + 'C')   # Display the temperature value at the corresponding position of the OLED
       oled.add_text(1, 1, 'H:' + str(H) + '%')   # Display the humidity value at the corresponding position of the OLED
       oled.add_text(1, 2, 'L:' + str(L))         # Display the brightness level value at the corresponding position of the OLED
       sleep(2000)

.. _8.-Test-Result:

8. Test Result
^^^^^^^^^^^^^^

Click “Flash” to load the code to the micro:bit board.

.. image:: ./media/A3710.png
   :alt: Img

After downloading the code to the board, **power on via micro USB cable
or external power supply(turn the DIP switch to ON)**, and press the
reset button on the board.

.. image:: ./media/A455.png
   :alt: Img

The OLED displays the temperature and humidity values and the light
brightness level in real time.

ATTENTION: If the wiring is correct but you cannot see the results,
press the reset button on the back of the board.

.. image:: ./media/A838.gif
   :alt: Img

.. _Project-08:-Anti-theft-Alarm:

Project 08: Anti-theft Alarm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _1.-Overview:

1. Overview
^^^^^^^^^^^

When the smart anti-theft alarm detects that the anti-theft box has been
moved, the speaker on the micro:bit board will alarm and the red LED
will flash.

.. _2.-Components:

2. Components
^^^^^^^^^^^^^

.. container:: table-wrapper

   +-----------------------+-----------------------+-----------------------+
   | |image78|             | |image79|             | |image80|             |
   +=======================+=======================+=======================+
   | micro:bit board \*1   | micro:bit T-type      | micro USB cable \*1   |
   |                       | expansion board \*1   |                       |
   +-----------------------+-----------------------+-----------------------+
   | |image81|             | |image82|             | |image83|             |
   +-----------------------+-----------------------+-----------------------+
   | red LED \*1           | 220Ω resistor \*1     | jump wire \*2         |
   +-----------------------+-----------------------+-----------------------+
   | |image84|             | |image85|             | |image86|             |
   +-----------------------+-----------------------+-----------------------+
   | breadboard \*1        | battery holder \*1    | alarm card \*1        |
   |                       | (self-provided AA     |                       |
   |                       | batteries \*2)        |                       |
   +-----------------------+-----------------------+-----------------------+

.. _3.-Components-Knowledge:

3. Components Knowledge
^^^^^^^^^^^^^^^^^^^^^^^

**Accelerometer**

.. image:: ./media/A026.png
   :alt: Img

The micro:bit board boasts a built-in LSM303AGR acceleration sensor (we
called accelerometer) which includes standard, fast, plus and high-speed
mode (100 kHz, 400 kHz, 1 MHz and 3.4 MHz) of I2C serial bus interface
and SPI serial standard interface for external communication, with
resolution of 8/10/12 bits and range of ±2g, ±4g, or ±8g.

When the micro:bit board is at rest or in uniform motion, the
accelerometer only detects the acceleration of gravity. If it is
slightly swung, the detected acceleration is much less than the that of
gravity, so the difference can be ignored. Therefore, we mainly detect
the change of gravitational acceleration on x, y, and z axes.

.. _4.-Wiring-Diagram:

4. Wiring Diagram
^^^^^^^^^^^^^^^^^

.. image:: ./media/A219.png
   :alt: Img

The board control pin of LED is P1 (the pin of T-type expansion board is
digital 1).

.. _5.-Code-Flow:

5. Code Flow
^^^^^^^^^^^^

.. image:: ./media/A4434.png
   :alt: Img

.. _6.-Test-Code:

6. Test Code
^^^^^^^^^^^^

The code file is provided in folder Project 08：Burglar Alarm, file
Project-08-Burglar-Alarm.py.

.. image:: ./media/A3743.png
   :alt: Img

**Complete code:**

After importing the code, if the buzzer keeps sounding even though the
breadboard is not moved; it may be caused by geographical factors. You
can modify the threshold in the condition -60 and 50 according to actual
conditions.

.. code:: python

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

.. _7.-Test-Result:

7. Test Result
^^^^^^^^^^^^^^

Click “Flash” to load the code to the micro:bit board.

.. image:: ./media/A3757.png
   :alt: Img

After downloading the code to the board, **power on via micro USB cable
or external power supply(turn the DIP switch to ON)**, and press the
reset button on the board.

.. image:: ./media/A455.png
   :alt: Img

After downloading the code to the board, move the breadboard. If the
acceleration value x＜-60 or x＞50, the speaker on the board alarms and
the LED flashes, and the micro:bit LED matrix shows |image87|.
Otherwise, the speaker makes no sound and LED is off, and the micro:bit
LED matrix shows |image88|.

ATTENTION: If the wiring is correct but you cannot see the results,
press the reset button on the back of the board.

.. image:: ./media/A936.gif
   :alt: Img

.. _4.-Troubleshooting:

4. Troubleshooting
------------------

**Errors for Uploading Codes**

-  If messy icons are displayed on the matrix of the board after
   uploading code, check if any characters have been accidentally added
   or deleted. You may click “check”\ |image89|. But note that some are
   not errors, just warnings.

-  If the code is with a library, check whether the library is uploaded
   to the board. See “\ **How Mu Import Library to Micro:bit**\ ”. And
   then check if any characters have been accidentally added or deleted.

**No Printings on REPL**

-  After uploading code, click “REPL” |image90| and it prints nothing.
   In this case, we need to press the reset button on the back of
   micro:bit board.

.. image:: ./media/A455.png
   :alt: Img

.. |Img| image:: ./media/A503.png
.. |image1| image:: ./media/A903.png
.. |image2| image:: ./media/A910.png
.. |image3| image:: ./media/A850.png
.. |image4| image:: ./media/A858.png
.. |image5| image:: ./media/A906.png
.. |image6| image:: ./media/A937.png
.. |image7| image:: ./media/A944.png
.. |image8| image:: ./media/A950.png
.. |image9| image:: ./media/A017.png
.. |image10| image:: ./media/A024.png
.. |image11| image:: ./media/A920.png
.. |image12| image:: ./media/A512.png
.. |image13| image:: ./media/A518.png
.. |image14| image:: ./media/A527.png
.. |image15| image:: ./media/A850.png
.. |image16| image:: ./media/A858.png
.. |image17| image:: ./media/A906.png
.. |image18| image:: ./media/A937.png
.. |image19| image:: ./media/A5652.png
.. |image20| image:: ./media/A658.png
.. |image21| image:: ./media/A944.png
.. |image22| image:: ./media/A950.png
.. |image23| image:: ./media/A017.png
.. |image24| image:: ./media/A024.png
.. |image25| image:: ./media/A020.png
.. |image26| image:: ./media/A850.png
.. |image27| image:: ./media/A858.png
.. |image28| image:: ./media/A906.png
.. |image29| image:: ./media/A356.png
.. |image30| image:: ./media/A406.png
.. |image31| image:: ./media/A415.png
.. |image32| image:: ./media/A017.png
.. |image33| image:: ./media/A950.png
.. |image34| image:: ./media/A024.png
.. |image35| image:: ./media/A315.png
.. |image36| image:: ./media/A557.png
.. |image37| image:: ./media/A850.png
.. |image38| image:: ./media/A858.png
.. |image39| image:: ./media/A906.png
.. |image40| image:: ./media/A356.png
.. |image41| image:: ./media/A309.png
.. |image42| image:: ./media/A415.png
.. |image43| image:: ./media/A017.png
.. |image44| image:: ./media/A950.png
.. |image45| image:: ./media/A024.png
.. |image46| image:: ./media/A336.png
.. |image47| image:: ./media/A131.png
.. |image48| image:: ./media/A850.png
.. |image49| image:: ./media/A858.png
.. |image50| image:: ./media/A906.png
.. |image51| image:: ./media/A350.png
.. |image52| image:: ./media/A309.png
.. |image53| image:: ./media/A950.png
.. |image54| image:: ./media/A017.png
.. |image55| image:: ./media/A024.png
.. |image56| image:: ./media/A233.png
.. |image57| image:: ./media/A1326.png
.. |image58| image:: ./media/A850.png
.. |image59| image:: ./media/A858.png
.. |image60| image:: ./media/A906.png
.. |image61| image:: ./media/A500.png
.. |image62| image:: ./media/A944.png
.. |image63| image:: ./media/A950.png
.. |image64| image:: ./media/A017.png
.. |image65| image:: ./media/A024.png
.. |image66| image:: ./media/A621.png
.. |image67| image:: ./media/A850.png
.. |image68| image:: ./media/A858.png
.. |image69| image:: ./media/A906.png
.. |image70| image:: ./media/A2637.png
.. |image71| image:: ./media/A406.png
.. |image72| image:: ./media/A415.png
.. |image73| image:: ./media/A017.png
.. |image74| image:: ./media/A950.png
.. |image75| image:: ./media/A024.png
.. |image76| image:: ./media/A0715.png
.. |image77| image:: ./media/A557.png
.. |image78| image:: ./media/A850.png
.. |image79| image:: ./media/A858.png
.. |image80| image:: ./media/A906.png
.. |image81| image:: ./media/A937.png
.. |image82| image:: ./media/A944.png
.. |image83| image:: ./media/A950.png
.. |image84| image:: ./media/A017.png
.. |image85| image:: ./media/A024.png
.. |image86| image:: ./media/A952.png
.. |image87| image:: ./media/A706.png
.. |image88| image:: ./media/A720.png
.. |image89| image:: ./media/A5457.png
.. |image90| image:: ./media/A5530.png
