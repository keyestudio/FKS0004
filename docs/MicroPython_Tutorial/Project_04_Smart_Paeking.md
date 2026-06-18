### Project 04: Slim Parkeren

#### 1. Overzicht

Slimme parkeerplaatsen zijn overal. Kunnen we ook een slimme parkeerplaats maken? Natuurlijk. We kunnen een ultrasone sensor gebruiken om te detecteren of er voertuigen in de buurt zijn. Wanneer een voertuig (of object) wordt gedetecteerd dat nadert, besturen we een servo om de hefboom omhoog te brengen; als wordt gedetecteerd dat het zich verwijdert, zal de servo de hefboom laten zakken.

#### 2. Componenten

| ![Img](./media/A850.png) |       ![Img](./media/A858.png)       |              ![Img](./media/A906.png)              |
| :---------------------: | :---------------------------------: | :-----------------------------------------------: |
|   micro:bit board *1    | micro:bit T-type uitbreidingsbord *1 |                micro USB-kabel *1                 |
| ![Img](./media/A356.png) |       ![Img](./media/A309.png)       |              ![Img](./media/A415.png)              |
|  ultrasone sensor *1    |              servo *1               |                   DuPont draden                    |
| ![Img](./media/A017.png) |       ![Img](./media/A950.png)       |              ![Img](./media/A024.png)              |
|      breadboard *1      |             jump draden             |batterijhouder *1 <br> (<span style="color: rgb(255, 76, 65);">zelf meegebrachte AA-batterijen *2</span>)|
| ![Img](./media/A336.png) |       ![Img](./media/A131.png)       |                                                   |
|       bat card *1       |          hefboom kaart *1           |                                                   |

#### 3. Componenten Kennis

**Servo**

Een servo is een positiedrager. We kunnen een servo gebruiken om de exacte positie te regelen of een hoog koppel uit te voeren. Meestal wordt het gebruikt in robots, radiografisch bestuurbare auto's en zelfs vliegtuigmodellen. Er zijn veel specificaties, maar alle servo's hebben drie draden: signaal (oranje), positief (rood) en negatief (bruin). De kleur kan variëren per servomerk.

![Img](./media/A5525.png)

**Interne structuurdiagram:**

![Img](./media/A5534.png)

① Signaal: ontvangt besturingssignalen van de microcontroller;

② potentiometer: De positie van de uitgangsas kan worden gemeten, dit behoort tot het feedbackgedeelte van de hele servo;

③ Interne controller: Het ingebedde bord verwerkt signalen van externe besturing, stuurt de motor aan en geeft positieterugkoppelingen, dit is de kern van de hele servo;

④ DC-motor: Het fungeert als actuator om snelheid, koppel en positie uit te voeren;

⑤ Overbrenging / servomechanisme: Het mechanisme vergroot de slaguitgang van de motor naar de uiteindelijke uitgangshoek volgens een bepaalde overbrengingsverhouding.

**De servo aansturen**

Stuur PWM-signalen naar de servosignaallijn om de uitgang te regelen. De duty cycle van de PWM bepaalt direct de positie van de uitgangsas. De periode is meestal 20 milliseconden en wordt typisch ingesteld om pulsen te genereren met een frequentie van 50Hz.

<span style="color: rgb(255, 0, 0);">Bijvoorbeeld (180° servo):</span>

Wanneer we een pulsbreedte van 1,5 milliseconden (ms) naar de 180° servo sturen, beweegt de uitgangsas van de servo naar de middenpositie (90 graden);

Als de pulsbreedte 0,5 ms is, beweegt de uitgangsas naar 0 graden;

Als de pulsbreedte 2,5 ms is, beweegt de uitgangsas naar 180 graden;

![Img](./media/A5545.png)

**Parameters:**

- Bedrijfsspanning: DC 3,3V~5V

- Bedrijfstemperatuur: -10°C ~ +50°C

- Afmetingen: 32,25mm x 12,25mm x 30,42mm

- Interface: 3-pins interface met een afstand van 2,54mm

#### 4. Aansluitschema

![Img](./media/A606.png)

<span style="color: rgb(255, 76, 65);">**Bij gebruik van de ultrasone sensor en servo moeten we een externe voeding aansluiten en de DIP-schakelaar op ON zetten.**</span>

![Img](./media/A902.png)

![Img](./media/A701.png)

#### 5. Code Stroomdiagram

![Img](./media/A716.png)

#### 6. Testcode

Het codebestand is te vinden in map Project 04：Smart-Parking, bestand Project-04-Smart-Parking\.py.

![Img](./media/A3345.png)

**Volledige code:** <span style="color: rgb(255, 76, 65);">De drempelwaarde in de voorwaarde 10 kan worden aangepast aan de werkelijke omstandigheden.</span>

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

#### 7. Testresultaat

Klik op “<span style="color: rgb(255, 76, 65);">Flash</span>” om de code naar het micro:bit board te laden.

![Img](./media/A3400.png)

Na het downloaden van de code naar het board, **zet de voeding aan via micro USB-kabel of externe voeding (zet de DIP-schakelaar op ON)**, en druk op de resetknop op het board.

![Img](./media/A455.png)

Wanneer de ultrasone sensor een voertuig (of object) detecteert dat nadert, bestuurt de servo de hefboom omhoog; als de sensor detecteert dat het zich verwijdert, zal de servo de hefboom laten zakken.

<span style="color: rgb(255, 76, 65);">**LET OP:** Als de bedrading correct is maar je ziet geen resultaat, druk dan op de resetknop aan de achterkant van het board.</span>

![Img](./media/A021.gif)
