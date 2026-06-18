### Proyecto 02: Semáforos

#### 1. Resumen

En este proyecto, utilizamos tres LEDs (rojo, amarillo y verde), un altavoz en la placa micro:bit y una matriz LED 5x5 para crear un modelo de semáforo.

#### 2. Componentes

|              ![Img](./media/A850.png)              |       ![Img](./media/A858.png)       | ![Img](./media/A906.png) |
| :-----------------------------------------------: | :---------------------------------: | :---------------------: |
|                placa micro:bit *1                 | placa de expansión tipo T para micro:bit *1 |   cable micro USB *1    |
|              ![Img](./media/A937.png)              |      ![Img](./media/A5652.png)       | ![Img](./media/A658.png) |
|                    LED rojo *1                     |            LED amarillo *1            |      LED verde *1       |
|              ![Img](./media/A944.png)              |       ![Img](./media/A950.png)       | ![Img](./media/A017.png) |
|                 resistencia 220Ω *3                |             cables de conexión              |      protoboard *1      |
|              ![Img](./media/A024.png)              |       ![Img](./media/A020.png)       |                         |
| portapilas *1 <br> (<span style="color: rgb(255, 76, 65);">pilas AA auto-proporcionadas *2</span>)|       tarjeta de semáforo *1        |                         |

#### 3. Conocimiento de Componentes

**Altavoz**

![Img](./media/A833.png)

Micro:bit viene con un altavoz, lo que facilita hacer sonidos en tu proyecto.

#### 4. Diagrama de Conexiones

![Img](./media/A908.png)

<span style="color: rgb(255, 76, 65);">**Nota:** la placa micro:bit debe insertarse en la placa de expansión tipo T como se muestra a continuación. La matriz LED de la placa micro:bit debe estar en el mismo lado que el logo de la placa de expansión.</span>

![Img](./media/A940.png)

#### 5. Flujo del Código

![Img](./media/A5956.png)

#### 6. Código de Prueba

El archivo de código se encuentra en la carpeta Proyecto 02：Semáforos, archivo Project-02-Traffic-Lights\.py.

![Img](./media/A250.png)

**Código completo:** 

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

#### 7. Resultado de la Prueba

Haz clic en “<span style="color: rgb(255, 76, 65);">Flash</span>” para cargar el código en la placa micro:bit.

![Img](./media/A353.png)

Después de descargar el código a la placa, **enciende mediante el cable micro USB o fuente de alimentación externa (gira el interruptor DIP a ON)**, y presiona el botón de reinicio en la placa.

![Img](./media/A455.png)

El LED verde se enciende y la matriz LED 5×5 cuenta regresivamente 6 segundos. Después de que el LED verde se apaga, el LED amarillo parpadea y la matriz cuenta 3 segundos con sonido del altavoz. Finalmente, el LED rojo se enciende con una cuenta regresiva de 6 segundos. Estas acciones se repiten.

<span style="color: rgb(255, 76, 65);">**ATENCIÓN:** Si el cableado es correcto pero no ves resultados, presiona el botón de reinicio en la parte trasera de la placa.</span>

![Img](./media/A459.gif)

<span style="color: rgb(255, 76, 65);">**Al alimentar con fuente externa, gira el interruptor DIP a ON.**</span>

![Img](./media/A904.png)
