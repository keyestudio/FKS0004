### Progetto 05: Quadrante Auto

#### 1. Panoramica

In questo progetto, combiniamo un potenziometro regolabile, un servo e una bella scheda quadrante per realizzare un semplice modello di quadrante per auto.

#### 2. Componenti

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| scheda micro:bit *1 | scheda di espansione micro:bit tipo T *1 | cavo micro USB *1 |
| ![Img](./media/A350.png)| ![Img](./media/A309.png)| ![Img](./media/A950.png) |
| potenziometro *1 | servo *1 | fili jumper |
|![Img](./media/A017.png)  | ![Img](./media/A024.png) |![Img](./media/A233.png) |
|breadboard *1 |portapile *1 <br> (<span style="color: rgb(255, 76, 65);">pile AA auto-fornite *2</span>)| scheda potenziometro *1 |
|![Img](./media/A1326.png) |  |  |
|scheda quadrante auto*1| |  |

#### 3. Conoscenze sui Componenti

**potenziometro**

![Img](./media/A350.png)

Un potenziometro è anche un elemento resistivo con tre contatti, il cui valore di resistenza può essere regolato secondo una certa regolarità.

Sono disponibili in tutte le forme, dimensioni e valori, ma hanno tutti in comune:

① Tre terminali (o punti di connessione).

② Una manopola o cursore mobile che può cambiare la resistenza tra il terminale intermedio e qualsiasi terminale esterno.

③ Quando la manopola viene spostata, la resistenza tra il terminale intermedio e qualsiasi terminale esterno varia da 0Ω al suo massimo.

Il simbolo circuitale del potenziometro:

![Img](./media/A654.png)

(1)\. Come partitore di tensione

Il potenziometro è una resistenza regolabile continuamente. Quando si ruota il suo cursore, il contatto mobile scorre lungo la resistenza. A questo punto, può essere fornita una tensione in uscita in base alla tensione applicata al potenziometro e all'angolo o corsa di rotazione del cursore mobile.

(2)\. Come resistore variabile

Quando il potenziometro è usato come resistore variabile, si collega il suo terminale intermedio a uno dei due terminali aggiuntivi nel circuito. In questo modo, si può ottenere un valore di resistenza stabile e continuamente variabile all'interno del suo intervallo.

(3)\. Come controllore di corrente

Quando è usato come controllore di corrente, il contatto mobile deve essere collegato come uno dei terminali di uscita.

#### 4. Schema di Collegamento

![Img](./media/A812.png)

<span style="color: rgb(255, 76, 65);">Quando si usa il servo, dobbiamo collegare un'alimentazione esterna e impostare l'interruttore DIP su ON.</span>

![Img](./media/A902.png)

![Img](./media/A836.png)

#### 5. Flusso del Codice

![Img](./media/A0854.png)

#### 6. Codice di Test

Il file del codice è fornito nella cartella Progetto 05：Quadrante Auto, file Project-05-Car-Dial.hex.

![Img](./media/A922.png)

**Carica i blocchi di codice:**

![Img](./media/A942.png)

#### 7. Risultato del Test

Dopo aver scaricato il codice sulla scheda, ruotare la manopola sul potenziometro e il servo muove l'indicatore sul quadrante.

<span style="color: rgb(255, 76, 65);">**ATTENZIONE:** Se il cablaggio è corretto ma non si vedono risultati, premere il pulsante di reset sul retro della scheda.</span>

![Img](./media/A706.gif)
