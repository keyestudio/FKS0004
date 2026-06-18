### Projekt 05: Auto-Drehzahlmesser

#### 1. Übersicht

In diesem Projekt kombinieren wir ein einstellbares Potentiometer, einen Servo und eine schöne Ziffernblattkarte, um ein einfaches Auto-Drehzahlmesser-Modell zu erstellen.

#### 2. Komponenten

| ![Img](./media/A850.png)  |              ![Img](./media/A858.png)              | ![Img](./media/A906.png) |
| :----------------------: | :-----------------------------------------------: | :---------------------: |
|    micro:bit Board *1    |        micro:bit T-Typ Erweiterungsboard *1        |   micro USB Kabel *1    |
| ![Img](./media/A350.png)  |              ![Img](./media/A309.png)              | ![Img](./media/A950.png) |
|     Potentiometer *1     |                     Servo *1                      |       Jumper-Kabel      |
| ![Img](./media/A017.png)  |              ![Img](./media/A024.png)              | ![Img](./media/A233.png) |
|      Steckbrett *1       |Batteriehalter *1 <br> (<span style="color: rgb(255, 76, 65);">selbst mitgebrachte AA Batterien *2</span>)|  Potentiometer-Karte *1  |
| ![Img](./media/A1326.png) |                                                   |                         |
|     Auto-Drehzahlmesser-Karte *1      |                                                   |                         |

#### 3. Komponentenwissen

**Potentiometer**

![Img](./media/A350.png)

Ein Potentiometer ist ebenfalls ein Widerstandselement mit drei Anschlüssen, dessen Widerstandswert nach einer bestimmten Regelmäßigkeit einstellbar ist.

Sie gibt es in allen Formen, Größen und Werten, aber sie haben alle Folgendes gemeinsam:

① Drei Anschlüsse (oder Verbindungspunkte).

② Einen beweglichen Knopf oder Schieberegler, der den Widerstand zwischen dem mittleren Anschluss und einem der äußeren Anschlüsse verändern kann.

③ Wenn der Knopf bewegt wird, variiert der Widerstand zwischen dem mittleren Anschluss und einem der äußeren Anschlüsse von 0Ω bis zum Maximalwert.

Das Schaltzeichen des Potentiometers:

![Img](./media/A654.png)

(1)\. Als Spannungsteiler

Das Potentiometer ist ein kontinuierlich einstellbarer Widerstand. Wenn Sie seinen Schieberegler drehen, gleitet der bewegliche Kontakt über den Widerstand. Dabei kann eine Spannung ausgegeben werden, die von der angelegten Spannung am Potentiometer und dem Winkel oder Hub des beweglichen Reglers abhängt.

(2)\. Als veränderlicher Widerstand

Wenn das Potentiometer als veränderlicher Widerstand verwendet wird, verbinden Sie seinen mittleren Anschluss mit einem der beiden zusätzlichen Anschlüsse im Stromkreis. So erhalten Sie einen stabilen und kontinuierlich veränderlichen Widerstandswert innerhalb seines Bereichs.

(3)\. Als Stromregler

Wenn es als Stromregler verwendet wird, muss der bewegliche Kontakt als einer der Ausgangsanschlüsse angeschlossen werden.

#### 4. Schaltplan

![Img](./media/A812.png)

<span style="color: rgb(255, 76, 65);">**Beim Einsatz des Servos müssen wir eine externe Stromversorgung anschließen und den DIP-Schalter auf ON stellen.**</span>

![Img](./media/A902.png)

![Img](./media/A836.png)

#### 5. Programmablauf

![Img](./media/A0854.png)

#### 6. Testcode

Die Code-Datei befindet sich im Ordner Projekt 05：Auto-Drehzahlmesser, Datei Project-05-Car-Dial\.py.

![Img](./media/A3438.png)

**Vollständiger Code:**

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

#### 7. Testergebnis

Klicken Sie auf „<span style="color: rgb(255, 76, 65);">Flash</span>“, um den Code auf das micro:bit Board zu laden.

![Img](./media/A3457.png)

Nach dem Herunterladen des Codes auf das Board **mit dem micro USB Kabel oder einer externen Stromversorgung einschalten (DIP-Schalter auf ON stellen)** und die Reset-Taste auf dem Board drücken.

![Img](./media/A455.png)

Drehen Sie den Knopf am Potentiometer, und der Servo bewegt den Zeiger auf dem Ziffernblatt.

<span style="color: rgb(255, 76, 65);">**ACHTUNG:** Wenn die Verkabelung korrekt ist, Sie aber keine Ergebnisse sehen, drücken Sie die Reset-Taste auf der Rückseite des Boards.</span>

![Img](./media/A706.gif)
