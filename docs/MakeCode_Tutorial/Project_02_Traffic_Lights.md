### Project 02: Verkeerslichten

#### 1. Overzicht

In dit project gebruiken we drie LEDs (rood, geel en groen), een speaker op de micro:bit board en een 5x5 LED-matrix om een model van verkeerslichten te maken.

#### 2. Componenten

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit board *1 | micro:bit T-type uitbreidingsbord *1 | micro USB-kabel *1 |
| ![Img](./media/A937.png)| ![Img](./media/A5652.png) | ![Img](./media/A658.png) |
| rode LED *1 | gele LED *1 | groene LED *1 |
| ![Img](./media/A944.png) | ![Img](./media/A950.png) |![Img](./media/A017.png) |
| 220Ω weerstand *3 | verbindingsdraden | breadboard *1 |
|  ![Img](./media/A024.png) |  ![Img](./media/A020.png) |  |
| batterijhouder *1 <br> (<span style="color: rgb(255, 76, 65);">zelf meegebrachte AA-batterijen *2</span>) | verkeerslichtenkaart *1 | |

#### 3. Componentenkennis

**Speaker**

![Img](./media/A833.png)

De micro:bit wordt geleverd met een speaker, waardoor het eenvoudig is om geluid te maken in je project.

#### 4. Aansluitschema

![Img](./media/A908.png)

<span style="color: rgb(255, 76, 65);">**Let op:** het micro:bit board moet in het T-type uitbreidingsbord worden gestoken zoals hieronder getoond. De LED-matrix van het micro:bit board moet aan dezelfde kant zitten als het logo van het uitbreidingsbord.</span>

![Img](./media/A940.png)

#### 5. Codeflow

![Img](./media/A5956.png)

#### 6. Testcode

Het codebestand is te vinden in de map Project 02：Traffic Lights, bestand Project-02-Traffic-Lights.hex.

![Img](./media/A0017.png)

**Laad codeblokken:**

![Img](./media/A605.png)

#### 7. Testresultaat

Voor de Windows 10-app, klik op “<span style="color: rgb(255, 76, 65);">Download</span>”. Voor browsers, stuur het gedownloade “<span style="color: rgb(255, 76, 65);">.hex</span>” bestand naar het micro:bit board.

Na het downloaden van de code naar het board, gaat de groene LED aan en telt de 5×5 LED-matrix 6 seconden af. Nadat de groene LED uitgaat, knippert de gele LED en telt de matrix 3 seconden af met geluid van de speaker. Tot slot gaat de rode LED aan met een aftelling van 6 seconden. Deze handelingen herhalen zich.

<span style="color: rgb(255, 76, 65);">**LET OP:** Als de bedrading correct is maar je ziet geen resultaat, druk dan op de resetknop aan de achterkant van het board.</span>

![Img](./media/A459.gif)

<span style="color: rgb(255, 76, 65);">**Bij voeding via externe stroomvoorziening, zet de DIP-schakelaar op ON.**</span>

![Img](./media/A904.png)
