## 3. Dépannage

#### MAINTENANCE : Le code ne se télécharge pas sur Micro:bit

**1. Problème**

Récemment, de nombreux utilisateurs rencontrent le problème que la carte Micro:bit ne répond pas lors du téléchargement du code.

Si votre méthode d’opération est correcte, il se peut que vous ayez accidentellement appuyé sur le bouton de réinitialisation et entré en mode Maintenance ou que le firmware ait été perdu à cause d’une mauvaise manipulation.

Branchez la carte Micro:bit, le lecteur « <span style="color: rgb(255, 76, 65);">MAINTENANCE</span> » apparaît, ce qui signifie que le programme ne peut pas être téléchargé.

![Img](./media/A158.png)

**2. Solutions**

(1) Téléchargez le fichier <span style="color: rgb(255, 76, 65);">.hex</span> depuis cette page sur votre ordinateur.

Téléchargez [le dernier firmware micro:bit-0255](https://www.microbit.org/get-started/user-guide/firmware/). Si vous ne souhaitez pas le télécharger depuis ce site, nous le fournissons également dans notre tutoriel.

(2) Une fois le dernier firmware téléchargé, glissez Firmware for V2.20_V2.21 dans le lecteur « <span style="color: rgb(255, 76, 65);">MAINTENANCE</span> » pour remettre le Micro:bit en mode normal.

<span style="color: rgb(255, 76, 65);">Nous installons différents firmwares selon les modèles de carte micro:bit. Ici, il s’agit du Firmware pour V2.20_V2.21.</span>

![Img](./media/A326.png)

![Img](./media/A331.png)

**3. Éviter d’entrer en “MAINTENANCE”**

(1) Assurez-vous que le bouton Reset n’est pas pressé lors du branchement de la carte via le câble USB.

![Img](./media/A228.png)

(2) Ne débranchez pas soudainement le câble pendant le téléchargement du programme micro:bit, sinon le firmware sera perdu et le micro:bit entrera en mode « MAINTENANCE ».

(3) Dans l’expérience, un mauvais câblage peut aussi provoquer un court-circuit ou la perte du firmware.

#### Dépannage des téléchargements avec WebUSB

Cliquez : [Dépannage des téléchargements avec WebUSB](https://makecode.microbit.org/device/usb/webusb/troubleshoot)

Vous avez des problèmes pour appairer votre micro:bit avec WebUSB ? Essayons de comprendre pourquoi !

**Étape 1 : Vérifiez votre câble**

Assurez-vous que votre micro:bit est connecté à votre ordinateur avec un câble micro USB. Par exemple, dans l’Explorateur Windows, vous devriez voir apparaître un lecteur **MICROBIT** lorsqu’il est connecté.

![Img](./media/A321.png)

Si vous voyez le lecteur MICROBIT, passez à l’étape 2. Sinon :

(1) Assurez-vous que le câble USB fonctionne.

Le câble fonctionne-t-il sur un autre ordinateur ? Sinon, trouvez un autre câble à utiliser. Certains câbles ne fournissent qu’une connexion d’alimentation et ne transfèrent pas réellement de données.

(2) Essayez un autre port USB sur votre ordinateur.

Le câble est bon mais vous ne voyez toujours pas le lecteur MICROBIT ? Hmm, vous pourriez avoir un problème avec votre micro:bit.

Essayez les étapes supplémentaires décrites sur la [page de dépannage sur microbit.org](https://support.microbit.org/support/solutions/articles/19000024000-fault-finding-with-a-micro-bit). Si cela ne vous aide pas, vous pouvez [créer un ticket de support](https://support.microbit.org/support/tickets/new) pour notifier la Micro:bit Foundation du problème. Passez les étapes restantes de dépannage.

**Étape 2 : Vérifiez la version de votre firmware**

Si vos téléchargements ne fonctionnent toujours pas, il est possible que la version du firmware sur le micro:bit doive être mise à jour. Vérifions :

1. Allez dans le lecteur **MICROBIT** ;

2. Ouvrez le fichier <span style="color: rgb(255, 76, 65);">DETAILS.TXT</span> ;

![Img](./media/A0452.png)

3. Trouvez le numéro de version du firmware ; Cherchez une ligne dans le fichier qui indique le numéro de version. Elle doit indiquer Version :

![Img](./media/A501.png)

Si la version est 0234, 0241, 0243, vous DEVEZ mettre à jour le firmware de votre micro:bit. Passez à l’étape 3 et suivez les instructions de mise à jour.

Si la version est 0249, 0250 ou supérieure, vous avez le bon firmware, passez à l’étape 4.

**Étape 3 : Mettre à jour le firmware**

(1) Mettez votre micro:bit en mode MAINTENANCE.

Pour ce faire, débranchez le câble USB du micro:bit puis reconnectez-le tout en maintenant le bouton reset enfoncé. Une fois le câble inséré, vous pouvez relâcher le bouton reset.

Vous devriez maintenant voir un lecteur MAINTENANCE au lieu du lecteur MICROBIT comme avant. De plus, une LED jaune restera allumée à côté du bouton reset.

![maintenance](./media/maintenance.gif)

(2) Téléchargez le [fichier firmware .hex](https://microbit.org/guide/firmware/).

<span style="color: rgb(255, 76, 65);">Nous installons différents firmwares selon les modèles de carte micro:bit. Ici, il s’agit du Firmware pour V2.20_V2.21.</span>

![Img](./media/A0629.png)

(3) Glissez et déposez ce fichier sur le lecteur **MAINTENANCE**.

(4) Surveillez la LED clignotante.

La LED jaune clignotera pendant la copie du fichier HEX. Lorsque la copie est terminée, la LED s’éteindra et le micro:bit se réinitialisera. Le lecteur MAINTENANCE redevient MICROBIT.

(5) Mise à jour terminée.

La mise à jour est terminée ! Vous pouvez ouvrir le fichier <span style="color: rgb(255, 76, 65);">DETAILS.TXT</span> pour vérifier que la version du firmware a changé et correspond à la version du fichier HEX que vous avez copié.

Si vous souhaitez en savoir plus sur la connexion de la carte, le mode MAINTENANCE et la mise à jour du firmware, lisez le [guide Firmware](https://microbit.org/guide/firmware/).

**Étape 4 : Vérifiez la version de votre navigateur**

WebUSB est une fonctionnalité assez récente et peut nécessiter une mise à jour de votre navigateur. Vérifiez que la version de votre navigateur correspond à l’une de celles ci-dessous : versions de navigateur pour Android, Chrome OS, Linux, macOS, et Chrome 65+ pour Windows 10.

**Étape 5 : Appairer l’appareil**

Une fois que vous avez mis à jour le firmware, ouvrez le navigateur Chrome, allez dans l’éditeur et cliquez sur Appairer l’appareil dans le menu en forme de roue dentée. Voir [WebUSB(/device/usb/webusb)](https://microbit.org/get-started/user-guide/web-usb/) pour les instructions d’appairage.

Profitez de téléchargements rapides !
