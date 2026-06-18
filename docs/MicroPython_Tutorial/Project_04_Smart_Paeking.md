### Projekt 04: Smart Parking

#### 1. Übersicht

Intelligente Parkplätze sind überall. Können wir auch einen intelligenten Parkplatz erstellen? Natürlich. Wir können einen Ultraschallsensor verwenden, um zu erkennen, ob sich Fahrzeuge davor befinden. Wenn ein Fahrzeug (oder Gegenstand) erkannt wird, das sich nähert, steuern wir den Servo, um die Hebestange anzuheben; Wenn erkannt wird, dass es sich entfernt, senkt der Servo die Hebestange.

#### 2. Komponenten

| ![Img](./media/A850.png) |       ![Img](./media/A858.png)       |              ![Img](./media/A906.png)              |
| :---------------------: | :---------------------------------: | :-----------------------------------------------: |
|   micro:bit board *1    | micro:bit T-Typ Erweiterungsplatine *1 |                micro USB Kabel *1                 |
| ![Img](./media/A356.png) |       ![Img](./media/A309.png)       |              ![Img](./media/A415.png)              |
|  Ultraschallsensor *1   |              Servo *1               |                   DuPont Kabel                    |
| ![Img](./media/A017.png) |       ![Img](./media/A950.png)       |              ![Img](./media/A024.png)              |
|      Steckbrett *1      |             Jumper Kabel            |Batteriehalter *1 <br> (<span style="color: rgb(255, 76, 65);">selbst mitgebrachte AA Batterien *2</span>)|
| ![Img](./media/A336.png) |       ![Img](./media/A131.png)       |                                                   |
|       Batteriekarte *1       |          Hebestangenkarte *1           |                                                   |

#### 3. Komponentenwissen

**Servo**

Ein Servo ist ein Positionsantrieb. Wir können einen Servo verwenden, um die genaue Position zu steuern oder ein hohes Drehmoment auszugeben. Üblicherweise wird er in Robotern, ferngesteuerten Autos und sogar Flugzeugmodellen eingesetzt. Es gibt viele Spezifikationen, aber alle Servos haben drei Kabel: Signal (orange), Plus (rot) und Minus (braun). Die Farben können je nach Servo-Marke variieren.

![Img](./media/A5525.png)

**Innere Strukturdiagramm:**

![Img](./media/A5534.png)

① Signal: empfängt Steuersignale vom Mikrocontroller;

② Potentiometer: Die Position der Ausgangswelle kann gemessen werden, es gehört zum Feedback-Teil des gesamten Servos;

③ Interner Controller: Die eingebettete Platine verarbeitet Signale von der externen Steuerung, steuert den Motor und das Positionsfeedback, dies ist der Kern des gesamten Servos;

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

<span style="color: rgb(255, 76, 65);">**Beim Einsatz des Ultraschallsensors und Servos müssen wir eine externe Stromversorgung anschließen und den DIP-Schalter auf ON stellen.**</span>

![Img](./media/A902.png)

![Img](./media/A701.png)

#### 5. Programmablauf

![Img](./media/A716.png)

#### 6. Testcode

Die Code-Datei befindet sich im Ordner Projekt 04：Smart-Parking, Datei Project-04-Smart-Parking\.py.

![Img](./media/A3345.png)

**Vollständiger Code:** <span style="color: rgb(255, 76, 65);">Der Schwellenwert in der Bedingung 10 kann je nach tatsächlichen Bedingungen angepasst werden.</span>

```python
'''
Function: smart parking
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from microbit import *
import ustruct
import machine
from time import sleep_us

distance = 0              # set variable distance initial value to 0
lastEchoDuration = 0      # set variable lastEchoDuration initial value to 0

val = Image("09990:""09090:""09990:""09000:""09000")  # set iamge
display.show(val)        # LED matrix shows image
pin0.write_analog(25.6)    # set P0 pin analog to 25.6, servo angle to 0°
sleep(200)

while True:
    pin0.set_analog_period(20) # set servo frequency
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
    if distance < 10:          # if distance < 10cm
       pin0.write_analog(77)   # servo rotate to 90°
       sleep(2000)
    else:  # or
       sleep(2000)
       pin0.write_analog(25.6)
       sleep(2000)
```

#### 7. Testergebnis

Klicken Sie auf „<span style="color: rgb(255, 76, 65);">Flash</span>“, um den Code auf das micro:bit Board zu laden.

![Img](./media/A3400.png)

Nach dem Herunterladen des Codes auf das Board **mit dem micro USB Kabel oder externer Stromversorgung einschalten (DIP-Schalter auf ON stellen)** und die Reset-Taste auf dem Board drücken.

![Img](./media/A455.png)

Wenn der Ultraschallsensor ein Fahrzeug (oder Gegenstand) erkennt, das sich nähert, steuert der Servo die Hebestange zum Anheben; Wenn der Sensor erkennt, dass es sich entfernt, senkt der Servo die Hebestange.

<span style="color: rgb(255, 76, 65);">**ACHTUNG:** Wenn die Verkabelung korrekt ist, Sie aber keine Ergebnisse sehen, drücken Sie die Reset-Taste auf der Rückseite des Boards.</span>

![Img](./media/A021.gif)
