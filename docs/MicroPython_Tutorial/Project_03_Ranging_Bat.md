### Projekt 03: Entfernungs-Bat

#### 1. Übersicht

Basierend auf einem Ultraschallsensor erkennt die Entfernungs-Bat die Entfernung von Hindernissen und zeigt diese in Echtzeit auf einem OLED an. Wenn die Entfernung weniger als 10 cm beträgt, gibt der Lautsprecher Alarm.

#### 2. Komponenten

| ![Img](./media/A850.png) |       ![Img](./media/A858.png)       |              ![Img](./media/A906.png)              |
| :---------------------: | :---------------------------------: | :-----------------------------------------------: |
|   micro:bit Board *1    | micro:bit T-Typ Erweiterungsboard *1 |                micro USB Kabel *1                 |
| ![Img](./media/A356.png) |       ![Img](./media/A406.png)       |              ![Img](./media/A415.png)              |
|  Ultraschallsensor *1   |           OLED Modul *1             |                   DuPont Kabel                    |
| ![Img](./media/A017.png) |       ![Img](./media/A950.png)       |              ![Img](./media/A024.png)              |
|      Breadboard *1      |             Jumper Kabel            | Batteriehalter *1 <br> (<span style="color: rgb(255, 76, 65);">selbst bereitgestellte AA Batterien *2</span>)|
| ![Img](./media/A315.png) |       ![Img](./media/A557.png)       |                                                   |
|       Bat Karte *1      |            OLED Karte *1            |                                                   |

#### 3. Komponentenwissen

**Ultraschallsensor**

Ultraschallwellen werden zurückgeworfen, wenn sie auf ein Hindernis treffen. Wir messen die Entfernung, indem wir das Zeitintervall zwischen dem Senden und Empfangen der Wellen berechnen. Da die Ausbreitungsgeschwindigkeit des Schalls in Luft konstant v=340m/s ist, berechnen wir die Entfernung zwischen Sensor und Hindernis: s=vt/2.

![Img](./media/A846.png)

Das HC-SR04 Ultraschallmodul integriert einen Sender und Empfänger. Der Sender wandelt elektrische Signale (elektrische Energie) in hochfrequente (für Menschen nicht hörbare) Schallwellen (mechanische Energie) um, während der Empfänger das Gegenteil macht.

Das Schaltbild des HC SR04:

![Img](./media/A642.png)

**Pin-Belegung:**

![Img](./media/A702.png)

**Parameter:**

- Betriebsspannung: 5V
- Betriebsstrom: 12mA
- Minimale Messdistanz: 2cm
- Maximale Messdistanz: 200cm

**Arbeitsprinzip:**

Ein High-Pegel-Puls von mindestens 10µs wird am Trig-Pin ausgegeben, und das Modul beginnt, Ultraschallwellen zu senden. Gleichzeitig wird der Echo-Pin auf High gezogen. Wenn das Modul eine Ultraschallwelle zurückerhält, weil es auf ein Hindernis trifft, wird der Echo-Pin auf Low gezogen. Die Dauer des High-Pegels am Echo-Pin ist die Gesamtzeit der Welle vom Senden bis zum Empfangen: s=vt/2.

![Img](./media/A728.png)

**OLED Modul**

OLED-Technologie zeichnet sich durch eine reiche Farbdarstellung, hohen Kontrast und weite Betrachtungswinkel aus und liefert klare und lebendige Bilder, besonders herausragend bei Schwarz.

Jeder Pixel des OLED-Displays strahlt selbst Licht aus, ohne Hintergrundbeleuchtung, daher ist der Stromverbrauch relativ gering. Mit kleiner Größe, hoher Auflösung und niedrigem Stromverbrauch ist das 0,9-Zoll OLED-Display sehr gut für tragbare Geräte geeignet.

![Img](./media/A636.png)

<span style="color: rgb(255, 76, 65);">**In diesem Projekt wird das OLED-Display-Modul mit dem SDA-Anschluss an Pin P20 und SCL an Pin P19 angeschlossen.**</span>

**Parameter:**

- Betriebsspannung: DC 3,3V-5V

- Betriebsstrom: 30mA

- Schnittstelle: Pin-Anschlüsse mit 2,54mm Abstand

- Kommunikationsmodus: I2C

- Interner Treiberchip: SSD1306

- Auflösung: 128*64

- Betrachtungswinkel: größer als 150°

#### 4. Schaltplan

![Img](./media/A1849.png)

<span style="color: rgb(255, 76, 65);">**Beim Einsatz des OLED-Displays und Ultraschallsensors muss eine externe Stromversorgung angeschlossen und der DIP-Schalter auf ON gestellt werden.**</span>

![Img](./media/A902.png)

![Img](./media/A1906.png)

#### 5. Bibliothek importieren

Falls Sie die benötigten Bibliotheksdateien (oled_ssd1306) noch nicht hinzugefügt haben, importieren Sie diese bitte gemäß [Wie Mu Bibliothek in Micro:bit importiert](https://docs.keyestudio.com/projects/FKS0004/en/latest/docs/MicroPython_Tutorial/MicroPython_Tutorial.html#how-mu-import-library-to-micro-bit).

#### 6. Programmablauf

![Img](./media/A924.png)

#### 7. Testcode

Die Code-Datei befindet sich im Ordner Projekt 03：Entfernungs-Bat, Datei Project-03-Ranging-Bat\.py.

![Img](./media/A302.png)

**Vollständiger Code:** <span style="color: rgb(255, 76, 65);">**Der Schwellenwert 10 in der Bedingung kann je nach tatsächlichen Gegebenheiten angepasst werden.**</span>

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

#### 8. Testergebnis

Klicken Sie auf „<span style="color: rgb(255, 76, 65);">Flash</span>“, um den Code auf das micro:bit Board zu laden.

![Img](./media/A3323.png)

Nach dem Herunterladen des Codes auf das Board **mit micro USB Kabel oder externer Stromversorgung einschalten (DIP-Schalter auf ON stellen)** und den Reset-Knopf auf dem Board drücken.

![Img](./media/A455.png)

Das OLED zeigt die Entfernung zwischen Ultraschallsensor und Hindernis in Echtzeit an. Wenn der Abstandswert weniger als 10 cm beträgt, gibt der Lautsprecher auf dem micro:bit Board Alarm.

<span style="color: rgb(255, 76, 65);"><span style="color: rgb(255, 76, 65);">**ACHTUNG:** Wenn die Verkabelung korrekt ist, Sie aber keine Ergebnisse sehen, drücken Sie den Reset-Knopf auf der Rückseite des Boards.</span></span>

![Img](./media/A605.gif)
