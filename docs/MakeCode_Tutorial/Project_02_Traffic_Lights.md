### Progetto 02: Semaforo

#### 1. Panoramica

In questo progetto, utilizziamo tre LED (rosso, giallo e verde), un altoparlante sulla scheda micro:bit e una matrice LED 5x5 per realizzare un modello di semaforo.

#### 2. Componenti

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| scheda micro:bit *1 | scheda di espansione tipo T per micro:bit *1 | cavo micro USB *1 |
| ![Img](./media/A937.png)| ![Img](./media/A5652.png) | ![Img](./media/A658.png) |
| LED rosso *1 | LED giallo *1 | LED verde *1 |
| ![Img](./media/A944.png) | ![Img](./media/A950.png) |![Img](./media/A017.png) |
| resistore 220Ω *3 | fili jumper | breadboard *1 |
|  ![Img](./media/A024.png) |  ![Img](./media/A020.png) |  |
| portabatterie *1 <br> (<span style="color: rgb(255, 76, 65);">batterie AA auto-fornite *2</span>) | scheda semaforo *1 | |

#### 3. Conoscenza dei Componenti

**Altoparlante**

![Img](./media/A833.png)

Micro:bit è dotato di un altoparlante, che facilita la produzione di suoni nel tuo progetto.

#### 4. Schema di Collegamento

![Img](./media/A908.png)

<span style="color: rgb(255, 76, 65);">**Nota:** la scheda micro:bit deve essere inserita nella scheda di espansione tipo T come mostrato sotto. La matrice LED della scheda micro:bit deve essere sullo stesso lato del logo della scheda di espansione.</span>

![Img](./media/A940.png)

#### 5. Flusso del Codice

![Img](./media/A5956.png)

#### 6. Codice di Test

Il file del codice è fornito nella cartella Progetto 02：Semaforo, file Project-02-Traffic-Lights.hex.

![Img](./media/A0017.png)

**Carica i blocchi di codice:**

![Img](./media/A605.png)

#### 7. Risultato del Test

Per l'app Windows 10, clicca su “<span style="color: rgb(255, 76, 65);">Download</span>”. Per i browser, invia il file “<span style="color: rgb(255, 76, 65);">.hex</span>” scaricato alla scheda micro:bit.

Dopo aver scaricato il codice sulla scheda, il LED verde si accende e la matrice LED 5×5 effettua un conto alla rovescia di 6 secondi. Dopo lo spegnimento del LED verde, il LED giallo lampeggia e la matrice conta 3 secondi con l'altoparlante che suona. Infine, il LED rosso si accende con un conto alla rovescia di 6 secondi. Queste azioni si ripetono.

<span style="color: rgb(255, 76, 65);">**ATTENZIONE:** Se il cablaggio è corretto ma non vedi i risultati, premi il pulsante di reset sul retro della scheda.</span>

![Img](./media/A459.gif)

<span style="color: rgb(255, 76, 65);">**Quando si alimenta tramite alimentatore esterno, impostare l'interruttore DIP su ON.**</span>

![Img](./media/A904.png)
