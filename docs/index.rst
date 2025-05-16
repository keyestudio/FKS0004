.. _**After-sales-Service**:

**After-sales Service**
=======================

If something is found missing or broken, or you have some difficulty
learning the kit, please feel free to contact us. Welcome to send email
to us: service@keyestudio.com

We will endeavor to update projects and products continuously from your
sincere advice! Thanks!

.. _Product-Introduction:

Product Introduction
====================

**FKS0004 Keyestudio microbit learning kit**

.. image:: ./media/A30.jpg
   :alt: Img

This learning kit covers sensors and components as well as a Micro:bit
board, and the included animation card makes experiments more exquisite
and beautiful. It not only enables makers to experience the charm and
practicality of technology, but also cultivates their logical thinking.

At the same time, it fully demonstrates the practical value and
educational significance of the application of science and technology.

.. _Obtain-Resources-(**Important**):

Obtain Resources (**Important**)
================================

**Download
(Important)**\ ::download:`MakeCode_Tutorial <MakeCode_Tutorial.7z>`
.

**Special reminder:** After downloading MakeCode_Tutorial file, extract
it. The folder includes codes, USB driver, etc.

**Download
(Important)**\ ：:download:`MicroPython_Tutorial <MicroPython_Tutorial.7z>`
.

**Special reminder:** After downloading MicroPython_Tutorial file,
extract it. The folder includes codes, Library, USB driver, etc.

.. _Product-Kit-List:

Product Kit List
================

Please check the list to ensure that all parts are intact. If you find
missing ones, please contact our sales staff immediately.

.. container:: table-wrapper

   == ========= ================================ ===
   #  PIC       NAME                             QTY
   == ========= ================================ ===
   1  |Img|     micro:bit V2.0 main board        1
   2  |image1|  breadboard                       1
   3  |image2|  ultrasonic sensor                1
   4  |image3|  Micro USB cable                  1
   5  |image4|  jump wire                        1
   6  |image5|  servo                            1
   7  |image6|  micro:bit T-type expansion board 1
   8  |image7|  DuPont wire                      1
   9  |image8|  XHT11 (compatible with DHT11)    1
   10 |image9|  OLED module                      1
   11 |image10| RGB LED                          1
   12 |image11| potentiometer                    1
   13 |image12| 220Ω resistor                    5
   14 |image13| 1kΩ resistor                     5
   15 |image14| 10kΩ resistor                    5
   16 |image15| red LED                          5
   17 |image16| yellow LED                       5
   18 |image17| green LED                        5
   12 |image18| resistance card                  1
   12 |image19| battery holder                   1
   13 |image20| AA battery (self-provided)       2
   14 |image21| card                             1
   15 |image22| card                             1
   == ========= ================================ ===

.. _T-type-Expansion-Board:

T-type Expansion Board
======================

.. image:: ./media/A718.png
   :alt: Img

.. _1.-Introduction:

1. Introduction
---------------

In the education market, micro:bit boards are becoming more and more
popular. However, it is not easy to test a single micro:bit board with
other sensor modules. Hence, we have specially designed this micro:bit
T-type expansion board.

Micro:bit T-type expansion board splits all the IO ports on the board
into pins with a spacing of 2.54mm (GND, 5V, 3V3, Signal), which is very
convenient to connect with other sensor modules and electronic
components.

In addition, you can power the micro:bit board through the white DC port
(DC 3V) or micro USB interface (DC 5V) on the expansion board.

The expansion board is able to boost or converse the voltage. If it is
powered by an external power 3V, it can output 3.3V and 5V voltages.

.. _2.-Features:

2. Features
-----------

-  Input voltage: white DC port (DC 3V) or micro USB interface (DC 5V)

-  Output voltage: 3.3V or 5V

-  The IO ports of micro:bit is divided into pins with a spacing of
   2.54mm

-  Dimensions: 64mm x 56mm x 18mm

-  Weight: 13.1g

.. _3.-Pin-out:

3. Pin-out
----------

.. image:: ./media/A854.png
   :alt: Img

.. _About-Micro:bit:

About Micro:bit
===============

.. _1.-What-is-Micro:bit:

1. What is Micro:bit
--------------------

Launched by British Broadcasting Corporation (BBC), micro:bit is a
microcomputer development board designed for programming education for
teenagers.

Though it is just the size of a credit card, the board integrates many
components, including a 5x5 LED matrix, 2 programmable buttons, an
accelerometer, a compass, a thermometer, a touch-sensitive logo and a
MEMS microphone, a low energy Bluetooth module and a buzzer. This
built-in buzzer plays all kinds of sounds without any external
equipment. Moreover, its sleeping mode lowers power consumption of
batteries when the Reset&Power button is long-pressed.

.. _1.1.-Micro:bit-V2-Board-Layout:

1.1. Micro:bit V2 Board Layout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./media/A549.png
   :alt: Img

.. _1.2.-Micro:bit-V2-Pin-out:

1.2. Micro:bit V2 Pin-out
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./media/A639.png
   :alt: Img

Micro:bit pin functions:

.. container:: table-wrapper

   +---------------------+-----------------------------------------------+
   | function            | pins                                          |
   +=====================+===============================================+
   | GPIO                | P0，P1，P2，P3，P4，P5，P6，P7，P8，P9        |
   |                     | ，P10，P11，P12，P13，P14，P15，P16，P19，P20 |
   +---------------------+-----------------------------------------------+
   | ADC/DAC             | P0，P1，P2，P3，P4，P10                       |
   +---------------------+-----------------------------------------------+
   | IIC                 | P19（SCL），P20（SDA）                        |
   +---------------------+-----------------------------------------------+
   | SPI                 | P13（SCK），P14（MISO），P15（MOSI）          |
   +---------------------+-----------------------------------------------+
   | PWM (commonly used) | P0，P1，P2，P3，P4，P10                       |
   +---------------------+-----------------------------------------------+
   | occupied            | P5(Button A)，P6(LED Col4)，P7(LED            |
   |                     | Col2)，P10(LED Col5)，P11(Button B)           |
   +---------------------+-----------------------------------------------+

For more please visit official website:

-  https://tech.microbit.org/hardware/edgeconnector/

-  https://microbit.org/guide/hardware/pins/

.. _1.3.-Notes-for-the-Application-of-Micro:bit-V2:

1.3. Notes for the Application of Micro:bit V2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. It is recommended to cover it with a silicone protector to prevent
   short circuit for it has a lot of sophisticated electronic
   components.

#. Its IO port is very weak in driving since it can merely handle
   current less than 300mA. Therefore, do not connect it with devices
   operating in large current, such as servo MG995 and DC motor, or it
   will get burnt. Furthermore, you must figure out the current
   requirements of the devices before you use them and it is generally
   recommended to use the board together with a Micro:bit shield.

#. It is recommended to power the main board via the USB interface or
   via the battery of 3V. The IO port of this board is 3V3, so it does
   not support sensors of 5V. If you need 5V, the expansion board is
   required to connect to an external power.

#. When using pins(P3, P4, P6, P7 and P10) shared with the LED dot
   matrix, block them from the matrix. Otherwise, the LED may display
   randomly and the data about connected sensors maybe wrong.

#. **Pin 19 and 20 can not be used as IO ports** though the Makecode
   shows they can. They can only be used for I2C communication.

#. The battery port of 3V cannot be connected with battery more than
   3.3V, or the board will be damaged.

#. Forbid to operate it on metal products to avoid short circuit.

Simply put, micro:bit is like a microcomputer which has made programming
at our fingertips and enhanced digital innovation.

.. _2.-Micro:bit-Driver:

2. Micro:bit Driver
-------------------

Micro:bit is free of driver installation. However, in case your computer
fail to recognize the main board, you need to install the diver.

**Driver installation instructions:**

Connect micro:bit main board to computer via USB cable.

.. image:: ./media/A252.png
   :alt: Img

In both MicroPython_Tutorial folder and MicroPython_Tutorial folder, we
provide driver files. You choose one of them. click the driver file to
“\ **Install**\ ”.

.. image:: ./media/A323a.png
   :alt: Img

.. image:: ./media/A323.png
   :alt: Img

.. image:: ./media/A327.png
   :alt: Img

“\ **Install**\ ” and “\ **Next**\ ”.

.. image:: ./media/A347.png
   :alt: Img

“\ **Install**\ ” and “\ **Finish**\ ”.

.. image:: ./media/A408.png
   :alt: Img

.. image:: ./media/A349.png
   :alt: Img

After that, enter “\ **Computer**\ ” —> “\ **Properties**\ ” —>
“\ **Device manager**\ ”:

.. image:: ./media/A427.png
   :alt: Img

.. |Img| image:: ./media/A107.png
.. |image1| image:: ./media/A314.png
.. |image2| image:: ./media/A332.png
.. |image3| image:: ./media/A400.png
.. |image4| image:: ./media/A457.png
.. |image5| image:: ./media/A516.png
.. |image6| image:: ./media/A534.png
.. |image7| image:: ./media/A602.png
.. |image8| image:: ./media/A620.png
.. |image9| image:: ./media/A636.png
.. |image10| image:: ./media/A652.png
.. |image11| image:: ./media/A221.png
.. |image12| image:: ./media/A237.png
.. |image13| image:: ./media/A257.png
.. |image14| image:: ./media/A316.png
.. |image15| image:: ./media/A333.png
.. |image16| image:: ./media/A401.png
.. |image17| image:: ./media/A416.png
.. |image18| image:: ./media/A434.png
.. |image19| image:: ./media/A452.png
.. |image20| image:: ./media/A757.png
.. |image21| image:: ./media/A3343.png
.. |image22| image:: ./media/A3237.png
