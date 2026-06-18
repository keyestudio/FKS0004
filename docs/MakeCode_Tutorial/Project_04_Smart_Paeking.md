### Projet 04 : Parking Intelligent

#### 1. Aperçu

Les parkings intelligents sont partout. Pouvons-nous aussi créer un parking intelligent ? Bien sûr. Nous pouvons utiliser un capteur ultrasonique pour détecter s'il y a des véhicules devant. Lorsqu'un véhicule (ou un objet) est détecté en approche, nous contrôlons le servo pour lever la barre de levage ; s'il est détecté en train de s'éloigner, le servo abaissera la barre de levage.

#### 2. Composants

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| carte micro:bit *1 | carte d'extension micro:bit type T *1 | câble micro USB *1 |
| ![Img](./media/A356.png)| ![Img](./media/A309.png)| ![Img](./media/A415.png) |
| capteur ultrasonique *1 | servo *1 | fils DuPont |
|![Img](./media/A017.png) | ![Img](./media/A950.png) | ![Img](./media/A024.png) |
| breadboard *1 | fils de liaison | support de batterie *1 <br> (<span style="color: rgb(255, 76, 65);">piles AA auto-fournies *2</span>)|
|![Img](./media/A336.png) |![Img](./media/A131.png) | |
| carte bat *1 | carte de barre de levage *1| |

#### 3. Connaissances sur les composants

**Servo**

Le servo est un actionneur de position. Nous pouvons utiliser le servo pour contrôler la position exacte ou fournir un couple élevé. Il est généralement utilisé dans les robots, les voitures télécommandées, et même les modèles d'avions. Il existe de nombreuses spécifications, mais tous les servos ont trois fils : signal (orange), positif (rouge) et négatif (marron). La couleur peut varier selon les marques de servo.

![Img](./media/A5525.png)

**Schéma de structure interne :**

![Img](./media/A5534.png)

① Signal : reçoit les signaux de contrôle du microcontrôleur ;

② potentiomètre : la position de l'arbre de sortie peut être mesurée, ce qui fait partie du retour d'information de l'ensemble du servo ;

③ Contrôleur interne : la carte embarquée traite les signaux de contrôle externes, pilote le moteur et les signaux de retour de position, c'est le cœur de tout le servo ;

④ Moteur DC : agit comme un actionneur pour fournir vitesse, couple, position ;

⑤ Transmission / mécanisme servo : le mécanisme amplifie la course fournie par le moteur jusqu'à l'angle de sortie final selon un certain rapport de transmission.

**Piloter le servo**

Envoyer des signaux PWM à la ligne de signal du servo pour contrôler sa sortie. Le rapport cyclique du PWM détermine directement la position de l'arbre de sortie. La période est généralement de 20 millisecondes et est typiquement réglée pour générer des impulsions à une fréquence de 50Hz.

<span style="color: rgb(255, 0, 0);">Par exemple (servo 180°) :</span>

Lorsque nous envoyons une largeur d'impulsion de 1,5 millisecondes (ms) au servo 180°, l'arbre de sortie du servo se déplacera à la position médiane (90 degrés) ;

Si la largeur d'impulsion est de 0,5 ms, l'arbre de sortie se déplacera à 0 degré ;

Si la largeur d'impulsion est de 2,5 ms, l'arbre de sortie se déplacera à 180 degrés ;

![Img](./media/A5545.png)

**Paramètres :**

- Tension de fonctionnement : DC 3,3V~5V

- Température de fonctionnement : -10°C ~ +50°C

- Dimensions : 32,25 mm x 12,25 mm x 30,42 mm

- Interface : interface 3 broches avec un espacement de 2,54 mm

#### 4. Schéma de câblage

![Img](./media/A606.png)

<span style="color: rgb(255, 76, 65);">**Lors de l'utilisation du capteur ultrasonique et du servo, nous devons connecter une alimentation externe et mettre l'interrupteur DIP sur ON.**</span>

![Img](./media/A902.png)

![Img](./media/A701.png)

#### 5. Flux du code

![Img](./media/A716.png)

#### 6. Code de test

Le fichier de code est fourni dans le dossier Projet 04 : Smart-Parking, fichier Project-04-Smart-Parking.hex.

![Img](./media/A758.png)

**Charger les blocs de code :** <span style="color: rgb(255, 76, 65);">**Le seuil dans la condition 10 peut être modifié selon les conditions réelles.**</span>

![Img](./media/A832.png)

#### 7. Résultat du test

Après avoir téléchargé le code sur la carte, lorsque le capteur ultrasonique détecte un véhicule (ou un objet) en approche, le servo contrôle la barre de levage pour la lever ; si le capteur détecte qu'il s'éloigne, le servo abaissera la barre de levage.

<span style="color: rgb(255, 76, 65);">**ATTENTION :** Si le câblage est correct mais que vous ne voyez pas les résultats, appuyez sur le bouton reset à l'arrière de la carte.</span>

![Img](./media/A021.gif)
