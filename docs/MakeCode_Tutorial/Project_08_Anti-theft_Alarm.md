### Projet 08 : Alarme anti-vol

#### 1. Aperçu

Lorsque l'alarme anti-vol intelligente détecte que la boîte anti-vol a été déplacée, le haut-parleur sur la carte micro:bit émettra une alarme et la LED rouge clignotera.

#### 2. Composants

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| carte micro:bit *1 | carte d'extension T-type micro:bit *1 | câble micro USB *1 |
| ![Img](./media/A937.png)| ![Img](./media/A944.png) | ![Img](./media/A950.png) |
| LED rouge *1 | résistance 220Ω *1 | fil de connexion *2 |
| ![Img](./media/A017.png) | ![Img](./media/A024.png) | ![Img](./media/A952.png)  |
| breadboard *1 | support de pile *1 <br> (<span style="color: rgb(255, 76, 65);">piles AA auto-fournies *2</span>)| carte d'alarme *1 |

#### 3. Connaissances sur les composants

**Accéléromètre**

![Img](./media/A026.png)

La carte micro:bit dispose d'un capteur d'accélération intégré LSM303AGR (appelé accéléromètre) qui comprend les modes standard, rapide, plus et haute vitesse (100 kHz, 400 kHz, 1 MHz et 3,4 MHz) de l'interface de bus série I2C et une interface série standard SPI pour la communication externe, avec une résolution de 8/10/12 bits et une plage de ±2g, ±4g ou ±8g.

Lorsque la carte micro:bit est au repos ou en mouvement uniforme, l'accéléromètre ne détecte que l'accélération de la gravité. Si elle est légèrement balancée, l'accélération détectée est bien inférieure à celle de la gravité, donc la différence peut être ignorée. Par conséquent, nous détectons principalement le changement de l'accélération gravitationnelle sur les axes x, y et z.

#### 4. Schéma de câblage

![Img](./media/A219.png)

<span style="color: rgb(255, 76, 65);">**La broche de contrôle de la LED sur la carte est P1 (la broche de la carte d'extension T-type est digital 1).**</span>

#### 5. Flux du code

![Img](./media/A4434.png)

#### 6. Code de test

Le fichier de code est fourni dans le dossier Projet 08 : Alarme anti-intrusion, fichier Project-08-Burglar-Alarm.hex.

![Img](./media/A4518.png)

**Charger les blocs de code :**

<span style="color: rgb(255, 76, 65);">**Après avoir importé le code, si le buzzer continue de sonner même si la breadboard n'est pas déplacée ; cela peut être dû à des facteurs géographiques. Vous pouvez modifier le seuil dans la condition -60 et 50 selon les conditions réelles.**</span>

![Img](./media/A611.png)

#### 7. Résultat du test

Après avoir téléchargé le code sur la carte, déplacez la breadboard. Si la valeur d'accélération x＜-60 ou x＞50, le haut-parleur sur la carte sonne et la LED clignote, et la matrice LED du micro:bit affiche ![Img](./media/A706.png). Sinon, le haut-parleur ne fait aucun bruit et la LED est éteinte, et la matrice LED du micro:bit affiche ![Img](./media/A720.png).

<span style="color: rgb(255, 76, 65);">**ATTENTION :** Si le câblage est correct mais que vous ne voyez pas les résultats, appuyez sur le bouton reset à l'arrière de la carte.</span>

![Img](./media/A936.gif)
