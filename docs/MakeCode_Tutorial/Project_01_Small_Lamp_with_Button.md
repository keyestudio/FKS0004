### Project 01: Kleine Lamp met Knop

#### 1. Overzicht

Er zijn twee programmeerbare knoppen aan de voorkant van de micro:bit board (A en B). We combineren ze met een rode LED en een lampkaart om een kleine bureaulamp te bouwen. Wanneer knop A wordt ingedrukt, gaat de rode LED aan; wanneer knop B wordt ingedrukt, gaat deze uit.

#### 2. Componenten

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit board *1 | micro:bit T-type uitbreidingsbord *1 | micro USB-kabel *1 |
| ![Img](./media/A937.png)| ![Img](./media/A944.png) | ![Img](./media/A950.png) |
| rode LED *1 | 220Ω weerstand *1 | jumper draad *2 |
| ![Img](./media/A017.png) | ![Img](./media/A024.png) | ![Img](./media/A920.png)  |
| breadboard *1 | batterijhouder *1 <br> (<span style="color: rgb(255, 76, 65);">zelf meegebrachte AA batterijen *2</span>) | lampkaart *1 |

#### 3. Componenten Kennis

**Knoppen**

Knoppen kunnen de schakeling aan en uit zetten. Wanneer een knop is aangesloten op een schakeling, is de schakeling open wanneer de knop niet wordt ingedrukt; de schakeling wordt gesloten nadat de knop is ingedrukt.

Er zijn drie knoppen op de micro:bit board: een resetknop aan de achterkant en twee programmeerbare knoppen (A en B) aan de voorkant.

![Img](./media/A230.png)

**Weerstanden**

![Img](./media/A248.png)

Een weerstand is een elektronisch component dat de stroom in een tak van een schakeling beperkt. De weerstand van een vaste weerstand kan niet worden aangepast, terwijl die van een potentiometer of variabele weerstand dat wel kan.

Hier zijn twee veelvoorkomende schakelsymbolen voor weerstanden. Als je deze symbolen in een schakeling ziet, vertegenwoordigen ze een weerstand.

![Img](./media/A303.png)

Ω is de eenheid van weerstand, inclusief Ω, KΩ, MΩ, enz. Ze kunnen worden uitgedrukt als: 1 MΩ=1000 KΩ, 1 KΩ =1000 Ω. Over het algemeen zijn sommige weerstanden gemarkeerd op het oppervlak.

Bij het gebruik van een weerstand moeten we eerst de weerstand weten. Er zijn twee manieren: observeer de kleurband erop, of meet de weerstand met een multimeter. Uiteraard is de eerste manier handiger en sneller.

![Img](./media/A317.png)

Zoals te zien op de weerstandkaart, vertegenwoordigt elke kleur een nummer.

![Img](./media/A3335.png)

4-bands en 5-bands weerstanden worden vaak gebruikt.

Vaak, wanneer je een weerstand krijgt, kan het moeilijk zijn te bepalen waar je moet beginnen met het lezen van de kleur.

**Daarom kun je de ruimte tussen de twee banden aan één uiteinde observeren; als deze breder is dan andere bandruimtes, lees dan vanaf het tegenovergestelde uiteinde.**

<span style="color: rgb(255, 76, 65);">**Let op dat de ruimte tussen de 4e en 5e banden (de 3e en 4e) relatief breed is bij een 5-bands (4-bands) weerstand.**</span>

Laten we zien hoe we de weerstand van een 5-bands weerstand lezen, zoals hieronder weergegeven:

![Img](./media/A426.png)

Voor deze weerstand moet de weerstand van links naar rechts worden gelezen. De waarde moet zijn: 1e band 2e band 3e band x 10^vermenigvuldiger(Ω), ±tolerantie%.

Daarom is de weerstand van deze weerstand 2(rood) 2(rood) 0(zwart) × 10^0 (zwart)Ω = 220Ω, ±1%(bruin). Leer meer over [weerstand van Wiki](https://en.wikipedia.org/wiki/Resistor).

**LED**

LED, volledig genoemd "light-emitting diode", is een elektronisch apparaat gemaakt van halfgeleidermaterialen (silicium, selenium, germanium, enz.). Het is polair, met een positieve pool - de lange pin verbonden met VCC (V of 3.3V of 5V of +), en een negatieve pool - de korte pin verbonden met GND (G of -). De stroom vloeit van positief naar negatief, in éénrichtingsstroom.

Elektronisch en grafisch symbool van LED:

![Img](./media/A515.png)

LED in verschillende maten en kleuren:

![Img](./media/A525.png)

Rood, geel, blauw, groen en wit zijn de meest voorkomende kleuren van LED, wat overeenkomt met hun uiterlijk. We gebruiken zelden transparante LED's, en het uitgestraalde licht is mogelijk niet wit. Er zijn vier maten LED: 3mm, 5mm (meest voorkomend), 8mm en 10mm.

![Img](./media/A535.png)

Voorwaartse spanning moet worden gebruikt wanneer de LED aan is. Het is een zeer belangrijke parameter om te weten bij het gebruik van een LED, omdat het bepaalt hoeveel vermogen je gebruikt en hoe groot de stroombegrenzende weerstand moet zijn. Voor de meeste rode, gele, oranje en lichtgroene LED's gebruiken ze typisch een spanning tussen 1,9V en 2,1V.

![Img](./media/A548.png)

Volgens de wet van Ohm neemt de stroom door de schakeling af naarmate de weerstand toeneemt, waardoor de LED dimt.

I = (VP-Vl)/R

Om de LED veilig te maken en de juiste helderheid te hebben, hoeveel weerstand moeten we dan in de schakeling gebruiken?

Voor 99% van de 5mm LED's is de aanbevolen stroom 20mA, wat te zien is in de condities-kolom in het datasheet:

![Img](./media/A613.png)

Nu zetten we de bovenstaande formule om in het volgende:

R = (VP-Vl)/I

Als VP = 5V, Vl (voorwaartse spanning) = 2V, en I = 20mA, kunnen we zeggen dat R 150Ω is. Daarom kunnen we de LED helderder maken door de weerstand te verlagen, maar de weerstand mag niet onder 150Ω komen (deze waarde kan onnauwkeurig zijn omdat de geleverde LED kan variëren).

De voorwaartse spanning en golflengte van verschillende kleuren LED zijn hieronder weergegeven ter referentie:

![Img](./media/A629.png)

<span style="color: rgb(255, 76, 65);">**Sluit geen weerstand met zeer lage weerstand direct aan op de twee polen van de voeding, anders kunnen elektronische componenten beschadigd raken door overmatige stroom. Weerstanden zijn niet-polair.**</span>

**Breadboard**

Voordat je een schakeling voltooit, wordt een breadboard gebruikt om snel schakelingen te ontwerpen en te testen. Er zijn veel gaatjes op een breadboard waarin schakelingcomponenten (zoals weerstanden) kunnen worden gestoken. Een typisch breadboard wordt hieronder getoond:

![Img](./media/A655.png)

Een breadboard heeft veel metalen strips eronder die verbinding maken met de gaatjes aan de bovenkant. Ze zijn gerangschikt zoals hieronder weergegeven.

<span style="color: rgb(255, 76, 65);">Let op dat de bovenste en onderste gaatjes horizontaal verbonden zijn, terwijl de rest van de gaatjes verticaal verbonden zijn.</span>

![Img](./media/A723.png)

De eerste twee rijen (boven) en de laatste twee (onder) van het breadboard worden respectievelijk gebruikt voor de positieve (+) en negatieve (-) polen van de voeding. Het geleidende layoutdiagram wordt hieronder getoond:

![Img](./media/A730.png)

Bij het aansluiten van DIP (Dual In-line Packages) componenten, zoals geïntegreerde schakelingen, microcontrollers, chips, enz., is de groefoleiding tussen de twee delen. Daarom kunnen DIP-componenten als hieronder worden aangesloten:

![Img](./media/A740.png)

![Img](./media/A747.png)

**Jumper draad en DuPont draad**

Jumper draden en DuPont draden verbinden twee aansluitingen. Er zijn verschillende types, maar hier richten we ons op die gebruikt worden in breadboards. Ze zenden elektrische signalen van overal op het breadboard naar de input/output pinnen van een microcontroller.

Bij gebruik steek je "twee pinnen" van de draden in het breadboard zonder te solderen. Er zijn meerdere sets parallelle strips onder het oppervlak van het breadboard, dus draden hoeven alleen in specifieke gaatjes in een bepaald prototype te worden gestoken.

Er zijn drie types DuPont draden: F-F, M-M en M-F. Op de draad wordt de pin mannelijke kant (M) genoemd, terwijl het gaatje vrouwelijk (F) is.

![Img](./media/A811.png)

Meer dan één type kan in een project worden gebruikt. Hoewel de kleuren van de draden verschillen, dienen ze hetzelfde doel. Kleuren worden gebruikt om schakelingen te onderscheiden.

#### 4. Aansluitschema

<span style="color: rgb(255, 76, 65);">Let op: de micro:bit board moet in het T-type uitbreidingsbord worden gestoken zoals hieronder weergegeven. De micro:bit board LED-matrix moet aan dezelfde zijde zijn als het logo van het uitbreidingsbord.</span>

![Img](./media/A156.png)

<span style="color: rgb(255, 76, 65);">De board besturingspin van de LED is P0 (de pin van het T-type uitbreidingsbord is digitaal 0).</span>

#### 5. Code Flow

![Img](./media/A4323.png)

#### 6. Test Code

Het codebestand is beschikbaar in de map Project 01：Kleine Lamp met Knop, bestand Project-01-Small-Lamp-with-Button.hex.

![Img](./media/A357.png)

**Laad codeblokken:**

![Img](./media/A440.png)

#### 7. Testresultaat

Voor Windows 10 App, klik op “<span style="color: rgb(255, 76, 65);">Download</span>”. Voor browsers, stuur het gedownloade “<span style="color: rgb(255, 76, 65);">.hex</span>” bestand naar de micro:bit board.

Na het downloaden van de code naar de board, toont de 5x5 LED-matrix het ![Img](./media/A512.png) icoon. Druk op knop A, en de 5x5 LED-matrix toont het ![Img](./media/A518.png) icoon, LED gaat aan. Druk op knop B, en de 5x5 LED-matrix toont het ![Img](./media/A527.png) icoon, LED gaat uit. Lijkt het op een mini lamp?

<span style="color: rgb(255, 76, 65);">**LET OP:** Als de bedrading correct is maar je ziet geen resultaat, druk dan op de resetknop aan de achterkant van de board.</span>

![Img](./media/A359.gif)

<span style="color: rgb(255, 76, 65);">**Bij voeding via externe voeding, zet de DIP-schakelaar op AAN.**</span>

![Img](./media/A904.png)
