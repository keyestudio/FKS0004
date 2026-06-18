## 1. Programmazione su MakeCode

Le seguenti istruzioni si applicano al sistema Windows ma possono anche servire come riferimento se si utilizza un sistema diverso.

#### 1.1. Avvio rapido

**Passo 1 Collegare al micro:bit**

Collegare la scheda al computer tramite cavo USB.

![Img](./media/A800.png)

Se il LED rosso sul retro della scheda è acceso, significa che la scheda è alimentata. Quando il computer comunica con la scheda principale tramite il cavo USB, il LED giallo lampeggia. Ad esempio, lampeggia quando si carica un file “.hex”.

La scheda principale Micro:bit apparirà quindi sul computer come un driver chiamato “MICROBIT”. Si noti che non è un disco USB ordinario come mostrato di seguito.

![Img](./media/A849.png)

**Passo 2 Scrivere il programma heartbeat**

Accedi al link: [versione online di Makecode](https://makecode.microbit.org/)

Clicca su “<span style="color: rgb(255, 76, 65);">Nuovo Progetto</span>” e vedrai “<span style="color: rgb(255, 76, 65);">Creazione di un progetto</span>”, inserisci “<span style="color: rgb(255, 76, 65);">heartbeat</span>” e clicca su “<span style="color: rgb(255, 76, 65);">Crea √</span>”.

<span style="color: rgb(255, 76, 65);">Qui scriviamo programmi su Google Chrome.</span>

![Img](./media/A021.png)

Scriviamo un codice micro:bit.

Puoi trascinare alcuni blocchi nell'area di modifica e quindi eseguire il programma nel simulatore come mostrato di seguito. Qui dimostriamo come modificare il programma <span style="color: rgb(255, 76, 65);">heartbeat</span>.

Video guida operativa:

![Img](./media/A100.png)

**Passo 3 Scaricare i codici**

Generalmente, per l'app Windows 10 ([Ottieni l'app Windows 10](https://apps.microsoft.com/detail/9pjc7sv48lcx?hl=zh-CN&gl=CN#activetab=pivot:overviewtabdocx))(Clicca), basta cliccare su “<span style="color: rgb(255, 76, 65);">Download</span>” per scaricare direttamente il codice sulla scheda micro:bit senza ulteriori passaggi.

Per i browser, invece:

Clicca su “<span style="color: rgb(255, 76, 65);">Download</span>” nell'editor. Questo scaricherà un file “hex”, un formato che la scheda micro:bit può leggere. Successivamente, copialo sulla tua scheda micro:bit come faresti con un file su una chiavetta USB. Su Windows, puoi anche cliccare con il tasto destro sul file “<span style="color: rgb(255, 76, 65);">.hex</span>” e selezionare “**Invia a → MICROBIT**” per copiare il file sulla scheda micro:bit.

![Img](./media/A319.png)

![Img](./media/A449.png)

Oppure, puoi trascinare direttamente il file “<span style="color: rgb(255, 76, 65);">.hex</span>” in MICROBIT.

![Img](./media/A341.png)

![Img](./media/A345.png)

Durante la copia del file “<span style="color: rgb(255, 76, 65);">.hex</span>” sul Micro:bit, il LED giallo sul retro della scheda lampeggia. Quando la copia è completata, il LED smette di lampeggiare e rimane acceso.

**Passo 4 Eseguire il programma**

Dopo che il programma è stato caricato sul Micro:bit, puoi alimentarlo tramite cavo USB o alimentazione esterna. La matrice LED 5 x 5 mostrerà un motivo a battito cardiaco.

![Img](./media/A425.png)

<span style="color: rgb(255, 76, 65);">**Attenzione:**</span> Ogni volta che programmi, il driver del Micro:bit si espelle automaticamente e ritorna, quindi i file hex scompaiono. La scheda ha solo accesso ai file hex ma non li salva.

#### 1.2. MakeCode

Accedi alla [versione online Makecode Google Chrome](https://makecode.microbit.org/). Ecco la sua interfaccia principale.

![Img](./media/A637.png)

Nell'area di modifica del codice ci sono i blocchi “**on start**” e “**forever**”. <span style="color: rgb(255, 76, 65);">Dopo l'accensione, il codice in “on start” viene eseguito una sola volta, mentre quello in “forever” viene eseguito ciclicamente.</span>

Clicca sulla lingua “**JS JavaScript**”:

![Img](./media/A754.png)

Cambia in “**Python**”:

![Img](./media/A814.png)


#### 1.3. Introduzione alle funzioni WebUSB

Come detto prima, se il tuo computer è Windows 10 e hai scaricato l'app MakeCode, puoi scaricare rapidamente i codici sulla scheda tramite il pulsante “<span style="color: rgb(255, 76, 65);">Download</span>”. Usiamo il webUSB di **<span style="color: rgb(255, 76, 65);">Google Chrome</span>** per accedere al dispositivo hardware collegato via USB.

**Accoppiamento dispositivi:**

1\. Collega la scheda al computer tramite cavo USB.

![Img](./media/A951.png)

2\. Clicca su “<span style="color: rgb(255, 76, 65);">Download</span>” -> “<span style="color: rgb(255, 76, 65);">...</span>” e “<span style="color: rgb(255, 76, 65);">Connetti dispositivo</span>”.

![Img](./media/A028.png)

3\. “<span style="color: rgb(255, 76, 65);">Avanti</span>”.

![Img](./media/A046.png)

4\. “<span style="color: rgb(255, 76, 65);">Accoppia</span>”.

![Img](./media/A104.png)

5\. Seleziona il dispositivo corrispondente e “<span style="color: rgb(255, 76, 65);">Connetti</span>”.

![Img](./media/A127.png)

6\. “<span style="color: rgb(255, 76, 65);">Fatto</span>”.

![Img](./media/A144.png)

**Scarica il programma:**

Dopo la connessione, clicca su “<span style="color: rgb(255, 76, 65);">Download</span>” e vedrai che ![Img](./media/A212.png) diventa ![Img](./media/A220.png). Il programma viene scaricato sulla scheda micro:bit.

![Img](./media/A232.png)

Se non appare nessun dispositivo per la selezione, consulta [Risoluzione problemi download con WebUSB](https://makecode.microbit.org/device/usb/webusb/troubleshoot). Consulta [la guida utente](https://microbit.org/guide/firmware/) per sapere come aggiornare il firmware micro:bit.

#### 1.4. Libreria di estensioni MakeCode

**3.4.1 Importa estensioni libreria**

Apri Makecode per entrare in un progetto specifico, clicca su ![Img](./media/A806.png) per scegliere “**Estensioni**”.

![Img](./media/A842.png)

Oppure clicca su “**Estensioni**” sopra la sezione Avanzate.

![Img](./media/A900.png)

Cerca la libreria che desideri.

![Img](./media/A909.png)

Forniamo i file di codice per ogni progetto contenenti tutto il necessario per eseguire un progetto, quindi puoi caricarli direttamente. Se vuoi costruire i blocchi di codice da solo, ricorda di aggiungere le seguenti tre estensioni.

<span style="color: rgb(0, 209, 0);">**Estensione OLED:**</span>

1\. Clicca su “**Estensioni**” per aggiungere estensioni libreria.

![Img](./media/A236.png)

2\. Cerca “**OLED**” e clicca ![Img](./media/A3257.png).

![Img](./media/A306.png)

Clicca sul primo **oled-ssd1306** e aspetta che venga aggiunto.

![Img](./media/A3316.png)

3\. Aggiunta riuscita:

![Img](./media/A335.png)

<span style="color: rgb(0, 209, 0);">**Estensione sensore ultrasonico:**</span>

1\. Clicca su “**Estensioni**” per aggiungere estensioni libreria.

![Img](./media/A236.png)

2\. Cerca “**sonar**” e clicca ![Img](./media/A3257.png) per trovare e caricare “sonar”.

![Img](./media/A506.png)

3\. Aggiunta riuscita:

![Img](./media/A522.png)

<span style="color: rgb(0, 209, 0);">**Estensione sensore DHT11:**</span>

1\. Clicca su “**Estensioni**” per aggiungere estensioni libreria.

![Img](./media/A236.png)

2\. Cerca “**DHT11**” e clicca ![Img](./media/A3257.png) per trovare e caricare “DHT11_DHT22”.

![Img](./media/A616.png)

3\. Aggiunta riuscita:

![Img](./media/A645.png)

**3.4.2 Aggiorna/Elimina estensioni**

1\. Clicca su “**JavaScript**” per passare al codice testuale.

![Img](./media/A724.png)

2\. Clicca su “**Explorer**”.

![Img](./media/A749.png)

3\. Trova la libreria “**OLED**” e clicca ![Img](./media/A813.png) per eliminarla.

![Img](./media/A824.png)

4\. “**Rimuovi**”.

![Img](./media/A727.png)

È stata rimossa.

#### 1.5. Come importare codici in MakeCode

Prendiamo il progetto “**heartbeat**” come esempio per mostrare come caricare il codice.

1\. Apri la versione Web di Makecode o l'app Windows 10 Makecode e clicca su “<span style="color: rgb(255, 76, 65);">Importa</span>”.

![Img](./media/A956.png)

2\. “<span style="color: rgb(255, 76, 65);">Importa file...</span>”

![Img](./media/A042.png)

3\. “<span style="color: rgb(255, 76, 65);">Scegli file</span>” per importare il file che vuoi caricare.

![Img](./media/A06.png)

4\. Qui carichiamo “<span style="color: rgb(255, 76, 65);">heartbeat.hex</span>”.

![Img](./media/A28.png)

5\. “<span style="color: rgb(255, 76, 65);">Procedi √</span>”

![Img](./media/A149.png)

Oltre al metodo sopra, puoi anche trascinare il codice di prova nell'area di modifica del codice, come mostrato di seguito:

![Img](./media/A202.png)

Attendi il caricamento.

![Img](./media/A217.png)
