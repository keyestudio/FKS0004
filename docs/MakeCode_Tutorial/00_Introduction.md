## 1. Programmeren met MakeCode

De volgende instructies zijn van toepassing op het Windows-systeem, maar kunnen ook als referentie dienen als je een ander systeem gebruikt.

#### 1.1. Snelle start

**Stap 1 Verbinden met micro:bit**

Verbind de board met de computer via een USB-kabel.

![Img](./media/A800.png)

Als de rode LED aan de achterkant van de board brandt, betekent dit dat de board van stroom wordt voorzien. Wanneer je computer via de USB-kabel communiceert met de hoofdboard, knippert de gele LED daarop. Bijvoorbeeld, het knippert wanneer je een “.hex” bestand brandt.

Dan verschijnt de Micro:bit hoofdboard op je computer als een driver genaamd “MICROBIT”. Let op dat het geen gewone USB-schijf is zoals hieronder getoond.

![Img](./media/A849.png)

**Stap 2 Schrijf heartbeat-programma**

Ga naar de link: [online versie van Makecode](https://makecode.microbit.org/)

Klik op “<span style="color: rgb(255, 76, 65);">Nieuw Project</span>” en je ziet “<span style="color: rgb(255, 76, 65);">Project aanmaken</span>”, vul het in met “<span style="color: rgb(255, 76, 65);">heartbeat</span>” en klik op “<span style="color: rgb(255, 76, 65);">Maak √</span>”.

<span style="color: rgb(255, 76, 65);">Hier schrijven we programma's in Google Chrome.</span>

![Img](./media/A021.png)

Laten we een micro:bit-code schrijven.

Je kunt enkele blokken naar het bewerkingsgebied slepen en vervolgens je programma uitvoeren in de simulator zoals hieronder getoond. Hier demonstreren we hoe je het <span style="color: rgb(255, 76, 65);">heartbeat</span>-programma bewerkt.

Bedieningsvideo gids:

![Img](./media/A100.png)

**Stap 3 Download codes**

Over het algemeen, voor de Windows 10 APP ([Windows 10 App krijgen](https://apps.microsoft.com/detail/9pjc7sv48lcx?hl=zh-CN&gl=CN#activetab=pivot:overviewtabdocx))(Klik), volstaat het om op “<span style="color: rgb(255, 76, 65);">Download</span>” te klikken om de code direct naar de micro:bit board te downloaden zonder extra stappen.

Voor browsers, doe het volgende:

Klik op “<span style="color: rgb(255, 76, 65);">Download</span>” in de editor. Dit zal een “hex” bestand downloaden, een formaat dat de micro:bit board kan lezen. Kopieer het daarna naar je micro:bit board zoals je een bestand naar een USB-drive zou kopiëren. Op Windows kun je ook met de rechtermuisknop op het “<span style="color: rgb(255, 76, 65);">.hex</span>” bestand klikken en “**Verzenden naar → MICROBIT**” selecteren om het bestand naar de micro:bit board te kopiëren.

![Img](./media/A319.png)

![Img](./media/A449.png)

Of je kunt het “<span style="color: rgb(255, 76, 65);">.hex</span>” bestand direct naar MICROBIT slepen.

![Img](./media/A341.png)

![Img](./media/A345.png)

Tijdens het kopiëren van het “<span style="color: rgb(255, 76, 65);">.hex</span>” bestand naar de Micro:bit knippert de gele LED aan de achterkant van de board. Wanneer het kopiëren voltooid is, stopt de LED met knipperen en blijft aan.

**Stap 4 Programma uitvoeren**

Nadat het programma is geüpload naar de Micro:bit, kun je het van stroom voorzien via USB-kabel of externe voeding. Dan toont de 5 x 5 LED-puntmatrix een hartslagpatroon.

![Img](./media/A425.png)

<span style="color: rgb(255, 76, 65);">**Let op:**</span> Elke keer dat je programmeert, wordt de driver van Micro:bit automatisch uitgeworpen en teruggezet, waardoor de hex-bestanden verdwijnen. De board heeft alleen toegang tot hex-bestanden, maar slaat ze niet op.

#### 1.2. MakeCode

Ga naar [Makecode Google Chrome online versie](https://makecode.microbit.org/). Dit is de hoofdinterface.

![Img](./media/A637.png)

Er zijn blokken “**on start**” en “**forever**” in het codebewerkingsgebied. <span style="color: rgb(255, 76, 65);">Na het inschakelen wordt code in “on start” slechts één keer uitgevoerd, terwijl code in “forever” cyclisch draait.</span>

Klik op de taal “**JS JavaScript**”:

![Img](./media/A754.png)

Schakel over naar “**Python**” taal:

![Img](./media/A814.png)


#### 1.3. Introductie tot WebUSB-functies

Zoals eerder vermeld, als je computer Windows 10 is en je de MakeCode APP hebt gedownload, kun je snel codes naar de board downloaden via de “<span style="color: rgb(255, 76, 65);">Download</span>” knop. We gebruiken de webUSB van **<span style="color: rgb(255, 76, 65);">Google Chrome</span>** om toegang te krijgen tot het hardwareapparaat dat via USB is verbonden.

**Apparaat koppelen:**

1\. Verbind de board met de computer via USB-kabel.

![Img](./media/A951.png)

2\. Klik op “<span style="color: rgb(255, 76, 65);">Download</span>” -> “<span style="color: rgb(255, 76, 65);">...</span>” en “<span style="color: rgb(255, 76, 65);">Apparaat verbinden</span>”.

![Img](./media/A028.png)

3\. “<span style="color: rgb(255, 76, 65);">Volgende</span>”.

![Img](./media/A046.png)

4\. “<span style="color: rgb(255, 76, 65);">Koppelen</span>”.

![Img](./media/A104.png)

5\. Selecteer vervolgens het overeenkomstige apparaat en “<span style="color: rgb(255, 76, 65);">Verbinden</span>”.

![Img](./media/A127.png)

6\. “<span style="color: rgb(255, 76, 65);">Klaar</span>”.

![Img](./media/A144.png)

**Programma downloaden:**

Na verbinding klik je op “<span style="color: rgb(255, 76, 65);">Download</span>” en zie je dat ![Img](./media/A212.png) verandert in ![Img](./media/A220.png). Het programma wordt naar de micro:bit board gedownload.

![Img](./media/A232.png)

Als er geen apparaat verschijnt om te selecteren, raadpleeg dan [Problemen oplossen bij downloads met WebUSB](https://makecode.microbit.org/device/usb/webusb/troubleshoot). Bekijk [de gebruikershandleiding](https://microbit.org/guide/firmware/) om te weten hoe je de micro:bit firmware bijwerkt.

#### 1.4. MakeCode Extensiebibliotheek

**3.4.1 Bibliotheekextensies importeren**

Open Makecode om een bepaald project te openen, klik op ![Img](./media/A806.png) om “**Extensies**” te kiezen.

![Img](./media/A842.png)

Of klik op “**Extensies**” boven Geavanceerd.

![Img](./media/A900.png)

Zoek de bibliotheek die je wilt.

![Img](./media/A909.png)

We bieden de codebestanden voor elk project aan die alles bevatten wat je nodig hebt om een project uit te voeren, dus je kunt ze direct laden. Als je zelf codeblokken wilt bouwen, vergeet dan niet de volgende drie extensies toe te voegen.

<span style="color: rgb(0, 209, 0);">**OLED-extensie:**</span>

1\. Klik op “**Extensies**” om bibliotheekextensies toe te voegen.

![Img](./media/A236.png)

2\. Zoek “**OLED**” en klik op ![Img](./media/A3257.png).

![Img](./media/A306.png)

Klik op de eerste **oled-ssd1306** en wacht tot deze is toegevoegd.

![Img](./media/A3316.png)

3\. Succesvol toegevoegd:

![Img](./media/A335.png)

<span style="color: rgb(0, 209, 0);">**Ultrasone sensor-extensie:**</span>

1\. Klik op “**Extensies**” om bibliotheekextensies toe te voegen.

![Img](./media/A236.png)

2\. Zoek “**sonar**” en klik op ![Img](./media/A3257.png) om “sonar” te vinden en te laden.

![Img](./media/A506.png)

3\. Succesvol toegevoegd:

![Img](./media/A522.png)

<span style="color: rgb(0, 209, 0);">**DHT11 sensor-extensie:**</span>

1\. Klik op “**Extensies**” om bibliotheekextensies toe te voegen.

![Img](./media/A236.png)

2\. Zoek “**DHT11**” en klik op ![Img](./media/A3257.png) om “DHT11_DHT22” te vinden en te laden.

![Img](./media/A616.png)

3\. Succesvol toegevoegd:

![Img](./media/A645.png)

**3.4.2 Extensies bijwerken/verwijderen**

1\. Klik op “**JavaScript**” om over te schakelen naar tekstcode.

![Img](./media/A724.png)

2\. Klik op “**Verkenner**”.

![Img](./media/A749.png)

3\. Zoek de “**OLED**” bibliotheek en klik op ![Img](./media/A813.png) om deze te verwijderen.

![Img](./media/A824.png)

4\. “**Verwijderen**”.

![Img](./media/A727.png)

Het is verwijderd.

#### 1.5. Hoe codes te importeren in MakeCode

Laten we het project “**heartbeat**” als voorbeeld nemen om te laten zien hoe je de code laadt.

1\. Open de webversie van Makecode of de Windows 10 App Makecode en klik op “<span style="color: rgb(255, 76, 65);">Importeren</span>”.

![Img](./media/A956.png)

2\. “<span style="color: rgb(255, 76, 65);">Bestand importeren...</span>”

![Img](./media/A042.png)

3\. “<span style="color: rgb(255, 76, 65);">Bestand kiezen</span>” om het bestand te importeren dat je wilt laden.

![Img](./media/A06.png)

4\. Hier laden we “<span style="color: rgb(255, 76, 65);">heartbeat.hex</span>”.

![Img](./media/A28.png)

5\. “<span style="color: rgb(255, 76, 65);">Doorgaan √</span>”

![Img](./media/A149.png)

Naast bovenstaande methode kun je ook de testcode in het codebewerkingsgebied slepen, zoals hieronder getoond:

![Img](./media/A202.png)

Wacht tot het laden is voltooid.

![Img](./media/A217.png)
