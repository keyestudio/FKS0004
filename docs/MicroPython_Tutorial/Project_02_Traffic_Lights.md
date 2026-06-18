### Projet 02 : Feux de circulation

#### 1. Aperçu

Dans ce projet, nous utilisons trois LEDs (rouge, jaune et verte), un haut-parleur sur la carte micro:bit et une matrice LED 5x5 pour réaliser un modèle de feux de circulation.

#### 2. Composants

|              ![Img](./media/A850.png)              |       ![Img](./media/A858.png)       | ![Img](./media/A906.png) |
| :-----------------------------------------------: | :---------------------------------: | :---------------------: |
|                carte micro:bit *1                  | carte d'extension T-type micro:bit *1 |   câble micro USB *1    |
|              ![Img](./media/A937.png)              |      ![Img](./media/A5652.png)       | ![Img](./media/A658.png) |
|                    LED rouge *1                    |            LED jaune *1             |      LED verte *1       |
|              ![Img](./media/A944.png)              |       ![Img](./media/A950.png)       | ![Img](./media/A017.png) |
|                 résistance 220Ω *3                 |             fils de connexion       |      breadboard *1      |
|              ![Img](./media/A024.png)              |       ![Img](./media/A020.png)       |                         |
| support de pile *1 <br> (<span style="color: rgb(255, 76, 65);">piles AA auto-fournies *2</span>)|       carte feux de circulation *1  |                         |

#### 3. Connaissances sur les composants

**Haut-parleur**

![Img](./media/A833.png)

Le micro:bit est équipé d'un haut-parleur, ce qui facilite la production de sons dans votre projet.

#### 4. Schéma de câblage

![Img](./media/A908.png)

<span style="color: rgb(255, 76, 65);">**Remarque :** la carte micro:bit doit être insérée dans la carte d'extension T-type comme indiqué ci-dessous. La matrice LED de la carte micro:bit doit être du même côté que le logo de la carte d'extension.</span>

![Img](./media/A940.png)

#### 5. Flux du code

![Img](./media/A5956.png)

#### 6. Code de test

Le fichier de code est fourni dans le dossier Projet 02 : Feux de circulation, fichier Project-02-Traffic-Lights\.py.

![Img](./media/A250.png)

**Code complet :** 

```python
'''
Function: traffic lights with countdowns and buzzes
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import microbit related libraries
from microbit import *

pin1.write_digital(0) # set P1 pin to low
pin2.write_digital(0) # set P2 pin to low
pin8.write_digital(0) # set P8 pin to low

import music # import music libraries

while True:
   pin1.write_digital(1)  # P1 pin to high
   display.show('6')  # LED matrixs shows 6
   sleep(1000)        # delay 1s
   display.show('5')
   sleep(1000)
   display.show('4')
   sleep(1000)
   display.show('3')
   sleep(1000)
   display.show('2')
   sleep(1000)
   display.show('1')
   sleep(1000)
   display.show('0')
   sleep(1000)
   pin1.write_digital(0)
   pin2.write_digital(1)
   music.play("C4:4")    # speaker plays C4 tone
   display.show('2')
   sleep(500)
   pin2.write_digital(0)
   music.reset()         # no tone
   sleep(500)
   pin2.write_digital(1)
   music.play("C4:4")
   display.show('1')
   sleep(500)
   pin2.write_digital(0)
   music.reset()
   sleep(500)
   pin2.write_digital(1)
   music.play("C4:4")
   display.show('0')
   sleep(500)
   pin2.write_digital(0)
   music.reset()
   sleep(500)
   pin8.write_digital(1)
   display.show('6')
   sleep(1000)
   display.show('5')
   sleep(1000)
   display.show('4')
   sleep(1000)
   display.show('3')
   sleep(1000)
   display.show('2')
   sleep(1000)
   display.show('1')
   sleep(1000)
   display.show('0')
   sleep(1000)
   pin8.write_digital(0)
```

#### 7. Résultat du test

Cliquez sur “<span style="color: rgb(255, 76, 65);">Flash</span>” pour charger le code sur la carte micro:bit.

![Img](./media/A353.png)

Après avoir téléchargé le code sur la carte, **alimentez via le câble micro USB ou une alimentation externe (passez l'interrupteur DIP sur ON)**, puis appuyez sur le bouton reset de la carte.

![Img](./media/A455.png)

La LED verte s'allume et la matrice LED 5×5 compte à rebours 6 secondes. Après que la LED verte s'éteint, la LED jaune clignote et la matrice compte à rebours 3s avec le haut-parleur qui sonne. Enfin, la LED rouge s'allume avec un compte à rebours de 6s. Ces actions se répètent.

<span style="color: rgb(255, 76, 65);">**ATTENTION :** Si le câblage est correct mais que vous ne voyez pas les résultats, appuyez sur le bouton reset à l'arrière de la carte.</span>

![Img](./media/A459.gif)

<span style="color: rgb(255, 76, 65);">**Lors de l'alimentation via une alimentation externe, passez l'interrupteur DIP sur ON.**</span>

![Img](./media/A904.png)
