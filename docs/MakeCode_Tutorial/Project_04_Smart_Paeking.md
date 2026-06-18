### Progetto 04: Parcheggio Intelligente

#### 1. Panoramica

I parcheggi intelligenti sono ovunque. Possiamo anche creare un parcheggio intelligente? Certo. Possiamo usare un sensore a ultrasuoni per rilevare se ci sono veicoli davanti. Quando un veicolo (o oggetto) viene rilevato in avvicinamento, controlliamo il servo per sollevare l'asta di sollevamento; se viene rilevato che si sta allontanando, il servo abbasserà l'asta di sollevamento.

#### 2. Componenti

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| scheda micro:bit *1 | scheda di espansione micro:bit tipo T *1 | cavo micro USB *1 |
| ![Img](./media/A356.png)| ![Img](./media/A309.png)| ![Img](./media/A415.png) |
| sensore a ultrasuoni *1 | servo *1 | fili DuPont |
|![Img](./media/A017.png) | ![Img](./media/A950.png) | ![Img](./media/A024.png) |
|breadboard *1 | fili jumper | portabatterie *1 <br> (<span style="color: rgb(255, 76, 65);">batterie AA auto-fornite *2</span>)|
|![Img](./media/A336.png) |![Img](./media/A131.png) | |
|scheda bat *1 | scheda asta di sollevamento *1| |

#### 3. Conoscenza dei Componenti

**Servo**

Il servo è un attuatore di posizione. Possiamo usare il servo per controllare la posizione esatta o per fornire alta coppia. Solitamente viene usato in robot, automobili radiocomandate e persino modelli di aeroplani. Esistono molte specifiche, ma tutti i servi hanno tre fili: segnale (arancione), positivo (rosso) e negativo (marrone). Il colore può variare a seconda della marca del servo.

![Img](./media/A5525.png)

**Diagramma della struttura interna:**

![Img](./media/A5534.png)

① Segnale: riceve i segnali di controllo dal microcontrollore;

② potenziometro: può misurare la posizione dell'albero di uscita, fa parte del feedback dell'intero servo;

③ Controller interno: la scheda embedded elabora i segnali di controllo esterni, aziona il motore e i segnali di feedback della posizione, è il cuore dell'intero servo;

④ Motore DC: funge da attuatore per fornire velocità, coppia, posizione;

⑤ Trasmissione / meccanismo del servo: il meccanismo amplifica la corsa fornita dal motore fino all'angolo di uscita finale secondo un certo rapporto di trasmissione.

**Azionare il servo**

Inviare segnali PWM alla linea di segnale del servo per controllarne l'uscita. Il duty cycle del PWM determina direttamente la posizione dell'albero di uscita. Il periodo è solitamente di 20 millisecondi e tipicamente impostato per generare impulsi a una frequenza di 50Hz.

<span style="color: rgb(255, 0, 0);">Per esempio (servo 180°):</span>

Quando inviamo un impulso di larghezza 1,5 millisecondi (ms) al servo 180°, l'albero di uscita del servo si sposterà nella posizione centrale (90 gradi);

Se la larghezza dell'impulso è 0,5 ms, l'albero di uscita si sposterà a 0 gradi;

Se la larghezza dell'impulso è 2,5 ms, l'albero di uscita si sposterà a 180 gradi;

![Img](./media/A5545.png)

**Parametri:**

- Tensione di funzionamento: DC 3,3V~5V

- Temperatura di funzionamento: -10°C ~ +50°C

- Dimensioni: 32,25mm x 12,25mm x 30,42mm

- Interfaccia: interfaccia a 3 pin con passo di 2,54mm

#### 4. Schema di Collegamento

![Img](./media/A606.png)

<span style="color: rgb(255, 76, 65);">**Quando si usano il sensore a ultrasuoni e il servo, dobbiamo collegare un'alimentazione esterna e impostare l'interruttore DIP su ON.**</span>

![Img](./media/A902.png)

![Img](./media/A701.png)

#### 5. Flusso del Codice

![Img](./media/A716.png)

#### 6. Codice di Test

Il file del codice è fornito nella cartella Progetto 04：Smart-Parking, file Project-04-Smart-Parking.hex.

![Img](./media/A758.png)

**Carica i blocchi di codice:** <span style="color: rgb(255, 76, 65);">**La soglia nella condizione 10 può essere modificata in base alle condizioni reali.**</span>

![Img](./media/A832.png)

#### 7. Risultato del Test

Dopo aver scaricato il codice sulla scheda, quando il sensore a ultrasuoni rileva un veicolo (o oggetto) in avvicinamento, il servo controlla l'asta di sollevamento per sollevarla; se il sensore rileva che si sta allontanando, il servo abbasserà l'asta di sollevamento.

<span style="color: rgb(255, 76, 65);">**ATTENZIONE:** Se il cablaggio è corretto ma non si vedono risultati, premere il pulsante di reset sul retro della scheda.</span>

![Img](./media/A021.gif)
