### Proyecto 06: Fiesta de Música

![Img](./media/A1317.png)

#### 1. Resumen

Cuando aplaudimos, el micrófono en la placa capta señales de sonido, y el altavoz reproduce una alegre canción de cumpleaños mientras el LED RGB emite una luz deslumbrante.

#### 2. Componentes

| ![Img](./media/A850.png) |              ![Img](./media/A858.png)              | ![Img](./media/A906.png) |
| :---------------------: | :-----------------------------------------------: | :---------------------: |
|   placa micro:bit *1    |        placa de expansión tipo T para micro:bit *1        |   cable micro USB *1    |
| ![Img](./media/A500.png) |              ![Img](./media/A944.png)              | ![Img](./media/A950.png) |
|       LED rojo *1       |                 resistencia 220Ω *3                  |      cable de salto *2       |
| ![Img](./media/A017.png) |              ![Img](./media/A024.png)              | ![Img](./media/A621.png) |
|      protoboard *1      |portapilas *1 <br> (<span style="color: rgb(255, 76, 65);">pilas AA auto-proporcionadas *2</span>)|       tarjeta RGB *1       |

#### 3. Conocimiento de Componentes

**Micrófono**

Un micrófono digital de alta calidad está integrado en el lado frontal de la placa micro:bit V2 para detectar señales de sonido y audio. El chip que controla y procesa el micrófono está en la parte trasera.

![Img](./media/A1317.png)

El micrófono está en un pequeño orificio redondo en la parte frontal de la placa, lo que facilita captar las señales de sonido circundantes. Simplemente coloque la placa micro:bit con la cara hacia arriba al usarla. Junto al orificio hay un indicador LED del micrófono. Cuando el micro:bit mide niveles de sonido, el indicador se ilumina.

![Img](./media/A116.png)

**LED RGB**

![Img](./media/A2127.png)

El LED RGB se representa en la intersección de tres colores primarios (RGB): rojo, verde y azul. La mayoría de los colores pueden sintetizarse con RGB en diferentes proporciones. Los LEDs rojo, verde y azul están empaquetados en una carcasa de plástico transparente para emitir colores de luz cambiando el voltaje de entrada de los pines R, G y B.

![Img](./media/A137.png)

**Teoría tricromática:**

![Img](./media/A150.png)

El LED RGB puede dividirse en dos tipos: ánodo común y cátodo común:

En un LED RGB de cátodo común, los tres LEDs comparten una conexión negativa (cátodo);

En un LED RGB de ánodo común, los tres LEDs comparten una conexión positiva (ánodo).

![Img](./media/A209.png)

<span style="color: rgb(255, 76, 65);">**Nota: Aquí proporcionamos un LED RGB de cátodo común.**</span>

**Pines del LED RGB:**

El LED RGB tiene 4 pines: GND (el más largo), R (rojo), G (verde) y B (azul). Coloque el LED RGB como se muestra a continuación, los pines de izquierda a derecha son rojo, GND, verde y azul.

![Img](./media/A239.png)

#### 4. Diagrama de Conexiones

![Img](./media/A308.png)

![Img](./media/A325.png)

#### 5. Flujo del Código

![Img](./media/A343.png)

#### 6. Código de Prueba

El archivo de código se proporciona en la carpeta Proyecto 06：Fiesta de Música, archivo Project-06-Music-Party\.py.

![Img](./media/A3523.png)

**Código completo:**

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

#### 7. Resultado de la Prueba

Haga clic en “<span style="color: rgb(255, 76, 65);">Flash</span>” para cargar el código en la placa micro:bit.

![Img](./media/A3540.png)

Después de descargar el código a la placa, **encienda mediante el cable micro USB o fuente de alimentación externa (gire el interruptor DIP a ON)**, y presione el botón de reinicio en la placa.

![Img](./media/A455.png)

Cuando aplaudimos, el micrófono en la placa capta señales de sonido, y el altavoz reproduce una alegre canción de cumpleaños mientras el LED RGB emite una luz deslumbrante. ¿No es la fiesta de música un ambiente feliz y alegre?

<span style="color: rgb(255, 76, 65);">**ATENCIÓN:** Si el cableado es correcto pero no ve los resultados, presione el botón de reinicio en la parte trasera de la placa.</span>

![Img](./media/A757.gif)
