### Progetto 08: Allarme Antifurto

#### 1. Panoramica

Quando l'allarme antifurto intelligente rileva che la scatola antifurto è stata spostata, l'altoparlante sulla scheda micro:bit emetterà un allarme e il LED rosso lampeggerà.

#### 2. Componenti

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| scheda micro:bit *1 | scheda di espansione T-type per micro:bit *1 | cavo micro USB *1 |
| ![Img](./media/A937.png)| ![Img](./media/A944.png) | ![Img](./media/A950.png) |
| LED rosso *1 | resistore 220Ω *1 | filo di collegamento *2 |
| ![Img](./media/A017.png) | ![Img](./media/A024.png) | ![Img](./media/A952.png)  |
| breadboard *1 | portabatterie *1 <br> (<span style="color: rgb(255, 76, 65);">batterie AA auto-fornite *2</span>)| scheda allarme *1 |

#### 3. Conoscenza dei Componenti

**Accelerometro**

![Img](./media/A026.png)

La scheda micro:bit dispone di un sensore di accelerazione integrato LSM303AGR (chiamato accelerometro) che include modalità standard, veloce, plus e ad alta velocità (100 kHz, 400 kHz, 1 MHz e 3.4 MHz) per l'interfaccia bus seriale I2C e interfaccia seriale standard SPI per comunicazione esterna, con risoluzione di 8/10/12 bit e intervallo di ±2g, ±4g o ±8g.

Quando la scheda micro:bit è a riposo o in moto uniforme, l'accelerometro rileva solo l'accelerazione di gravità. Se viene leggermente oscillata, l'accelerazione rilevata è molto inferiore a quella di gravità, quindi la differenza può essere ignorata. Pertanto, rileviamo principalmente il cambiamento dell'accelerazione gravitazionale sugli assi x, y e z.

#### 4. Schema di Collegamento

![Img](./media/A219.png)

<span style="color: rgb(255, 76, 65);">**Il pin di controllo della scheda per il LED è P1 (il pin della scheda di espansione T-type è digitale 1).**</span>

#### 5. Flusso del Codice

![Img](./media/A4434.png)

#### 6. Codice di Test

Il file del codice è fornito nella cartella Progetto 08：Allarme Antifurto, file Project-08-Burglar-Alarm.hex.

![Img](./media/A4518.png)

**Carica i blocchi di codice:** 

<span style="color: rgb(255, 76, 65);">**Dopo aver importato il codice, se il buzzer continua a suonare anche se la breadboard non viene spostata; potrebbe essere causato da fattori geografici. Puoi modificare la soglia nella condizione -60 e 50 in base alle condizioni reali.**</span>

![Img](./media/A611.png)

#### 7. Risultato del Test

Dopo aver scaricato il codice sulla scheda, muovi la breadboard. Se il valore di accelerazione x＜-60 o x＞50, l'altoparlante sulla scheda emette un allarme e il LED lampeggia, e la matrice LED del micro:bit mostra ![Img](./media/A706.png). Altrimenti, l'altoparlante non emette suono e il LED è spento, e la matrice LED del micro:bit mostra ![Img](./media/A720.png).

<span style="color: rgb(255, 76, 65);">**ATTENZIONE:** Se il cablaggio è corretto ma non vedi i risultati, premi il pulsante di reset sul retro della scheda.</span>

![Img](./media/A936.gif)
