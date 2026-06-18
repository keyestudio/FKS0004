### Projekt 07: Umweltüberwachung

#### 1. Übersicht

Auf dem OLED zeigt das intelligente Umweltüberwachungssystem die von dem DHT11-Sensor erfassten Temperatur- und Feuchtigkeitswerte in Echtzeit sowie den Helligkeitswert des Umgebungslichts, der vom eingebauten Lichtsensor erkannt wird.

#### 2. Komponenten

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit Board *1 | micro:bit T-Typ Erweiterungsboard *1 | micro USB Kabel *1 |
| ![Img](./media/A2637.png)| ![Img](./media/A406.png)| ![Img](./media/A415.png) |
| XHT11 Temperatur- und Feuchtigkeitssensor *1 | OLED Modul *1 | DuPont Kabel |
|![Img](./media/A017.png) | ![Img](./media/A950.png) | ![Img](./media/A024.png) |
| Steckbrett *1 | Jumper Kabel | Batteriefach *1 <br> (<span style="color: rgb(255, 76, 65);">selbst mitgebrachte AA Batterien *2</span>)|
|![Img](./media/A0715.png) |![Img](./media/A557.png)  | |
| Wolkenkarte *1 | OLED Karte *1 | |

#### 3. Komponentenwissen

**XHT11 Temperatur- und Feuchtigkeitssensor**

![Img](./media/A2637.png)

Der XHT11 Temperatur- und Feuchtigkeitssensor ist ein kombinierter Sensor mit kalibrierter digitaler Signalausgabe, der die Luftfeuchtigkeit und Temperatur messen kann.

**Genauigkeit**: Feuchtigkeit ±5%RH, Temperatur ±2℃

**Messbereich**: Feuchtigkeit 5%RH ~ 95%RH, Temperatur -25℃ ~ +60℃

Der Sensor verwendet spezielle digitale Modulerfassung und Temperatur- und Feuchtigkeitsmesstechnik, um eine extrem hohe Zuverlässigkeit und ausgezeichnete Langzeitstabilität zu gewährleisten. Er beinhaltet ein resistives Feuchtigkeitssensorelement und ein NTC-Temperatursensorelement, was ihn sehr geeignet macht für Messungen mit relativ niedriger Genauigkeit und Echtzeitanforderungen.

**XHT11 Kommunikationsmodus:**

Es wird eine Ein-Draht-Kommunikation verwendet. Das bedeutet, dass es nur eine Datenleitung für Datenaustausch und Steuerung im System gibt.

- Definition der übertragenen Datenbits über den Ein-Draht-Bus:

Ein-Draht-Datenformat: 40 Bits werden auf einmal übertragen, wobei das höchstwertige Bit zuerst kommt.

8bit Feuchtigkeitsganzzahl + 8bit Feuchtigkeitsdezimal + 8bit Temperaturganzzahl + 8bit Temperaturdezimal + 8bit Paritätsbit (Der Dezimalteil der Feuchtigkeit ist 0)

- Definition des Paritätsbits

8bit Feuchtigkeitsganzzahl + 8bit Feuchtigkeitsdezimal + 8bit Temperaturganzzahl + 8bit Temperaturdezimal. 8bit Paritätsbit = die letzten 8 Bits des erhaltenen Ergebnisses

- Datenzeitachse:

Nachdem der Benutzerhost (MCU) ein Startsignal sendet, wechselt der XHT11 vom Niedrigstrommodus in den Hochgeschwindigkeitsmodus. Nach dem Startsignal sendet der XHT11 ein Antwortsignal und 40bit Daten und löst eine Signalaufnahme aus.

- Die Signalübertragung ist in der Abbildung dargestellt:

![Img](./media/A229.png)

 **Parameter**

- Betriebsspannung: DC 3,3V bis 5V

- Betriebsstrom: 2,1mA

- Maximale Leistung: 0,0105W

- Temperaturbereich: -25℃ ~ +60℃ (± 2℃)

- Feuchtigkeitsbereich: 5%RH ~ 95%RH (Genauigkeit ±5%RH bei ca. 25 °C)

**Microbit Lichtsensor**

![Img](./media/A0335.png)

Ein Lichtsensor ist ein Eingabegerät, das die Helligkeit des Umgebungslichts misst. Das micro:bit Board enthält keinen eingebauten Lichtsensor. Es erkennt und misst die Umgebungshelligkeit durch eine LED-Matrix, die die Lichtintensität wiederholt in einen Werteingang umwandelt, und dann wird die Spannungsabfallzeit abgetastet. Auf diese Weise ist <span style="color: rgb(255, 76, 65);">der erkannte Helligkeitswert ein relativer Wert</span>.

#### 4. Schaltplan

![Img](./media/A409.png)

<span style="color: rgb(255, 76, 65);">Beim Einsatz des OLED-Displays müssen wir eine externe Stromversorgung anschließen und den DIP-Schalter auf ON stellen.</span>

![Img](./media/A904.png)

![Img](./media/A554.png)

#### 5. Programmablauf

![Img](./media/A638.png)


#### 6. Testcode

Die Code-Datei befindet sich im Ordner Projekt 07：Umweltüberwachung, Datei Project-07-Environment-Monitoring.hex.

![Img](./media/A656.png)

**Codeblöcke laden:**

![Img](./media/A715.png)

#### 7. Testergebnis

Nach dem Herunterladen des Codes auf das Board zeigt das OLED die Temperatur- und Feuchtigkeitswerte sowie den Helligkeitswert des Lichts in Echtzeit an.

<span style="color: rgb(255, 76, 65);">**ACHTUNG:** Wenn die Verkabelung korrekt ist, Sie aber keine Ergebnisse sehen, drücken Sie die Reset-Taste auf der Rückseite des Boards.</span>

![Img](./media/A838.gif)
