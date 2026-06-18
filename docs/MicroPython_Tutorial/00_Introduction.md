## 1. Informazioni sul Software Mu

### 1.1. Installare MU

Clicca per visitare il [sito ufficiale del software Mu](https://codewith.mu/).

Mu è un editor di codice Python per programmatori principianti, come insegnanti e studenti. Possiamo ottenerlo tramite l'installer ufficiale per Windows, Mac OSX o Linux (Mu non supporta più Windows a 32 bit). La versione consigliata è Mu 1.2.0.

**Passo 1 - Assicurati del tuo sistema operativo e poi scarica l'installer di Mu**

Prima scopri il sistema operativo del tuo computer (Windows o Mac OSX). Apri “**Questo PC**” per vedere le “**Proprietà**”.

![Img](./media/A225.png)

Controlla il tipo di sistema: 64-bit o 32-bit.

![Img](./media/A253.png)

[Scarica MU](https://codewith.mu/en/download). Scarica la versione in base al sistema operativo del tuo computer.

![Img](./media/A348.png)

<span style="color: rgb(255, 76, 65);">Qui prendiamo come esempio il sistema Windows, che può essere un riferimento per Mac OSX e Linux.</span>

![Img](./media/A422.png)

**Passo 2 - Esegui l'installer**

Fai doppio clic sull'installer (probabilmente nella cartella Download) per eseguirlo.

![Img](./media/A440.png)

Abbiamo evidenziato i passaggi extra necessari per aiutare Windows a installare Mu su Windows 10. Le altre versioni saranno simili.

[Installer Mu per MacOS](https://codewith.mu/en/howto/1.1/install_macos).

[Installer Mu per sistema Linux](https://codewith.mu/en/howto/1.2/install_linux).

Per Windows 10, Defender mostrerà un messaggio di avviso. Dovresti cliccare sul link “**Ulteriori informazioni**”.

![Img](./media/A615.png)

Il messaggio cambierà fornendo più informazioni sull'installer e mostrerà un pulsante “**Esegui comunque**”. Clicca “**Esegui comunque**”.

![Img](./media/A626.png)

**Passo 3 - Accordo di Licenza**

Rivedi la licenza, seleziona la casella e clicca “**Installa**”.

![Img](./media/A1716.png)

**Passo 4 - Installazione**

Prenditi un caffè mentre Mu si installa sul tuo computer.

![Img](./media/A1740.png)

**Passo 5 - Completamento**

L'installazione è stata completata con successo, clicca “**Fine**” per chiudere l'installer.

![Img](./media/A817.png)

**Passo 6 - Avvia Mu**

Puoi avviare Mu cliccando sull'icona nel menu Start o digitando “Mu” nella casella di ricerca (entrambi evidenziati sotto). Al primo avvio, potrebbe richiedere un po' di tempo.

![Img](./media/A852.png)

Ecco come appare:

![Img](./media/A909.png)

### 1.2. Uso delle Modalità e della Barra del Menu

Imposta “<span style="color: rgb(255, 76, 65);">Modalità</span>” su BBC micro:bit.

Nel menu, clicca “**Modalità**” per impostarla su “**BBC micro：bit**”. La modalità micro:bit capisce come interagire e connettersi a un micro:bit.

![Img](./media/A022.png)

Clicca per [Iniziare con Mu](https://codewith.mu/en/tutorials/1.1/start).

Per ulteriori tutorial sull'uso di Mu, visita: https://codewith.mu/en/tutorials/

### 1.3. Programmare su Mu

Qui carichiamo il file “<span style="color: rgb(255, 76, 65);">heartbeat\.py</span>” su Mu. Lo trovi nella cartella “<span style="color: rgb(255, 76, 65);">Heart beat</span>” che abbiamo fornito.

![Img](./media/A200.png)

**Metodo uno:**

Apri Mu e clicca “<span style="color: rgb(255, 76, 65);">Carica</span>” per scegliere il percorso dove hai scaricato il codice.

![Img](./media/A341.png)

![Img](./media/A345.png)

Caricato con successo, come mostrato sotto:

![Img](./media/A354.png)

**Metodo due:**

Clicca “nuovo” ![Img](./media/A503.png) per creare un nuovo programma e trascina “heartbeat\.py” dentro:

![Img](./media/A521.png)

Caricato con successo, come mostrato sotto:

![Img](./media/A533.png)

<span style="color: rgb(255, 76, 65);">Lo stesso vale per aggiungere altri codici.</span>

### 1.4. Scaricare il Codice su Micro:bit

Collega la scheda al computer tramite cavo USB.

![Img](./media/A252.png)

Clicca “<span style="color: rgb(255, 76, 65);">**Flash**</span>” per scaricare il codice sulla scheda micro:bit.

![Img](./media/A3728.png)

Dopo, <span style="color: rgb(255, 76, 65);">**accendi tramite il cavo micro USB o alimentazione esterna (imposta l'interruttore DIP su ON)**</span>. Vedrai la matrice LED 5×5 a bordo mostrare ripetutamente ![Img](./media/A903.png) e poi ![Img](./media/A910.png).

<span style="color: rgb(255, 76, 65);">**Nota che se c'è un errore nel tuo codice, potrebbe comunque essere scaricato ma non funzionerà correttamente.**</span>

<span style="color: rgb(0, 209, 0);">Ad esempio, la funzione sleep() è scritta come sleeps() nel codice. Clicca “**Flash**” per caricare il codice sul micro:bit. Tuttavia, la matrice LED 5×5 mostra icone confuse.</span>

![Img](./media/A4003.png)

In questo caso, clicca “**REPL**” e premi il pulsante reset sulla scheda sul retro. Il messaggio di errore sarà mostrato nell'interfaccia REPL, come mostrato sotto:

![Img](./media/A029.png)

![Img](./media/A033.png)

Clicca di nuovo “**REPL**” per chiudere REPL. Poi clicca “<span style="color: rgb(255, 76, 65);">**Flash**</span>”.

Per assicurarti che il codice sia corretto, clicca “<span style="color: rgb(255, 76, 65);">**Controlla**</span>” dopo aver finito, e Mu indicherà l'errore nel codice.

![Img](./media/A119.png)

Modifica il codice secondo il messaggio di errore, e clicca di nuovo “<span style="color: rgb(255, 76, 65);">**Controlla**</span>”. Mu non mostrerà errori.

![Img](./media/A134.png)

Vedi [più tutorial che spiegano aspetti specifici di Mu](https://codewith.mu/en/tutorials/).

## 2. Come Mu Importa le Librerie su Micro:bit

<span style="color: rgb(255, 76, 65);">Prima di importare le librerie, dobbiamo caricare un codice .py (anche vuoto va bene) sulla scheda micro:bit. Qui prendiamo come esempio un codice vuoto.</span>

Collega la scheda al computer tramite cavo USB. Apri Mu e clicca “Flash” per caricare il codice .py (vuoto) sulla scheda.

![Img](./media/A252.png)

In questo tutorial, vengono usati i moduli OLED e DHT11. Pertanto, i file di libreria “<span style="color: rgb(255, 76, 65);">**oled_ssd1306\.py**</span>” e “<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>” devono essere importati nella scheda micro:bit.

La directory predefinita dove Mu salva i file è “mu_code” nella directory principale dell'utente.

Link di riferimento: [https://codewith.mu/en/tutorials/1.0/files](https://codewith.mu/en/tutorials/1.0/files)

**Istruzioni per importare le librerie:**

1\. Cerca la cartella “<span style="color: rgb(255, 76, 65);">mu_code</span>” nel Disco (C:).

![Img](./media/A543.png)

![Img](./media/A550.png)

2\. Apri “<span style="color: rgb(255, 76, 65);">mu_code</span>”.

![Img](./media/A628.png)

3\. Copia e incolla i file di libreria “<span style="color: rgb(255, 76, 65);">**oled_ssd1306\.py**</span>” e “<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>” in “<span style="color: rgb(255, 76, 65);">**Libraries**</span>”.

![Img](./media/A4716.png)

4\. Come mostrato sotto:

![Img](./media/A735.png)

5\. Apri Mu e clicca “<span style="color: rgb(255, 76, 65);">**Files**</span>”. Qui trascini la libreria “<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>” nel micro:bit.

![Img](./media/A816.png)

![Img](./media/A820.png)

6\. Dopo aver importato “<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>”, la vedrai nella casella a sinistra.

![Img](./media/A841.png)

7\. Facciamo lo stesso con “<span style="color: rgb(255, 76, 65);">**oled_ssd1306\.py**</span>”.

![Img](./media/A916.png)

![Img](./media/A4920.png)

<span style="color: rgb(255, 76, 65);">**Nota che quando carichi altri file sul micro:bit, sovrascriveranno il contenuto originale quindi devi reimportarli la prossima volta che li usi.**</span>
