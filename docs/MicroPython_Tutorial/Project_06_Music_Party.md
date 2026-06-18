### Projet 06 : Fête de la Musique

![Img](./media/A1317.png)

#### 1. Aperçu

Lorsque nous applaudissons, le microphone sur la carte capte les signaux sonores, et le haut-parleur joue une joyeuse chanson d'anniversaire tandis que la LED RGB émet une lumière éblouissante.

#### 2. Composants

| ![Img](./media/A850.png) |              ![Img](./media/A858.png)              | ![Img](./media/A906.png) |
| :---------------------: | :-----------------------------------------------: | :---------------------: |
|   carte micro:bit *1    |        carte d'extension micro:bit type T *1       |   câble micro USB *1    |
| ![Img](./media/A500.png) |              ![Img](./media/A944.png)              | ![Img](./media/A950.png) |
|       LED rouge *1      |                 résistance 220Ω *3                  |      fil de connexion *2       |
| ![Img](./media/A017.png) |              ![Img](./media/A024.png)              | ![Img](./media/A621.png) |
|      breadboard *1      |porte-piles *1 <br> (<span style="color: rgb(255, 76, 65);">piles AA auto-fournies *2</span>)|       carte RGB *1       |

#### 3. Connaissances sur les composants

**Microphone**

Un microphone numérique de haute qualité est intégré sur la face avant de la carte micro:bit V2 pour détecter les signaux sonores et audio. La puce qui contrôle et traite le microphone se trouve à l'arrière.

![Img](./media/A1317.png)

Le microphone est situé dans un petit trou rond sur la face avant de la carte, ce qui facilite la capture des signaux sonores environnants. Il suffit de placer la carte micro:bit face vers le haut lors de l'utilisation. À côté du trou se trouve un indicateur LED du microphone. Lorsque le micro:bit mesure les niveaux sonores, l'indicateur s'allume.

![Img](./media/A116.png)

**LED RGB**

![Img](./media/A2127.png)

La LED RGB est représentée par l'intersection des trois couleurs primaires (RGB) : rouge, vert et bleu. La plupart des couleurs peuvent être synthétisées par le RGB en différentes proportions. Les LED rouge, verte et bleue sont encapsulées dans un boîtier plastique transparent pour émettre des couleurs lumineuses en modifiant la tension d'entrée des broches R, G et B.

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

Le fichier de code est fourni dans le dossier Projet 06 : Fête de la Musique, fichier Project-06-Music-Party\.py.

![Img](./media/A3523.png)

**Code complet :**

```python
'''
Function: Clap your hands, the microbit microphone receives the sound signal, the music sounds, and the RGB emits a dazzling light to simulate a musical party
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from microbit import *
import music

display.clear() # clear LED matrix

while True:
    if microphone.current_event() == SoundEvent.LOUD:  # If the microphone picks up a loud signal
       music.play(["G3:4", "G3", "A4"]) # the speaker plays some tones
       pin1.write_analog(1023)      # P1 analog value is 1023,RGB is red
       pin2.write_analog(0)
       # pin3.write_analog(0)
       sleep(100)
       music.play(["G4:4", "C5", "B4"])
       pin1.write_analog(0)         # P1 analog value is 0,RGB is not red
       pin2.write_analog(1023)      # P2 analog value is 1023,RGB is green
       # pin3.write_analog(0)
       sleep(100)
       pin1.write_analog(10)
       pin2.write_analog(10)
       # pin3.write_analog(1023)      # P3 analog value is 1023,RGB is blue
       sleep(100)
       music.play(["G4:4", "D5", "C5"])
       pin1.write_analog(123)
       pin2.write_analog(123)
       # pin3.write_analog(0)
       sleep(100)
       music.play(["G4:4", "D5", "C5"])
       pin1.write_analog(1023)
       pin2.write_analog(400)
       # pin3.write_analog(1023)
       sleep(100)
       music.play(["G3:4", "G3", "G4"])
       pin1.write_analog(10)
       pin2.write_analog(1023)
       # pin3.write_analog(1023)
       sleep(100)
       pin1.write_analog(1023)
       pin2.write_analog(1023)
       # pin3.write_analog(1023)
       sleep(100)
       music.play(["E5:4", "C5", "B4", "A4"])
       pin1.write_analog(32)
       pin2.write_analog(184)
       # pin3.write_analog(336)
       sleep(100)
       pin1.write_analog(640)
       pin2.write_analog(328)
       # pin3.write_analog(180)
       sleep(100)
       music.play(["F5:4", "F5", "E5"])
       pin1.write_analog(552)
       pin2.write_analog(172)
       # pin3.write_analog(904)
       sleep(100)
       pin1.write_analog(1020)
       pin2.write_analog(796)
       # pin3.write_analog(560)
       sleep(100)
       music.play(["C5:4", "D5", "C5"])
       pin1.write_analog(136)
       pin2.write_analog(560)
       # pin3.write_analog(140)
       sleep(100)
       pin1.write_analog(0)
       pin2.write_analog(0)
       # pin3.write_analog(0)
       sleep(100)
if microphone.current_event() == SoundEvent.QUIET:  # If the microphone picks up a quie signal
       pin1.write_analog(0)
       pin2.write_analog(0)
```

#### 7. Résultat du test

Cliquez sur “<span style="color: rgb(255, 76, 65);">Flash</span>” pour charger le code sur la carte micro:bit.

![Img](./media/A3540.png)

Après avoir téléchargé le code sur la carte, **alimentez via le câble micro USB ou une alimentation externe (passez l'interrupteur DIP sur ON)**, puis appuyez sur le bouton reset de la carte.

![Img](./media/A455.png)

Lorsque nous applaudissons, le microphone sur la carte capte les signaux sonores, et le haut-parleur joue une joyeuse chanson d'anniversaire tandis que la LED RGB émet une lumière éblouissante. La fête de la musique n'est-elle pas dans une ambiance heureuse et joyeuse ?

<span style="color: rgb(255, 76, 65);">**ATTENTION :** Si le câblage est correct mais que vous ne voyez pas les résultats, appuyez sur le bouton reset à l'arrière de la carte.</span>

![Img](./media/A757.gif)
