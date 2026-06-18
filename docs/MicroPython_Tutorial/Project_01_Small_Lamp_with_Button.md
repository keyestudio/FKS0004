### Progetto 01: Piccola Lampada con Pulsante

#### 1. Panoramica

Ci sono due pulsanti programmabili sulla parte frontale della scheda micro:bit (A e B). Li combiniamo con un LED rosso e una scheda lampada per costruire una piccola lampada da scrivania. Quando si preme il pulsante A, il LED rosso si accende; quando si preme B, si spegne.

#### 2. Componenti

| ![Img](./media/A850.png) |              ![Img](./media/A858.png)              | ![Img](./media/A906.png) |
| :---------------------: | :-----------------------------------------------: | :---------------------: |
|   scheda micro:bit *1    |        scheda di espansione micro:bit tipo T *1        |   cavo micro USB *1    |
| ![Img](./media/A937.png) |              ![Img](./media/A944.png)              | ![Img](./media/A950.png) |
|       LED rosso *1        |                 resistore 220Ω *1                  |      filo jumper *2       |
| ![Img](./media/A017.png) |              ![Img](./media/A024.png)              | ![Img](./media/A920.png) |
|      breadboard *1      | portabatterie *1 <br> (<span style="color: rgb(255, 76, 65);">batterie AA auto-fornite *2</span>) |      scheda lampada *1       |

#### 3. Conoscenza dei Componenti

**Pulsanti**

I pulsanti possono controllare l'accensione e lo spegnimento del circuito. Quando un pulsante è collegato a un circuito, il circuito è aperto quando il pulsante non è premuto; il circuito si chiude dopo aver premuto il pulsante.

Ci sono tre pulsanti sulla scheda micro:bit: un pulsante di reset sul retro e due pulsanti programmabili (A e B) sulla parte frontale.

![Img](./media/A230.png)

**Resistori**

![Img](./media/A248.png)

Un resistore è un componente elettronico che limita la corrente in un ramo del circuito. La resistenza di un resistore fisso non può essere regolata, mentre quella di un potenziometro o di un resistore variabile può esserlo.

Ecco due simboli circuitali comuni per i resistori. Se vedi questi simboli in un circuito, rappresentano un resistore.

![Img](./media/A303.png)

Ω è l'unità di resistenza, inclusi Ω, KΩ, MΩ, ecc. Possono essere espressi come: 1 MΩ=1000 KΩ, 1 KΩ =1000 Ω. In generale, alcune resistenze sono indicate sulla superficie.

Quando si usa un resistore, dobbiamo prima conoscere la sua resistenza. Ci sono due modi: osservare la banda colorata su di esso, o misurare la sua resistenza con un multimetro. Ovviamente, il primo è più comodo e veloce.

![Img](./media/A317.png)

Come mostrato nella scheda dei resistori, ogni colore rappresenta un numero.

![Img](./media/A3335.png)

I resistori a 4 e 5 bande sono comunemente usati.

Spesso, quando si riceve un resistore, può essere difficile decidere da dove iniziare a leggere i colori.

**Pertanto, puoi osservare lo spazio tra le due bande a un'estremità; se è più ampio di qualsiasi altro spazio tra bande, leggi dall'estremità opposta.**

<span style="color: rgb(255, 76, 65);">**Nota che lo spazio tra la 4ª e la 5ª banda (la 3ª e la 4ª) è relativamente ampio in un resistore a 5 bande (4 bande).**</span>

Vediamo come leggere la resistenza di un resistore a 5 bande, come mostrato di seguito:

![Img](./media/A426.png)

Per questo resistore, la resistenza dovrebbe essere letta da sinistra a destra. Il valore dovrebbe essere: 1ª banda 2ª banda 3ª banda x 10^moltiplicatore(Ω), ±tolleranza%.

Quindi, la resistenza di questo resistore è 2(rosso) 2(rosso) 0(nero) × 10^0 (nero)Ω = 220Ω, ±1%(marrone). Per saperne di più sul [resistore da Wiki](https://en.wikipedia.org/wiki/Resistor).

**LED**

LED, chiamato completamente “diodo a emissione luminosa”, è un dispositivo elettronico fatto di materiali semiconduttori (silicio, selenio, germanio, ecc.). È polare, con un polo positivo - il pin lungo collegato a VCC (V o 3.3V o 5V o +), e un polo negativo - il pin corto collegato a GND (G o -). La corrente scorre dal positivo al negativo, in un flusso unidirezionale.

Simbolo elettronico e grafico del LED:

![Img](./media/A515.png)

LED di varie dimensioni e colori:

![Img](./media/A525.png)

Rosso, giallo, blu, verde e bianco sono i colori più comuni del LED, che corrispondono ai loro colori di aspetto. Raramente si usa il LED trasparente, e la luce emessa potrebbe non essere bianca. Ci sono quattro dimensioni di LED: 3mm, 5mm (più comune), 8mm e 10mm.

![Img](./media/A535.png)

La tensione diretta deve essere usata quando il LED è acceso. È un parametro molto importante da conoscere quando si usa un LED, poiché determina quanta potenza si usa e quanto grande deve essere il resistore limitatore di corrente. Per la maggior parte dei LED rossi, gialli, arancioni e verde chiaro, tipicamente usano una tensione tra 1.9V e 2.1V.

![Img](./media/A548.png)

Secondo la legge di Ohm, la corrente attraverso il circuito diminuisce all'aumentare della resistenza, causando l'attenuazione del LED.

I = (VP-Vl)/R

Per rendere il LED sicuro e con la giusta luminosità, quanta resistenza dovremmo usare nel circuito?

Per il 99% dei LED da 5mm, la corrente raccomandata è 20mA, come si vede dalla colonna delle condizioni nella sua scheda tecnica:

![Img](./media/A613.png)

Ora convertiamo la formula sopra nella seguente:

R = (VP-Vl)/I

Se VP = 5V, Vl (tensione diretta) = 2V, e I = 20mA, possiamo dire che R è 150Ω. Pertanto, possiamo rendere il LED più luminoso riducendo la resistenza, ma la resistenza non dovrebbe essere inferiore a 150Ω (questo valore potrebbe non essere preciso perché il LED fornito varia).

La tensione diretta e la lunghezza d'onda dei LED di diversi colori sono mostrate di seguito come riferimento:

![Img](./media/A629.png)

<span style="color: rgb(255, 76, 65);">**Non collegare un resistore con resistenza molto bassa direttamente ai due poli dell'alimentazione, altrimenti i componenti elettronici potrebbero danneggiarsi a causa della corrente eccessiva. I resistori non sono polari.**</span>

**Breadboard**

Prima di completare qualsiasi circuito, si usa una breadboard per progettare e testare rapidamente i circuiti. Ci sono molti fori su una breadboard in cui possono essere inseriti componenti del circuito (ad esempio, resistori). Una breadboard tipica è mostrata di seguito:

![Img](./media/A655.png)

Una breadboard ha molte strisce metalliche sotto di essa per connettersi ai fori in alto. Sono disposte come mostrato di seguito.

<span style="color: rgb(255, 76, 65);">**Nota che i fori in alto e in basso sono collegati orizzontalmente, mentre gli altri fori sono collegati verticalmente.**</span>

![Img](./media/A723.png)

Le prime due file (in alto) e le ultime due (in basso) della breadboard sono usate rispettivamente per i poli positivo (+) e negativo (-) dell'alimentazione. Il diagramma della disposizione conduttiva è mostrato di seguito:

![Img](./media/A730.png)

Quando si collegano componenti DIP (Dual In-line Packages), come circuiti integrati, microcontrollori, chip, ecc., la scanalatura isola le due parti. Pertanto, i componenti DIP possono essere collegati come mostrato di seguito:

![Img](./media/A740.png)

![Img](./media/A747.png)

**Filo jumper e filo DuPont**

I fili jumper e i fili DuPont collegano due terminali. Esistono vari tipi, ma qui ci concentriamo su quelli usati nella breadboard. Trasmettono segnali elettrici da qualsiasi punto della breadboard ai pin di input/output di un microcontrollore.

Durante l'uso, inserire “due pin” dei fili nella breadboard senza saldatura. Diverse serie di piste parallele sono disposte sotto la superficie della breadboard, quindi i fili devono essere inseriti solo in fori specifici in un particolare prototipo.

Ci sono tre tipi di fili DuPont: F-F, M-M e M-F. Sul filo, il pin è chiamato estremità maschio (M), mentre il foro è femmina (F).

![Img](./media/A811.png)

Più di un tipo può essere usato in un progetto. Sebbene i colori dei fili siano diversi, servono allo stesso scopo. I colori sono usati per distinguere i circuiti.

#### 4. Schema di Collegamento

<span style="color: rgb(255, 76, 65);">Nota: la scheda micro:bit deve essere inserita nella scheda di espansione tipo T come mostrato di seguito. La matrice LED della scheda micro:bit deve essere sullo stesso lato del logo della scheda di espansione.</span>

![Img](./media/A156.png)

<span style="color: rgb(255, 76, 65);">**Il pin di controllo della scheda per il LED è P0 (il pin della scheda di espansione tipo T è digitale 0).**</span>

#### 5. Flusso del Codice

![Img](./media/A4323.png)

#### 6. Codice di Test

Il file di codice è fornito nella cartella Progetto 01：Piccola Lampada con Pulsante, file Project-01-Small-Lamp-with-Button\.py.

![Img](./media/A100.png)

**Codice completo:**

```python
'''
Function: microbit on-board buttons A&B control LED
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import microbit related libraries
from microbit import *

display.show(Image.HEART) # LED matrix displays ❤
pin0.write_digital(0) # set P0 pin to low

while True:
    if button_a.is_pressed():     # if A is pressed
        pin0.write_digital(1)     # P0 is high
        display.show(Image.HAPPY) # LED matrix displays a smile face
    elif button_b.is_pressed():   # or else B is pressed
        pin0.write_digital(0)     # P0 is low
        display.show(Image.SAD)   # LED matrix displays a crying face
```

#### 7. Risultato del Test

Clicca “<span style="color: rgb(255, 76, 65);">Flash</span>” per caricare il codice sulla scheda micro:bit.

![Img](./media/A2156.png)

Dopo aver scaricato il codice sulla scheda, **accendi tramite cavo micro USB o alimentazione esterna (imposta l'interruttore DIP su ON)**, e premi il pulsante di reset sulla scheda.

![Img](./media/A455.png)

Possiamo osservare il fenomeno: la matrice LED 5x5 mostra ![Img](./media/A512.png). Premi il pulsante A, e la matrice LED 5x5 mostra ![Img](./media/A518.png), il LED si accende. Premi il pulsante B, la matrice LED 5x5 mostra ![Img](./media/A527.png), il LED si spegne. Sembra una mini lampada?

<span style="color: rgb(255, 76, 65);">**ATTENZIONE:** Se il cablaggio è corretto ma non vedi i risultati, premi di nuovo il pulsante di reset sul retro della scheda.</span>

![Img](./media/A359.gif)

<span style="color: rgb(255, 76, 65);">Quando si alimenta tramite alimentazione esterna, impostare l'interruttore DIP su ON.</span>

![Img](./media/A904.png)
