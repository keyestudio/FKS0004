## 1. Programmierung mit MakeCode

Die folgenden Anweisungen gelten für das Windows-System, können aber auch als Referenz dienen, wenn Sie ein anderes System verwenden.

#### 1.1. Schneller Start

**Schritt 1 Verbindung zum micro:bit herstellen**

Verbinden Sie das Board über ein USB-Kabel mit dem Computer.

![Img](./media/A800.png)

Wenn die rote LED auf der Rückseite des Boards leuchtet, bedeutet dies, dass das Board mit Strom versorgt wird. Wenn Ihr Computer über das USB-Kabel mit dem Hauptboard kommuniziert, blinkt die gelbe LED darauf. Zum Beispiel blinkt sie, wenn Sie eine „.hex“-Datei übertragen.

Dann erscheint das Micro:bit-Hauptboard auf Ihrem Computer als Laufwerk mit dem Namen „MICROBIT“. Bitte beachten Sie, dass es sich nicht um ein gewöhnliches USB-Laufwerk handelt, wie unten gezeigt.

![Img](./media/A849.png)

**Schritt 2 Herzschlag-Programm schreiben**

Öffnen Sie den Link: [Online-Version von Makecode](https://makecode.microbit.org/)

Klicken Sie auf „<span style="color: rgb(255, 76, 65);">Neues Projekt</span>“ und Sie sehen „<span style="color: rgb(255, 76, 65);">Projekt wird erstellt</span>“, geben Sie „<span style="color: rgb(255, 76, 65);">heartbeat</span>“ ein und klicken Sie auf „<span style="color: rgb(255, 76, 65);">Erstellen √</span>“.

<span style="color: rgb(255, 76, 65);">Hier schreiben wir Programme im Google Chrome.</span>

![Img](./media/A021.png)

Lassen Sie uns einen micro:bit-Code schreiben.

Sie können einige Blöcke in den Bearbeitungsbereich ziehen und dann Ihr Programm im Simulator ausführen, wie unten gezeigt. Hier demonstrieren wir, wie man das <span style="color: rgb(255, 76, 65);">heartbeat</span>-Programm bearbeitet.

Videoanleitung:

![Img](./media/A100.png)

**Schritt 3 Codes herunterladen**

Im Allgemeinen, für die Windows 10 APP ([Windows 10 App herunterladen](https://apps.microsoft.com/detail/9pjc7sv48lcx?hl=zh-CN&gl=CN#activetab=pivot:overviewtabdocx))(Klick), reicht ein Klick auf „<span style="color: rgb(255, 76, 65);">Download</span>“, um den Code direkt auf das micro:bit-Board herunterzuladen, ohne weitere Schritte.

Für Browser gilt jedoch:

Klicken Sie im Editor auf „<span style="color: rgb(255, 76, 65);">Download</span>“. Dadurch wird eine „hex“-Datei heruntergeladen, ein Format, das das micro:bit-Board lesen kann. Kopieren Sie diese dann auf Ihr micro:bit-Board, so wie Sie eine Datei auf ein USB-Laufwerk kopieren würden. Unter Windows können Sie auch mit der rechten Maustaste auf die „<span style="color: rgb(255, 76, 65);">.hex</span>“-Datei klicken und „**Senden an → MICROBIT**“ wählen, um die Datei auf das micro:bit-Board zu kopieren.

![Img](./media/A319.png)

![Img](./media/A449.png)

Alternativ können Sie die „<span style="color: rgb(255, 76, 65);">.hex</span>“-Datei direkt in MICROBIT ziehen.

![Img](./media/A341.png)

![Img](./media/A345.png)

Während des Kopiervorgangs der „<span style="color: rgb(255, 76, 65);">.hex</span>“-Datei zum Micro:bit blinkt die gelbe LED auf der Rückseite des Boards. Wenn die Übertragung abgeschlossen ist, hört die LED auf zu blinken und bleibt an.

**Schritt 4 Programm ausführen**

Nachdem das Programm auf das Micro:bit hochgeladen wurde, können Sie es über das USB-Kabel oder eine externe Stromquelle mit Strom versorgen. Dann zeigt die 5 x 5 LED-Punktmatrix ein Herzschlagmuster an.

![Img](./media/A425.png)

<span style="color: rgb(255, 76, 65);">**Achtung:**</span> Wenn Sie jedes Mal programmieren, wird der Treiber des Micro:bit automatisch ausgeworfen und zurückgesetzt, sodass die hex-Dateien verschwinden. Das Board hat nur Zugriff auf hex-Dateien, speichert sie aber nicht.

#### 1.2. MakeCode

Öffnen Sie die [Makecode Google Chrome Online-Version](https://makecode.microbit.org/). Hier ist die Hauptoberfläche.

![Img](./media/A637.png)

Im Code-Bearbeitungsbereich gibt es die Blöcke „**on start**“ und „**forever**“. <span style="color: rgb(255, 76, 65);">Nach dem Einschalten wird der Code in „on start“ nur einmal ausgeführt, während der Code in „forever“ zyklisch läuft.</span>

Klicken Sie auf die Sprache „**JS JavaScript**“:

![Img](./media/A754.png)

Wechseln Sie zu „**Python**“:

![Img](./media/A814.png)


#### 1.3. Einführung in WebUSB-Funktionen

Wie bereits erwähnt, wenn Ihr Computer Windows 10 ist und Sie die APP MakeCode heruntergeladen haben, können Sie Codes schnell über die „<span style="color: rgb(255, 76, 65);">Download</span>“-Schaltfläche auf das Board herunterladen. Wir verwenden das WebUSB von **<span style="color: rgb(255, 76, 65);">Google Chrome</span>**, um auf das per USB angeschlossene Hardwaregerät zuzugreifen.

**Geräte koppeln:**

1\. Verbinden Sie das Board über USB-Kabel mit dem Computer.

![Img](./media/A951.png)

2\. Klicken Sie auf „<span style="color: rgb(255, 76, 65);">Download</span>“ -> „<span style="color: rgb(255, 76, 65);">...</span>“ und dann „<span style="color: rgb(255, 76, 65);">Gerät verbinden</span>“.

![Img](./media/A028.png)

3\. „<span style="color: rgb(255, 76, 65);">Weiter</span>“.

![Img](./media/A046.png)

4\. „<span style="color: rgb(255, 76, 65);">Koppeln</span>“.

![Img](./media/A104.png)

5\. Wählen Sie dann das entsprechende Gerät und „<span style="color: rgb(255, 76, 65);">Verbinden</span>“.

![Img](./media/A127.png)

6\. „<span style="color: rgb(255, 76, 65);">Fertig</span>“.

![Img](./media/A144.png)

**Programm herunterladen:**

Nach der Verbindung klicken Sie auf „<span style="color: rgb(255, 76, 65);">Download</span>“ und Sie sehen, dass das ![Img](./media/A212.png) zu ![Img](./media/A220.png) wird. Das Programm wird auf das micro:bit-Board heruntergeladen.

![Img](./media/A232.png)

Wenn kein Gerät zur Auswahl angezeigt wird, lesen Sie bitte [Fehlerbehebung bei Downloads mit WebUSB](https://makecode.microbit.org/device/usb/webusb/troubleshoot). Besuchen Sie [die Benutzeranleitung](https://microbit.org/guide/firmware/), um zu erfahren, wie Sie die micro:bit-Firmware aktualisieren.

#### 1.4. MakeCode Erweiterungsbibliothek

**3.4.1 Bibliothekserweiterungen importieren**

Öffnen Sie Makecode, um ein bestimmtes Projekt zu betreten, klicken Sie auf ![Img](./media/A806.png) und wählen Sie „**Erweiterungen**“.

![Img](./media/A842.png)

Oder klicken Sie auf „**Erweiterungen**“ über dem Bereich „Erweitert“.

![Img](./media/A900.png)

Suchen Sie die gewünschte Bibliothek.

![Img](./media/A909.png)

Wir stellen für jedes Projekt die Code-Dateien bereit, die alles enthalten, was Sie zum Ausführen eines Projekts benötigen, sodass Sie sie direkt laden können. Wenn Sie die Codeblöcke selbst erstellen möchten, denken Sie daran, die folgenden drei Erweiterungen hinzuzufügen.

<span style="color: rgb(0, 209, 0);">**OLED-Erweiterung:**</span>

1\. Klicken Sie auf „**Erweiterungen**“, um Bibliothekserweiterungen hinzuzufügen.

![Img](./media/A236.png)

2\. Suchen Sie „**OLED**“ und klicken Sie ![Img](./media/A3257.png).

![Img](./media/A306.png)

Klicken Sie auf das erste **oled-ssd1306** und warten Sie, bis es hinzugefügt wurde.

![Img](./media/A3316.png)

3\. Erfolgreich hinzugefügt:

![Img](./media/A335.png)

<span style="color: rgb(0, 209, 0);">**Ultraschallsensor-Erweiterung:**</span>

1\. Klicken Sie auf „**Erweiterungen**“, um Bibliothekserweiterungen hinzuzufügen.

![Img](./media/A236.png)

2\. Suchen Sie „**sonar**“ und klicken Sie ![Img](./media/A3257.png), um „sonar“ zu finden und zu laden.

![Img](./media/A506.png)

3\. Erfolgreich hinzugefügt:

![Img](./media/A522.png)

<span style="color: rgb(0, 209, 0);">**DHT11-Sensor-Erweiterung:**</span>

1\. Klicken Sie auf „**Erweiterungen**“, um Bibliothekserweiterungen hinzuzufügen.

![Img](./media/A236.png)

2\. Suchen Sie „**DHT11**“ und klicken Sie ![Img](./media/A3257.png), um „DHT11_DHT22“ zu finden und zu laden.

![Img](./media/A616.png)

3\. Erfolgreich hinzugefügt:

![Img](./media/A645.png)

**3.4.2 Erweiterungen aktualisieren/löschen**

1\. Klicken Sie auf „**JavaScript**“, um zum Textcode zu wechseln.

![Img](./media/A724.png)

2\. Klicken Sie auf „**Explorer**“.

![Img](./media/A749.png)

3\. Finden Sie die „**OLED**“-Bibliothek und klicken Sie ![Img](./media/A813.png), um sie zu löschen.

![Img](./media/A824.png)

4\. „**Entfernen**“.

![Img](./media/A727.png)

Sie wurde entfernt.

#### 1.5. Wie man Codes in MakeCode importiert

Nehmen wir das Projekt „**heartbeat**“ als Beispiel, um zu zeigen, wie man den Code lädt.

1\. Öffnen Sie die Web-Version von Makecode oder die Windows 10 App Makecode und klicken Sie auf „<span style="color: rgb(255, 76, 65);">Importieren</span>“.

![Img](./media/A956.png)

2\. „<span style="color: rgb(255, 76, 65);">Datei importieren...</span>“

![Img](./media/A042.png)

3\. „<span style="color: rgb(255, 76, 65);">Datei auswählen</span>“, um die Datei zu importieren, die Sie laden möchten.

![Img](./media/A06.png)

4\. Hier laden wir „<span style="color: rgb(255, 76, 65);">heartbeat.hex</span>“.

![Img](./media/A28.png)

5\. „<span style="color: rgb(255, 76, 65);">Weiter √</span>“

![Img](./media/A149.png)

Neben der oben genannten Methode können Sie den Testcode auch in den Code-Bearbeitungsbereich ziehen, wie unten gezeigt:

![Img](./media/A202.png)

Warten Sie auf das Laden.

![Img](./media/A217.png)
