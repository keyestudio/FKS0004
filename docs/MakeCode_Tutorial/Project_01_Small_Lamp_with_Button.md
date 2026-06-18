### Projekt 01: Kleine Lampe mit Knopf

#### 1. Überblick

Auf der Vorderseite des micro:bit Boards befinden sich zwei programmierbare Tasten (A und B). Wir kombinieren sie mit einer roten LED und einer Lampenkarte, um eine kleine Schreibtischlampe zu bauen. Wenn die Taste A gedrückt wird, leuchtet die rote LED; wenn B gedrückt wird, geht sie aus.

#### 2. Komponenten

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit Board *1 | micro:bit T-Typ Erweiterungsboard *1 | micro USB Kabel *1 |
| ![Img](./media/A937.png)| ![Img](./media/A944.png) | ![Img](./media/A950.png) |
| rote LED *1 | 220Ω Widerstand *1 | Steckdraht *2 |
| ![Img](./media/A017.png) | ![Img](./media/A024.png) | ![Img](./media/A920.png)  |
| Steckbrett *1 | Batteriefach *1 <br> (<span style="color: rgb(255, 76, 65);">selbst mitgebrachte AA Batterien *2</span>) | Lampenkarte *1 |

#### 3. Komponentenwissen

**Tasten**

Tasten können den Stromkreis ein- und ausschalten. Wenn eine Taste mit einem Stromkreis verbunden ist, ist der Stromkreis geöffnet, wenn die Taste nicht gedrückt wird; der Stromkreis wird geschlossen, nachdem die Taste gedrückt wurde.

Auf dem micro:bit Board befinden sich drei Tasten: eine Reset-Taste auf der Rückseite und zwei programmierbare Tasten (A und B) auf der Vorderseite.

![Img](./media/A230.png)

**Widerstände**

![Img](./media/A248.png)

Ein Widerstand ist ein elektronisches Bauteil, das den Strom in einem Zweigkreis begrenzt. Der Widerstand eines Festwiderstands kann nicht eingestellt werden, während der eines Potentiometers oder eines veränderlichen Widerstands verstellbar ist.

Hier sind zwei gängige Schaltzeichensymbole für Widerstände. Wenn Sie diese Symbole in einem Schaltkreis sehen, repräsentieren sie einen Widerstand.

![Img](./media/A303.png)

Ω ist die Einheit des Widerstands, einschließlich Ω, KΩ, MΩ usw. Sie können wie folgt ausgedrückt werden: 1 MΩ = 1000 KΩ, 1 KΩ = 1000 Ω. Im Allgemeinen sind einige Widerstände auf der Oberfläche markiert.

Beim Verwenden eines Widerstands müssen wir zuerst seinen Widerstandswert kennen. Es gibt zwei Möglichkeiten: die Farbringe darauf beobachten oder den Widerstand mit einem Multimeter messen. Offensichtlich ist die erste Methode bequemer und schneller.

![Img](./media/A317.png)

Wie auf der Widerstandskarte gezeigt, steht jede Farbe für eine Zahl.

![Img](./media/A3335.png)

4-Band- und 5-Band-Widerstände werden häufig verwendet.

Oft ist es schwierig zu entscheiden, von welcher Seite man die Farbringe lesen soll, wenn man einen Widerstand erhält.

**Daher können Sie den Abstand zwischen den beiden Bändern an einem Ende beobachten; wenn dieser breiter ist als jeder andere Bandabstand, lesen Sie von der gegenüberliegenden Seite.**

<span style="color: rgb(255, 76, 65);">**Beachten Sie, dass der Abstand zwischen dem 4. und 5. Band (bzw. 3. und 4. Band) bei einem 5-Band- (bzw. 4-Band-) Widerstand relativ breit ist.**</span>

Sehen wir uns an, wie man den Widerstand eines 5-Band-Widerstands liest, wie unten gezeigt:

![Img](./media/A426.png)

Für diesen Widerstand sollte der Wert von links nach rechts gelesen werden. Der Wert lautet: 1. Band 2. Band 3. Band × 10^Multiplikator(Ω), ±Toleranz%.

Daher beträgt der Widerstand dieses Widerstands 2(rot) 2(rot) 0(schwarz) × 10^0 (schwarz)Ω = 220Ω, ±1%(braun). Mehr über [Widerstände bei Wiki](https://en.wikipedia.org/wiki/Resistor).

**LED**

LED, vollständig „Licht emittierende Diode“ genannt, ist ein elektronisches Bauteil aus Halbleitermaterialien (Silizium, Selen, Germanium usw.). Sie ist polarisiert, mit einem positiven Pol – dem langen Anschluss, der mit VCC (V oder 3.3V oder 5V oder +) verbunden ist, und einem negativen Pol – dem kurzen Anschluss, der mit GND (G oder -) verbunden ist. Der Strom fließt vom positiven zum negativen Pol, in einem Einwegfluss.

Elektronisches und grafisches Symbol der LED:

![Img](./media/A515.png)

LEDs in verschiedenen Größen und Farben:

![Img](./media/A525.png)

Rot, Gelb, Blau, Grün und Weiß sind die gebräuchlichsten LED-Farben, entsprechend ihrer Erscheinungsfarben. Transparente LEDs werden selten verwendet, und das ausgestrahlte Licht ist möglicherweise nicht weiß. Es gibt vier LED-Größen: 3mm, 5mm (am häufigsten), 8mm und 10mm.

![Img](./media/A535.png)

Die Vorwärtsspannung muss verwendet werden, wenn die LED eingeschaltet ist. Sie ist ein sehr wichtiger Parameter beim Einsatz einer LED, da sie bestimmt, wie viel Leistung verwendet wird und wie groß der strombegrenzende Widerstand sein sollte. Für die meisten roten, gelben, orangen und hellgrünen LEDs liegt die Spannung typischerweise zwischen 1,9V und 2,1V.

![Img](./media/A548.png)

Nach dem Ohmschen Gesetz verringert sich der Strom durch den Stromkreis mit zunehmendem Widerstand, wodurch die LED dunkler wird.

I = (VP-Vl)/R

Um die LED sicher und mit der richtigen Helligkeit zu betreiben, welchen Widerstand sollten wir im Stromkreis verwenden?

Für 99% der 5mm LEDs wird ein Strom von 20mA empfohlen, was aus der Spalte „Bedingungen“ im Datenblatt ersichtlich ist:

![Img](./media/A613.png)

Nun wandeln wir die obige Formel um zu:

R = (VP-Vl)/I

Wenn VP = 5V, Vl (Vorwärtsspannung) = 2V und I = 20mA, ergibt sich R = 150Ω. Daher kann die LED heller gemacht werden, indem der Widerstand verringert wird, aber der Widerstand sollte nicht unter 150Ω liegen (dieser Wert ist möglicherweise nicht genau, da die verwendete LED variiert).

Die Vorwärtsspannung und Wellenlänge verschiedener LED-Farben sind unten zu Ihrer Information dargestellt:

![Img](./media/A629.png)

<span style="color: rgb(255, 76, 65);">**Schließen Sie keinen Widerstand mit sehr niedrigem Widerstandswert direkt an die beiden Pole der Stromversorgung an, da elektronische Bauteile durch zu hohen Strom beschädigt werden können. Widerstände sind nicht polarisiert.**</span>

**Steckbrett**

Vor dem Fertigstellen eines Stromkreises wird ein Steckbrett verwendet, um Schaltungen schnell zu entwerfen und zu testen. Auf einem Steckbrett befinden sich viele Löcher, in die Bauteile (z.B. Widerstände) gesteckt werden können. Ein typisches Steckbrett sieht wie folgt aus:

![Img](./media/A655.png)

Unter dem Steckbrett befinden sich viele Metallstreifen, die die Löcher an der Oberseite verbinden. Sie sind wie unten gezeigt angeordnet.

<span style="color: rgb(255, 76, 65);">Beachten Sie, dass die oberen und unteren Löcher horizontal verbunden sind, während die restlichen Löcher vertikal verbunden sind.</span>

![Img](./media/A723.png)

Die ersten zwei Reihen (oben) und die letzten zwei Reihen (unten) des Steckbretts werden für die positiven (+) und negativen (-) Pole der Stromversorgung verwendet. Das leitfähige Layout ist unten dargestellt:

![Img](./media/A730.png)

Beim Anschluss von DIP (Dual In-line Package) Bauteilen, wie integrierten Schaltkreisen, Mikrocontrollern, Chips usw., trennt die Rille die beiden Teile. Daher können DIP-Bauteile wie unten gezeigt angeschlossen werden:

![Img](./media/A740.png)

![Img](./media/A747.png)

**Steckdraht und DuPont-Draht**

Steckdrähte und DuPont-Drähte verbinden zwei Anschlüsse. Es gibt verschiedene Typen, hier konzentrieren wir uns auf die, die im Steckbrett verwendet werden. Sie übertragen elektrische Signale von beliebigen Stellen auf dem Steckbrett zu den Ein-/Ausgangspins eines Mikrocontrollers.

Beim Gebrauch werden „zwei Pins“ der Drähte ohne Löten in das Steckbrett gesteckt. Unter der Oberfläche des Steckbretts sind mehrere parallele Leiterbahnen angeordnet, sodass Drähte nur in bestimmten Löchern eines bestimmten Prototyps eingesteckt werden müssen.

Es gibt drei Typen von DuPont-Drähten: F-F, M-M und M-F. Am Draht wird der Pin als männliches Ende (M) bezeichnet, während das Loch weiblich (F) ist.

![Img](./media/A811.png)

Mehrere Typen können in einem Projekt verwendet werden. Obwohl die Farben der Drähte unterschiedlich sind, dienen sie dem gleichen Zweck. Farben werden verwendet, um Schaltungen zu unterscheiden.

#### 4. Schaltplan

<span style="color: rgb(255, 76, 65);">Hinweis: Das micro:bit Board muss wie unten gezeigt in das T-Typ Erweiterungsboard eingesetzt werden. Die LED-Matrix des micro:bit Boards sollte auf derselben Seite wie das Logo des Erweiterungsboards sein.</span>

![Img](./media/A156.png)

<span style="color: rgb(255, 76, 65);">Der Steuerpin der LED ist P0 (der Pin des T-Typ Erweiterungsboards ist digital 0).</span>

#### 5. Programmablauf

![Img](./media/A4323.png)

#### 6. Testcode

Die Code-Datei befindet sich im Ordner Projekt 01：Kleine Lampe mit Knopf, Datei Project-01-Small-Lamp-with-Button.hex.

![Img](./media/A357.png)

**Codeblöcke laden:**

![Img](./media/A440.png)

#### 7. Testergebnis

Für die Windows 10 App klicken Sie auf „<span style="color: rgb(255, 76, 65);">Download</span>“. Für Browser senden Sie die heruntergeladene „<span style="color: rgb(255, 76, 65);">.hex</span>“-Datei an das micro:bit Board.

Nach dem Herunterladen des Codes auf das Board zeigt die 5x5 LED-Matrix das ![Img](./media/A512.png) Symbol. Drücken Sie die Taste A, und die 5x5 LED-Matrix zeigt das ![Img](./media/A518.png) Symbol, die LED leuchtet. Drücken Sie die Taste B, und die 5x5 LED-Matrix zeigt das ![Img](./media/A527.png) Symbol, die LED geht aus. Sieht es aus wie eine Mini-Lampe?

<span style="color: rgb(255, 76, 65);">**ACHTUNG:** Wenn die Verkabelung korrekt ist, Sie aber keine Ergebnisse sehen, drücken Sie die Reset-Taste auf der Rückseite des Boards.</span>

![Img](./media/A359.gif)

<span style="color: rgb(255, 76, 65);">**Beim Betrieb über eine externe Stromversorgung den DIP-Schalter auf ON stellen.**</span>

![Img](./media/A904.png)
