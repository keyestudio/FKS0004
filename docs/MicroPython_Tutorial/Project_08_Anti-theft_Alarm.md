### Projet 08 : Alarme anti-vol

#### 1. Vue d'ensemble

Lorsque l'alarme anti-vol intelligente détecte que la boîte anti-vol a été déplacée, le haut-parleur sur la carte micro:bit émettra une alarme et la LED rouge clignotera.

#### 2. Composants

| ![Img](./media/A850.png) |              ![Img](./media/A858.png)              | ![Img](./media/A906.png) |
| :---------------------: | :-----------------------------------------------: | :---------------------: |
|   carte micro:bit *1    |        carte d'extension micro:bit type T *1        |   câble micro USB *1    |
| ![Img](./media/A937.png) |              ![Img](./media/A944.png)              | ![Img](./media/A950.png) |
|       LED rouge *1      |                 résistance 220Ω *1                  |      fil de connexion *2       |
| ![Img](./media/A017.png) |              ![Img](./media/A024.png)              | ![Img](./media/A952.png) |
|      breadboard *1      |porte-piles *1 <br> (<span style="color: rgb(255, 76, 65);">piles AA auto-fournies *2</span>)|      carte alarme *1      |

#### 3. Connaissances sur les composants

**Accéléromètre**

![Img](./media/A026.png)

La carte micro:bit dispose d'un capteur d'accélération intégré LSM303AGR (appelé accéléromètre) qui comprend les modes standard, rapide, plus et haute vitesse (100 kHz, 400 kHz, 1 MHz et 3,4 MHz) de l'interface bus série I2C ainsi qu'une interface série standard SPI pour la communication externe, avec une résolution de 8/10/12 bits et une plage de ±2g, ±4g ou ±8g.

Lorsque la carte micro:bit est au repos ou en mouvement uniforme, l'accéléromètre ne détecte que l'accélération due à la gravité. Si elle est légèrement balancée, l'accélération détectée est bien inférieure à celle de la gravité, donc la différence peut être ignorée. Par conséquent, nous détectons principalement le changement de l'accélération gravitationnelle sur les axes x, y et z.

#### 4. Schéma de câblage

![Img](./media/A219.png)

<span style="color: rgb(255, 76, 65);">La broche de contrôle de la LED sur la carte est P1 (la broche de la carte d'extension type T est digitale 1).</span>

#### 5. Flux du code

![Img](./media/A4434.png)

#### 6. Code de test

Le fichier de code est fourni dans le dossier Projet 08 : Alarme anti-intrusion, fichier Project-08-Burglar-Alarm\.py.

![Img](./media/A3743.png)

**Code complet :** 

<span style="color: rgb(255, 76, 65);">**Après avoir importé le code, si le buzzer continue de sonner même si la breadboard n'est pas déplacée ; cela peut être dû à des facteurs géographiques. Vous pouvez modifier le seuil dans la condition -60 et 50 selon les conditions réelles.**</span>

```python
'''
Function: The accelerometer controls a buzzer and LED to simulate a anti-theft alarm
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from microbit import *
import music

display.show(Image.HAPPY) # LED matrix displays a smile face

while True:
    if accelerometer.get_x()<-60 or accelerometer.get_x()>50: # If the value of the accelerometer in the X direction is less than -60 or greater than 50
       music.play("C4:4")      # speaker plays C4 tone
       pin1.write_digital(1)   # P1 pin value is high, LED on
       sleep(200)
       pin1.write_digital(0)   # P1 pin value is low, LED off
       sleep(200)
       display.show(Image.NO)  # LED matrix shows X
    else:  # or
        display.show(Image.HAPPY) # LED matrix displays a smile face
        pin1.write_digital(0)
        music.reset()             # no tone
```

#### 7. Résultat du test

Cliquez sur “<span style="color: rgb(255, 76, 65);">Flash</span>” pour charger le code sur la carte micro:bit.

![Img](./media/A3757.png)

Après avoir téléchargé le code sur la carte, **alimentez via le câble micro USB ou une alimentation externe (passez l'interrupteur DIP sur ON)**, puis appuyez sur le bouton reset de la carte.

![Img](./media/A455.png)

Après avoir téléchargé le code sur la carte, déplacez la breadboard. Si la valeur d'accélération x＜-60 ou x＞50, le haut-parleur de la carte sonne et la LED clignote, et la matrice LED du micro:bit affiche ![Img](./media/A706.png). Sinon, le haut-parleur ne produit aucun son et la LED est éteinte, et la matrice LED du micro:bit affiche ![Img](./media/A720.png).

<span style="color: rgb(255, 76, 65);">**ATTENTION :** Si le câblage est correct mais que vous ne voyez pas les résultats, appuyez sur le bouton reset à l'arrière de la carte.</span>

![Img](./media/A936.gif)
