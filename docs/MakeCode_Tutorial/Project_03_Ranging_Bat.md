### Projet 03 : Chauve-souris à distance

#### 1. Vue d'ensemble

Basée sur un capteur ultrasonique, la chauve-souris à distance détecte la distance des obstacles et l'affiche en temps réel sur un OLED. Lorsque la distance est inférieure à 10 cm, le haut-parleur émet une alarme.

#### 2. Composants

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| carte micro:bit *1 | carte d'extension micro:bit type T *1 | câble micro USB *1 |
| ![Img](./media/A356.png)| ![Img](./media/A406.png)| ![Img](./media/A415.png) |
| capteur ultrasonique *1 | module OLED *1 | fils DuPont |
|![Img](./media/A017.png) | ![Img](./media/A950.png) | ![Img](./media/A024.png) |
| breadboard *1 | fils de connexion | support de pile *1 <br> (<span style="color: rgb(255, 76, 65);">piles AA auto-fournies *2</span>)|
|![Img](./media/A315.png)|![Img](./media/A557.png) | |
| carte chauve-souris *1| carte OLED *1 | |

#### 3. Connaissances sur les composants

**capteur ultrasonique**

Les ondes ultrasoniques rebondissent lorsqu'elles rencontrent un obstacle. Nous mesurons la distance en calculant l'intervalle de temps entre l'émission et la réception des ondes. Comme la vitesse de propagation du son dans l'air est constante v=340m/s, nous calculons la distance entre le capteur et l'obstacle : s=vt/2.

![Img](./media/A846.png)

Le module ultrasonique HC-SR04 intègre un émetteur et un récepteur. Le premier convertit les signaux électriques (énergie électrique) en ondes sonores à haute fréquence (au-delà de l'audition humaine) (énergie mécanique), tandis que le second fait l'inverse.

Le schéma du HC SR04 :

![Img](./media/A642.png)

**Définition des broches :**

![Img](./media/A702.png)

**Paramètres :**

- Tension de fonctionnement : 5V
- Courant de fonctionnement : 12mA
- Distance minimale de mesure : 2cm
- Distance maximale de mesure : 200cm

**Principe de fonctionnement :**

Une impulsion de niveau haut d'au moins 10µs est envoyée sur la broche Trig, et le module commence à émettre des ondes ultrasoniques. En même temps, la broche Echo est mise à niveau haut. Lorsque le module reçoit une onde ultrasonique de retour après avoir rencontré un obstacle, la broche Echo passe à niveau bas. La durée du niveau haut de la broche Echo correspond au temps total de l'onde entre l'émission et la réception : s=vt/2.

![Img](./media/A728.png)

**Module OLED**

La technologie OLED offre une riche performance de couleurs, un contraste élevé et un large angle de vue, fournissant des images claires et vives, particulièrement remarquables dans les noirs.

Chaque pixel de l'écran OLED émet sa propre lumière sans rétroéclairage, ce qui consomme relativement peu d'énergie. Avec une petite taille, une haute résolution et une faible consommation, l'écran OLED de 0,9 pouce est très adapté aux dispositifs portables.

![Img](./media/A636.png)

<span style="color: rgb(255, 76, 65);">**Dans ce projet, le module d'affichage OLED connecte l'interface SDA à la broche P20 et SCL à la broche P19.**</span>

**Paramètres :**

- Tension de fonctionnement : DC 3.3V-5V

- Courant de fonctionnement : 30mA

- Interface : ports à broches avec un espacement de 2.54mm

- Mode de communication : I2C

- Puce pilote interne : SSD1306

- Résolution : 128*64

- Angle de vue : supérieur à 150°

#### 4. Schéma de câblage

![Img](./media/A1849.png)

<span style="color: rgb(255, 76, 65);">**Lors de l'utilisation de l'écran OLED et du capteur ultrasonique, il faut connecter une alimentation externe et mettre l'interrupteur DIP sur ON.**</span>

![Img](./media/A902.png)

![Img](./media/A1906.png)

#### 5. Flux du code

![Img](./media/A924.png)

#### 6. Code de test

Le fichier de code est fourni dans le dossier Projet 03 : Chauve-souris à distance, fichier Project-03-Ranging-Bat.hex.

![Img](./media/A955.png)

**Charger les blocs de code :** <span style="color: rgb(255, 76, 65);">Le seuil dans la condition 10 peut être modifié selon les conditions réelles.</span>

![Img](./media/A022.png)

#### 7. Résultat du test

Pour l'application Windows 10, cliquez sur “<span style="color: rgb(255, 76, 65);">Download</span>”. Pour les navigateurs, envoyez le fichier “<span style="color: rgb(255, 76, 65);">.hex</span>” téléchargé vers la carte micro:bit.

Après avoir téléchargé le code sur la carte, <span style="color: rgb(255, 76, 65);">alimentez via une alimentation externe et mettez l'interrupteur DIP sur ON</span>, et l'OLED affiche en temps réel la distance entre le capteur ultrasonique et l'obstacle. Lorsque la valeur de distance est inférieure à 10 cm, le haut-parleur de la carte micro:bit émet une alarme.

<span style="color: rgb(255, 76, 65);"><span style="color: rgb(255, 76, 65);">**ATTENTION :** Si le câblage est correct mais que vous ne voyez pas les résultats, appuyez sur le bouton reset à l'arrière de la carte.</span></span>

![Img](./media/A605.gif)
