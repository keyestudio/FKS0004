### Project 04: Slim Parkeren

#### 1. Overzicht

Slimme parkeerplaatsen zijn overal. Kunnen we ook een slimme parkeerplaats maken? Natuurlijk. We kunnen een ultrasone sensor gebruiken om te detecteren of er voertuigen in de buurt zijn. Wanneer een voertuig (of object) wordt gedetecteerd dat nadert, besturen we een servo om de hefboom omhoog te brengen; Als wordt gedetecteerd dat het weg beweegt, zal de servo de hefboom laten zakken.

#### 2. Componenten

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit board *1 | micro:bit T-type uitbreidingsbord *1 | micro USB-kabel *1 |
| ![Img](./media/A356.png)| ![Img](./media/A309.png)| ![Img](./media/A415.png) |
| ultrasone sensor *1 | servo *1 | DuPont draden |
|![Img](./media/A017.png) | ![Img](./media/A950.png) | ![Img](./media/A024.png) |
| breadboard *1 | jump wires | batterijhouder *1 <br> (<span style="color: rgb(255, 76, 65);">zelf meegebrachte AA batterijen *2</span>)|
|![Img](./media/A336.png) |![Img](./media/A131.png) | |
| bat kaart *1 | hefboom kaart *1| |

#### 3. Componentenkennis

**Servo**

Een servo is een positie-aandrijving. We kunnen een servo gebruiken om de exacte positie te regelen of een hoog koppel uit te voeren. Meestal wordt het gebruikt in robots, radiografisch bestuurbare auto's en zelfs vliegtuigmodellen. Er zijn veel specificaties, maar alle servo's hebben drie draden: signaal (oranje), positief (rood) en negatief (bruin). De kleur kan variëren per servomerk.

![Img](./media/A5525.png)

**Interne structuurdiagram:**

![Img](./media/A5534.png)

① Signaal: ontvangt besturingssignalen van de microcontroller;

② potentiometer: De positie van de uitgangsas kan worden gemeten, dit behoort tot het feedbackgedeelte van de hele servo;

③ Interne controller: Het ingebedde bord verwerkt signalen van externe besturing, stuurt de motor aan en geeft positieterugkoppelingen, dit is de kern van de hele servo;

④ DC-motor: Het fungeert als actuator om snelheid, koppel en positie uit te voeren;

⑤ Overbrenging / servomechanisme: Het mechanisme vergroot de slaguitgang van de motor tot de uiteindelijke uitgangshoek volgens een bepaalde overbrengingsverhouding.

**De servo aansturen**

Stuur PWM-signalen naar de servosignaaldraad om de uitgang te regelen. De duty cycle van de PWM bepaalt direct de positie van de uitgangsas. De periode is meestal 20 milliseconden en wordt typisch ingesteld om pulsen te genereren met een frequentie van 50Hz.

<span style="color: rgb(255, 0, 0);">Bijvoorbeeld (180° servo):</span>

Wanneer we een pulsbreedte van 1,5 milliseconden (ms) naar de 180° servo sturen, zal de uitgangsas van de servo naar de middenpositie (90 graden) bewegen;

Als de pulsbreedte 0,5 ms is, zal de uitgangsas naar 0 graden bewegen;

Als de pulsbreedte 2,5 ms is, zal de uitgangsas naar 180 graden bewegen;

![Img](./media/A5545.png)

**Parameters:**

- Bedrijfsspanning: DC 3,3V~5V

- Bedrijfstemperatuur: -10°C ~ +50°C

- Afmetingen: 32,25mm x 12,25mm x 30,42mm

- Interface: 3-pins interface met een afstand van 2,54mm

#### 4. Aansluitschema

![Img](./media/A606.png)

<span style="color: rgb(255, 76, 65);">**Bij gebruik van de ultrasone sensor en servo moeten we een externe voeding aansluiten en de DIP-schakelaar op ON zetten.**</span>

![Img](./media/A902.png)

![Img](./media/A701.png)

#### 5. Code Flow

![Img](./media/A716.png)

#### 6. Testcode

Het codebestand is beschikbaar in map Project 04：Smart-Parking, bestand Project-04-Smart-Parking.hex.

![Img](./media/A758.png)

**Laad codeblokken:** <span style="color: rgb(255, 76, 65);">**De drempelwaarde in de voorwaarde 10 kan worden aangepast aan de werkelijke omstandigheden.**</span>

![Img](./media/A832.png)

#### 7. Testresultaat

Na het downloaden van de code naar het board, wanneer de ultrasone sensor een voertuig (of object) detecteert dat nadert, bestuurt de servo de hefboom om omhoog te gaan; Als de sensor detecteert dat het weg beweegt, zal de servo de hefboom laten zakken.

<span style="color: rgb(255, 76, 65);">**LET OP:** Als de bedrading correct is maar je ziet geen resultaat, druk dan op de resetknop aan de achterkant van het board.</span>

![Img](./media/A021.gif)
