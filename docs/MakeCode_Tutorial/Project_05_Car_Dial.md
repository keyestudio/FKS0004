### Projekt 05: Auto-Zifferblatt

#### 1. Übersicht

In diesem Projekt kombinieren wir ein einstellbares Potentiometer, einen Servo und eine schöne Zifferblattkarte, um ein einfaches Auto-Zifferblattmodell zu erstellen.

#### 2. Komponenten

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit Board *1 | micro:bit T-Typ Erweiterungsboard *1 | micro USB Kabel *1 |
| ![Img](./media/A350.png)| ![Img](./media/A309.png)| ![Img](./media/A950.png) |
| Potentiometer *1 | Servo *1 | Verbindungskabel |
|![Img](./media/A017.png)  | ![Img](./media/A024.png) |![Img](./media/A233.png) |
| Steckbrett *1 | Batteriefach *1 <br> (<span style="color: rgb(255, 76, 65);">selbst mitgebrachte AA Batterien *2</span>)| Potentiometer-Karte *1 |
|![Img](./media/A1326.png) |  |  |
| Auto-Zifferblattkarte *1| |  |

#### 3. Komponentenwissen

**Potentiometer**

![Img](./media/A350.png)

Ein Potentiometer ist ebenfalls ein Widerstandselement mit drei Anschlüssen, dessen Widerstandswert nach einer gewissen Regelmäßigkeit einstellbar ist.

Sie gibt es in allen Formen, Größen und Werten, aber sie haben alle Folgendes gemeinsam:

① Drei Anschlüsse (oder Verbindungspunkte).

② Einen beweglichen Knopf oder Schieberegler, der den Widerstand zwischen dem mittleren Anschluss und einem der äußeren Anschlüsse verändern kann.

③ Wenn der Knopf bewegt wird, variiert der Widerstand zwischen dem mittleren Anschluss und einem der äußeren Anschlüsse von 0Ω bis zum Maximalwert.

Das Schaltzeichen des Potentiometers:

![Img](./media/A654.png)

(1)\. Als Spannungsteiler

Das Potentiometer ist ein kontinuierlich einstellbarer Widerstand. Wenn Sie seinen Schieberegler drehen, gleitet der bewegliche Kontakt über den Widerstand. Zu diesem Zeitpunkt kann eine Spannung entsprechend der am Potentiometer angelegten Spannung und dem Winkel oder Hub der Drehung des beweglichen Reglers ausgegeben werden.

(2)\. Als veränderlicher Widerstand

Wenn das Potentiometer als veränderlicher Widerstand verwendet wird, verbinden Sie seinen mittleren Anschluss mit einem der beiden zusätzlichen Anschlüsse im Stromkreis. Auf diese Weise erhalten Sie einen stabilen und kontinuierlich variierenden Widerstandswert innerhalb seines Bereichs.

(3)\. Als Stromregler

Wenn es als Stromregler verwendet wird, muss der bewegliche Kontakt als einer der Ausgangsanschlüsse angeschlossen werden.

#### 4. Schaltplan

![Img](./media/A812.png)

<span style="color: rgb(255, 76, 65);">Beim Einsatz des Servos müssen wir eine externe Stromversorgung anschließen und den DIP-Schalter auf ON stellen.</span>

![Img](./media/A902.png)

![Img](./media/A836.png)

#### 5. Programmablauf

![Img](./media/A0854.png)

#### 6. Testcode

Die Code-Datei befindet sich im Ordner Projekt 05：Auto-Zifferblatt, Datei Project-05-Car-Dial.hex.

![Img](./media/A922.png)

**Codeblöcke laden:**

![Img](./media/A942.png)

#### 7. Testergebnis

Nach dem Herunterladen des Codes auf das Board drehen Sie den Knopf am Potentiometer und der Servo bewegt den Zeiger auf dem Zifferblatt.

<span style="color: rgb(255, 76, 65);">**ACHTUNG:** Wenn die Verkabelung korrekt ist, Sie aber keine Ergebnisse sehen, drücken Sie die Reset-Taste auf der Rückseite des Boards.</span>

![Img](./media/A706.gif)
