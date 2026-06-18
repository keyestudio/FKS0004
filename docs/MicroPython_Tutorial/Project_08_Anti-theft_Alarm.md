### Project 08: Anti-diefstal Alarm

#### 1. Overzicht

Wanneer het slimme anti-diefstal alarm detecteert dat de anti-diefstal doos is verplaatst, zal de speaker op de micro:bit board alarm slaan en zal de rode LED knipperen.

#### 2. Componenten

| ![Img](./media/A850.png) |              ![Img](./media/A858.png)              | ![Img](./media/A906.png) |
| :---------------------: | :-----------------------------------------------: | :---------------------: |
|   micro:bit board *1    |        micro:bit T-type uitbreidingsbord *1       |   micro USB kabel *1    |
| ![Img](./media/A937.png) |              ![Img](./media/A944.png)              | ![Img](./media/A950.png) |
|       rode LED *1       |                 220Ω weerstand *1                  |      verbindingsdraad *2|
| ![Img](./media/A017.png) |              ![Img](./media/A024.png)              | ![Img](./media/A952.png) |
|      breadboard *1      |batterijhouder *1 <br> (<span style="color: rgb(255, 76, 65);">zelf meegebrachte AA batterijen *2</span>)|      alarmkaart *1      |

#### 3. Componenten Kennis

**Versnellingsmeter**

![Img](./media/A026.png)

De micro:bit board beschikt over een ingebouwde LSM303AGR versnellingssensor (we noemen dit een versnellingsmeter) die standaard, snel, plus en hoge-snelheidsmodus (100 kHz, 400 kHz, 1 MHz en 3.4 MHz) van I2C seriële bus interface en SPI seriële standaard interface voor externe communicatie bevat, met een resolutie van 8/10/12 bits en een bereik van ±2g, ±4g, of ±8g.

Wanneer de micro:bit board in rust is of in eenparige beweging, detecteert de versnellingsmeter alleen de zwaartekrachtversnelling. Als het licht wordt bewogen, is de gedetecteerde versnelling veel minder dan die van de zwaartekracht, dus het verschil kan worden genegeerd. Daarom detecteren we voornamelijk de verandering van zwaartekrachtversnelling op de x-, y- en z-assen.

#### 4. Aansluitschema

![Img](./media/A219.png)

<span style="color: rgb(255, 76, 65);">De besturingspin van de LED op het bord is P1 (de pin van het T-type uitbreidingsbord is digitaal 1).</span>

#### 5. Code Stroomdiagram

![Img](./media/A4434.png)

#### 6. Testcode

Het codebestand is te vinden in map Project 08：Burglar Alarm, bestand Project-08-Burglar-Alarm\.py.

![Img](./media/A3743.png)

**Volledige code:** 

<span style="color: rgb(255, 76, 65);">**Na het importeren van de code, als de buzzer blijft klinken terwijl de breadboard niet is verplaatst; kan dit veroorzaakt worden door geografische factoren. Je kunt de drempelwaarden in de conditie -60 en 50 aanpassen aan de werkelijke situatie.**</span>

```python
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
```

#### 7. Testresultaat

Klik op “<span style="color: rgb(255, 76, 65);">Flash</span>” om de code op de micro:bit board te laden.

![Img](./media/A3757.png)

Na het downloaden van de code naar de board, **zet de voeding aan via micro USB kabel of externe voeding (zet de DIP-schakelaar op ON)**, en druk op de resetknop op de board.

![Img](./media/A455.png)

Na het downloaden van de code naar de board, beweeg de breadboard. Als de versnelling x＜-60 of x＞50 is, slaat de speaker op de board alarm en knippert de LED, en toont de micro:bit LED-matrix ![Img](./media/A706.png). Anders maakt de speaker geen geluid en is de LED uit, en toont de micro:bit LED-matrix ![Img](./media/A720.png).

<span style="color: rgb(255, 76, 65);">**LET OP:** Als de bedrading correct is maar je ziet geen resultaat, druk dan op de resetknop aan de achterkant van de board.</span>

![Img](./media/A936.gif)
