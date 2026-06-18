## 1. Programmation sur MakeCode

Les instructions suivantes s'appliquent au système Windows mais peuvent également servir de référence si vous utilisez un autre système.

#### 1.1. Démarrage rapide

**Étape 1 Connecter au micro:bit**

Connectez la carte à l'ordinateur via un câble USB.

![Img](./media/A800.png)

Si la LED rouge à l'arrière de la carte est allumée, cela signifie que la carte est alimentée. Lorsque votre ordinateur communique avec la carte principale via le câble USB, la LED jaune clignote. Par exemple, elle clignote lorsque vous transférez un fichier “.hex”.

Ensuite, la carte principale Micro:bit apparaîtra sur votre ordinateur comme un lecteur nommé “MICROBIT”. Veuillez noter qu'il ne s'agit pas d'un disque USB ordinaire comme montré ci-dessous.

![Img](./media/A849.png)

**Étape 2 Écrire le programme heartbeat**

Accédez au lien : [version en ligne de Makecode](https://makecode.microbit.org/)

Cliquez sur “<span style="color: rgb(255, 76, 65);">Nouveau Projet</span>” et vous verrez “<span style="color: rgb(255, 76, 65);">Création d'un projet</span>”, remplissez avec “<span style="color: rgb(255, 76, 65);">heartbeat</span>” et cliquez sur “<span style="color: rgb(255, 76, 65);">Créer √</span>”.

<span style="color: rgb(255, 76, 65);">Ici, nous écrivons les programmes sur Google Chrome.</span>

![Img](./media/A021.png)

Écrivons un code micro:bit.

Vous pouvez glisser des blocs dans la zone d'édition puis exécuter votre programme dans le simulateur comme montré ci-dessous. Ici, nous montrons comment éditer le programme <span style="color: rgb(255, 76, 65);">heartbeat</span>.

Vidéo guide opérationnelle :

![Img](./media/A100.png)

**Étape 3 Télécharger les codes**

Généralement, pour l'application Windows 10 ([Obtenir l'application Windows 10](https://apps.microsoft.com/detail/9pjc7sv48lcx?hl=zh-CN&gl=CN#activetab=pivot:overviewtabdocx))(Cliquez), un simple clic sur “<span style="color: rgb(255, 76, 65);">Télécharger</span>” téléchargera directement le code sur la carte micro:bit sans étapes supplémentaires.

Pour les navigateurs, veuillez :

Cliquer sur “<span style="color: rgb(255, 76, 65);">Télécharger</span>” dans l'éditeur. Cela téléchargera un fichier “hex”, un format que la carte micro:bit peut lire. Ensuite, copiez-le sur votre carte micro:bit comme vous copieriez un fichier sur une clé USB. Sous Windows, vous pouvez aussi faire un clic droit sur le fichier “<span style="color: rgb(255, 76, 65);">.hex</span>” et sélectionner “**Envoyer vers → MICROBIT**” pour copier le fichier sur la carte micro:bit.

![Img](./media/A319.png)

![Img](./media/A449.png)

Ou, vous pouvez directement glisser le fichier “<span style="color: rgb(255, 76, 65);">.hex</span>” dans MICROBIT.

![Img](./media/A341.png)

![Img](./media/A345.png)

Pendant la copie du fichier “<span style="color: rgb(255, 76, 65);">.hex</span>” vers le Micro:bit, la LED jaune à l'arrière de la carte clignote. Lorsque la copie est terminée, la LED cesse de clignoter et reste allumée.

**Étape 4 Exécuter le programme**

Après que le programme est téléchargé sur le Micro:bit, vous pouvez l'alimenter via le câble USB ou une alimentation externe. Ensuite, la matrice LED 5 x 5 affiche un motif de battement de cœur.

![Img](./media/A425.png)

<span style="color: rgb(255, 76, 65);">**Attention :**</span> À chaque programmation, le pilote du Micro:bit s'éjecte automatiquement puis revient, donc les fichiers hex disparaissent. La carte n'a accès qu'aux fichiers hex mais ne les sauvegarde pas.

#### 1.2. MakeCode

Accédez à la [version en ligne Makecode Google Chrome](https://makecode.microbit.org/). Voici son interface principale.

![Img](./media/A637.png)

Il y a les blocs “**on start**” et “**forever**” dans la zone d'édition de code. <span style="color: rgb(255, 76, 65);">Après mise sous tension, le code dans “on start” s'exécute une seule fois, tandis que celui dans “forever” s'exécute en boucle.</span>

Cliquez sur la langue “**JS JavaScript**” :

![Img](./media/A754.png)

Changez-la en “**Python**” :

![Img](./media/A814.png)


#### 1.3. Introduction aux fonctions WebUSB

Comme mentionné précédemment, si votre ordinateur est sous Windows 10 et que vous avez téléchargé l'application MakeCode, vous pouvez rapidement télécharger les codes sur la carte via le bouton “<span style="color: rgb(255, 76, 65);">Télécharger</span>”. Nous utilisons le webUSB de **<span style="color: rgb(255, 76, 65);">Google Chrome</span>** pour accéder au périphérique matériel connecté par USB.

**Appairage des appareils :**

1\. Connectez la carte à l'ordinateur via un câble USB.

![Img](./media/A951.png)

2\. Cliquez sur “<span style="color: rgb(255, 76, 65);">Télécharger</span>” -> “<span style="color: rgb(255, 76, 65);">...</span>” , puis “<span style="color: rgb(255, 76, 65);">Connecter l'appareil</span>”.

![Img](./media/A028.png)

3\. “<span style="color: rgb(255, 76, 65);">Suivant</span>”.

![Img](./media/A046.png)

4\. “<span style="color: rgb(255, 76, 65);">Appairer</span>”.

![Img](./media/A104.png)

5\. Sélectionnez ensuite l'appareil correspondant et “<span style="color: rgb(255, 76, 65);">Connecter</span>”.

![Img](./media/A127.png)

6\. “<span style="color: rgb(255, 76, 65);">Terminé</span>”.

![Img](./media/A144.png)

**Télécharger le programme :**

Après la connexion, cliquez sur “<span style="color: rgb(255, 76, 65);">Télécharger</span>” et vous verrez que ![Img](./media/A212.png) devient ![Img](./media/A220.png). Le programme est téléchargé sur la carte micro:bit.

![Img](./media/A232.png)

Si aucun appareil n'apparaît pour la sélection, veuillez consulter [Dépannage des téléchargements avec WebUSB](https://makecode.microbit.org/device/usb/webusb/troubleshoot). Consultez [le guide utilisateur](https://microbit.org/guide/firmware/) pour savoir comment mettre à jour le firmware micro:bit.

#### 1.4. Bibliothèque d'extensions MakeCode

**3.4.1 Importer des extensions de bibliothèque**

Ouvrez Makecode pour entrer dans un projet donné, cliquez sur ![Img](./media/A806.png) pour choisir “**Extensions**”.

![Img](./media/A842.png)

Ou cliquez sur “**Extensions**” au-dessus de la section Avancé.

![Img](./media/A900.png)

Recherchez la bibliothèque que vous souhaitez.

![Img](./media/A909.png)

Nous fournissons les fichiers de code pour chaque projet contenant tout ce dont vous avez besoin pour exécuter un projet, vous pouvez donc les charger directement. Si vous souhaitez créer vous-même des blocs de code, n'oubliez pas d'ajouter les trois extensions suivantes.

<span style="color: rgb(0, 209, 0);">**Extension OLED :**</span>

1\. Cliquez sur “**Extensions**” pour ajouter des extensions de bibliothèque.

![Img](./media/A236.png)

2\. Recherchez “**OLED**” et cliquez sur ![Img](./media/A3257.png).

![Img](./media/A306.png)

Cliquez sur le premier **oled-ssd1306** et attendez qu'il soit ajouté.

![Img](./media/A3316.png)

3\. Ajout réussi :

![Img](./media/A335.png)

<span style="color: rgb(0, 209, 0);">**Extension capteur ultrasonique :**</span>

1\. Cliquez sur “**Extensions**” pour ajouter des extensions de bibliothèque.

![Img](./media/A236.png)

2\. Recherchez “**sonar**” et cliquez sur ![Img](./media/A3257.png) pour trouver et charger “sonar”.

![Img](./media/A506.png)

3\. Ajout réussi :

![Img](./media/A522.png)

<span style="color: rgb(0, 209, 0);">**Extension capteur DHT11 :**</span>

1\. Cliquez sur “**Extensions**” pour ajouter des extensions de bibliothèque.

![Img](./media/A236.png)

2\. Recherchez “**DHT11**” et cliquez sur ![Img](./media/A3257.png) pour trouver et charger “DHT11_DHT22”.

![Img](./media/A616.png)

3\. Ajout réussi :

![Img](./media/A645.png)

**3.4.2 Mettre à jour/Supprimer des extensions**

1\. Cliquez sur “**JavaScript**” pour passer au code texte.

![Img](./media/A724.png)

2\. Cliquez sur “**Explorateur**”.

![Img](./media/A749.png)

3\. Trouvez la bibliothèque “**OLED**” et cliquez sur ![Img](./media/A813.png) pour la supprimer.

![Img](./media/A824.png)

4\. “**Supprimer**”.

![Img](./media/A727.png)

Elle est supprimée.

#### 1.5. Comment importer des codes dans MakeCode

Prenons le projet “**heartbeat**” comme exemple pour montrer comment charger le code.

1\. Ouvrez la version Web de Makecode ou l'application Windows 10 Makecode, et cliquez sur “<span style="color: rgb(255, 76, 65);">Importer</span>”.

![Img](./media/A956.png)

2\. “<span style="color: rgb(255, 76, 65);">Importer un fichier...</span>”

![Img](./media/A042.png)

3\. “<span style="color: rgb(255, 76, 65);">Choisir un fichier</span>” pour importer le fichier que vous souhaitez charger.

![Img](./media/A06.png)

4\. Ici, nous chargeons “<span style="color: rgb(255, 76, 65);">heartbeat.hex</span>”.

![Img](./media/A28.png)

5\. “<span style="color: rgb(255, 76, 65);">Continuer √</span>”

![Img](./media/A149.png)

En plus de la méthode ci-dessus, vous pouvez également glisser le code test dans la zone d'édition de code, comme montré ci-dessous :

![Img](./media/A202.png)

Attendez le chargement.

![Img](./media/A217.png)
