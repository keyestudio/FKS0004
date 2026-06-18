### Progetto 03: Pipistrello a Rilevamento Distanza

#### 1. Panoramica

Basato su un sensore ad ultrasuoni, il pipistrello a rilevamento distanza misura la distanza degli ostacoli e la visualizza in tempo reale su un OLED. Quando è inferiore a 10cm, l'altoparlante emette un allarme.

#### 2. Componenti

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| scheda micro:bit *1 | scheda di espansione micro:bit tipo T *1 | cavo micro USB *1 |
| ![Img](./media/A356.png)| ![Img](./media/A406.png)| ![Img](./media/A415.png) |
| sensore ad ultrasuoni *1 | modulo OLED *1 | fili DuPont |
|![Img](./media/A017.png) | ![Img](./media/A950.png) | ![Img](./media/A024.png) |
|breadboard *1 | fili jumper | portabatterie *1 <br> (<span style="color: rgb(255, 76, 65);">batterie AA auto-fornite *2</span>)|
|![Img](./media/A315.png)|![Img](./media/A557.png) | |
|scheda pipistrello *1| scheda OLED *1 | |

#### 3. Conoscenza dei Componenti

**sensore ad ultrasuoni**

Le onde ultrasoniche rimbalzano quando colpiscono un ostacolo. Misuriamo la distanza calcolando l'intervallo di tempo tra l'invio e la ricezione delle onde. Poiché la velocità di propagazione del suono nell'aria è una costante v=340m/s, calcoliamo la distanza tra il sensore e l'ostacolo: s=vt/2.

![Img](./media/A846.png)

Il modulo ad ultrasuoni HC-SR04 integra un trasmettitore e un ricevitore. Il primo converte segnali elettrici (energia elettrica) in onde sonore ad alta frequenza (oltre l'udito umano) (energia meccanica), mentre il secondo fa l'opposto.

Lo schema del HC SR04:

![Img](./media/A642.png)

**Definizione dei Pin:**

![Img](./media/A702.png)

**Parametri:**

- Tensione di funzionamento: 5V
- Corrente di funzionamento: 12mA
- Distanza minima di misurazione: 2cm
- Distanza massima di misurazione: 200cm

**Principio di funzionamento:**

Un impulso di livello alto della durata di almeno 10us viene inviato sul pin Trig, e il modulo inizia a trasmettere onde ultrasoniche. Allo stesso tempo, il pin Echo viene portato alto. Quando il modulo riceve un'onda ultrasonica di ritorno dopo aver incontrato un ostacolo, il pin Echo viene portato basso. La durata del livello alto del pin Echo è il tempo totale dell'onda dall'invio alla ricezione: s=vt/2.

![Img](./media/A728.png)

**Modulo OLED**

La tecnologia OLED presenta una ricca resa cromatica, alto contrasto e ampio angolo di visuale, fornendo immagini chiare e vivide, particolarmente eccellente nel nero.

Ogni pixel del display OLED emette luce propria senza retroilluminazione, quindi consuma relativamente poca energia. Con dimensioni ridotte, alta risoluzione e basso consumo, il display OLED da 0,9 pollici è molto adatto per dispositivi indossabili.

![Img](./media/A636.png)

<span style="color: rgb(255, 76, 65);">**In questo progetto, il modulo display OLED collega l'interfaccia SDA al pin P20 e SCL al pin P19.**</span>

**Parametri:**

- Tensione di funzionamento: DC 3.3V-5V

- Corrente di funzionamento: 30mA

- Interfaccia: porte pin con passo di 2.54mm

- Modalità di comunicazione: I2C

- Chip driver interno: SSD1306

- Risoluzione: 128*64

- Angolo di visuale: maggiore di 150°

#### 4. Schema di Collegamento

![Img](./media/A1849.png)

<span style="color: rgb(255, 76, 65);">**Quando si utilizzano il display OLED e il sensore ad ultrasuoni, è necessario collegare un'alimentazione esterna e impostare l'interruttore DIP su ON.**</span>

![Img](./media/A902.png)

![Img](./media/A1906.png)

#### 5. Flusso del Codice

![Img](./media/A924.png)

#### 6. Codice di Test

Il file di codice è fornito nella cartella Progetto 03：Pipistrello a Rilevamento Distanza, file Project-03-Ranging-Bat.hex.

![Img](./media/A955.png)

**Carica i blocchi di codice:** <span style="color: rgb(255, 76, 65);">La soglia nella condizione 10 può essere modificata in base alle condizioni reali.</span>

![Img](./media/A022.png)

#### 7. Risultato del Test

Per l'App Windows 10, cliccare su “<span style="color: rgb(255, 76, 65);">Download</span>”. Per i browser, inviare il file “<span style="color: rgb(255, 76, 65);">.hex</span>” scaricato alla scheda micro:bit.

Dopo aver scaricato il codice sulla scheda, <span style="color: rgb(255, 76, 65);">accendere tramite alimentazione esterna e impostare l'interruttore DIP su ON</span>, e l'OLED visualizza in tempo reale la distanza tra il sensore ad ultrasuoni e l'ostacolo. Quando il valore della distanza è inferiore a 10cm, l'altoparlante sulla scheda micro:bit emette un allarme.

<span style="color: rgb(255, 76, 65);"><span style="color: rgb(255, 76, 65);">**ATTENZIONE:** Se il cablaggio è corretto ma non si vedono i risultati, premere il pulsante di reset sul retro della scheda.</span></span>

![Img](./media/A605.gif)
