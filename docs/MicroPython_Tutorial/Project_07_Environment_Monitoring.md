### Projekt 07: Umweltüberwachung

#### 1. Übersicht

Auf dem OLED zeigt das intelligente Umweltüberwachungssystem die vom DHT11-Sensor erfassten Temperatur- und Feuchtigkeitswerte in Echtzeit sowie den Helligkeitswert des Umgebungslichts, der vom eingebauten Lichtsensor erkannt wird.

#### 2. Komponenten

|         ![Img](./media/A850.png)          |       ![Img](./media/A858.png)       |              ![Img](./media/A906.png)              |
| :--------------------------------------: | :---------------------------------: | :-----------------------------------------------: |
|            micro:bit board *1            | micro:bit T-type Erweiterungsplatine *1 |                micro USB Kabel *1                 |
|         ![Img](./media/A2637.png)         |       ![Img](./media/A406.png)       |              ![Img](./media/A415.png)              |
| XHT11 Temperatur- und Feuchtigkeitssensor *1 |           OLED Modul *1            |                   DuPont Kabel                    |
|         ![Img](./media/A017.png)          |       ![Img](./media/A950.png)       |              ![Img](./media/A024.png)              |
|              Steckbrett *1               |             Jumper Kabel             |Batteriehalter *1 <br> (<span style="color: rgb(255, 76, 65);">selbstbereitgestellte AA Batterien *2</span>)|
|         ![Img](./media/A0715.png)         |       ![Img](./media/A557.png)       |                                                   |
|              Cloud-Karte *1               |            OLED-Karte *1             |                                                   |

#### 3. Komponentenwissen

**XHT11 Temperatur- und Feuchtigkeitssensor**

![Img](./media/A2637.png)

Der XHT11 Temperatur- und Feuchtigkeitssensor ist ein zusammengesetzter Sensor mit kalibrierter digitaler Signalausgabe, der die Luftfeuchtigkeit und Temperatur messen kann.

**Genauigkeit**: Feuchtigkeit ±5%RH, Temperatur ±2℃

**Messbereich**: Feuchtigkeit 5%RH ~ 95%RH, Temperatur -25℃ ~ +60℃

Der Sensor verwendet spezielle digitale Module zur Erfassung sowie Temperatur- und Feuchtigkeitssensortechnologie, um eine extrem hohe Zuverlässigkeit und ausgezeichnete Langzeitstabilität zu gewährleisten. Er beinhaltet ein resistives Feuchtigkeitssensorelement und ein NTC-Temperatursensorelement, was ihn sehr geeignet für Messungen mit relativ niedriger Genauigkeit und Echtzeitanforderungen macht.

**XHT11 Kommunikationsmodus:**

Es wird eine Ein-Bus-Kommunikation verwendet. Das bedeutet, dass es nur eine Datenleitung für Datenaustausch und Steuerung im System gibt.

- Definition der vom Ein-Bus übertragenen Datenbits:

Ein-Bus-Datenformat: 40 Bits werden auf einmal übertragen, wobei das höchstwertige Bit zuerst kommt.

8bit Feuchtigkeitsganzzahl + 8bit Feuchtigkeitsdezimal + 8bit Temperaturganzzahl + 8bit Temperaturdezimal + 8bit Paritätsbit (Der Dezimalteil der Feuchtigkeit ist 0)

- Definition des Paritätsbits:

8bit Feuchtigkeitsganzzahl + 8bit Feuchtigkeitsdezimal + 8bit Temperaturganzzahl + 8bit Temperaturdezimal. 8bit Paritätsbit = die letzten 8 Bits des erhaltenen Ergebnisses

- Datenzeitachse:

Nachdem der Benutzerhost (MCU) ein Startsignal sendet, wechselt der XHT11 vom Niedrigstrommodus in den Hochgeschwindigkeitsmodus. Nach dem Startsignal sendet der XHT11 ein Antwortsignal und 40bit Daten und löst eine Signalaufnahme aus.

- Die Signalübertragung ist in der Abbildung dargestellt:

![Img](./media/A229.png)

 **Parameter**

- Betriebsspannung: DC 3.3V bis 5V

- Betriebsstrom: 2.1mA

- Maximale Leistung: 0.0105W

- Temperaturbereich: -25℃ ~ +60℃ (± 2℃)

- Feuchtigkeitsbereich: 5%RH ~ 95%RH (Genauigkeit ±5%RH bei ca. 25 °C)

**Microbit Lichtsensor**

![Img](./media/A0335.png)

Ein Lichtsensor ist ein Eingabegerät, das die Helligkeit des Umgebungslichts misst. Das micro:bit Board enthält keinen eingebauten Lichtsensor. Es erkennt und misst die Umgebungshelligkeit durch eine LED-Matrix, die die Lichtintensität wiederholt in einen Eingabewert umwandelt, und dann wird die Spannungsabfallzeit abgetastet. Auf diese Weise ist <span style="color: rgb(255, 76, 65);">der erkannte Helligkeitswert ein relativer Wert</span>.

#### 4. Schaltplan

![Img](./media/A409.png)

<span style="color: rgb(255, 76, 65);">**Beim Einsatz des OLED-Displays müssen wir eine externe Stromversorgung anschließen und den DIP-Schalter auf ON stellen.**</span>

![Img](./media/A904.png)

![Img](./media/A554.png)

#### 5. Bibliothek importieren

Falls Sie die benötigten Bibliotheksdateien (DHT11 und oled_ssd1306) noch nicht hinzugefügt haben, importieren Sie diese bitte unter Bezugnahme auf [Wie Mu Bibliothek in Micro:bit importiert](https://docs.keyestudio.com/projects/FKS0004/en/latest/docs/MicroPython_Tutorial/MicroPython_Tutorial.html#how-mu-import-library-to-micro-bit).

#### 6. Programmablauf

![Img](./media/A638.png)


#### 7. Testcode

Die Code-Datei befindet sich im Ordner Projekt 07：Environment Monitoring中找文件Project-07-Environment-Monitoring\.py.

![Img](./media/A3641.png)

**Vollständiger Code:**

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

#### 8. Testergebnis

Klicken Sie auf „<span style="color: rgb(255, 76, 65);">Flash</span>“, um den Code auf das micro:bit Board zu laden.

![Img](./media/A3710.png)

Nach dem Herunterladen des Codes auf das Board **mit micro USB Kabel oder externer Stromversorgung einschalten (DIP-Schalter auf ON stellen)** und die Reset-Taste auf dem Board drücken.

![Img](./media/A455.png)

Das OLED zeigt die Temperatur- und Feuchtigkeitswerte sowie den Helligkeitswert des Lichts in Echtzeit an.

<span style="color: rgb(255, 76, 65);">**ACHTUNG:** Wenn die Verkabelung korrekt ist, Sie aber keine Ergebnisse sehen, drücken Sie die Reset-Taste auf der Rückseite des Boards.</span>

![Img](./media/A838.gif)
