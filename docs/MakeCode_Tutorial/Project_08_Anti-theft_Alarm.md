### Projekt 08: Diebstahlalarm

#### 1. Übersicht

Wenn der intelligente Diebstahlalarm erkennt, dass die Diebstahlsicherung bewegt wurde, ertönt der Lautsprecher auf dem micro:bit Board und die rote LED blinkt.

#### 2. Komponenten

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit Board *1 | micro:bit T-Typ Erweiterungsboard *1 | micro USB Kabel *1 |
| ![Img](./media/A937.png)| ![Img](./media/A944.png) | ![Img](./media/A950.png) |
| rote LED *1 | 220Ω Widerstand *1 | Steckdraht *2 |
| ![Img](./media/A017.png) | ![Img](./media/A024.png) | ![Img](./media/A952.png)  |
| Steckbrett *1 | Batteriefach *1 <br> (<span style="color: rgb(255, 76, 65);">selbstbereitgestellte AA Batterien *2</span>)| Alarmkarte *1 |

#### 3. Komponentenwissen

**Beschleunigungssensor**

![Img](./media/A026.png)

Das micro:bit Board verfügt über einen eingebauten LSM303AGR Beschleunigungssensor (wir nennen ihn Beschleunigungsmesser), der einen Standard-, Schnell-, Plus- und Hochgeschwindigkeitsmodus (100 kHz, 400 kHz, 1 MHz und 3,4 MHz) des I2C-Serienbus-Interfaces sowie ein SPI-Serienstandardinterface für die externe Kommunikation bietet, mit einer Auflösung von 8/10/12 Bit und einem Messbereich von ±2g, ±4g oder ±8g.

Wenn das micro:bit Board ruht oder sich gleichförmig bewegt, misst der Beschleunigungssensor nur die Erdbeschleunigung. Wenn es leicht geschwenkt wird, ist die gemessene Beschleunigung viel geringer als die der Erdbeschleunigung, sodass die Differenz vernachlässigt werden kann. Daher erfassen wir hauptsächlich die Änderung der Erdbeschleunigung auf den x-, y- und z-Achsen.

#### 4. Schaltplan

![Img](./media/A219.png)

<span style="color: rgb(255, 76, 65);">**Der Steuerpin des LED-Boards ist P1 (der Pin des T-Typ Erweiterungsboards ist digital 1).**</span>

#### 5. Programmablauf

![Img](./media/A4434.png)

#### 6. Testcode

Die Code-Datei befindet sich im Ordner Projekt 08：Burglar Alarm, Datei Project-08-Burglar-Alarm.hex.

![Img](./media/A4518.png)

**Codeblöcke laden:** 

<span style="color: rgb(255, 76, 65);">**Nach dem Importieren des Codes, wenn der Summer ständig ertönt, obwohl das Steckbrett nicht bewegt wird; kann dies durch geografische Faktoren verursacht sein. Sie können die Schwellenwerte in der Bedingung -60 und 50 entsprechend den tatsächlichen Bedingungen anpassen.**</span>

![Img](./media/A611.png)

#### 7. Testergebnis

Nach dem Herunterladen des Codes auf das Board bewegen Sie das Steckbrett. Wenn der Beschleunigungswert x＜-60 oder x＞50 ist, ertönt der Lautsprecher auf dem Board und die LED blinkt, und die micro:bit LED-Matrix zeigt ![Img](./media/A706.png). Andernfalls gibt der Lautsprecher keinen Ton von sich und die LED ist aus, und die micro:bit LED-Matrix zeigt ![Img](./media/A720.png).

<span style="color: rgb(255, 76, 65);">**ACHTUNG:** Wenn die Verkabelung korrekt ist, Sie aber keine Ergebnisse sehen, drücken Sie die Reset-Taste auf der Rückseite des Boards.</span>

![Img](./media/A936.gif)
