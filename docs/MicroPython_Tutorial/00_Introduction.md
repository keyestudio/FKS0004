## 1. À propos du logiciel Mu

### 1.1. Installer MU

Cliquez pour visiter le [site officiel du logiciel Mu](https://codewith.mu/).

Mu est un éditeur de code Python pour les programmeurs débutants, comme les enseignants et les étudiants. Nous pouvons l’obtenir via l’installateur officiel pour Windows, Mac OSX ou Linux (Mu ne supporte plus Windows 32 bits). La version recommandée est Mu 1.2.0.

**Étape 1 - Assurez-vous de votre système d’exploitation puis téléchargez l’installateur Mu**

Commencez par vérifier le système d’exploitation de votre ordinateur (Windows ou Mac OSX). Ouvrez « **Ce PC** » pour voir « **Propriétés** ».

![Img](./media/A225.png)

Vérifiez le type de système : 64 bits ou 32 bits.

![Img](./media/A253.png)

[Download MU](https://codewith.mu/en/download). Téléchargez la version correspondant à votre système d’exploitation.

![Img](./media/A348.png)

<span style="color: rgb(255, 76, 65);">Ici, nous prenons le système Windows comme exemple, ce qui peut servir de référence pour Mac OSX et Linux.</span>

![Img](./media/A422.png)

**Étape 2 - Exécutez l’installateur**

Double-cliquez sur l’installateur (probablement dans votre dossier Téléchargements) pour le lancer.

![Img](./media/A440.png)

Nous avons décrit les étapes supplémentaires nécessaires pour aider Windows à installer Mu sous Windows 10. Les autres versions seront similaires.

[Installateur Mu pour MacOS](https://codewith.mu/en/howto/1.1/install_macos).

[Installateur Mu pour Linux](https://codewith.mu/en/howto/1.2/install_linux).

Pour Windows 10, Defender affichera un message d’avertissement. Vous devez cliquer sur le lien « **Plus d’infos** ».

![Img](./media/A615.png)

Le message changera pour vous donner plus d’informations sur l’installateur et affichera un bouton « **Exécuter quand même** ». Cliquez sur « **Exécuter quand même** ».

![Img](./media/A626.png)

**Étape 3 - Contrat de licence**

Lisez la licence, cochez la case et cliquez sur « **Installer** ».

![Img](./media/A1716.png)

**Étape 4 - Installation**

Allez vous faire un café pendant que Mu s’installe sur votre ordinateur.

![Img](./media/A1740.png)

**Étape 5 - Terminé**

L’installation est terminée avec succès, cliquez sur « **Terminer** » pour fermer l’installateur.

![Img](./media/A817.png)

**Étape 6 - Démarrer Mu**

Vous pouvez démarrer Mu en cliquant sur l’icône dans le menu Démarrer ou en tapant « Mu » dans la barre de recherche (les deux sont surlignés ci-dessous). Au premier démarrage, cela peut prendre un certain temps.

![Img](./media/A852.png)

Voici à quoi cela ressemble :

![Img](./media/A909.png)

### 1.2. Utilisation des modes & barre de menu

Réglez le « <span style="color: rgb(255, 76, 65);">Mode</span> » sur BBC micro:bit.

Dans le menu, cliquez sur « **Mode** » pour le régler sur « **BBC micro：bit** ». Le mode micro:bit comprend comment interagir et se connecter à un micro:bit.

![Img](./media/A022.png)

Cliquez pour [Commencer avec Mu](https://codewith.mu/en/tutorials/1.1/start).

Pour plus de tutoriels sur l’utilisation de Mu, veuillez visiter : https://codewith.mu/en/tutorials/

### 1.3. Programmer sur Mu

Ici, nous chargeons le fichier « <span style="color: rgb(255, 76, 65);">heartbeat\.py</span> » dans Mu. Trouvez-le dans le dossier « <span style="color: rgb(255, 76, 65);">Heart beat</span> » que nous avons fourni.

![Img](./media/A200.png)

**Méthode un :**

Ouvrez Mu et cliquez sur « <span style="color: rgb(255, 76, 65);">Load</span> » pour choisir le chemin où vous avez téléchargé le code.

![Img](./media/A341.png)

![Img](./media/A345.png)

Chargé avec succès, comme montré ci-dessous :

![Img](./media/A354.png)

**Méthode deux :**

Cliquez sur « new » ![Img](./media/A503.png) pour créer un nouveau programme et glissez « heartbeat\.py » dedans :

![Img](./media/A521.png)

Chargé avec succès, comme montré ci-dessous :

![Img](./media/A533.png)

<span style="color: rgb(255, 76, 65);">Il en va de même pour l’ajout d’autres codes.</span>

### 1.4. Télécharger le code sur Micro:bit

Connectez la carte à l’ordinateur via un câble USB.

![Img](./media/A252.png)

Cliquez sur « <span style="color: rgb(255, 76, 65);">**Flash**</span> » pour télécharger le code sur la carte micro:bit.

![Img](./media/A3728.png)

Après cela, <span style="color: rgb(255, 76, 65);">**alimentez via le câble micro USB ou une alimentation externe (mettez l’interrupteur DIP sur ON)**</span>. Vous verrez la matrice LED 5×5 embarquée afficher en boucle ![Img](./media/A903.png) puis ![Img](./media/A910.png).

<span style="color: rgb(255, 76, 65);">**Notez que s’il y a une erreur dans votre code, il peut quand même être téléchargé mais ne fonctionnera pas correctement.**</span>

<span style="color: rgb(0, 209, 0);">Par exemple, la fonction sleep() est écrite sleeps() dans le code. Cliquez sur « **Flash** » pour charger le code sur micro:bit. Cependant, la matrice LED 5×5 affiche des icônes désordonnées.</span>

![Img](./media/A4003.png)

Dans ce cas, cliquez sur « **REPL** » et appuyez sur le bouton reset à l’arrière de la carte. Le message d’erreur s’affichera dans l’interface REPL, comme montré ci-dessous :

![Img](./media/A029.png)

![Img](./media/A033.png)

Cliquez à nouveau sur « **REPL** » pour fermer REPL. Puis cliquez sur « <span style="color: rgb(255, 76, 65);">**Flash**</span> ».

Pour s’assurer que le code est correct, cliquez sur « <span style="color: rgb(255, 76, 65);">**Check**</span> » après avoir terminé, et Mu indiquera les erreurs dans le code.

![Img](./media/A119.png)

Modifiez le code selon le message d’erreur, puis cliquez à nouveau sur « <span style="color: rgb(255, 76, 65);">**Check**</span> ». Mu ne montre plus d’erreur.

![Img](./media/A134.png)

Voir [plus de tutoriels expliquant des aspects spécifiques de Mu](https://codewith.mu/en/tutorials/).

## 2. Comment Mu importe une bibliothèque sur Micro:bit

<span style="color: rgb(255, 76, 65);">Avant d’importer des bibliothèques, nous devons télécharger un code .py (un code vide convient aussi) sur la carte micro:bit. Ici, nous prenons un code vide comme exemple.</span>

Connectez la carte à l’ordinateur via un câble USB. Ouvrez Mu et cliquez sur « Flash » pour télécharger le code .py (code vide) sur la carte.

![Img](./media/A252.png)

Dans ce tutoriel, les modules OLED et DHT11 sont utilisés. Par conséquent, les fichiers de bibliothèque « <span style="color: rgb(255, 76, 65);">**oled_ssd1306\.py**</span> » et « <span style="color: rgb(255, 76, 65);">**DHT11\.py**</span> » doivent être importés dans la carte micro:bit.

Le répertoire par défaut où Mu sauvegarde les fichiers est « mu_code » dans le répertoire racine du dossier utilisateur.

Lien de référence : [https://codewith.mu/en/tutorials/1.0/files](https://codewith.mu/en/tutorials/1.0/files)

**Instructions pour importer les bibliothèques :**

1\. Cherchez le dossier « <span style="color: rgb(255, 76, 65);">mu_code</span> » sur le disque (C:).

![Img](./media/A543.png)

![Img](./media/A550.png)

2\. Ouvrez « <span style="color: rgb(255, 76, 65);">mu_code</span> ».

![Img](./media/A628.png)

3\. Copiez et collez les fichiers de bibliothèque « <span style="color: rgb(255, 76, 65);">**oled_ssd1306\.py**</span> » et « <span style="color: rgb(255, 76, 65);">**DHT11\.py**</span> » dans « <span style="color: rgb(255, 76, 65);">**Libraries**</span> ».

![Img](./media/A4716.png)

4\. Comme montré ci-dessous :

![Img](./media/A735.png)

5\. Ouvrez Mu et cliquez sur « <span style="color: rgb(255, 76, 65);">**Files**</span> ». Ici, nous glissons la bibliothèque « <span style="color: rgb(255, 76, 65);">**DHT11\.py**</span> » dans micro:bit.

![Img](./media/A816.png)

![Img](./media/A820.png)

6\. Après avoir importé « <span style="color: rgb(255, 76, 65);">**DHT11\.py**</span> », vous la verrez dans la boîte à gauche.

![Img](./media/A841.png)

7\. Faisons la même chose pour « <span style="color: rgb(255, 76, 65);">**oled_ssd1306\.py**</span> ».

![Img](./media/A916.png)

![Img](./media/A4920.png)

<span style="color: rgb(255, 76, 65);">**Notez que lorsque vous téléchargez d’autres fichiers sur le micro:bit, ils écrasent le contenu original, donc vous devez les réimporter pour la prochaine utilisation.**</span>
