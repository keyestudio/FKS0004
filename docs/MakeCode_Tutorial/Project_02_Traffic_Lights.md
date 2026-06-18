### Projet 02 : Feux de circulation

#### 1. Aperçu

Dans ce projet, nous utilisons trois LED (rouge, jaune et verte), un haut-parleur sur la carte micro:bit et une matrice LED 5x5 pour réaliser un modèle de feux de circulation.

#### 2. Composants

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| carte micro:bit *1 | carte d'extension de type T pour micro:bit *1 | câble micro USB *1 |
| ![Img](./media/A937.png)| ![Img](./media/A5652.png) | ![Img](./media/A658.png) |
| LED rouge *1 | LED jaune *1 | LED verte *1 |
| ![Img](./media/A944.png) | ![Img](./media/A950.png) |![Img](./media/A017.png) |
| résistance 220Ω *3 | fils de connexion | breadboard *1 |
|  ![Img](./media/A024.png) |  ![Img](./media/A020.png) |  |
| support de pile *1 <br> (<span style="color: rgb(255, 76, 65);">piles AA auto-fournies *2</span>) | carte de feux de circulation *1 | |

#### 3. Connaissances sur les composants

**Haut-parleur**

![Img](./media/A833.png)

Le micro:bit est équipé d’un haut-parleur, ce qui facilite la production de sons dans votre projet.

#### 4. Schéma de câblage

![Img](./media/A908.png)

<span style="color: rgb(255, 76, 65);">**Remarque :** la carte micro:bit doit être insérée dans la carte d'extension de type T comme indiqué ci-dessous. La matrice LED de la carte micro:bit doit être du même côté que le logo de la carte d'extension.</span>

![Img](./media/A940.png)

#### 5. Flux du code

![Img](./media/A5956.png)

#### 6. Code de test

Le fichier de code est fourni dans le dossier Projet 02 : Feux de circulation, fichier Project-02-Traffic-Lights.hex.

![Img](./media/A0017.png)

**Charger les blocs de code :**

![Img](./media/A605.png)

#### 7. Résultat du test

Pour l’application Windows 10, cliquez sur “<span style="color: rgb(255, 76, 65);">Télécharger</span>”. Pour les navigateurs, envoyez le fichier “<span style="color: rgb(255, 76, 65);">.hex</span>” téléchargé vers la carte micro:bit.

Après avoir téléchargé le code sur la carte, la LED verte s’allume et la matrice LED 5×5 compte à rebours pendant 6 secondes. Après l’extinction de la LED verte, la LED jaune clignote et la matrice compte à rebours 3 s avec le haut-parleur qui sonne. Enfin, la LED rouge s’allume avec un compte à rebours de 6 s. Ces actions se répètent.

<span style="color: rgb(255, 76, 65);">**ATTENTION :** Si le câblage est correct mais que vous ne voyez pas les résultats, appuyez sur le bouton de réinitialisation à l’arrière de la carte.</span>

![Img](./media/A459.gif)

<span style="color: rgb(255, 76, 65);">**Lors de l’alimentation via une source externe, mettez l’interrupteur DIP sur ON.**</span>

![Img](./media/A904.png)
