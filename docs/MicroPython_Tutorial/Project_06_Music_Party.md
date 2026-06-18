### Project 06: Muziekfeest

![Img](./media/A1317.png)

#### 1. Overzicht

Wanneer we in onze handen klappen, vangt de microfoon op de board geluidssignalen op, en speelt de speaker een vrolijk verjaardagslied terwijl de RGB LED schitterend licht uitstraalt.

#### 2. Componenten

| ![Img](./media/A850.png) |              ![Img](./media/A858.png)              | ![Img](./media/A906.png) |
| :---------------------: | :-----------------------------------------------: | :---------------------: |
|   micro:bit board *1    |        micro:bit T-type uitbreidingsboard *1      |   micro USB-kabel *1    |
| ![Img](./media/A500.png) |              ![Img](./media/A944.png)              | ![Img](./media/A950.png) |
|       rode LED *1       |                 220Ω weerstand *3                  |      verbindingsdraad *2|
| ![Img](./media/A017.png) |              ![Img](./media/A024.png)              | ![Img](./media/A621.png) |
|      breadboard *1      |batterijhouder *1 <br> (<span style="color: rgb(255, 76, 65);">zelf meegebrachte AA-batterijen *2</span>)|       RGB kaart *1       |

#### 3. Kennis over componenten

**Microfoon**

Een hoogwaardige digitale microfoon is geïntegreerd aan de voorkant van de micro:bit V2 board om geluid- en audiosignalen te detecteren. De chip die de microfoon aanstuurt en verwerkt bevindt zich aan de achterkant.

![Img](./media/A1317.png)

De microfoon zit in een klein rond gaatje aan de voorkant van de board, wat handig is om omgevingsgeluiden op te vangen. Plaats de micro:bit board gewoon met de voorkant naar boven tijdens gebruik. Naast het gaatje zit een microfoon LED-indicator. Wanneer de micro:bit geluidsniveaus meet, zal de indicator oplichten.

![Img](./media/A116.png)

**RGB LED**

![Img](./media/A2127.png)

RGB LED is gebaseerd op de combinatie van drie primaire kleuren (RGB): rood, groen en blauw. De meeste kleuren kunnen worden samengesteld door RGB in verschillende verhoudingen te mengen. De rode, groene en blauwe LEDs zijn verpakt in een transparante plastic behuizing om kleuren licht uit te stralen door de ingangsspanning van de R-, G- en B-pinnen te veranderen.

![Img](./media/A137.png)

**Driekleuren theorie:**

![Img](./media/A150.png)

RGB LED kan worden onderverdeeld in twee types: gemeenschappelijke anode en gemeenschappelijke kathode:

In een gemeenschappelijke kathode RGB LED delen de drie LEDs een negatieve aansluiting (kathode);

In een gemeenschappelijke anode RGB LED delen de drie LEDs een positieve aansluiting (anode).

![Img](./media/A209.png)

<span style="color: rgb(255, 76, 65);">**Let op: Hier bieden wij een gemeenschappelijke kathode RGB LED aan.**</span>

**RGB LED-pinnen:**

RGB LED heeft 4 pinnen: GND (de langste), R (rood), G (groen) en B (blauw). Plaats de RGB LED zoals hieronder getoond, pinnen van links naar rechts zijn rood, GND, groen en blauw.

![Img](./media/A239.png)

#### 4. Aansluitschema

![Img](./media/A308.png)

![Img](./media/A325.png)

#### 5. Codeflow

![Img](./media/A343.png)

#### 6. Testcode

Het codebestand is te vinden in de map Project 06：Music Party, bestand Project-06-Music-Party\.py.

![Img](./media/A3523.png)

**Volledige code:**

```python
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
```

#### 7. Testresultaat

Klik op “<span style="color: rgb(255, 76, 65);">Flash</span>” om de code op de micro:bit board te laden.

![Img](./media/A3540.png)

Na het downloaden van de code naar de board, **zet de voeding aan via micro USB-kabel of externe voeding (zet de DIP-schakelaar op ON)**, en druk op de resetknop op de board.

![Img](./media/A455.png)

Wanneer we in onze handen klappen, vangt de microfoon op de board geluidssignalen op, en speelt de speaker een vrolijk verjaardagslied terwijl de RGB LED schitterend licht uitstraalt. Is het muziekfeest niet in een vrolijke en blije sfeer?

<span style="color: rgb(255, 76, 65);">**LET OP:** Als de bedrading correct is maar je ziet geen resultaat, druk dan op de resetknop aan de achterkant van de board.</span>

![Img](./media/A757.gif)
