### Progetto 02: Semaforo

#### 1. Panoramica

In questo progetto, utilizziamo tre LED (rosso, giallo e verde), un altoparlante sulla scheda micro:bit e una matrice LED 5x5 per realizzare un modello di semaforo.

#### 2. Componenti

|              ![Img](./media/A850.png)              |       ![Img](./media/A858.png)       | ![Img](./media/A906.png) |
| :-----------------------------------------------: | :---------------------------------: | :---------------------: |
|                scheda micro:bit *1                 | scheda di espansione micro:bit tipo T *1 |   cavo micro USB *1    |
|              ![Img](./media/A937.png)              |      ![Img](./media/A5652.png)       | ![Img](./media/A658.png) |
|                    LED rosso *1                     |            LED giallo *1            |      LED verde *1       |
|              ![Img](./media/A944.png)              |       ![Img](./media/A950.png)       | ![Img](./media/A017.png) |
|                 resistore 220Ω *3                  |             fili jumper              |      breadboard *1      |
|              ![Img](./media/A024.png)              |       ![Img](./media/A020.png)       |                         |
| portabatterie *1 <br> (<span style="color: rgb(255, 76, 65);">batterie AA auto-fornite *2</span>)|       scheda semaforo *1        |                         |

#### 3. Conoscenza dei Componenti

**Altoparlante**

![Img](./media/A833.png)

Micro:bit è dotato di un altoparlante, che rende facile produrre suoni nel tuo progetto.

#### 4. Schema di Collegamento

![Img](./media/A908.png)

<span style="color: rgb(255, 76, 65);">**Nota:** la scheda micro:bit deve essere inserita nella scheda di espansione tipo T come mostrato sotto. La matrice LED della scheda micro:bit deve essere sullo stesso lato del logo della scheda di espansione.</span>

![Img](./media/A940.png)

#### 5. Flusso del Codice

![Img](./media/A5956.png)

#### 6. Codice di Test

Il file di codice è fornito nella cartella Progetto 02：Semaforo, file Project-02-Traffic-Lights\.py.

![Img](./media/A250.png)

**Codice completo:** 

```python
'''
Function: traffic lights with countdowns and buzzes
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import microbit related libraries
from microbit import *

pin1.write_digital(0) # set P1 pin to low
pin2.write_digital(0) # set P2 pin to low
pin8.write_digital(0) # set P8 pin to low

import music # import music libraries

while True:
   pin1.write_digital(1)  # P1 pin to high
   display.show('6')  # LED matrixs shows 6
   sleep(1000)        # delay 1s
   display.show('5')
   sleep(1000)
   display.show('4')
   sleep(1000)
   display.show('3')
   sleep(1000)
   display.show('2')
   sleep(1000)
   display.show('1')
   sleep(1000)
   display.show('0')
   sleep(1000)
   pin1.write_digital(0)
   pin2.write_digital(1)
   music.play("C4:4")    # speaker plays C4 tone
   display.show('2')
   sleep(500)
   pin2.write_digital(0)
   music.reset()         # no tone
   sleep(500)
   pin2.write_digital(1)
   music.play("C4:4")
   display.show('1')
   sleep(500)
   pin2.write_digital(0)
   music.reset()
   sleep(500)
   pin2.write_digital(1)
   music.play("C4:4")
   display.show('0')
   sleep(500)
   pin2.write_digital(0)
   music.reset()
   sleep(500)
   pin8.write_digital(1)
   display.show('6')
   sleep(1000)
   display.show('5')
   sleep(1000)
   display.show('4')
   sleep(1000)
   display.show('3')
   sleep(1000)
   display.show('2')
   sleep(1000)
   display.show('1')
   sleep(1000)
   display.show('0')
   sleep(1000)
   pin8.write_digital(0)
```

#### 7. Risultato del Test

Clicca su “<span style="color: rgb(255, 76, 65);">Flash</span>” per caricare il codice sulla scheda micro:bit.

![Img](./media/A353.png)

Dopo aver scaricato il codice sulla scheda, **accendi tramite cavo micro USB o alimentatore esterno (imposta l'interruttore DIP su ON)**, e premi il pulsante di reset sulla scheda.

![Img](./media/A455.png)

Il LED verde si accende e la matrice LED 5×5 conta alla rovescia 6 secondi. Dopo che il LED verde si spegne, il LED giallo lampeggia e la matrice conta 3 secondi con suono dall'altoparlante. Infine, il LED rosso si accende con un conto alla rovescia di 6 secondi. Queste azioni si ripetono.

<span style="color: rgb(255, 76, 65);">**ATTENZIONE:** Se il cablaggio è corretto ma non vedi i risultati, premi il pulsante di reset sul retro della scheda.</span>

![Img](./media/A459.gif)

<span style="color: rgb(255, 76, 65);">**Quando si alimenta tramite alimentatore esterno, impostare l'interruttore DIP su ON.**</span>

![Img](./media/A904.png)
