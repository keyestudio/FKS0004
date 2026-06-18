### Projekt 02: Ampel

#### 1. Übersicht

In diesem Projekt verwenden wir drei LEDs (rot, gelb und grün), einen Lautsprecher auf dem micro:bit Board und eine 5x5 LED-Matrix, um ein Modell einer Ampel zu erstellen.

#### 2. Komponenten

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit Board *1 | micro:bit T-Typ Erweiterungsboard *1 | micro USB Kabel *1 |
| ![Img](./media/A937.png)| ![Img](./media/A5652.png) | ![Img](./media/A658.png) |
| rote LED *1 | gelbe LED *1 | grüne LED *1 |
| ![Img](./media/A944.png) | ![Img](./media/A950.png) |![Img](./media/A017.png) |
| 220Ω Widerstand *3 | Jumper Kabel | Steckbrett *1 |
|  ![Img](./media/A024.png) |  ![Img](./media/A020.png) |  |
| Batteriefach *1 <br> (<span style="color: rgb(255, 76, 65);">selbst mitgebrachte AA Batterien *2</span>) | Ampelkarte *1 | |

#### 3. Komponentenwissen

**Lautsprecher**

![Img](./media/A833.png)

Der micro:bit ist mit einem Lautsprecher ausgestattet, was es einfach macht, in deinem Projekt Töne zu erzeugen.

#### 4. Schaltplan

![Img](./media/A908.png)

<span style="color: rgb(255, 76, 65);">**Hinweis:** Das micro:bit Board muss wie unten gezeigt in das T-Typ Erweiterungsboard eingesteckt werden. Die LED-Matrix des micro:bit Boards sollte auf derselben Seite wie das Logo des Erweiterungsboards sein.</span>

![Img](./media/A940.png)

#### 5. Programmablauf

![Img](./media/A5956.png)

#### 6. Testcode

Die Code-Datei befindet sich im Ordner Projekt 02：Ampel, Datei Project-02-Traffic-Lights.hex.

![Img](./media/A0017.png)

**Codeblöcke laden:**

![Img](./media/A605.png)

#### 7. Testergebnis

Für die Windows 10 App klicke auf „<span style="color: rgb(255, 76, 65);">Download</span>“. Für Browser sende die heruntergeladene „<span style="color: rgb(255, 76, 65);">.hex</span>“-Datei an das micro:bit Board.

Nach dem Herunterladen des Codes auf das Board leuchtet die grüne LED und die 5×5 LED-Matrix zählt 6 Sekunden herunter. Nachdem die grüne LED aus ist, blinkt die gelbe LED und die Matrix zählt 3 Sekunden mit Ton vom Lautsprecher herunter. Zum Schluss leuchtet die rote LED mit einem Countdown von 6 Sekunden. Diese Abläufe wiederholen sich.

<span style="color: rgb(255, 76, 65);">**ACHTUNG:** Wenn die Verkabelung korrekt ist, du aber keine Ergebnisse siehst, drücke den Reset-Knopf auf der Rückseite des Boards.</span>

![Img](./media/A459.gif)

<span style="color: rgb(255, 76, 65);">**Beim Betrieb über externe Stromversorgung den DIP-Schalter auf ON stellen.**</span>

![Img](./media/A904.png)
