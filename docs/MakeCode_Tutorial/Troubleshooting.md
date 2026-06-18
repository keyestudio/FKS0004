## 3. Problemen oplossen

#### MAINTENANCE: Code kan niet naar Micro:bit worden gedownload

**1. Probleem**

Onlangs ervaren veel gebruikers het probleem dat het Micro:bit-bord niet reageert bij het downloaden van code.

Als je de juiste werkwijze volgt, is het mogelijk dat je per ongeluk de resetknop hebt ingedrukt en in de MAINTENANCEsmodus bent gekomen, of dat de firmware verloren is gegaan door een verkeerde handeling.

Sluit het Micro:bit-bord aan, de “<span style="color: rgb(255, 76, 65);">MAINTENANCE</span>” schijf verschijnt, wat betekent dat het programma niet kan worden gedownload.

![Img](./media/A158.png)

**2. Oplossingen**

(1) Download het <span style="color: rgb(255, 76, 65);">.hex</span>-bestand van deze pagina naar je computer.

Download [de nieuwste micro:bit firmware-0255](https://www.microbit.org/get-started/user-guide/firmware/). Als je niet van deze website wilt downloaden, bieden wij het ook aan in onze tutorial.

(2) Nadat de nieuwste firmware is gedownload, sleep je Firmware voor V2.20_V2.21 naar de “<span style="color: rgb(255, 76, 65);">MAINTENANCE</span>” schijf om de Micro:bit terug te zetten naar de normale modus.

<span style="color: rgb(255, 76, 65);">We installeren verschillende firmwares afhankelijk van het micro:bit bordmodel. Hier is het Firmware voor V2.20_V2.21.</span>

![Img](./media/A326.png)

![Img](./media/A331.png)

**3. Voorkom dat je in “MAINTENANCE” komt**

(1) Zorg ervoor dat de Reset-knop niet wordt ingedrukt bij het aansluiten van het bord met de USB-kabel.

![Img](./media/A228.png)

(2) Trek de kabel niet plotseling uit tijdens het downloaden van het micro:bit-programma, anders gaat de firmware verloren en komt de micro:bit in de “MAINTENANCE” modus.

(3) Verkeerd aansluiten tijdens het experiment kan ook kortsluiting of firmwareverlies veroorzaken.

#### Problemen oplossen bij downloads met WebUSB

Klik: [Problemen oplossen bij downloads met WebUSB](https://makecode.microbit.org/device/usb/webusb/troubleshoot)

Problemen met het koppelen van je micro:bit met WebUSB? Laten we proberen te achterhalen waarom!

**Stap 1: Controleer je kabel**

Zorg ervoor dat je micro:bit met een micro USB-kabel op je computer is aangesloten. Bijvoorbeeld, in Windows Verkenner zou je een **MICROBIT** schijf moeten zien verschijnen wanneer deze is aangesloten.

![Img](./media/A321.png)

Als je de MICROBIT-schijf ziet, ga dan naar stap 2. Als je de schijf niet ziet:

(1) Controleer of de USB-kabel werkt.

Werkt de kabel op een andere computer? Zo niet, gebruik dan een andere kabel. Sommige kabels bieden alleen stroom en kunnen geen data overdragen.

(2) Probeer een andere USB-poort op je computer.

Is de kabel goed maar zie je nog steeds de MICROBIT-schijf niet? Hmm, dan is er mogelijk een probleem met je micro:bit.

Probeer de extra stappen beschreven op de [foutopsporingspagina op microbit.org](https://support.microbit.org/support/solutions/articles/19000024000-fault-finding-with-a-micro-bit). Helpt dit niet, dan kun je een [supportticket aanmaken](https://support.microbit.org/support/tickets/new) om de Micro:bit Foundation op de hoogte te stellen van het probleem. Sla de resterende stappen over.

**Stap 2: Controleer je firmwareversie**

Als je downloads nog steeds niet werken, is het mogelijk dat de firmwareversie op de micro:bit een update nodig heeft. Laten we het controleren:

1. Ga naar de **MICROBIT** schijf;

2. Open het <span style="color: rgb(255, 76, 65);">DETAILS.TXT</span> bestand;

![Img](./media/A0452.png)

3. Zoek het firmwareversienummer; Zoek een regel in het bestand die het versienummer vermeldt. Het zou moeten zeggen Version:

![Img](./media/A501.png)

Als de versie 0234, 0241, 0243 is, MOET je de firmware op je micro:bit bijwerken. Ga naar Stap 3 en volg de upgrade-instructies.

Als de versie 0249, 0250 of hoger is, heb je de juiste firmware en ga je naar stap 4.

**Stap 3: Firmware upgraden**

(1) Zet je micro:bit in MAINTENANCE-modus.

Koppel de USB-kabel los van de micro:bit en sluit deze opnieuw aan terwijl je de resetknop ingedrukt houdt. Zodra je de kabel aansluit, kun je de resetknop loslaten.

Je zou nu een MAINTENANCE-schijf moeten zien in plaats van de MICROBIT-schijf zoals voorheen. Ook blijft een gele LED naast de resetknop branden.

![maintenance](./media/maintenance.gif)

(2) Download het [firmware .hex-bestand](https://microbit.org/guide/firmware/).

<span style="color: rgb(255, 76, 65);">We installeren verschillende firmwares afhankelijk van het micro:bit bordmodel. Hier is het Firmware voor V2.20_V2.21.</span>

![Img](./media/A0629.png)

(3) Sleep dat bestand naar de **MAINTENANCE** schijf.

(4) Let op de knipperende LED.

De gele LED knippert terwijl het HEX-bestand wordt gekopieerd. Wanneer de kopie klaar is, gaat de LED uit en reset de micro:bit. De MAINTENANCE-schijf verandert nu terug naar MICROBIT.

(5) Upgrade voltooid.

De upgrade is voltooid! Je kunt het <span style="color: rgb(255, 76, 65);">DETAILS.TXT</span> bestand openen om te controleren of de firmwareversie is veranderd naar de versie van het HEX-bestand dat je hebt gekopieerd.

Wil je meer weten over het aansluiten van het bord, de MAINTENANCE-modus en het upgraden van de firmware, lees dan de [Firmware-gids](https://microbit.org/guide/firmware/).

**Stap 4: Controleer je browserversie**

WebUSB is een vrij nieuwe functie en kan vereisen dat je je browser bijwerkt. Controleer of je browserversie overeenkomt met een van de onderstaande: Browser versies voor Android, Chrome OS, Linux, macOS en Chrome 65+ voor Windows 10.

**Stap 5: Koppel het apparaat**

Zodra je de firmware hebt bijgewerkt, open je de Chrome-browser, ga je naar de editor en klik je op Koppel apparaat in het tandwielmenu. Zie [WebUSB(/device/usb/webusb)](https://microbit.org/get-started/user-guide/web-usb/) voor koppelingsinstructies.

Geniet van snelle downloads!
