### Projet 03 : Chauve-souris à ultrasons

#### 1. Aperçu

Basée sur un capteur à ultrasons, la chauve-souris à ultrasons détecte la distance des obstacles et l'affiche en temps réel sur un OLED. Lorsque la distance est inférieure à 10 cm, le haut-parleur émet une alarme.

#### 2. Composants

| ![Img](./media/A850.png) |       ![Img](./media/A858.png)       |              ![Img](./media/A906.png)              |
| :---------------------: | :---------------------------------: | :-----------------------------------------------: |
|   micro:bit board *1    | micro:bit T-type expansion board *1 |                micro USB cable *1                 |
| ![Img](./media/A356.png) |       ![Img](./media/A406.png)       |              ![Img](./media/A415.png)              |
|  ultrasonic sensor *1   |           OLED module *1            |                   DuPont wires                    |
| ![Img](./media/A017.png) |       ![Img](./media/A950.png)       |              ![Img](./media/A024.png)              |
|      breadboard *1      |             jump wires              | battery holder *1 <br> (<span style="color: rgb(255, 76, 65);">piles AA auto-fournies *2</span>)|
| ![Img](./media/A315.png) |       ![Img](./media/A557.png)       |                                                   |
|       bat card *1       |            OLED card *1             |                                                   |

#### 3. Connaissances sur les composants

**capteur à ultrasons**

Les ondes ultrasonores rebondissent lorsqu'elles rencontrent un obstacle. Nous mesurons la distance en calculant l'intervalle de temps entre l'émission et la réception des ondes. Comme la vitesse de propagation du son dans l'air est constante v=340m/s, nous calculons la distance entre le capteur et l'obstacle : s=vt/2.

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

Une impulsion de niveau haut d'au moins 10µs est envoyée sur la broche Trig, et le module commence à émettre des ondes ultrasonores. En même temps, la broche Echo est mise à niveau haut. Lorsque le module reçoit une onde ultrasonore de retour après avoir rencontré un obstacle, la broche Echo passe à niveau bas. La durée du niveau haut de la broche Echo correspond au temps total de l'onde entre l'émission et la réception : s=vt/2.

![Img](./media/A728.png)

**Module OLED**

La technologie OLED offre une riche performance de couleurs, un contraste élevé et un large angle de vue, fournissant des images claires et vives, particulièrement remarquables dans les noirs.

Chaque pixel de l'écran OLED émet sa propre lumière sans rétroéclairage, ce qui consomme relativement peu d'énergie. Avec une petite taille, une haute résolution et une faible consommation, l'écran OLED de 0,9 pouce est très adapté aux dispositifs portables.

![Img](./media/A636.png)

<span style="color: rgb(255, 76, 65);">**Dans ce projet, le module d'affichage OLED connecte l'interface SDA à la broche P20 et SCL à la broche P19.**</span>

**Paramètres :**

- Tension de fonctionnement : DC 3.3V-5V

- Courant de fonctionnement : 30mA

- Interface : ports à broches avec un espacement de 2,54 mm

- Mode de communication : I2C

- Puce pilote interne : SSD1306

- Résolution : 128*64

- Angle de vue : supérieur à 150°

#### 4. Schéma de câblage

![Img](./media/A1849.png)

<span style="color: rgb(255, 76, 65);">**Lors de l'utilisation de l'écran OLED et du capteur à ultrasons, il faut connecter une alimentation externe et mettre l'interrupteur DIP sur ON.**</span>

![Img](./media/A902.png)

![Img](./media/A1906.png)

#### 5. Importer la bibliothèque

Si vous n'avez pas encore ajouté les fichiers de bibliothèque requis (oled_ssd1306), veuillez l'importer en vous référant à [Comment Mu importe la bibliothèque vers Micro:bit](https://docs.keyestudio.com/projects/FKS0004/en/latest/docs/MicroPython_Tutorial/MicroPython_Tutorial.html#how-mu-import-library-to-micro-bit).

#### 6. Flux du code

![Img](./media/A924.png)

#### 7. Code de test

Le fichier de code est fourni dans le dossier Projet 03：Chauve-souris à ultrasons, fichier Project-03-Ranging-Bat\.py.

![Img](./media/A302.png)

**Code complet :** <span style="color: rgb(255, 76, 65);">**Le seuil dans la condition 10 peut être modifié selon les conditions réelles.**</span>

```python
'''
Function: bat ranging
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from microbit import *
import ustruct
import machine
from time import sleep_us
import oled_ssd1306 as oled
import music

display.show(Image.HAPPY) # LED matrix displays a smile face
distance = 0              # set variable distance initial value to 0
lastEchoDuration = 0      # set variable lastEchoDuration initial value to 0

# initialize and clear oled
oled.initialize()
oled.clear_oled()

while True:
    # Ultrasonic sensor sends and receives signals
    pin1.write_digital(0)
    sleep_us(2)
    pin1.write_digital(1)
    sleep_us(15)
    pin1.write_digital(0)

    # measure the time interval between "when rising edge detected from the pin2" and "until the pin becomes low again"
    # unit is μs. Assign the interval to variable t.
    t = machine.time_pulse_us(pin2, 1, 35000)

    # a conditional statement, used to check whether the values of two variables t and lastechoduration satisfy specific conditions.
    # If both conditions are met, the block of code under the condition statement is executed.
    if (t <= 0 and lastEchoDuration >= 0):
        t = lastEchoDuration   # variable t = variable lastechoduration
    else:
        lastEchoDuration = t
    distance = int(t * 0.017)  # calculate distance
    oled.clear_oled()          # clear OLED
    oled.add_text(1, 0, str(distance) + 'cm')  # Display distance in the corresponding position of OLED
    sleep(200)
    if distance < 10:       # if distance < 10cm
        music.play("C4:4")  # speaker plays C4 tone
        sleep(200)          # delay 
        music.reset()       # no tone
        sleep(200)
```

#### 8. Résultat du test

Cliquez sur “<span style="color: rgb(255, 76, 65);">Flash</span>” pour charger le code sur la carte micro:bit.

![Img](./media/A3323.png)

Après avoir téléchargé le code sur la carte, **alimentez via le câble micro USB ou une alimentation externe (mettre l'interrupteur DIP sur ON)**, puis appuyez sur le bouton reset de la carte.

![Img](./media/A455.png)

L'OLED affiche en temps réel la distance entre le capteur à ultrasons et l'obstacle. Lorsque la valeur de distance est inférieure à 10 cm, le haut-parleur de la carte micro:bit émet une alarme.

<span style="color: rgb(255, 76, 65);"><span style="color: rgb(255, 76, 65);">**ATTENTION :** Si le câblage est correct mais que vous ne voyez pas les résultats, appuyez sur le bouton reset à l'arrière de la carte.</span></span>

![Img](./media/A605.gif)
