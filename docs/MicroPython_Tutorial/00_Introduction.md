## 1. Über die Mu-Software

### 1.1. Mu installieren

Klicken Sie, um die [offizielle Mu-Software-Webseite](https://codewith.mu/) zu besuchen.

Mu ist ein Python-Code-Editor für Anfänger, wie Lehrer und Schüler. Wir können ihn über den offiziellen Installer für Windows, Mac OSX oder Linux erhalten (Mu unterstützt keine 32-Bit-Windows-Versionen mehr). Die empfohlene Version ist Mu 1.2.0.

**Schritt 1 - Stellen Sie sicher, welches Betriebssystem Sie haben, und laden Sie dann den Mu-Installer herunter**

Finden Sie zuerst heraus, welches Betriebssystem Ihr Computer hat (Windows oder Mac OSX). Öffnen Sie „**Dieser PC**“, um die „**Eigenschaften**“ zu sehen.

![Img](./media/A225.png)

Überprüfen Sie den Systemtyp: 64-Bit oder 32-Bit.

![Img](./media/A253.png)

[MU herunterladen](https://codewith.mu/en/download). Laden Sie die Version entsprechend Ihrem Betriebssystem herunter.

![Img](./media/A348.png)

<span style="color: rgb(255, 76, 65);">Hier nehmen wir das Windows-System als Beispiel, das als Referenz für Mac OSX und Linux dienen kann.</span>

![Img](./media/A422.png)

**Schritt 2 - Führen Sie den Installer aus**

Doppelklicken Sie auf den Installer (wahrscheinlich im Ordner „Downloads“), um ihn auszuführen.

![Img](./media/A440.png)

Wir haben die zusätzlichen Schritte skizziert, die nötig sind, um Mu unter Windows 10 zu installieren. Andere Versionen sind ähnlich.

[Mu-Installer für MacOS](https://codewith.mu/en/howto/1.1/install_macos).

[Mu-Installer für Linux-System](https://codewith.mu/en/howto/1.2/install_linux).

Für Windows 10 erscheint eine Warnmeldung vom Defender. Klicken Sie auf den Link „**Weitere Informationen**“.

![Img](./media/A615.png)

Die Meldung ändert sich und zeigt Ihnen mehr Informationen zum Installer sowie eine Schaltfläche „**Trotzdem ausführen**“. Klicken Sie auf „**Trotzdem ausführen**“.

![Img](./media/A626.png)

**Schritt 3 - Lizenzvereinbarung**

Überprüfen Sie die Lizenz, wählen Sie das Kontrollkästchen aus und klicken Sie auf „**Installieren**“.

![Img](./media/A1716.png)

**Schritt 4 - Installation**

Gehen Sie eine Tasse Kaffee holen, während Mu auf Ihrem Computer installiert wird.

![Img](./media/A1740.png)

**Schritt 5 - Fertig**

Die Installation wurde erfolgreich abgeschlossen, klicken Sie auf „**Fertigstellen**“, um den Installer zu schließen.

![Img](./media/A817.png)

**Schritt 6 - Mu starten**

Sie können Mu starten, indem Sie auf das Symbol im Startmenü klicken oder „Mu“ in das Suchfeld eingeben (beides unten hervorgehoben). Beim ersten Start kann es etwas dauern.

![Img](./media/A852.png)

So sieht es aus:

![Img](./media/A909.png)

### 1.2. Modi & Menüleiste verwenden

Stellen Sie den „<span style="color: rgb(255, 76, 65);">Modus</span>“ auf BBC micro:bit ein.

Klicken Sie im Menü auf „**Modus**“ und wählen Sie „**BBC micro：bit**“. Der micro:bit-Modus versteht, wie man mit einem micro:bit interagiert und sich verbindet.

![Img](./media/A022.png)

Klicken Sie, um [mit Mu zu starten](https://codewith.mu/en/tutorials/1.1/start).

Für weitere Tutorials zur Verwendung von Mu besuchen Sie bitte: https://codewith.mu/en/tutorials/

### 1.3. Programmieren mit Mu

Hier laden wir die Datei „<span style="color: rgb(255, 76, 65);">heartbeat\.py</span>“ in Mu. Sie finden sie im Ordner „<span style="color: rgb(255, 76, 65);">Heart beat</span>“, den wir bereitgestellt haben.

![Img](./media/A200.png)

**Methode eins:**

Öffnen Sie Mu und klicken Sie auf „<span style="color: rgb(255, 76, 65);">Laden</span>“, um den Pfad auszuwählen, wo Sie den Code heruntergeladen haben.

![Img](./media/A341.png)

![Img](./media/A345.png)

Erfolgreich geladen, wie unten gezeigt:

![Img](./media/A354.png)

**Methode zwei:**

Klicken Sie auf „neu“ ![Img](./media/A503.png), um ein neues Programm zu erstellen, und ziehen Sie „heartbeat\.py“ hinein:

![Img](./media/A521.png)

Erfolgreich geladen, wie unten gezeigt:

![Img](./media/A533.png)

<span style="color: rgb(255, 76, 65);">Das Gleiche gilt für das Hinzufügen anderer Codes.</span>

### 1.4. Code auf Micro:bit herunterladen

Verbinden Sie das Board über ein USB-Kabel mit dem Computer.

![Img](./media/A252.png)

Klicken Sie auf „<span style="color: rgb(255, 76, 65);">**Flash**</span>“, um den Code auf das micro:bit-Board herunterzuladen.

![Img](./media/A3728.png)

Danach <span style="color: rgb(255, 76, 65);">**schalten Sie die Stromversorgung über das Micro-USB-Kabel oder eine externe Stromquelle ein (DIP-Schalter auf ON stellen)**</span>. Sie werden sehen, dass die eingebaute 5×5 LED-Matrix wiederholt ![Img](./media/A903.png) und dann ![Img](./media/A910.png) anzeigt.

<span style="color: rgb(255, 76, 65);">**Beachten Sie, dass wenn ein Fehler im Code ist, er trotzdem heruntergeladen werden kann, aber nicht richtig funktioniert.**</span>

<span style="color: rgb(0, 209, 0);">Zum Beispiel ist die Funktion sleep() im Code als sleeps() geschrieben. Klicken Sie auf „**Flash**“, um den Code auf den micro:bit zu laden. Die 5×5 LED-Matrix zeigt jedoch chaotische Symbole an.</span>

![Img](./media/A4003.png)

In diesem Fall klicken Sie auf „**REPL**“ und drücken den Reset-Knopf auf der Rückseite des Boards. Die Fehlermeldung wird im REPL-Fenster angezeigt, wie unten gezeigt:

![Img](./media/A029.png)

![Img](./media/A033.png)

Klicken Sie erneut auf „**REPL**“, um REPL zu schließen. Und dann klicken Sie auf „<span style="color: rgb(255, 76, 65);">**Flash**</span>“.

Um sicherzustellen, dass der Code korrekt ist, klicken Sie nach Fertigstellung auf „<span style="color: rgb(255, 76, 65);">**Check**</span>“ und Mu zeigt Fehler im Code an.

![Img](./media/A119.png)

Ändern Sie den Code entsprechend der Fehlermeldung und klicken Sie erneut auf „<span style="color: rgb(255, 76, 65);">**Check**</span>“. Mu zeigt keinen Fehler mehr an.

![Img](./media/A134.png)

Siehe [weitere Tutorials, die spezifische Aspekte von Mu erklären](https://codewith.mu/en/tutorials/).

## 2. Wie Mu Bibliotheken auf Micro:bit importiert

<span style="color: rgb(255, 76, 65);">Bevor Bibliotheken importiert werden, müssen wir einen .py-Code (auch leerer Code ist ok) auf das micro:bit-Board hochladen. Hier nehmen wir einen leeren Code als Beispiel.</span>

Verbinden Sie das Board über ein USB-Kabel mit dem Computer. Öffnen Sie Mu und klicken Sie auf „Flash“, um den .py-Code (leerer Code) auf das Board hochzuladen.

![Img](./media/A252.png)

In diesem Tutorial werden OLED- und DHT11-Module verwendet. Daher müssen die Bibliotheksdateien „<span style="color: rgb(255, 76, 65);">**oled_ssd1306\.py**</span>“ und „<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>“ in das micro:bit-Board importiert werden.

Das Standardverzeichnis, in dem Mu Dateien speichert, ist „mu_code“ im Stammverzeichnis des Benutzerverzeichnisses.

Referenzlink: [https://codewith.mu/en/tutorials/1.0/files](https://codewith.mu/en/tutorials/1.0/files)

**Anleitung zum Importieren von Bibliotheken:**

1\. Suchen Sie den Ordner „<span style="color: rgb(255, 76, 65);">mu_code</span>“ auf Laufwerk (C:).

![Img](./media/A543.png)

![Img](./media/A550.png)

2\. Öffnen Sie „<span style="color: rgb(255, 76, 65);">mu_code</span>“.

![Img](./media/A628.png)

3\. Kopieren und fügen Sie die Bibliotheksdateien „<span style="color: rgb(255, 76, 65);">**oled_ssd1306\.py**</span>“ und „<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>“ in „<span style="color: rgb(255, 76, 65);">**Libraries**</span>“ ein.

![Img](./media/A4716.png)

4\. Wie unten gezeigt:

![Img](./media/A735.png)

5\. Öffnen Sie Mu und klicken Sie auf „<span style="color: rgb(255, 76, 65);">**Dateien**</span>“. Ziehen Sie hier die Bibliothek „<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>“ in den micro:bit.

![Img](./media/A816.png)

![Img](./media/A820.png)

6\. Nach dem Import von „<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>“ sehen Sie sie im linken Feld.

![Img](./media/A841.png)

7\. Machen wir dasselbe mit „<span style="color: rgb(255, 76, 65);">**oled_ssd1306\.py**</span>“.

![Img](./media/A916.png)

![Img](./media/A4920.png)

<span style="color: rgb(255, 76, 65);">**Beachten Sie, dass wenn Sie andere Dateien auf den micro:bit hochladen, diese den ursprünglichen Inhalt überschreiben, sodass Sie sie für die nächste Verwendung erneut importieren müssen.**</span>
