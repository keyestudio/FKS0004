### Projet 07 : Surveillance de l'environnement

#### 1. Aperçu

Sur l'OLED, le système intelligent de surveillance de l'environnement affiche en temps réel les valeurs de température et d'humidité détectées par le capteur DHT11, ainsi que la valeur du niveau de luminosité de la lumière ambiante détectée par le capteur de lumière intégré.

#### 2. Composants

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| carte micro:bit *1 | carte d'extension micro:bit de type T *1 | câble micro USB *1 |
| ![Img](./media/A2637.png)| ![Img](./media/A406.png)| ![Img](./media/A415.png) |
| capteur de température et d'humidité XHT11 *1 | module OLED *1 | fils DuPont |
|![Img](./media/A017.png) | ![Img](./media/A950.png) | ![Img](./media/A024.png) |
| breadboard *1 | fils de connexion | support de batterie *1 <br> (<span style="color: rgb(255, 76, 65);">piles AA auto-fournies *2</span>)|
|![Img](./media/A0715.png) |![Img](./media/A557.png)  | |
| carte cloud *1| carte OLED *1 | |

#### 3. Connaissances sur les composants

**Capteur de température et d'humidité XHT11**

![Img](./media/A2637.png)

Le capteur de température et d'humidité XHT11 est un capteur composite avec sortie numérique calibrée, capable de détecter l'humidité et la température de l'air.

**Précision** : humidité ±5%RH, température ±2℃

**Plage de détection** : humidité 5%RH ~ 95%RH, température -25℃ ~ +60℃

Le capteur utilise une acquisition par module numérique spécial et une technologie de détection de température et d'humidité pour garantir une fiabilité extrêmement élevée et une excellente stabilité à long terme. Il comprend un élément de détection d'humidité résistif et un élément de détection de température NTC, ce qui le rend très adapté aux mesures avec une précision relativement faible et des exigences en temps réel.

**Mode de communication XHT11 :**

La communication par bus unique est adoptée. Cela signifie qu'il n'y a qu'une seule ligne de données pour l'échange de données et le contrôle dans le système.

- Définition des bits de données transmis par bus unique :

Format des données du bus unique : 40 bits de données sont transmis à la fois, avec le bit de poids fort en premier.

8 bits humidité entière + 8 bits humidité décimale + 8 bits température entière + 8 bits température décimale + 8 bits bit de parité (La partie décimale de l'humidité est 0)

- Définition du bit de parité

8 bits humidité entière + 8 bits humidité décimale + 8 bits température entière + 8 bits température décimale. 8 bits bit de parité = les 8 derniers bits du résultat obtenu

- Chronologie des données :

Après que l'hôte utilisateur (MCU) envoie un signal de démarrage, le XHT11 passe du mode basse consommation au mode haute vitesse. Après le signal de démarrage, le XHT11 envoie un signal de réponse et 40 bits de données, et déclenche une acquisition de signal.

- La transmission du signal est illustrée dans la figure :

![Img](./media/A229.png)

 **Paramètres**

- Tension de fonctionnement : DC 3.3V à 5V

- Courant de fonctionnement : 2.1mA

- Puissance maximale : 0.0105W

- Plage de température : -25℃ ~ +60℃ (± 2℃)

- Plage d'humidité : 5%RH ~ 95%RH (précision ±5%RH autour de 25 °C)

**Capteur de lumière Microbit**

![Img](./media/A0335.png)

Un capteur de lumière est un dispositif d'entrée qui mesure la luminosité de la lumière externe. La carte micro:bit ne comprend pas de capteur de lumière intégré. Elle détecte et mesure la luminosité ambiante par une matrice de LED qui convertit à plusieurs reprises l'intensité lumineuse en une valeur d'entrée, puis le temps d'atténuation de la tension est échantillonné. De cette façon, <span style="color: rgb(255, 76, 65);">le niveau de luminosité détecté est une valeur relative</span>.

#### 4. Schéma de câblage

![Img](./media/A409.png)

<span style="color: rgb(255, 76, 65);">Lors de l'utilisation de l'affichage OLED, nous devons connecter une alimentation externe et mettre l'interrupteur DIP sur ON.</span>

![Img](./media/A904.png)

![Img](./media/A554.png)

#### 5. Flux du code

![Img](./media/A638.png)


#### 6. Code de test

Le fichier de code est fourni dans le dossier Projet 07：Surveillance de l'environnement, fichier Project-07-Environment-Monitoring.hex.

![Img](./media/A656.png)

**Charger les blocs de code :**

![Img](./media/A715.png)

#### 7. Résultat du test

Après avoir téléchargé le code sur la carte, l'OLED affiche en temps réel les valeurs de température et d'humidité ainsi que le niveau de luminosité de la lumière.

<span style="color: rgb(255, 76, 65);">**ATTENTION :** Si le câblage est correct mais que vous ne voyez pas les résultats, appuyez sur le bouton reset à l'arrière de la carte.</span>

![Img](./media/A838.gif)
