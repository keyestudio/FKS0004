## 3. Fehlerbehebung

#### MAINTENANCE: Code kann nicht auf Micro:bit heruntergeladen werden

**1. Problem**

In letzter Zeit haben viele Benutzer das Problem, dass das Micro:bit-Board beim Herunterladen des Codes nicht reagiert.

Wenn die Bedienung korrekt ist, haben Sie möglicherweise versehentlich die Reset-Taste gedrückt und den MAINTENANCEsmodus aktiviert oder die Firmware wurde durch Fehlbedienung gelöscht.

Wenn Sie das Micro:bit-Board anschließen, erscheint das Laufwerk „<span style="color: rgb(255, 76, 65);">MAINTENANCE</span>“, was bedeutet, dass das Programm nicht heruntergeladen werden kann.

![Img](./media/A158.png)

**2. Lösungen**

(1) Laden Sie die <span style="color: rgb(255, 76, 65);">.hex</span>-Datei von dieser Seite auf Ihren Computer herunter.

Laden Sie [die neueste micro:bit Firmware-0255](https://www.microbit.org/get-started/user-guide/firmware/) herunter. Wenn Sie nicht von dieser Website herunterladen möchten, stellen wir sie auch in unserem Tutorial bereit.

(2) Nachdem die neueste Firmware heruntergeladen wurde, ziehen Sie die Firmware für V2.20_V2.21 in das „<span style="color: rgb(255, 76, 65);">MAINTENANCE</span>“-Laufwerk, um das Micro:bit wieder in den Normalmodus zu versetzen.

<span style="color: rgb(255, 76, 65);">Wir installieren unterschiedliche Firmwares je nach Micro:bit-Board-Modell. Hier ist die Firmware für V2.20_V2.21.</span>

![Img](./media/A326.png)

![Img](./media/A331.png)

**3. Vermeiden Sie den Eintritt in den „MAINTENANCE“-Modus**

(1) Stellen Sie sicher, dass die Reset-Taste beim Anschließen des Boards über das USB-Kabel nicht gedrückt wird.

![Img](./media/A228.png)

(2) Ziehen Sie das Kabel während des Herunterladens des Micro:bit-Programms nicht plötzlich ab, da sonst die Firmware verloren geht und das Micro:bit in den „MAINTENANCE“-Modus wechselt.

(3) Falsche Verdrahtung im Experiment kann ebenfalls einen Kurzschluss oder Firmwareverlust verursachen.

#### Fehlerbehebung bei Downloads mit WebUSB

Klicken Sie hier: [Fehlerbehebung bei Downloads mit WebUSB](https://makecode.microbit.org/device/usb/webusb/troubleshoot)

Probleme bei der Verbindung Ihres micro:bit mit WebUSB? Lassen Sie uns herausfinden, warum!

**Schritt 1: Überprüfen Sie Ihr Kabel**

Stellen Sie sicher, dass Ihr micro:bit mit einem Micro-USB-Kabel an Ihren Computer angeschlossen ist. Zum Beispiel sollte im Windows Explorer ein **MICROBIT**-Laufwerk erscheinen, wenn es verbunden ist.

![Img](./media/A321.png)

Wenn Sie das MICROBIT-Laufwerk sehen, fahren Sie mit Schritt 2 fort. Wenn Sie das Laufwerk nicht sehen:

(1) Stellen Sie sicher, dass das USB-Kabel funktioniert.

Funktioniert das Kabel an einem anderen Computer? Wenn nicht, verwenden Sie ein anderes Kabel. Einige Kabel bieten nur eine Stromverbindung und übertragen keine Daten.

(2) Versuchen Sie einen anderen USB-Anschluss an Ihrem Computer.

Ist das Kabel in Ordnung, aber Sie sehen das MICROBIT-Laufwerk immer noch nicht? Hmm, möglicherweise liegt ein Problem mit Ihrem micro:bit vor.

Versuchen Sie die zusätzlichen Schritte auf der [Fehlerbehebungsseite bei microbit.org](https://support.microbit.org/support/solutions/articles/19000024000-fault-finding-with-a-micro-bit). Wenn das nicht hilft, können Sie [ein Support-Ticket erstellen](https://support.microbit.org/support/tickets/new), um die Micro:bit Foundation über das Problem zu informieren. Überspringen Sie die restlichen Fehlerbehebungsschritte.

**Schritt 2: Überprüfen Sie Ihre Firmware-Version**

Wenn Ihre Downloads immer noch nicht funktionieren, muss die Firmware-Version auf dem micro:bit möglicherweise aktualisiert werden. Lassen Sie uns das überprüfen:

1. Gehen Sie zum **MICROBIT**-Laufwerk;

2. Öffnen Sie die Datei <span style="color: rgb(255, 76, 65);">DETAILS.TXT</span>;

![Img](./media/A0452.png)

3. Finden Sie die Firmware-Versionsnummer; Suchen Sie in der Datei nach einer Zeile, die die Versionsnummer angibt. Dort sollte „Version:“ stehen:

![Img](./media/A501.png)

Wenn die Version 0234, 0241 oder 0243 ist, MÜSSEN Sie die Firmware auf Ihrem micro:bit aktualisieren. Gehen Sie zu Schritt 3 und folgen Sie den Upgrade-Anweisungen.

Wenn die Version 0249, 0250 oder höher ist, haben Sie die richtige Firmware und können mit Schritt 4 fortfahren.

**Schritt 3: Firmware aktualisieren**

(1) Versetzen Sie Ihr micro:bit in den MAINTENANCES-Modus.

Dazu ziehen Sie das USB-Kabel vom micro:bit ab und schließen es erneut an, während Sie die Reset-Taste gedrückt halten. Sobald Sie das Kabel einstecken, können Sie die Reset-Taste loslassen.

Sie sollten jetzt ein MAINTENANCES-Laufwerk anstelle des MICROBIT-Laufwerks sehen. Außerdem leuchtet eine gelbe LED neben der Reset-Taste dauerhaft.

![maintenance](./media/maintenance.gif)

(2) Laden Sie die [Firmware .hex-Datei](https://microbit.org/guide/firmware/) herunter.

<span style="color: rgb(255, 76, 65);">Wir installieren unterschiedliche Firmwares je nach Micro:bit-Board-Modell. Hier ist die Firmware für V2.20_V2.21.</span>

![Img](./media/A0629.png)

(3) Ziehen Sie diese Datei auf das **MAINTENANCE**-Laufwerk.

(4) Achten Sie auf die blinkende LED.

Die gelbe LED blinkt, während die HEX-Datei kopiert wird. Wenn der Kopiervorgang abgeschlossen ist, erlischt die LED und das micro:bit startet neu. Das MAINTENANCE-Laufwerk wechselt zurück zu MICROBIT.

(5) Upgrade abgeschlossen.

Das Upgrade ist abgeschlossen! Sie können die Datei <span style="color: rgb(255, 76, 65);">DETAILS.TXT</span> öffnen, um zu überprüfen, ob die Firmware-Version auf die Version der kopierten HEX-Datei geändert wurde.

Wenn Sie mehr über das Anschließen des Boards, den MAINTENANCES-Modus und das Firmware-Upgrade erfahren möchten, lesen Sie den [Firmware-Leitfaden](https://microbit.org/guide/firmware/).

**Schritt 4: Überprüfen Sie Ihre Browserversion**

WebUSB ist eine relativ neue Funktion und erfordert möglicherweise ein Update Ihres Browsers. Stellen Sie sicher, dass Ihre Browserversion einer der folgenden entspricht: Browser-Versionen für Android, Chrome OS, Linux, macOS und Chrome 65+ für Windows 10.

**Schritt 5: Gerät koppeln**

Nachdem Sie die Firmware aktualisiert haben, öffnen Sie den Chrome-Browser, gehen Sie zum Editor und klicken Sie im Zahnrad-Menü auf „Gerät koppeln“. Siehe [WebUSB(/device/usb/webusb)](https://microbit.org/get-started/user-guide/web-usb/) für Anweisungen zum Koppeln.

Genießen Sie schnelle Downloads!
