### Project 05: Auto Wijzerplaat

#### 1. Overzicht

In dit project combineren we een instelbare potentiometer, een servo en een mooie wijzerplaatkaart om een eenvoudig model van een auto wijzerplaat te maken.

#### 2. Componenten

| ![Img](./media/A850.png)  |              ![Img](./media/A858.png)              | ![Img](./media/A906.png) |
| :----------------------: | :-----------------------------------------------: | :---------------------: |
|    micro:bit board *1    |        micro:bit T-type uitbreidingsbord *1       |   micro USB kabel *1    |
| ![Img](./media/A350.png)  |              ![Img](./media/A309.png)              | ![Img](./media/A950.png) |
|     potentiometer *1     |                     servo *1                      |       jump wires        |
| ![Img](./media/A017.png)  |              ![Img](./media/A024.png)              | ![Img](./media/A233.png) |
|      breadboard *1       |batterijhouder *1 <br> (<span style="color: rgb(255, 76, 65);">zelf meegebrachte AA batterijen *2</span>)|  potentiometer kaart *1  |
| ![Img](./media/A1326.png) |                                                   |                         |
|     auto wijzerplaat kaart*1      |                                                   |                         |

#### 3. Componenten Kennis

**potentiometer**

![Img](./media/A350.png)

Een potentiometer is ook een weerstandselement met drie aansluitingen, waarvan de weerstandwaarde volgens een bepaalde regelmaat kan worden aangepast.

Ze komen in alle vormen, maten en waarden, maar ze hebben allemaal het volgende gemeen:

① Drie terminals (of aansluitpunten).

② Een beweegbare knop of schuifregelaar die de weerstand tussen de middelste terminal en een van de externe terminals kan veranderen.

③ Terwijl de knop wordt bewogen, varieert de weerstand tussen de middelste terminal en een van de externe terminals van 0Ω tot het maximum.

Het schakelsymbool van een potentiometer:

![Img](./media/A654.png)

(1)\. Als spanningsdeler

De potentiometer is een continu instelbare weerstand. Wanneer je de schuifregelaar draait, schuift het bewegende contact over de weerstand. Op dat moment kan er een spanning worden uitgegeven afhankelijk van de spanning die op de potentiometer wordt toegepast en de hoek of slag van de draaibeweging van de beweegbare schuifregelaar.

(2)\. Als variabele weerstand

Wanneer de potentiometer wordt gebruikt als variabele weerstand, sluit je de middelste terminal aan op een van de twee extra terminals in het circuit. Op deze manier kun je een stabiele en continu variërende weerstandwaarde binnen het bereik verkrijgen.

(3)\. Als stroomregelaar

Wanneer het wordt gebruikt als stroomregelaar, moet het bewegende contact worden aangesloten als een van de uitgangsterminals.

#### 4. Bedradingsschema

![Img](./media/A812.png)

<span style="color: rgb(255, 76, 65);">**Bij gebruik van de servo moeten we een externe voeding aansluiten en de DIP-schakelaar op ON zetten.**</span>

![Img](./media/A902.png)

![Img](./media/A836.png)

#### 5. Code Stroomdiagram

![Img](./media/A0854.png)

#### 6. Testcode

Het codebestand is te vinden in de map Project 05：Car Dial, bestand Project-05-Car-Dial\.py.

![Img](./media/A3438.png)

**Volledige code:**

```python
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
```

#### 7. Testresultaat

Klik op “<span style="color: rgb(255, 76, 65);">Flash</span>” om de code op het micro:bit board te laden.

![Img](./media/A3457.png)

Na het downloaden van de code naar het board, **zet de voeding aan via micro USB-kabel of externe voeding (zet de DIP-schakelaar op ON)**, en druk op de resetknop op het board.

![Img](./media/A455.png)

Draai aan de knop van de potentiometer en de servo beweegt de wijzer op de wijzerplaat.

<span style="color: rgb(255, 76, 65);">**LET OP:** Als de bedrading correct is maar je ziet geen resultaat, druk dan op de resetknop aan de achterkant van het board.</span>

![Img](./media/A706.gif)
