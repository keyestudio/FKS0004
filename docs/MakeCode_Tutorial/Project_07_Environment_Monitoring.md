### Project 07: Omgevingsbewaking

#### 1. Overzicht

Op de OLED toont het slimme omgevingsbewakingssysteem de temperatuur- en vochtigheidswaarden die door de DHT11-sensor in realtime worden gedetecteerd, evenals de helderheidswaarde van het omgevingslicht die wordt gedetecteerd door de ingebouwde lichtsensor.

#### 2. Componenten

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit board *1 | micro:bit T-type uitbreidingsbord *1 | micro USB-kabel *1 |
| ![Img](./media/A2637.png)| ![Img](./media/A406.png)| ![Img](./media/A415.png) |
| XHT11 temperatuur- en vochtigheidssensor *1 | OLED-module *1 | DuPont-draad |
|![Img](./media/A017.png) | ![Img](./media/A950.png) | ![Img](./media/A024.png) |
| breadboard *1 | jump wires | batterijhouder *1 <br> (<span style="color: rgb(255, 76, 65);">zelf meegebrachte AA-batterijen *2</span>)|
|![Img](./media/A0715.png) |![Img](./media/A557.png)  | |
| cloud card *1| OLED card *1 | |

#### 3. Componentkennis

**XHT11 temperatuur- en vochtigheidssensor**

![Img](./media/A2637.png)

De XHT11 temperatuur- en vochtigheidssensor is een samengestelde sensor met gekalibreerde digitale signaaluitgang, die de luchtvochtigheid en temperatuur kan detecteren.

**Nauwkeurigheid**: vochtigheid ±5%RH, temperatuur ±2℃

**Detectiebereik**: vochtigheid 5%RH ~ 95%RH, temperatuur -25℃ ~ +60℃

De sensor gebruikt speciale digitale module-acquisitie en temperatuur- en vochtigheidssensingtechnologie om een uiterst hoge betrouwbaarheid en uitstekende langetermijnstabiliteit te garanderen. Hij bevat een resistief vochtigheidssensorelement en een NTC-temperatuursensorelement, wat zeer geschikt is voor metingen met relatief lage nauwkeurigheid en realtime vereisten.

**XHT11 communicatiemodus:**

Er wordt gebruikgemaakt van single bus-communicatie. Dit betekent dat er slechts één datalijn is voor gegevensuitwisseling en controle in het systeem.

- Definitie van databit die door single bus wordt verzonden:

Single bus dataformaat: 40 bits data worden in één keer verzonden, met de hoogste bit eerst.

8bit vochtigheidsinteger + 8bit vochtigheidsdecimaal + 8bit temperatuurinteger + 8bit temperatuurdecimaal + 8bit pariteitsbit (Het decimale deel van de vochtigheid is 0)

- Definitie van pariteitsbit

8bit vochtigheidsinteger + 8bit vochtigheidsdecimaal + 8bit temperatuurinteger + 8bit temperatuurdecimaal. 8bit pariteitsbit = de laatste 8 bits van het verkregen resultaat

- Datatijdlijn:

Nadat de gebruikershost (MCU) een startsignaal heeft verzonden, schakelt de XHT11 over van laag stroomverbruik naar hoge snelheid modus. Na het startsignaal stuurt XHT11 een antwoordsignaal en 40bit data, en activeert een signaalacquisitie.

- De signaaloverdracht wordt getoond in de afbeelding:

![Img](./media/A229.png)

 **Parameters**

- Bedrijfsspanning: DC 3.3V tot 5V

- Bedrijfstroom: 2.1mA

- Maximale stroom: 0.0105W

- Temperatuurbereik: -25℃ ~ +60℃ (± 2℃)

- Vochtigheidsbereik: 5%RH ~ 95%RH (nauwkeurigheid ±5%RH rond 25 °C)

**Microbit Lichtsensor**

![Img](./media/A0335.png)

Een lichtsensor is een invoerapparaat dat de helderheid van extern licht meet. De micro:bit board bevat geen ingebouwde lichtsensor. Het detecteert en meet de omgevingshelderheid via een LED-matrix die herhaaldelijk de lichtintensiteit omzet in een waarde-invoer, waarna de spanningsvervaltijd wordt bemonsterd. Op deze manier is <span style="color: rgb(255, 76, 65);">de gedetecteerde helderheidswaarde een relatieve waarde</span>.

#### 4. Aansluitschema

![Img](./media/A409.png)

<span style="color: rgb(255, 76, 65);">Bij gebruik van het OLED-display moeten we een externe voeding aansluiten en de DIP-schakelaar op ON zetten.</span>

![Img](./media/A904.png)

![Img](./media/A554.png)

#### 5. Codeflow

![Img](./media/A638.png)


#### 6. Testcode

Het codebestand wordt geleverd in map Project 07：Environment Monitoring, bestand Project-07-Environment-Monitoring.hex.

![Img](./media/A656.png)

**Laad codeblokken:**

![Img](./media/A715.png)

#### 7. Testresultaat

Na het downloaden van de code naar het board toont de OLED realtime de temperatuur- en vochtigheidswaarden en het lichthelderheidsniveau.

<span style="color: rgb(255, 76, 65);">**LET OP:** Als de bedrading correct is maar u ziet geen resultaten, druk dan op de resetknop aan de achterkant van het board.</span>

![Img](./media/A838.gif)
