### Projekt 01: Kleine Lampe mit Knopf

#### 1. Übersicht

Auf der Vorderseite des micro:bit Boards befinden sich zwei programmierbare Tasten (A und B). Wir kombinieren sie mit einer roten LED und einer Lampenkarte, um eine kleine Schreibtischlampe zu bauen. Wenn die Taste A gedrückt wird, leuchtet die rote LED; wenn B gedrückt wird, geht sie aus.

#### 2. Komponenten

| ![Img](./media/A850.png) |              ![Img](./media/A858.png)              | ![Img](./media/A906.png) |
| :---------------------: | :-----------------------------------------------: | :---------------------: |
|   micro:bit Board *1    |        micro:bit T-Typ Erweiterungsboard *1        |   micro USB Kabel *1    |
| ![Img](./media/A937.png) |              ![Img](./media/A944.png)              | ![Img](./media/A950.png) |
|       rote LED *1       |                 220Ω Widerstand *1                 |      Jumper Kabel *2    |
| ![Img](./media/A017.png) |              ![Img](./media/A024.png)              | ![Img](./media/A920.png) |
|      Breadboard *1      | Batteriehalter *1 <br> (<span style="color: rgb(255, 76, 65);">selbst mitgebrachte AA Batterien *2</span>) |      Lampenkarte *1     |

#### 3. Komponentenwissen

**Tasten**

Tasten können den Stromkreis ein- und ausschalten. Wenn eine Taste mit einem Stromkreis verbunden ist, ist der Stromkreis geöffnet, wenn die Taste nicht gedrückt wird; der Stromkreis wird geschlossen, nachdem die Taste gedrückt wird.

Es gibt drei Tasten auf dem micro:bit Board: eine Reset-Taste auf der Rückseite und zwei programmierbare Tasten (A und B) auf der Vorderseite.

![Img](./media/A230.png)

**Widerstände**

![Img](./media/A248.png)

Ein Widerstand ist ein elektronisches Bauteil, das den Strom in einem Zweigkreis begrenzt. Der Widerstand eines Festwiderstands kann nicht eingestellt werden, während der eines Potentiometers oder eines veränderlichen Widerstands einstellbar ist.

Hier sind zwei gängige Schaltzeichensymbole für Widerstände. Wenn Sie diese Symbole in einem Stromkreis sehen, repräsentieren sie einen Widerstand.

![Img](./media/A303.png)

Ω ist die Einheit des Widerstands, einschließlich Ω, KΩ, MΩ usw. Sie können wie folgt ausgedrückt werden: 1 MΩ = 1000 KΩ, 1 KΩ = 1000 Ω. Im Allgemeinen sind einige Widerstände auf der Oberfläche markiert.

Beim Verwenden eines Widerstands müssen wir zuerst seinen Widerstandswert kennen. Es gibt zwei Möglichkeiten: die Farbringe darauf beobachten oder den Widerstand mit einem Multimeter messen. Offensichtlich ist die erste Methode bequemer und schneller.

![Img](./media/A317.png)

Wie auf der Widerstandskarte gezeigt, repräsentiert jede Farbe eine Zahl.

![Img](./media/A3335.png)

4- und 5-Band Widerstände werden häufig verwendet.

Oft fällt es schwer zu entscheiden, von welcher Seite man die Farbringe liest, wenn man einen Widerstand erhält.

**Daher können Sie den Abstand zwischen den beiden Bändern an einem Ende beobachten; wenn dieser breiter ist als jeder andere Bandabstand, lesen Sie von der gegenüberliegenden Seite.**

<span style="color: rgb(255, 76, 65);">**Beachten Sie, dass der Abstand zwischen dem 4. und 5. Band (bzw. 3. und 4. Band) bei einem 5-Band (4-Band) Widerstand relativ breit ist.**</span>

Sehen wir uns an, wie man den Widerstand eines 5-Band Widerstands liest, wie unten gezeigt:

![Img](./media/A426.png)

Für diesen Widerstand sollte der Wert von links nach rechts gelesen werden. Der Wert lautet: 1. Band 2. Band 3. Band x 10^Multiplikator(Ω), ±Toleranz%.

Daher beträgt der Widerstand dieses Widerstands 2(rot) 2(rot) 0(schwarz) × 10^0 (schwarz)Ω = 220Ω, ±1%(braun). Mehr über [Widerstände bei Wiki](https://en.wikipedia.org/wiki/Resistor).

**LED**

LED, vollständig „Licht emittierende Diode“ genannt, ist ein elektronisches Bauteil aus Halbleitermaterialien (Silizium, Selen, Germanium usw.). Sie ist polarisiert, mit einem Pluspol – dem langen Pin, der mit VCC (V oder 3.3V oder 5V oder +) verbunden ist, und einem Minuspol – dem kurzen Pin, der mit GND (G oder -) verbunden ist. Der Strom fließt vom Plus- zum Minuspol, in einem Einwegfluss.

Elektronisches und grafisches Symbol der LED:

![Img](./media/A515.png)

LEDs in verschiedenen Größen und Farben:

![Img](./media/A525.png)

Rot, Gelb, Blau, Grün und Weiß sind die gebräuchlichsten LED-Farben, die den Farben ihres Aussehens entsprechen. Transparente LEDs werden selten verwendet, und das ausgestrahlte Licht ist möglicherweise nicht weiß. Es gibt vier LED-Größen: 3mm, 5mm (am häufigsten), 8mm und 10mm.

![Img](./media/A535.png)

Die Vorwärtsspannung muss verwendet werden, wenn die LED eingeschaltet ist. Dies ist ein sehr wichtiger Parameter bei der Verwendung einer LED, da er bestimmt, wie viel Leistung Sie verwenden und wie groß der strombegrenzende Widerstand sein sollte. Für die meisten roten, gelben, orangen und hellgrünen LEDs liegt die Spannung typischerweise zwischen 1,9V und 2,1V.

![Img](./media/A548.png)

Nach dem Ohmschen Gesetz nimmt der Strom im Stromkreis ab, wenn der Widerstand steigt, wodurch die LED dunkler wird.

I = (VP-Vl)/R

Um die LED sicher und mit der richtigen Helligkeit zu betreiben, wie viel Widerstand sollten wir im Stromkreis verwenden?

Für 99% der 5mm LEDs wird ein empfohlener Strom von 20mA angegeben, was in der Bedingungsspalte ihres Datenblatts zu sehen ist:

![Img](./media/A613.png)

Nun wandeln wir die obige Formel um zu:

R = (VP-Vl)/I

Wenn VP = 5V, Vl (Vorwärtsspannung) = 2V und I = 20mA, ergibt sich R = 150Ω. Daher können wir die LED heller machen, indem wir den Widerstand verringern, aber der Widerstand sollte nicht unter 150Ω liegen (dieser Wert ist möglicherweise nicht genau, da die verwendete LED variiert).

Die Vorwärtsspannung und Wellenlänge verschiedener LED-Farben sind unten zu Ihrer Referenz dargestellt:

![Img](./media/A629.png)

<span style="color: rgb(255, 76, 65);">**Schließen Sie keinen Widerstand mit sehr niedrigem Widerstand direkt an die beiden Pole der Stromversorgung an, da sonst elektronische Bauteile durch zu hohen Strom beschädigt werden können. Widerstände sind nicht polarisiert.**</span>

**Breadboard**

Bevor ein Stromkreis fertiggestellt wird, wird ein Breadboard zum schnellen Entwerfen und Testen von Schaltungen verwendet. Ein Breadboard hat viele Löcher, in die Bauteile (z.B. Widerstände) gesteckt werden können. Ein typisches Breadboard sieht wie folgt aus:

![Img](./media/A655.png)

Ein Breadboard hat viele Metallstreifen darunter, die die Löcher oben verbinden. Sie sind wie unten angeordnet.

<span style="color: rgb(255, 76, 65);">**Beachten Sie, dass die oberen und unteren Löcher horizontal verbunden sind, während die restlichen Löcher vertikal verbunden sind.**</span>

![Img](./media/A723.png)

Die ersten zwei Reihen (oben) und die letzten zwei Reihen (unten) des Breadboards werden für die positiven (+) und negativen (-) Pole der Stromversorgung verwendet. Das leitfähige Layout ist unten dargestellt:

![Img](./media/A730.png)

Beim Anschluss von DIP (Dual In-line Package) Bauteilen, wie integrierten Schaltkreisen, Mikrocontrollern, Chips usw., trennt die Rille die beiden Teile. Daher können DIP-Bauteile wie unten gezeigt angeschlossen werden:

![Img](./media/A740.png)

![Img](./media/A747.png)

**Jumper-Kabel und DuPont-Kabel**

Jumper-Kabel und DuPont-Kabel verbinden zwei Anschlüsse. Es gibt verschiedene Typen, hier konzentrieren wir uns auf die, die im Breadboard verwendet werden. Sie übertragen elektrische Signale von überall auf dem Breadboard zu den Ein-/Ausgangspins eines Mikrocontrollers.

Beim Gebrauch werden „zwei Pins“ der Kabel ohne Löten in das Breadboard gesteckt. Unter der Oberfläche des Breadboards sind mehrere parallele Leiterbahnen angeordnet, sodass Kabel nur in bestimmten Löchern eines bestimmten Prototyps eingesteckt werden müssen.

Es gibt drei Typen von DuPont-Kabeln: F-F, M-M und M-F. Am Kabel wird der Pin als männliches Ende (M) bezeichnet, während das Loch weiblich (F) ist.

![Img](./media/A811.png)

Mehrere Typen können in einem Projekt verwendet werden. Obwohl die Farben der Kabel unterschiedlich sind, dienen sie dem gleichen Zweck. Farben werden verwendet, um Schaltungen zu unterscheiden.

#### 4. Schaltplan

<span style="color: rgb(255, 76, 65);">Hinweis: Das micro:bit Board muss wie unten gezeigt in das T-Typ Erweiterungsboard eingesteckt werden. Die LED-Matrix des micro:bit Boards sollte auf derselben Seite wie das Logo des Erweiterungsboards sein.</span>

![Img](./media/A156.png)

<span style="color: rgb(255, 76, 65);">**Der Steuerpin des Boards für die LED ist P0 (der Pin des T-Typ Erweiterungsboards ist digital 0).**</span>

#### 5. Programmablauf

![Img](./media/A4323.png)

#### 6. Testcode

Die Code-Datei befindet sich im Ordner Projekt 01：Kleine Lampe mit Knopf, Datei Project-01-Small-Lamp-with-Button\.py.

![Img](./media/A100.png)

**Vollständiger Code:**

```python
'''
Function: microbit on-board buttons A&B control LED
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import microbit related libraries
from microbit import *

display.show(Image.HEART) # LED matrix displays ❤
pin0.write_digital(0) # set P0 pin to low

while True:
    if button_a.is_pressed():     # if A is pressed
        pin0.write_digital(1)     # P0 is high
        display.show(Image.HAPPY) # LED matrix displays a smile face
    elif button_b.is_pressed():   # or else B is pressed
        pin0.write_digital(0)     # P0 is low
        display.show(Image.SAD)   # LED matrix displays a crying face
```

#### 7. Testergebnis

Klicken Sie auf „<span style="color: rgb(255, 76, 65);">Flash</span>“, um den Code auf das micro:bit Board zu laden.

![Img](./media/A2156.png)

Nachdem der Code auf das Board heruntergeladen wurde, **schalten Sie die Stromversorgung über das micro USB Kabel oder eine externe Stromquelle ein (DIP-Schalter auf ON stellen)** und drücken Sie die Reset-Taste auf dem Board.

![Img](./media/A455.png)

Wir können folgendes Phänomen beobachten: Die 5x5 LED-Matrix zeigt ![Img](./media/A512.png). Drücken Sie die Taste A, zeigt die 5x5 LED-Matrix ![Img](./media/A518.png), die LED leuchtet. Drücken Sie die Taste B, zeigt die 5x5 LED-Matrix ![Img](./media/A527.png), die LED geht aus. Sieht das nicht aus wie eine Mini-Lampe?

<span style="color: rgb(255, 76, 65);">**ACHTUNG:** Wenn die Verdrahtung korrekt ist, Sie aber keine Ergebnisse sehen, drücken Sie erneut die Reset-Taste auf der Rückseite des Boards.</span>

![Img](./media/A359.gif)

<span style="color: rgb(255, 76, 65);">Wenn die Stromversorgung über eine externe Quelle erfolgt, stellen Sie den DIP-Schalter auf ON.</span>

![Img](./media/A904.png)
