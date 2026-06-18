### Project 03: Ranging Bat

#### 1. Overzicht

Op basis van een ultrasone sensor detecteert de ranging bat de afstand van obstakels en toont deze in realtime op een OLED. Wanneer de afstand minder dan 10 cm is, geeft de speaker een alarm.

#### 2. Componenten

| ![Img](./media/A850.png) |       ![Img](./media/A858.png)       |              ![Img](./media/A906.png)              |
| :---------------------: | :---------------------------------: | :-----------------------------------------------: |
|   micro:bit board *1    | micro:bit T-type uitbreidingsbord *1 |                micro USB-kabel *1                 |
| ![Img](./media/A356.png) |       ![Img](./media/A406.png)       |              ![Img](./media/A415.png)              |
|  ultrasone sensor *1    |           OLED-module *1            |                   DuPont-draadjes                 |
| ![Img](./media/A017.png) |       ![Img](./media/A950.png)       |              ![Img](./media/A024.png)              |
|      breadboard *1      |             jump wires              | batterijhouder *1 <br> (<span style="color: rgb(255, 76, 65);">zelf meegebrachte AA-batterijen *2</span>)|
| ![Img](./media/A315.png) |       ![Img](./media/A557.png)       |                                                   |
|       bat card *1       |            OLED card *1             |                                                   |

#### 3. Kennis over componenten

**ultrasone sensor**

Ultrasone golven kaatsen terug wanneer ze een obstakel raken. We meten de afstand door het tijdsinterval te berekenen tussen het verzenden en ontvangen van de golven. Aangezien de voortplantingssnelheid van geluid in lucht constant is v=340m/s, berekenen we de afstand tussen de sensor en het obstakel: s=vt/2.

![Img](./media/A846.png)

De HC-SR04 ultrasone module integreert een zender en ontvanger. De eerste zet elektrische signalen (elektrische energie) om in hoogfrequente (buiten het gehoor van mensen) geluidsgolven (mechanische energie), terwijl de tweede het omgekeerde doet.

Het schema van de HC SR04:

![Img](./media/A642.png)

**Pin-definitie:**

![Img](./media/A702.png)

**Parameters:**

- Bedrijfsspanning: 5V
- Bedrijfsstroom: 12mA
- Minimale meetafstand: 2cm
- Maximale meetafstand: 200cm

**Werking:**

Een hoog niveau puls van minstens 10us wordt uitgegeven op de Trig-pin, en de module begint ultrasone golven uit te zenden. Tegelijkertijd wordt de Echo-pin hoog getrokken. Wanneer de module een ultrasone golf terug ontvangt bij een obstakel, wordt de Echo-pin laag getrokken. De duur van het hoge niveau van de Echo-pin is de totale tijd van golf van verzenden tot ontvangen: s=vt/2.

![Img](./media/A728.png)

**OLED-module**

OLED-technologie kenmerkt zich door rijke kleurweergave, hoog contrast en brede kijkhoek, wat zorgt voor heldere en levendige beelden, vooral uitstekend in zwart.

Elke pixel van het OLED-scherm zendt zelf licht uit zonder achtergrondverlichting, waardoor het relatief weinig stroom verbruikt. Met een kleine afmeting, hoge resolutie en laag stroomverbruik is het 0,9-inch OLED-scherm zeer geschikt voor draagbare apparaten.

![Img](./media/A636.png)

<span style="color: rgb(255, 76, 65);">**In dit project is de OLED-displaymodule aangesloten met de SDA-interface op pin P20 en SCL op pin P19.**</span>

**Parameters:**

- Bedrijfsspanning: DC 3.3V-5V

- Bedrijfsstroom: 30mA

- Interface: Pin-poorten met een afstand van 2,54mm

- Communicatiemodus: I2C

- Interne driverchip: SSD1306

- Resolutie: 128*64

- Kijkhoek: groter dan 150°

#### 4. Aansluitschema

![Img](./media/A1849.png)

<span style="color: rgb(255, 76, 65);">**Bij gebruik van het OLED-display en ultrasone sensor moeten we een externe voeding aansluiten en de DIP-schakelaar op ON zetten.**</span>

![Img](./media/A902.png)

![Img](./media/A1906.png)

#### 5. Bibliotheek importeren

Als je de benodigde bibliotheekbestanden (oled_ssd1306) nog niet hebt toegevoegd, importeer deze dan volgens [Hoe Mu bibliotheek importeert naar Micro:bit](https://docs.keyestudio.com/projects/FKS0004/en/latest/docs/MicroPython_Tutorial/MicroPython_Tutorial.html#how-mu-import-library-to-micro-bit).

#### 6. Codeflow

![Img](./media/A924.png)

#### 7. Testcode

Het codebestand is te vinden in de map Project 03：Ranging Bat, bestand Project-03-Ranging-Bat\.py.

![Img](./media/A302.png)

**Volledige code:** <span style="color: rgb(255, 76, 65);">**De drempelwaarde in de voorwaarde 10 kan worden aangepast aan de werkelijke situatie.**</span>

```python
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
```

#### 8. Testresultaat

Klik op “<span style="color: rgb(255, 76, 65);">Flash</span>” om de code naar het micro:bit board te laden.

![Img](./media/A3323.png)

Na het downloaden van de code naar het board, **zet de voeding aan via micro USB-kabel of externe voeding (zet de DIP-schakelaar op ON)**, en druk op de resetknop op het board.

![Img](./media/A455.png)

De OLED toont de afstand tussen de ultrasone sensor en het obstakel in realtime. Wanneer de afstand minder dan 10 cm is, geeft de speaker op het micro:bit board alarm.

<span style="color: rgb(255, 76, 65);"><span style="color: rgb(255, 76, 65);">**LET OP:** Als de bedrading correct is maar je ziet geen resultaat, druk dan op de resetknop aan de achterkant van het board.</span></span>

![Img](./media/A605.gif)
