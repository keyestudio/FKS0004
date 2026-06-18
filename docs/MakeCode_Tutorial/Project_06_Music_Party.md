### Project 06: Muziekfeest

![Img](./media/A1317.png)

#### 1. Overzicht

Wanneer we in onze handen klappen, vangt de microfoon op de board geluidssignalen op, en speelt de speaker een vrolijk verjaardagslied terwijl de RGB LED schitterend licht uitstraalt.

#### 2. Componenten

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit board *1 | micro:bit T-type uitbreidingsboard *1 | micro USB-kabel *1 |
| ![Img](./media/A500.png)| ![Img](./media/A944.png) | ![Img](./media/A950.png) |
| rode LED *1 | 220Ω weerstand *3 | verbindingsdraad *2 |
| ![Img](./media/A017.png) | ![Img](./media/A024.png) | ![Img](./media/A621.png)  |
| breadboard *1 | batterijhouder *1 <br> (<span style="color: rgb(255, 76, 65);">zelf meegebrachte AA-batterijen *2</span>)| RGB-kaart *1 |

#### 3. Componentenkennis

**Microfoon**

Een hoogwaardige digitale microfoon is geïntegreerd aan de voorkant van het micro:bit V2 board om geluid- en audiosignalen te detecteren. De chip die de microfoon aanstuurt en verwerkt bevindt zich aan de achterkant.

![Img](./media/A1317.png)

De microfoon zit in een klein rond gaatje aan de voorkant van het board, wat handig is om omgevingsgeluid op te vangen. Plaats het micro:bit board gewoon met de voorkant naar boven tijdens gebruik. Naast het gaatje zit een microfoon LED-indicator. Wanneer de micro:bit geluidsniveaus meet, zal de indicator oplichten.

![Img](./media/A116.png)

**RGB LED**

![Img](./media/A2127.png)

RGB LED is gebaseerd op de combinatie van drie primaire kleuren (RGB): rood, groen en blauw. De meeste kleuren kunnen worden samengesteld door RGB in verschillende verhoudingen te mengen. De rode, groene en blauwe LEDs zijn verpakt in een transparante plastic behuizing die kleuren licht uitstraalt door de ingangsspanning van de R-, G- en B-pinnen te veranderen.

![Img](./media/A137.png)

**Trichromatische theorie:**

![Img](./media/A150.png)

RGB LED kan worden onderverdeeld in twee typen: common anode en common cathode:

In een common cathode RGB LED delen de drie LEDs een negatieve aansluiting (kathode);

In een common anode RGB LED delen de drie LEDs een positieve aansluiting (anode).

![Img](./media/A209.png)

<span style="color: rgb(255, 76, 65);">**Opmerking: Hier leveren wij een common cathode RGB LED.**</span>

**RGB LED-pinnen:**

RGB LED heeft 4 pinnen: GND (de langste), R (rood), G (groen) en B (blauw). Plaats de RGB LED zoals hieronder getoond, pinnen van links naar rechts zijn rood, GND, groen en blauw.

![Img](./media/A239.png)

#### 4. Aansluitschema

![Img](./media/A308.png)

![Img](./media/A325.png)

#### 5. Codeflow

![Img](./media/A343.png)

#### 6. Testcode

Het codebestand is te vinden in de map Project 06：Music Party, bestand Project-06-Music-Party.hex.

![Img](./media/A423.png)

**Codeblokken laden:**

![Img](./media/A445.png)

#### 7. Testresultaat

Na het downloaden van de code naar het board, wanneer we in onze handen klappen, vangt de microfoon op het board geluidssignalen op, en speelt de speaker een vrolijk verjaardagslied terwijl de RGB LED schitterend licht uitstraalt. Is het muziekfeest niet in een gelukkige en vreugdevolle sfeer?

<span style="color: rgb(255, 76, 65);">**LET OP:** Als de bedrading correct is maar je ziet geen resultaat, druk dan op de resetknop aan de achterkant van het board.</span>

![Img](./media/A757.gif)
