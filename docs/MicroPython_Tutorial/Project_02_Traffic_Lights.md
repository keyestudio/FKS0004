### Project 02: Verkeerslichten

#### 1. Overzicht

In dit project gebruiken we drie LEDs (rood, geel en groen), een speaker op de micro:bit board en een 5x5 LED-matrix om een model van verkeerslichten te maken.

#### 2. Componenten

|              ![Img](./media/A850.png)              |       ![Img](./media/A858.png)       | ![Img](./media/A906.png) |
| :-----------------------------------------------: | :---------------------------------: | :---------------------: |
|                micro:bit board *1                 | micro:bit T-type uitbreidingsboard *1 |   micro USB-kabel *1    |
|              ![Img](./media/A937.png)              |      ![Img](./media/A5652.png)       | ![Img](./media/A658.png) |
|                    rode LED *1                     |            gele LED *1              |      groene LED *1      |
|              ![Img](./media/A944.png)              |       ![Img](./media/A950.png)       | ![Img](./media/A017.png) |
|                 220Ω weerstand *3                  |             jumper draden           |      breadboard *1      |
|              ![Img](./media/A024.png)              |       ![Img](./media/A020.png)       |                         |
| batterijhouder *1 <br> (<span style="color: rgb(255, 76, 65);">zelf meegebrachte AA batterijen *2</span>)|       verkeerslichten kaart *1       |                         |

#### 3. Componentkennis

**Speaker**

![Img](./media/A833.png)

Micro:bit wordt geleverd met een speaker, wat het gemakkelijk maakt om geluid te maken in je project.

#### 4. Bedradingsschema

![Img](./media/A908.png)

<span style="color: rgb(255, 76, 65);">**Opmerking:** de micro:bit board moet in het T-type uitbreidingsboard worden gestoken zoals hieronder getoond. De LED-matrix van de micro:bit board moet aan dezelfde zijde zitten als het logo van het uitbreidingsboard.</span>

![Img](./media/A940.png)

#### 5. Code Flow

![Img](./media/A5956.png)

#### 6. Testcode

Het codebestand is te vinden in de map Project 02：Traffic Lights, bestand Project-02-Traffic-Lights\.py.

![Img](./media/A250.png)

**Volledige code:** 

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

#### 7. Testresultaat

Klik op “<span style="color: rgb(255, 76, 65);">Flash</span>” om de code op de micro:bit board te laden.

![Img](./media/A353.png)

Na het downloaden van de code naar de board, **zet de voeding aan via micro USB-kabel of externe voeding (zet de DIP-schakelaar op ON)**, en druk op de resetknop op de board.

![Img](./media/A455.png)

De groene LED gaat aan en de 5×5 LED-matrix telt 6 seconden af. Nadat de groene LED uitgaat, knippert de gele LED en telt de matrix 3 seconden af met geluid van de speaker. Tot slot gaat de rode LED aan met een aftelling van 6 seconden. Deze handelingen herhalen zich.

<span style="color: rgb(255, 76, 65);">**LET OP:** Als de bedrading correct is maar je ziet geen resultaat, druk dan op de resetknop aan de achterkant van de board.</span>

![Img](./media/A459.gif)

<span style="color: rgb(255, 76, 65);">**Bij voeding via externe voeding, zet de DIP-schakelaar op ON.**</span>

![Img](./media/A904.png)
