### Progetto 04: Parcheggio Intelligente

#### 1. Panoramica

I parcheggi intelligenti sono ovunque. Possiamo anche creare un parcheggio intelligente? Certo. Possiamo usare un sensore a ultrasuoni per rilevare se ci sono veicoli davanti. Quando un veicolo (o un oggetto) viene rilevato in avvicinamento, controlliamo il servo per sollevare l'asta di sollevamento; se viene rilevato che si allontana, il servo abbasserà l'asta di sollevamento.

#### 2. Componenti

| ![Img](./media/A850.png) |       ![Img](./media/A858.png)       |              ![Img](./media/A906.png)              |
| :---------------------: | :---------------------------------: | :-----------------------------------------------: |
|   micro:bit board *1    | micro:bit T-type expansion board *1 |                micro USB cable *1                 |
| ![Img](./media/A356.png) |       ![Img](./media/A309.png)       |              ![Img](./media/A415.png)              |
|  ultrasonic sensor *1   |              servo *1               |                   DuPont wires                    |
| ![Img](./media/A017.png) |       ![Img](./media/A950.png)       |              ![Img](./media/A024.png)              |
|      breadboard *1      |             jump wires              |battery holder *1 <br> (<span style="color: rgb(255, 76, 65);">batterie AA auto-fornite *2</span>)|
| ![Img](./media/A336.png) |       ![Img](./media/A131.png)       |                                                   |
|       bat card *1       |          lift rod card *1           |                                                   |

#### 3. Conoscenza dei Componenti

**Servo**

Il servo è un attuatore di posizione. Possiamo usare il servo per controllare la posizione esatta o fornire alta coppia. Di solito viene usato in robot, automobili radiocomandate e persino modelli di aeroplani. Esistono molte specifiche, ma tutti i servi hanno tre fili: segnale (arancione), positivo (rosso) e negativo (marrone). Il colore può variare a seconda della marca del servo.

![Img](./media/A5525.png)

**Diagramma della struttura interna:**

![Img](./media/A5534.png)

① Segnale: riceve i segnali di controllo dal microcontrollore;

② potenziometro: può misurare la posizione dell'albero di uscita, fa parte del feedback dell'intero servo;

③ Controllore interno: la scheda embedded elabora i segnali di controllo esterni, aziona il motore e i segnali di feedback della posizione, è il cuore dell'intero servo;

④ Motore DC: funge da attuatore per fornire velocità, coppia e posizione;

⑤ Trasmissione / meccanismo del servo: il meccanismo amplifica la corsa fornita dal motore all'angolo finale di uscita secondo un certo rapporto di trasmissione.

**Azionare il servo**

Inviare segnali PWM alla linea del segnale del servo per controllarne l'uscita. Il duty cycle del PWM determina direttamente la posizione dell'albero di uscita. Il periodo è solitamente di 20 millisecondi e tipicamente impostato per generare impulsi a una frequenza di 50Hz.

<span style="color: rgb(255, 0, 0);">Ad esempio (servo 180°):</span>

Quando inviamo un impulso di larghezza 1,5 millisecondi (ms) al servo 180°, l'albero di uscita del servo si sposterà nella posizione centrale (90 gradi);

Se la larghezza dell'impulso è 0,5ms, l'albero di uscita si sposterà a 0 gradi;

Se la larghezza dell'impulso è 2,5ms, l'albero di uscita si sposterà a 180 gradi;

![Img](./media/A5545.png)

**Parametri:**

- Tensione di funzionamento: DC 3.3V~5V

- Temperatura di funzionamento: -10°C ~ +50°C

- Dimensioni: 32.25mm x 12.25mm x 30.42mm

- Interfaccia: interfaccia a 3 pin con passo di 2.54mm

#### 4. Schema di Collegamento

![Img](./media/A606.png)

<span style="color: rgb(255, 76, 65);">**Quando si utilizzano il sensore a ultrasuoni e il servo, dobbiamo collegare un'alimentazione esterna e impostare l'interruttore DIP su ON.**</span>

![Img](./media/A902.png)

![Img](./media/A701.png)

#### 5. Flusso del Codice

![Img](./media/A716.png)

#### 6. Codice di Test

Il file del codice è fornito nella cartella Progetto 04：Smart-Parking, file Project-04-Smart-Parking\.py.

![Img](./media/A3345.png)

**Codice completo:** <span style="color: rgb(255, 76, 65);">La soglia nella condizione 10 può essere modificata in base alle condizioni reali.</span>

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

#### 7. Risultato del Test

Clicca “<span style="color: rgb(255, 76, 65);">Flash</span>” per caricare il codice sulla scheda micro:bit.

![Img](./media/A3400.png)

Dopo aver scaricato il codice sulla scheda, **accendi tramite cavo micro USB o alimentazione esterna (imposta l'interruttore DIP su ON)**, e premi il pulsante di reset sulla scheda.

![Img](./media/A455.png)

Quando il sensore a ultrasuoni rileva un veicolo (o oggetto) in avvicinamento, il servo controlla l'asta di sollevamento per alzarla; se il sensore rileva che si allontana, il servo abbasserà l'asta di sollevamento.

<span style="color: rgb(255, 76, 65);">**ATTENZIONE:** Se il cablaggio è corretto ma non vedi i risultati, premi il pulsante di reset sul retro della scheda.</span>

![Img](./media/A021.gif)
