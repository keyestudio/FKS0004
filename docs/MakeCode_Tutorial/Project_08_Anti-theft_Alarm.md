### Project 08: Diefstalalarm

#### 1. Overzicht

Wanneer het slimme diefstalalarm detecteert dat de diefstalbox is verplaatst, zal de speaker op de micro:bit board alarm slaan en zal de rode LED knipperen.

#### 2. Componenten

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit board *1 | micro:bit T-type uitbreidingsboard *1 | micro USB-kabel *1 |
| ![Img](./media/A937.png)| ![Img](./media/A944.png) | ![Img](./media/A950.png) |
| rode LED *1 | 220Ω weerstand *1 | verbindingsdraad *2 |
| ![Img](./media/A017.png) | ![Img](./media/A024.png) | ![Img](./media/A952.png)  |
| breadboard *1 | batterijhouder *1 <br> (<span style="color: rgb(255, 76, 65);">zelf meegebrachte AA-batterijen *2</span>)| alarmkaart *1 |

#### 3. Componentenkennis

**Versnellingsmeter**

![Img](./media/A026.png)

De micro:bit board beschikt over een ingebouwde LSM303AGR versnellingssensor (we noemen dit een versnellingsmeter) die standaard, snel, plus en hoge-snelheidsmodus (100 kHz, 400 kHz, 1 MHz en 3,4 MHz) van I2C-seriële businterface en SPI-seriële standaardinterface voor externe communicatie bevat, met een resolutie van 8/10/12 bits en een bereik van ±2g, ±4g of ±8g.

Wanneer de micro:bit board in rust is of in eenparige beweging, detecteert de versnellingsmeter alleen de zwaartekrachtversnelling. Als deze licht wordt bewogen, is de gedetecteerde versnelling veel kleiner dan die van de zwaartekracht, dus het verschil kan worden genegeerd. Daarom detecteren we voornamelijk de verandering van de zwaartekrachtversnelling op de x-, y- en z-assen.

#### 4. Aansluitschema

![Img](./media/A219.png)

<span style="color: rgb(255, 76, 65);">**De besturingspin van de LED op het board is P1 (de pin van het T-type uitbreidingsboard is digitaal 1).**</span>

#### 5. Codeflow

![Img](./media/A4434.png)

#### 6. Testcode

Het codebestand is te vinden in map Project 08：Burglar Alarm, bestand Project-08-Burglar-Alarm.hex.

![Img](./media/A4518.png)

**Laad codeblokken:** 

<span style="color: rgb(255, 76, 65);">**Na het importeren van de code, als de buzzer blijft klinken terwijl het breadboard niet wordt verplaatst; kan dit veroorzaakt worden door geografische factoren. Je kunt de drempelwaarden in de voorwaarde -60 en 50 aanpassen aan de werkelijke situatie.**</span>

![Img](./media/A611.png)

#### 7. Testresultaat

Na het downloaden van de code naar het board, beweeg het breadboard. Als de versnellingswaarde x＜-60 of x＞50 is, slaat de speaker op het board alarm en knippert de LED, en toont de micro:bit LED-matrix ![Img](./media/A706.png). Anders maakt de speaker geen geluid en is de LED uit, en toont de micro:bit LED-matrix ![Img](./media/A720.png).

<span style="color: rgb(255, 76, 65);">**LET OP:** Als de bedrading correct is maar je ziet geen resultaat, druk dan op de resetknop aan de achterkant van het board.</span>

![Img](./media/A936.gif)
