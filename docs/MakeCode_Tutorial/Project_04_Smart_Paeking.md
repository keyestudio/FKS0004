### Projekt 04: Smart Parking

#### 1. Übersicht

Intelligente Parkplätze sind überall. Können wir auch einen intelligenten Parkplatz erstellen? Natürlich. Wir können einen Ultraschallsensor verwenden, um zu erkennen, ob sich Fahrzeuge davor befinden. Wenn ein Fahrzeug (oder Gegenstand) erkannt wird, das sich nähert, steuern wir den Servo, um die Hebestange anzuheben; Wenn erkannt wird, dass es sich entfernt, senkt der Servo die Hebestange.

#### 2. Komponenten

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit Board *1 | micro:bit T-Typ Erweiterungsboard *1 | micro USB Kabel *1 |
| ![Img](./media/A356.png)| ![Img](./media/A309.png)| ![Img](./media/A415.png) |
| Ultraschallsensor *1 | Servo *1 | DuPont Kabel |
|![Img](./media/A017.png) | ![Img](./media/A950.png) | ![Img](./media/A024.png) |
| Breadboard *1 | Jumper Kabel | Batteriefach *1 <br> (<span style="color: rgb(255, 76, 65);">selbst bereitgestellte AA Batterien *2</span>)|
|![Img](./media/A336.png) |![Img](./media/A131.png) | |
| Batteriekarte *1 | Hebestangenkarte *1| |

#### 3. Komponentenwissen

**Servo**

Ein Servo ist ein Positionsantrieb. Wir können einen Servo verwenden, um die genaue Position zu steuern oder ein hohes Drehmoment auszugeben. Üblicherweise wird er in Robotern, ferngesteuerten Autos und sogar Flugzeugmodellen eingesetzt. Es gibt viele Spezifikationen, aber alle Servos haben drei Kabel: Signal (orange), Plus (rot) und Minus (braun). Die Farben können je nach Servo-Marke variieren.

![Img](./media/A5525.png)

**Innere Strukturdiagramm:**

![Img](./media/A5534.png)

① Signal: empfängt Steuersignale vom Mikrocontroller;

② Potentiometer: Die Position der Ausgangswelle kann gemessen werden, es gehört zum Feedback-Teil des gesamten Servos;

③ Interner Controller: Die eingebettete Platine verarbeitet Signale von der externen Steuerung, treibt den Motor an und gibt Positionssignale zurück, dies ist der Kern des gesamten Servos;

④ DC-Motor: Er dient als Aktuator zur Ausgabe von Geschwindigkeit, Drehmoment und Position;

⑤ Getriebe / Servomechanismus: Der Mechanismus vergrößert den vom Motor ausgegebenen Hub auf den endgültigen Ausgangswinkel entsprechend einem bestimmten Übersetzungsverhältnis.

**Servo ansteuern**

Senden Sie PWM-Signale an die Servosignalleitung, um dessen Ausgabe zu steuern. Der Tastgrad des PWM bestimmt direkt die Position der Ausgangswelle. Die Periode beträgt üblicherweise 20 Millisekunden und wird typischerweise so eingestellt, dass Impulse mit einer Frequenz von 50Hz erzeugt werden.

<span style="color: rgb(255, 0, 0);">Zum Beispiel (180° Servo):</span>

Wenn wir einen Puls mit einer Breite von 1,5 Millisekunden (ms) an den 180° Servo senden, bewegt sich die Ausgangswelle des Servos in die Mittelstellung (90 Grad);

Ist die Pulsbreite 0,5 ms, bewegt sich die Ausgangswelle auf 0 Grad;

Ist die Pulsbreite 2,5 ms, bewegt sich die Ausgangswelle auf 180 Grad;

![Img](./media/A5545.png)

**Parameter:**

- Betriebsspannung: DC 3,3V~5V

- Betriebstemperatur: -10°C ~ +50°C

- Abmessungen: 32,25mm x 12,25mm x 30,42mm

- Schnittstelle: 3-Pin Schnittstelle mit einem Abstand von 2,54mm

#### 4. Schaltplan

![Img](./media/A606.png)

<span style="color: rgb(255, 76, 65);">**Beim Einsatz des Ultraschallsensors und Servos muss eine externe Stromversorgung angeschlossen und der DIP-Schalter auf ON gestellt werden.**</span>

![Img](./media/A902.png)

![Img](./media/A701.png)

#### 5. Programmablauf

![Img](./media/A716.png)

#### 6. Testcode

Die Code-Datei befindet sich im Ordner Projekt 04：Smart-Parking, Datei Project-04-Smart-Parking.hex.

![Img](./media/A758.png)

**Codeblöcke laden:** <span style="color: rgb(255, 76, 65);">**Der Schwellenwert in der Bedingung 10 kann je nach tatsächlichen Bedingungen angepasst werden.**</span>

![Img](./media/A832.png)

#### 7. Testergebnis

Nach dem Herunterladen des Codes auf das Board, wenn der Ultraschallsensor ein Fahrzeug (oder einen Gegenstand) erkennt, das sich nähert, steuert der Servo die Hebestange zum Anheben; Wenn der Sensor erkennt, dass es sich entfernt, senkt der Servo die Hebestange.

<span style="color: rgb(255, 76, 65);">**ACHTUNG:** Wenn die Verkabelung korrekt ist, Sie aber keine Ergebnisse sehen, drücken Sie die Reset-Taste auf der Rückseite des Boards.</span>

![Img](./media/A021.gif)
