### Projet 06 : Fête de la Musique

![Img](./media/A1317.png)

#### 1. Aperçu

Lorsque nous applaudissons, le microphone sur la carte capte les signaux sonores, et le haut-parleur joue une joyeuse chanson d'anniversaire tandis que la LED RGB émet une lumière éblouissante.

#### 2. Composants

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| carte micro:bit *1 | carte d'extension micro:bit type T *1 | câble micro USB *1 |
| ![Img](./media/A500.png)| ![Img](./media/A944.png) | ![Img](./media/A950.png) |
| LED rouge *1 | résistance 220Ω *3 | fil de connexion *2 |
| ![Img](./media/A017.png) | ![Img](./media/A024.png) | ![Img](./media/A621.png)  |
| breadboard *1 | support de pile *1 <br> (<span style="color: rgb(255, 76, 65);">piles AA auto-fournies *2</span>)| carte RGB *1 |

#### 3. Connaissances sur les composants

**Microphone**

Un microphone numérique de haute qualité est intégré sur la face avant de la carte micro:bit V2 pour détecter les signaux sonores et audio. La puce qui contrôle et traite le microphone se trouve à l'arrière.

![Img](./media/A1317.png)

Le microphone est situé dans un petit trou rond à l'avant de la carte, ce qui facilite la capture des signaux sonores environnants. Il suffit de placer la carte micro:bit face vers le haut lors de l'utilisation. À côté du trou se trouve un indicateur LED du microphone. Lorsque le micro:bit mesure les niveaux sonores, l'indicateur s'allume.

![Img](./media/A116.png)

**LED RGB**

![Img](./media/A2127.png)

La LED RGB est représentée par l'intersection de trois couleurs primaires (RGB) : rouge, vert et bleu. La plupart des couleurs peuvent être synthétisées par le RGB en différentes proportions. Les LED rouge, verte et bleue sont encapsulées dans un boîtier en plastique transparent pour émettre des couleurs de lumière en modifiant la tension d'entrée des broches R, G et B.

![Img](./media/A137.png)

**Théorie trichromatique :**

![Img](./media/A150.png)

La LED RGB peut être divisée en deux types : anode commune et cathode commune :

Dans une LED RGB à cathode commune, les trois LED partagent une connexion négative (cathode) ;

Dans une LED RGB à anode commune, les trois LED partagent une connexion positive (anode).

![Img](./media/A209.png)

<span style="color: rgb(255, 76, 65);">**Remarque : Ici, nous fournissons une LED RGB à cathode commune.**</span>

**Broches de la LED RGB :**

La LED RGB possède 4 broches : GND (la plus longue), R (rouge), G (vert) et B (bleu). Placez la LED RGB comme indiqué ci-dessous, les broches de gauche à droite sont rouge, GND, vert et bleu.

![Img](./media/A239.png)

#### 4. Schéma de câblage

![Img](./media/A308.png)

![Img](./media/A325.png)

#### 5. Flux du code

![Img](./media/A343.png)

#### 6. Code de test

Le fichier de code est fourni dans le dossier Projet 06 : Fête de la Musique, fichier Project-06-Music-Party.hex.

![Img](./media/A423.png)

**Charger les blocs de code :**

![Img](./media/A445.png)

#### 7. Résultat du test

Après avoir téléchargé le code sur la carte, lorsque nous applaudissons, le microphone sur la carte capte les signaux sonores, et le haut-parleur joue une joyeuse chanson d'anniversaire tandis que la LED RGB émet une lumière éblouissante. La fête de la musique n'est-elle pas dans une ambiance heureuse et joyeuse ?

<span style="color: rgb(255, 76, 65);">**ATTENTION :** Si le câblage est correct mais que vous ne voyez pas les résultats, appuyez sur le bouton de réinitialisation à l'arrière de la carte.</span>

![Img](./media/A757.gif)
