### Project 07: Omgevingsbewaking

#### 1. Overzicht

Op de OLED toont het slimme omgevingsbewakingssysteem in realtime de temperatuur- en vochtigheidswaarden die door de DHT11-sensor worden gedetecteerd, evenals de helderheidswaarde van het omgevingslicht die wordt gedetecteerd door de ingebouwde lichtsensor.

#### 2. Componenten

|         ![Img](./media/A850.png)          |       ![Img](./media/A858.png)       |              ![Img](./media/A906.png)              |
| :--------------------------------------: | :---------------------------------: | :-----------------------------------------------: |
|            micro:bit board *1            | micro:bit T-type uitbreidingsbord *1 |                micro USB-kabel *1                 |
|         ![Img](./media/A2637.png)         |       ![Img](./media/A406.png)       |              ![Img](./media/A415.png)              |
| XHT11 temperatuur- en vochtigheidssensor *1 |           OLED-module *1            |                   DuPont-draadjes                  |
|         ![Img](./media/A017.png)          |       ![Img](./media/A950.png)       |              ![Img](./media/A024.png)              |
|              breadboard *1               |             jump wires              |batterijhouder *1 <br> (<span style="color: rgb(255, 76, 65);">zelf meegebrachte AA-batterijen *2</span>)|
|         ![Img](./media/A0715.png)         |       ![Img](./media/A557.png)       |                                                   |
|              cloud card *1               |            OLED card *1             |                                                   |

#### 3. Componentkennis

**XHT11 temperatuur- en vochtigheidssensor**

![Img](./media/A2637.png)

De XHT11 temperatuur- en vochtigheidssensor is een samengestelde sensor met gekalibreerde digitale signaaluitgang, die de luchtvochtigheid en temperatuur kan detecteren.

**Nauwkeurigheid**: vochtigheid ±5%RH, temperatuur ±2℃

**Detectiebereik**: vochtigheid 5%RH ~ 95%RH, temperatuur -25℃ ~ +60℃

De sensor gebruikt een speciale digitale module-acquisitie en temperatuur- en vochtigheidssensingtechnologie om een extreem hoge betrouwbaarheid en uitstekende lange termijn stabiliteit te garanderen. Het bevat een resistief vochtigheidssensorelement en een NTC-temperatuursensorelement, wat zeer geschikt is voor metingen met relatief lage nauwkeurigheid en realtime eisen.

**XHT11 communicatiemodus:**

Er wordt gebruikgemaakt van single bus-communicatie. Dit betekent dat er slechts één datalijn is voor gegevensuitwisseling en controle in het systeem.

- Definitie van door single bus verzonden databits:

Single bus dataformaat: 40 bits data worden in één keer verzonden, met de hoogste bit eerst.

8bit vochtigheidsinteger + 8bit vochtigheidsdecimaal + 8bit temperatuurinteger + 8bit temperatuurdecimaal + 8bit pariteitsbit (Het decimale deel van de vochtigheid is 0)

- Definitie van pariteitsbit:

8bit vochtigheidsinteger + 8bit vochtigheidsdecimaal + 8bit temperatuurinteger + 8bit temperatuurdecimaal. 8bit pariteitsbit = de laatste 8 bits van het verkregen resultaat

- Datatijdlijn:

Nadat de gebruikershost (MCU) een startsignaal heeft verzonden, schakelt de XHT11 over van laag stroomverbruik naar hoge snelheid modus. Na het startsignaal zendt XHT11 een respons signaal en 40bit data, en activeert een signaalacquisitie.

- De signaaloverdracht wordt weergegeven in de afbeelding:

![Img](./media/A229.png)

 **Parameters**

- Bedrijfsspanning: DC 3.3V tot 5V

- Bedrijfstroom: 2.1mA

- Maximale stroom: 0.0105W

- Temperatuurbereik: -25℃ ~ +60℃ (± 2℃)

- Vochtigheidsbereik: 5%RH ~ 95%RH (nauwkeurigheid ±5%RH rond 25 °C)

**Microbit lichtsensor**

![Img](./media/A0335.png)

Een lichtsensor is een invoerapparaat dat de helderheid van extern licht meet. De micro:bit board bevat geen ingebouwde lichtsensor. Het detecteert en meet de omgevingshelderheid via een LED-matrix die herhaaldelijk de lichtintensiteit omzet in een waarde-invoer, waarna de spanningsvervaltijd wordt bemonsterd. Op deze manier is <span style="color: rgb(255, 76, 65);">de gedetecteerde helderheidswaarde een relatieve waarde</span>.

#### 4. Aansluitschema

![Img](./media/A409.png)

<span style="color: rgb(255, 76, 65);">**Bij gebruik van het OLED-display moeten we een externe voeding aansluiten en de DIP-schakelaar op ON zetten.**</span>

![Img](./media/A904.png)

![Img](./media/A554.png)

#### 5. Bibliotheek importeren

Als je de benodigde bibliotheekbestanden (DHT11 en oled_ssd1306) nog niet hebt toegevoegd, importeer deze dan volgens [Hoe Mu bibliotheek importeert naar Micro:bit](https://docs.keyestudio.com/projects/FKS0004/en/latest/docs/MicroPython_Tutorial/MicroPython_Tutorial.html#how-mu-import-library-to-micro-bit).

#### 6. Codeflow

![Img](./media/A638.png)


#### 7. Testcode

Het codebestand is te vinden in de map Project 07：Environment Monitoring中找文件Project-07-Environment-Monitoring\.py.

![Img](./media/A3641.png)

**Volledige code:**

```python
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
```

#### 8. Testresultaat

Klik op “<span style="color: rgb(255, 76, 65);">Flash</span>” om de code op de micro:bit board te laden.

![Img](./media/A3710.png)

Na het downloaden van de code naar de board, **zet de voeding aan via micro USB-kabel of externe voeding (zet de DIP-schakelaar op ON)**, en druk op de resetknop op de board.

![Img](./media/A455.png)

De OLED toont in realtime de temperatuur- en vochtigheidswaarden en het lichthelderheidsniveau.

<span style="color: rgb(255, 76, 65);">**LET OP:** Als de bedrading correct is maar je ziet geen resultaten, druk dan op de resetknop aan de achterkant van de board.</span>

![Img](./media/A838.gif)
