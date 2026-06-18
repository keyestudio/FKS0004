### Projekt 08: Diebstahlalarm

#### 1. Überblick

Wenn der intelligente Diebstahlalarm erkennt, dass die Diebstahlsicherung bewegt wurde, ertönt der Lautsprecher auf dem micro:bit Board und die rote LED blinkt.

#### 2. Komponenten

| ![Img](./media/A850.png) |              ![Img](./media/A858.png)              | ![Img](./media/A906.png) |
| :---------------------: | :-----------------------------------------------: | :---------------------: |
|   micro:bit Board *1    |        micro:bit T-Typ Erweiterungsboard *1        |   micro USB Kabel *1    |
| ![Img](./media/A937.png) |              ![Img](./media/A944.png)              | ![Img](./media/A950.png) |
|       rote LED *1       |                 220Ω Widerstand *1                 |      Steckdraht *2      |
| ![Img](./media/A017.png) |              ![Img](./media/A024.png)              | ![Img](./media/A952.png) |
|      Steckbrett *1      |Batteriehalter *1 <br> (<span style="color: rgb(255, 76, 65);">selbst bereitgestellte AA Batterien *2</span>)|      Alarmkarte *1      |

#### 3. Komponentenwissen

**Beschleunigungssensor**

![Img](./media/A026.png)

Das micro:bit Board verfügt über einen eingebauten LSM303AGR Beschleunigungssensor (wir nennen ihn Beschleunigungsmesser), der den Standard-, Schnell-, Plus- und Hochgeschwindigkeitsmodus (100 kHz, 400 kHz, 1 MHz und 3,4 MHz) der I2C-Seriellschnittstelle sowie die SPI-Seriellschnittstelle für die externe Kommunikation umfasst, mit einer Auflösung von 8/10/12 Bit und einem Messbereich von ±2g, ±4g oder ±8g.

Wenn das micro:bit Board ruht oder sich gleichförmig bewegt, misst der Beschleunigungsmesser nur die Erdbeschleunigung. Wenn es leicht geschwenkt wird, ist die gemessene Beschleunigung viel geringer als die der Erdbeschleunigung, sodass die Differenz vernachlässigt werden kann. Daher erfassen wir hauptsächlich die Änderung der Erdbeschleunigung auf den x-, y- und z-Achsen.

#### 4. Schaltplan

![Img](./media/A219.png)

<span style="color: rgb(255, 76, 65);">Der Steuerpin des LED-Boards ist P1 (der Pin des T-Typ Erweiterungsboards ist digital 1).</span>

#### 5. Programmablauf

![Img](./media/A4434.png)

#### 6. Testcode

Die Code-Datei befindet sich im Ordner Projekt 08：Diebstahlalarm, Datei Project-08-Burglar-Alarm\.py.

![Img](./media/A3743.png)

**Vollständiger Code:** 

<span style="color: rgb(255, 76, 65);">**Nach dem Importieren des Codes, wenn der Summer ständig ertönt, obwohl das Steckbrett nicht bewegt wird, kann dies durch geografische Faktoren verursacht sein. Sie können die Schwellenwerte in der Bedingung -60 und 50 entsprechend den tatsächlichen Bedingungen anpassen.**</span>

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

#### 7. Testergebnis

Klicken Sie auf „<span style="color: rgb(255, 76, 65);">Flash</span>“, um den Code auf das micro:bit Board zu laden.

![Img](./media/A3757.png)

Nach dem Herunterladen des Codes auf das Board **schalten Sie die Stromversorgung über das micro USB Kabel oder eine externe Stromquelle ein (stellen Sie den DIP-Schalter auf ON)** und drücken Sie die Reset-Taste auf dem Board.

![Img](./media/A455.png)

Nach dem Herunterladen des Codes auf das Board bewegen Sie das Steckbrett. Wenn der Beschleunigungswert x＜-60 oder x＞50 ist, ertönt der Lautsprecher auf dem Board und die LED blinkt, und die micro:bit LED-Matrix zeigt ![Img](./media/A706.png). Andernfalls ertönt kein Ton und die LED ist aus, und die micro:bit LED-Matrix zeigt ![Img](./media/A720.png).

<span style="color: rgb(255, 76, 65);">**ACHTUNG:** Wenn die Verkabelung korrekt ist, Sie aber keine Ergebnisse sehen, drücken Sie die Reset-Taste auf der Rückseite des Boards.</span>

![Img](./media/A936.gif)
