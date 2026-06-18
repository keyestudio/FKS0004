### Projekt 03: Entfernungsfledermaus

#### 1. Übersicht

Basierend auf einem Ultraschallsensor erkennt die Entfernungsfledermaus die Entfernung von Hindernissen und zeigt diese in Echtzeit auf einem OLED an. Wenn der Abstand weniger als 10 cm beträgt, gibt der Lautsprecher Alarm.

#### 2. Komponenten

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit Board *1 | micro:bit T-Typ Erweiterungsboard *1 | micro USB Kabel *1 |
| ![Img](./media/A356.png)| ![Img](./media/A406.png)| ![Img](./media/A415.png) |
| Ultraschallsensor *1 | OLED Modul *1 | DuPont Kabel |
|![Img](./media/A017.png) | ![Img](./media/A950.png) | ![Img](./media/A024.png) |
| Steckbrett *1 | Jumper Kabel | Batteriefach *1 <br> (<span style="color: rgb(255, 76, 65);">selbst mitgebrachte AA Batterien *2</span>)|
|![Img](./media/A315.png)|![Img](./media/A557.png) | |
| Fledermauskarte *1| OLED Karte *1 | |

#### 3. Komponentenwissen

**Ultraschallsensor**

Ultraschallwellen werden zurückgeworfen, wenn sie auf ein Hindernis treffen. Wir messen die Entfernung, indem wir das Zeitintervall zwischen dem Senden und Empfangen der Wellen berechnen. Da die Ausbreitungsgeschwindigkeit von Schall in Luft konstant v=340m/s ist, berechnen wir die Entfernung zwischen Sensor und Hindernis: s=vt/2.

![Img](./media/A846.png)

Das HC-SR04 Ultraschallmodul integriert einen Sender und Empfänger. Der Sender wandelt elektrische Signale (elektrische Energie) in hochfrequente (für Menschen nicht hörbare) Schallwellen (mechanische Energie) um, während der Empfänger das Gegenteil macht.

Das Schaltbild des HC SR04:

![Img](./media/A642.png)

**Pin-Belegung:**

![Img](./media/A702.png)

**Parameter:**

- Betriebsspannung: 5V
- Betriebsstrom: 12mA
- Minimale Messentfernung: 2cm
- Maximale Messentfernung: 200cm

**Arbeitsprinzip:**

Ein High-Pegel-Impuls von mindestens 10us wird am Trig-Pin ausgegeben, und das Modul beginnt mit der Aussendung von Ultraschallwellen. Gleichzeitig wird der Echo-Pin auf High gezogen. Wenn das Modul eine Ultraschallwelle zurückerhält, weil es auf ein Hindernis trifft, wird der Echo-Pin auf Low gezogen. Die Dauer des High-Pegels am Echo-Pin ist die Gesamtzeit der Welle vom Senden bis zum Empfangen: s=vt/2.

![Img](./media/A728.png)

**OLED Modul**

OLED-Technologie bietet eine reiche Farbdarstellung, hohen Kontrast und weite Betrachtungswinkel, wodurch klare und lebendige Bilder entstehen, besonders herausragend bei Schwarz.

Jeder Pixel des OLED-Displays strahlt selbst Licht aus, ohne Hintergrundbeleuchtung, daher ist der Stromverbrauch relativ gering. Mit kleiner Größe, hoher Auflösung und niedrigem Stromverbrauch ist das 0,9-Zoll OLED-Display sehr gut für tragbare Geräte geeignet.

![Img](./media/A636.png)

<span style="color: rgb(255, 76, 65);">**In diesem Projekt wird das OLED-Displaymodul mit dem SDA-Anschluss an Pin P20 und SCL an Pin P19 angeschlossen.**</span>

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

<span style="color: rgb(255, 76, 65);">**Beim Einsatz des OLED-Displays und des Ultraschallsensors muss eine externe Stromversorgung angeschlossen und der DIP-Schalter eingeschaltet werden.**</span>

![Img](./media/A902.png)

![Img](./media/A1906.png)

#### 5. Programmablauf

![Img](./media/A924.png)

#### 6. Testcode

Die Code-Datei befindet sich im Ordner Projekt 03：Entfernungsfledermaus, Datei Project-03-Ranging-Bat.hex.

![Img](./media/A955.png)

**Codeblöcke laden:** <span style="color: rgb(255, 76, 65);">Der Schwellenwert 10 in der Bedingung kann je nach tatsächlichen Gegebenheiten angepasst werden.</span>

![Img](./media/A022.png)

#### 7. Testergebnis

Für die Windows 10 App klicken Sie auf „<span style="color: rgb(255, 76, 65);">Download</span>“. Für Browser senden Sie die heruntergeladene „<span style="color: rgb(255, 76, 65);">.hex</span>“-Datei an das micro:bit Board.

Nach dem Herunterladen des Codes auf das Board <span style="color: rgb(255, 76, 65);">mit externer Stromversorgung einschalten und den DIP-Schalter auf ON stellen</span>, zeigt das OLED die Entfernung zwischen Ultraschallsensor und Hindernis in Echtzeit an. Wenn der Abstandswert weniger als 10 cm beträgt, gibt der Lautsprecher auf dem micro:bit Board Alarm.

<span style="color: rgb(255, 76, 65);"><span style="color: rgb(255, 76, 65);">**ACHTUNG:** Wenn die Verkabelung korrekt ist, Sie aber keine Ergebnisse sehen, drücken Sie die Reset-Taste auf der Rückseite des Boards.</span></span>

![Img](./media/A605.gif)
