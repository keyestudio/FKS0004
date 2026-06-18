## 1. Over Mu Software

### 1.1. Installeer MU

Klik om te bezoeken [Mu software officiële website](https://codewith.mu/).

Mu is een Python code-editor voor beginnende programmeurs, zoals leraren en studenten. We kunnen het verkrijgen via de officiële installer voor Windows, Mac OSX of Linux (Mu ondersteunt geen 32-bit Windows meer). De aanbevolen versie is Mu 1.2.0.

**Stap 1 - Zorg dat je OS bekend is en download dan de Mu Installer**

Ontdek eerst welk besturingssysteem je computer heeft (Windows of Mac OSX). Open “**Deze pc**” om “**Eigenschappen**” te zien.

![Img](./media/A225.png)

Controleer het systeemtype: 64-bit of 32-bit.

![Img](./media/A253.png)

[Download MU](https://codewith.mu/en/download). Download de versie die overeenkomt met je besturingssysteem.

![Img](./media/A348.png)

<span style="color: rgb(255, 76, 65);">Hier nemen we het Windows-systeem als voorbeeld, wat als referentie kan dienen voor Mac OSX en Linux.</span>

![Img](./media/A422.png)

**Stap 2 - Voer de installer uit**

Dubbelklik op de installer (waarschijnlijk in je Downloads-map) om deze uit te voeren.

![Img](./media/A440.png)

We hebben de extra stappen geschetst die nodig zijn om Windows te helpen Mu te installeren voor Windows 10. Andere versies zullen vergelijkbaar zijn.

[Mu installer voor MacOS](https://codewith.mu/en/howto/1.1/install_macos).

[Mu installer voor Linux systeem](https://codewith.mu/en/howto/1.2/install_linux).

Voor Windows 10 zal Defender een waarschuwing tonen. Klik op de link “**Meer info**”.

![Img](./media/A615.png)

Het bericht verandert en geeft meer informatie over de installer en toont een knop “**Toch uitvoeren**”. Klik op “**Toch uitvoeren**”.

![Img](./media/A626.png)

**Stap 3 - Licentieovereenkomst**

Bekijk de licentie, vink het vakje aan en klik op “**Installeren**”.

![Img](./media/A1716.png)

**Stap 4 - Installeren**

Ga een kop koffie halen terwijl Mu op je computer wordt geïnstalleerd.

![Img](./media/A1740.png)

**Stap 5 - Voltooid**

De installatie is succesvol afgerond, klik op “**Voltooien**” om de installer te sluiten.

![Img](./media/A817.png)

**Stap 6 - Start Mu**

Je kunt Mu starten door op het icoon in het Startmenu te klikken of door “Mu” in het zoekvak te typen (beide hieronder gemarkeerd). Bij de eerste keer starten kan het even duren.

![Img](./media/A852.png)

Zo ziet het eruit:

![Img](./media/A909.png)

### 1.2. Gebruik van Modi & Menubalk

Stel “<span style="color: rgb(255, 76, 65);">Modus</span>” in op BBC micro:bit.

Klik in het menu op “**Modus**” en stel het in op “**BBC micro：bit**”. De micro:bit modus begrijpt hoe te communiceren en verbinden met een micro:bit.

![Img](./media/A022.png)

Klik om te [Beginnen met Mu](https://codewith.mu/en/tutorials/1.1/start).

Voor meer tutorials over het gebruik van Mu, bezoek: https://codewith.mu/en/tutorials/

### 1.3. Programmeren in Mu

Hier laden we “<span style="color: rgb(255, 76, 65);">heartbeat\.py</span>” in Mu. Je vindt het in de map “<span style="color: rgb(255, 76, 65);">Hartslag</span>” die we hebben meegeleverd.

![Img](./media/A200.png)

**Methode één:**

Open Mu en klik op “<span style="color: rgb(255, 76, 65);">Laden</span>” om het pad te kiezen waar je de code hebt gedownload.

![Img](./media/A341.png)

![Img](./media/A345.png)

Succesvol geladen, zoals hieronder weergegeven:

![Img](./media/A354.png)

**Methode twee:**

Klik op “nieuw” ![Img](./media/A503.png) om een nieuw programma te maken en sleep “heartbeat\.py” erin:

![Img](./media/A521.png)

Succesvol geladen, zoals hieronder weergegeven:

![Img](./media/A533.png)

<span style="color: rgb(255, 76, 65);">Dit geldt ook voor het toevoegen van andere codes.</span>

### 1.4. Code downloaden naar Micro:bit

Verbind de board met de computer via USB-kabel.

![Img](./media/A252.png)

Klik op “<span style="color: rgb(255, 76, 65);">**Flash**</span>” om de code naar de micro:bit board te downloaden.

![Img](./media/A3728.png)

Daarna, <span style="color: rgb(255, 76, 65);">**zet aan via de micro USB-kabel of externe voeding (zet DIP-schakelaar op AAN)**</span>. Je zult zien dat de on-board 5×5 LED-matrix herhaaldelijk ![Img](./media/A903.png) en daarna ![Img](./media/A910.png) toont.

<span style="color: rgb(255, 76, 65);">**Let op dat als er een fout in je code zit, deze toch kan worden gedownload maar niet correct zal werken.**</span>

<span style="color: rgb(0, 209, 0);">Bijvoorbeeld, de functie sleep() is geschreven als sleeps() in de code. Klik op “**Flash**” om code naar micro:bit te laden. De 5×5 LED-matrix toont dan rommelige iconen.</span>

![Img](./media/A4003.png)

In dit geval, klik op “**REPL**” en druk op de resetknop aan de achterkant van de board. Het foutbericht wordt weergegeven in de REPL-interface, zoals hieronder:

![Img](./media/A029.png)

![Img](./media/A033.png)

Klik opnieuw op “**REPL**” om REPL te sluiten. Klik daarna op “<span style="color: rgb(255, 76, 65);">**Flash**</span>”.

Om zeker te zijn dat de code correct is, klik op “<span style="color: rgb(255, 76, 65);">**Controleren**</span>” na het afronden, en Mu zal fouten in de code aangeven.

![Img](./media/A119.png)

Pas de code aan volgens het foutbericht en klik opnieuw op “<span style="color: rgb(255, 76, 65);">**Controleren**</span>”. Mu toont geen fouten meer.

![Img](./media/A134.png)

Zie [meer tutorials die specifieke aspecten van Mu uitleggen](https://codewith.mu/en/tutorials/).

## 2. Hoe Mu Bibliotheken importeert naar Micro:bit

<span style="color: rgb(255, 76, 65);">Voordat we bibliotheken importeren, moeten we een .py code uploaden (lege code is ook oké) naar de micro:bit board. Hier nemen we een lege code als voorbeeld.</span>

Verbind de board met de computer via USB-kabel. Open Mu en klik op “Flash” om de .py code (lege code) naar de board te uploaden.

![Img](./media/A252.png)

In deze tutorial worden OLED en DHT11 modules gebruikt. Daarom moeten de “<span style="color: rgb(255, 76, 65);">**oled_ssd1306\.py**</span>” en “<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>” bibliotheekbestanden geïmporteerd worden naar de micro:bit board.

De standaardmap waar Mu bestanden opslaat is “mu_code” in de hoofdmap van de gebruikersdirectory.

Referentielink: [https://codewith.mu/en/tutorials/1.0/files](https://codewith.mu/en/tutorials/1.0/files)

**Instructies voor het importeren van bibliotheken:**

1\. Zoek de “<span style="color: rgb(255, 76, 65);">mu_code</span>” map op Disk(C:).

![Img](./media/A543.png)

![Img](./media/A550.png)

2\. Open “<span style="color: rgb(255, 76, 65);">mu_code</span>”.

![Img](./media/A628.png)

3\. Kopieer en plak de bibliotheekbestanden “<span style="color: rgb(255, 76, 65);">**oled_ssd1306\.py**</span>” en “<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>” naar “<span style="color: rgb(255, 76, 65);">**Libraries**</span>”.

![Img](./media/A4716.png)

4\. Zoals hieronder weergegeven:

![Img](./media/A735.png)

5\. Open Mu en klik op “<span style="color: rgb(255, 76, 65);">**Bestanden**</span>”. Hier slepen we de “<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>” bibliotheek naar micro:bit.

![Img](./media/A816.png)

![Img](./media/A820.png)

6\. Na het importeren van “<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>”, zie je het in het vak aan de linkerkant.

![Img](./media/A841.png)

7\. Laten we hetzelfde doen met “<span style="color: rgb(255, 76, 65);">**oled_ssd1306\.py**</span>”.

![Img](./media/A916.png)

![Img](./media/A4920.png)

<span style="color: rgb(255, 76, 65);">**Let op dat wanneer je andere bestanden uploadt naar de micro:bit, deze de originele inhoud overschrijven, dus moet je ze opnieuw importeren voor de volgende keer dat je ze gebruikt.**</span>
