### Progetto 06: Festa Musicale

![Img](./media/A1317.png)

#### 1. Panoramica

Quando battiamo le mani, il microfono sulla scheda rileva i segnali sonori e l'altoparlante riproduce una allegra canzone di compleanno mentre il LED RGB emette una luce abbagliante.

#### 2. Componenti

| ![Img](./media/A850.png) |              ![Img](./media/A858.png)              | ![Img](./media/A906.png) |
| :---------------------: | :-----------------------------------------------: | :---------------------: |
|   scheda micro:bit *1   |        scheda di espansione micro:bit tipo T *1   |   cavo micro USB *1     |
| ![Img](./media/A500.png) |              ![Img](./media/A944.png)              | ![Img](./media/A950.png) |
|       LED rosso *1      |                 resistore 220Ω *3                  |      filo jumper *2     |
| ![Img](./media/A017.png) |              ![Img](./media/A024.png)              | ![Img](./media/A621.png) |
|      breadboard *1      |portapile *1 <br> (<span style="color: rgb(255, 76, 65);">pile AA auto-fornite *2</span>)|       scheda RGB *1     |

#### 3. Conoscenza dei Componenti

**Microfono**

Un microfono digitale di alta qualità è integrato sul lato frontale della scheda micro:bit V2 per rilevare segnali sonori e audio. Il chip che controlla e processa il microfono si trova sul retro.

![Img](./media/A1317.png)

Il microfono è in un piccolo foro rotondo sul davanti della scheda, comodo per catturare i segnali sonori circostanti. Basta posizionare la scheda micro:bit con il lato frontale rivolto verso l'alto durante l'uso. Accanto al foro c'è un indicatore LED del microfono. Quando il micro:bit misura i livelli sonori, l'indicatore si accende.

![Img](./media/A116.png)

**LED RGB**

![Img](./media/A2127.png)

Il LED RGB è rappresentato dall'intersezione di tre colori primari (RGB): rosso, verde e blu. La maggior parte dei colori può essere sintetizzata da RGB in proporzioni diverse. I LED rosso, verde e blu sono racchiusi in un involucro di plastica trasparente per emettere colori di luce modificando la tensione di ingresso dei pin R, G e B.

![Img](./media/A137.png)

**Teoria tricromatica:**

![Img](./media/A150.png)

Il LED RGB può essere diviso in due tipi: anodo comune e catodo comune:

In un LED RGB a catodo comune, i tre LED condividono una connessione negativa (catodo);

In un LED RGB ad anodo comune, i tre LED condividono una connessione positiva (anodo).

![Img](./media/A209.png)

<span style="color: rgb(255, 76, 65);">**Nota: Qui forniamo un LED RGB a catodo comune.**</span>

**Pin del LED RGB:**

Il LED RGB ha 4 pin: GND (il più lungo), R (rosso), G (verde) e B (blu). Posizionare il LED RGB come mostrato sotto, i pin da sinistra a destra sono rosso, GND, verde e blu.

![Img](./media/A239.png)

#### 4. Schema di Collegamento

![Img](./media/A308.png)

![Img](./media/A325.png)

#### 5. Flusso del Codice

![Img](./media/A343.png)

#### 6. Codice di Test

Il file del codice è fornito nella cartella Progetto 06：Festa Musicale, file Project-06-Music-Party\.py.

![Img](./media/A3523.png)

**Codice completo:**

```python
'''
Function: Clap your hands, the microbit microphone receives the sound signal, the music sounds, and the RGB emits a dazzling light to simulate a musical party
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from microbit import *
import music

display.clear() # clear LED matrix

while True:
    if microphone.current_event() == SoundEvent.LOUD:  # If the microphone picks up a loud signal
       music.play(["G3:4", "G3", "A4"]) # the speaker plays some tones
       pin1.write_analog(1023)      # P1 analog value is 1023,RGB is red
       pin2.write_analog(0)
       # pin3.write_analog(0)
       sleep(100)
       music.play(["G4:4", "C5", "B4"])
       pin1.write_analog(0)         # P1 analog value is 0,RGB is not red
       pin2.write_analog(1023)      # P2 analog value is 1023,RGB is green
       # pin3.write_analog(0)
       sleep(100)
       pin1.write_analog(10)
       pin2.write_analog(10)
       # pin3.write_analog(1023)      # P3 analog value is 1023,RGB is blue
       sleep(100)
       music.play(["G4:4", "D5", "C5"])
       pin1.write_analog(123)
       pin2.write_analog(123)
       # pin3.write_analog(0)
       sleep(100)
       music.play(["G4:4", "D5", "C5"])
       pin1.write_analog(1023)
       pin2.write_analog(400)
       # pin3.write_analog(1023)
       sleep(100)
       music.play(["G3:4", "G3", "G4"])
       pin1.write_analog(10)
       pin2.write_analog(1023)
       # pin3.write_analog(1023)
       sleep(100)
       pin1.write_analog(1023)
       pin2.write_analog(1023)
       # pin3.write_analog(1023)
       sleep(100)
       music.play(["E5:4", "C5", "B4", "A4"])
       pin1.write_analog(32)
       pin2.write_analog(184)
       # pin3.write_analog(336)
       sleep(100)
       pin1.write_analog(640)
       pin2.write_analog(328)
       # pin3.write_analog(180)
       sleep(100)
       music.play(["F5:4", "F5", "E5"])
       pin1.write_analog(552)
       pin2.write_analog(172)
       # pin3.write_analog(904)
       sleep(100)
       pin1.write_analog(1020)
       pin2.write_analog(796)
       # pin3.write_analog(560)
       sleep(100)
       music.play(["C5:4", "D5", "C5"])
       pin1.write_analog(136)
       pin2.write_analog(560)
       # pin3.write_analog(140)
       sleep(100)
       pin1.write_analog(0)
       pin2.write_analog(0)
       # pin3.write_analog(0)
       sleep(100)
if microphone.current_event() == SoundEvent.QUIET:  # If the microphone picks up a quie signal
       pin1.write_analog(0)
       pin2.write_analog(0)
```

#### 7. Risultato del Test

Clicca su “<span style="color: rgb(255, 76, 65);">Flash</span>” per caricare il codice sulla scheda micro:bit.

![Img](./media/A3540.png)

Dopo aver scaricato il codice sulla scheda, **accendi tramite cavo micro USB o alimentazione esterna (imposta l'interruttore DIP su ON)** e premi il pulsante di reset sulla scheda.

![Img](./media/A455.png)

Quando battiamo le mani, il microfono sulla scheda rileva i segnali sonori e l'altoparlante riproduce una allegra canzone di compleanno mentre il LED RGB emette una luce abbagliante. Non è forse una festa musicale in un'atmosfera felice e gioiosa?

<span style="color: rgb(255, 76, 65);">**ATTENZIONE:** Se il cablaggio è corretto ma non vedi i risultati, premi il pulsante di reset sul retro della scheda.</span>

![Img](./media/A757.gif)
