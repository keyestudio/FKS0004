### Projet 05 : Cadran de voiture

#### 1. Aperçu

Dans ce projet, nous combinons un potentiomètre réglable, un servo et une belle carte de cadran pour réaliser un modèle simple de cadran de voiture.

#### 2. Composants

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| carte micro:bit *1 | carte d'extension micro:bit type T *1 | câble micro USB *1 |
| ![Img](./media/A350.png)| ![Img](./media/A309.png)| ![Img](./media/A950.png) |
| potentiomètre *1 | servo *1 | fils de connexion |
|![Img](./media/A017.png)  | ![Img](./media/A024.png) |![Img](./media/A233.png) |
| breadboard *1 | support de piles *1 <br> (<span style="color: rgb(255, 76, 65);">piles AA auto-fournies *2</span>)| carte de potentiomètre *1 |
|![Img](./media/A1326.png) |  |  |
| carte de cadran de voiture *1| |  |

#### 3. Connaissances sur les composants

**potentiomètre**

![Img](./media/A350.png)

Un potentiomètre est également un élément résistif à trois contacts, dont la valeur de résistance peut être ajustée selon une certaine régularité.

Ils existent sous toutes les formes, tailles et valeurs, mais ont tous en commun les points suivants :

① Trois bornes (ou points de connexion).

② Un bouton ou curseur mobile qui peut changer la résistance entre la borne intermédiaire et n'importe quelle borne externe.

③ Lorsque le bouton est déplacé, la résistance entre la borne intermédiaire et n'importe quelle borne externe varie de 0Ω à sa valeur maximale.

Le symbole de circuit du potentiomètre :

![Img](./media/A654.png)

(1)\. En tant que diviseur de tension

Le potentiomètre est une résistance réglable en continu. Lorsque vous faites tourner son curseur, le contact mobile glisse sur la résistance. À ce moment, une tension peut être sortie en fonction de la tension appliquée au potentiomètre et de l'angle ou de la course de rotation du curseur mobile.

(2)\. En tant que résistance variable

Lorsque le potentiomètre est utilisé comme résistance variable, connectez sa borne intermédiaire à l'une des deux bornes supplémentaires dans le circuit. De cette façon, vous pouvez obtenir une valeur de résistance stable et continuellement variable dans sa plage.

(3)\. En tant que contrôleur de courant

Lorsqu'il est utilisé comme contrôleur de courant, le contact mobile doit être connecté comme l'une des bornes de sortie.

#### 4. Schéma de câblage

![Img](./media/A812.png)

<span style="color: rgb(255, 76, 65);">Lors de l'utilisation du servo, nous devons connecter une alimentation externe et mettre l'interrupteur DIP sur ON.</span>

![Img](./media/A902.png)

![Img](./media/A836.png)

#### 5. Flux du code

![Img](./media/A0854.png)

#### 6. Code de test

Le fichier de code est fourni dans le dossier Projet 05 : Cadran de voiture, fichier Project-05-Car-Dial.hex.

![Img](./media/A922.png)

**Charger les blocs de code :**

![Img](./media/A942.png)

#### 7. Résultat du test

Après avoir téléchargé le code sur la carte, tournez le bouton du potentiomètre et le servo déplace l'aiguille sur le cadran.

<span style="color: rgb(255, 76, 65);">**ATTENTION :** Si le câblage est correct mais que vous ne voyez pas les résultats, appuyez sur le bouton reset à l'arrière de la carte.</span>

![Img](./media/A706.gif)
