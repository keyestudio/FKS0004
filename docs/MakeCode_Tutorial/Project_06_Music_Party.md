### Projekt 06: Musikparty

![Img](./media/A1317.png)

#### 1. Übersicht

Wenn wir in die Hände klatschen, nimmt das Mikrofon auf dem Board Tonsignale auf, und der Lautsprecher spielt ein fröhliches Geburtstagslied, während die RGB-LED blendendes Licht aussendet.

#### 2. Komponenten

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit Board *1 | micro:bit T-Typ Erweiterungsboard *1 | micro USB Kabel *1 |
| ![Img](./media/A500.png)| ![Img](./media/A944.png) | ![Img](./media/A950.png) |
| rote LED *1 | 220Ω Widerstand *3 | Steckdraht *2 |
| ![Img](./media/A017.png) | ![Img](./media/A024.png) | ![Img](./media/A621.png)  |
| Steckbrett *1 | Batteriefach *1 <br> (<span style="color: rgb(255, 76, 65);">selbst mitgebrachte AA Batterien *2</span>)| RGB Karte *1 |

#### 3. Komponentenwissen

**Mikrofon**

Ein hochwertiges digitales Mikrofon ist auf der Vorderseite des micro:bit V2 Boards integriert, um Ton- und Audiosignale zu erfassen. Der Chip, der das Mikrofon steuert und verarbeitet, befindet sich auf der Rückseite.

![Img](./media/A1317.png)

Das Mikrofon befindet sich in einem kleinen runden Loch auf der Vorderseite des Boards, was praktisch ist, um Umgebungsgeräusche aufzunehmen. Legen Sie das micro:bit Board beim Gebrauch einfach mit der Vorderseite nach oben. Neben dem Loch befindet sich eine Mikrofon-LED-Anzeige. Wenn das micro:bit den Geräuschpegel misst, leuchtet die Anzeige auf.

![Img](./media/A116.png)

**RGB LED**

![Img](./media/A2127.png)

Die RGB LED basiert auf der Kombination der drei Grundfarben (RGB): Rot, Grün und Blau. Die meisten Farben können durch unterschiedliche Mischverhältnisse von RGB erzeugt werden. Die roten, grünen und blauen LEDs sind in einem transparenten Kunststoffgehäuse verpackt und geben Farben ab, indem die Eingangsspannung der R-, G- und B-Pins verändert wird.

![Img](./media/A137.png)

**Dreifarbentheorie:**

![Img](./media/A150.png)

RGB LEDs lassen sich in zwei Typen unterteilen: gemeinsamer Anode und gemeinsamer Kathode:

Bei einer gemeinsamen Kathoden-RGB LED teilen sich die drei LEDs einen negativen Anschluss (Kathode);

Bei einer gemeinsamen Anoden-RGB LED teilen sich die drei LEDs einen positiven Anschluss (Anode).

![Img](./media/A209.png)

<span style="color: rgb(255, 76, 65);">**Hinweis: Hier verwenden wir eine gemeinsame Kathoden-RGB LED.**</span>

**RGB LED Pins:**

Die RGB LED hat 4 Pins: GND (der längste), R (rot), G (grün) und B (blau). Setzen Sie die RGB LED wie unten gezeigt ein, die Pins von links nach rechts sind rot, GND, grün und blau.

![Img](./media/A239.png)

#### 4. Schaltplan

![Img](./media/A308.png)

![Img](./media/A325.png)

#### 5. Programmablauf

![Img](./media/A343.png)

#### 6. Testcode

Die Code-Datei befindet sich im Ordner Projekt 06：Musikparty, Datei Project-06-Music-Party.hex.

![Img](./media/A423.png)

**Codeblöcke laden:**

![Img](./media/A445.png)

#### 7. Testergebnis

Nach dem Herunterladen des Codes auf das Board, wenn wir in die Hände klatschen, nimmt das Mikrofon auf dem Board Tonsignale auf, und der Lautsprecher spielt ein fröhliches Geburtstagslied, während die RGB LED blendendes Licht aussendet. Ist die Musikparty nicht in einer fröhlichen und glücklichen Atmosphäre?

<span style="color: rgb(255, 76, 65);">**ACHTUNG:** Wenn die Verkabelung korrekt ist, Sie aber keine Ergebnisse sehen, drücken Sie die Reset-Taste auf der Rückseite des Boards.</span>

![Img](./media/A757.gif)
