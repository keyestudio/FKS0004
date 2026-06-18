### Project 03: Ranging Bat

#### 1. Overzicht

Op basis van een ultrasone sensor detecteert de ranging bat de afstand van obstakels en toont deze in realtime op een OLED. Wanneer de afstand minder dan 10 cm is, geeft de speaker een alarm.

#### 2. Componenten

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit board *1 | micro:bit T-type uitbreidingsbord *1 | micro USB-kabel *1 |
| ![Img](./media/A356.png)| ![Img](./media/A406.png)| ![Img](./media/A415.png) |
| ultrasone sensor *1 | OLED-module *1 | DuPont draden |
|![Img](./media/A017.png) | ![Img](./media/A950.png) | ![Img](./media/A024.png) |
| breadboard *1 | jump wires | batterijhouder *1 <br> (<span style="color: rgb(255, 76, 65);">zelf meegebrachte AA-batterijen *2</span>)|
|![Img](./media/A315.png)|![Img](./media/A557.png) | |
| bat kaart *1| OLED kaart *1 | |

#### 3. Componenten Kennis

**ultrasone sensor**

Ultrasone golven kaatsen terug wanneer ze een obstakel raken. We meten de afstand door het tijdsinterval te berekenen tussen het verzenden en ontvangen van de golven. Aangezien de voortplantingssnelheid van geluid in lucht constant is v=340m/s, berekenen we de afstand tussen de sensor en het obstakel: s=vt/2.

![Img](./media/A846.png)

De HC-SR04 ultrasone module integreert een zender en ontvanger. De eerste zet elektrische signalen (elektrische energie) om in hoogfrequente (buiten het gehoor van mensen) geluidsgolven (mechanische energie), terwijl de tweede het omgekeerde doet.

Het schema van de HC SR04:

![Img](./media/A642.png)

**Pin-definitie:**

![Img](./media/A702.png)

**Parameters:**

- Bedrijfsspanning: 5V
- Bedrijfsstroom: 12mA
- Minimale meetafstand: 2cm
- Maximale meetafstand: 200cm

**Werkingsprincipe:**

Een hoog niveau puls van minstens 10us wordt uitgegeven op de Trig pin, en de module begint ultrasone golven uit te zenden. Tegelijkertijd wordt de Echo pin hoog getrokken. Wanneer de module een ultrasone golf terug ontvangt bij een obstakel, wordt de Echo pin laag getrokken. De duur van het hoge niveau van de Echo pin is de totale tijd van golf van verzenden tot ontvangen: s=vt/2.

![Img](./media/A728.png)

**OLED module**

OLED-technologie kenmerkt zich door rijke kleurweergave, hoog contrast en brede kijkhoek, wat zorgt voor heldere en levendige beelden, vooral uitstekend in zwart.

Elke pixel van het OLED-scherm straalt zelf licht uit zonder achtergrondverlichting, waardoor het relatief weinig stroom verbruikt. Met een kleine afmeting, hoge resolutie en laag stroomverbruik is het 0,9-inch OLED-scherm zeer geschikt voor draagbare apparaten.

![Img](./media/A636.png)

<span style="color: rgb(255, 76, 65);">**In dit project is de OLED display module aangesloten met de SDA-interface op pin P20 en SCL op pin P19.**</span>

**Parameters:**

- Bedrijfsspanning: DC 3.3V-5V

- Bedrijfsstroom: 30mA

- Interface: Pin-poorten met een afstand van 2,54mm

- Communicatiemodus: I2C

- Interne driverchip: SSD1306

- Resolutie: 128*64

- Kijkhoek: groter dan 150°

#### 4. Aansluitschema

![Img](./media/A1849.png)

<span style="color: rgb(255, 76, 65);">**Bij gebruik van het OLED-display en ultrasone sensor moeten we een externe voeding aansluiten en de DIP-schakelaar op ON zetten.**</span>

![Img](./media/A902.png)

![Img](./media/A1906.png)

#### 5. Code Flow

![Img](./media/A924.png)

#### 6. Testcode

Het codebestand is te vinden in map Project 03：Ranging Bat, bestand Project-03-Ranging-Bat.hex.

![Img](./media/A955.png)

**Laad codeblokken:** <span style="color: rgb(255, 76, 65);">De drempelwaarde in de voorwaarde 10 kan worden aangepast aan de werkelijke situatie.</span>

![Img](./media/A022.png)

#### 7. Testresultaat

Voor Windows 10 App, klik op “<span style="color: rgb(255, 76, 65);">Download</span>”. Voor browsers, stuur het gedownloade “<span style="color: rgb(255, 76, 65);">.hex</span>” bestand naar het micro:bit board.

Na het downloaden van de code naar het board, <span style="color: rgb(255, 76, 65);">zet de voeding aan via externe voeding en zet de DIP-schakelaar op ON</span>, en de OLED toont de afstand tussen de ultrasone sensor en het obstakel in realtime. Wanneer de afstand minder is dan 10 cm, geeft de speaker op het micro:bit board alarm.

<span style="color: rgb(255, 76, 65);"><span style="color: rgb(255, 76, 65);">**LET OP:** Als de bedrading correct is maar je ziet geen resultaat, druk dan op de resetknop aan de achterkant van het board.</span></span>

![Img](./media/A605.gif)
