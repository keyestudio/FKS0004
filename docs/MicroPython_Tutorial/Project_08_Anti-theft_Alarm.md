### Proyecto 08: Alarma Antirrobo

#### 1. Resumen

Cuando la alarma antirrobo inteligente detecta que la caja antirrobo ha sido movida, el altavoz en la placa micro:bit emitirá una alarma y el LED rojo parpadeará.

#### 2. Componentes

| ![Img](./media/A850.png) |              ![Img](./media/A858.png)              | ![Img](./media/A906.png) |
| :---------------------: | :-----------------------------------------------: | :---------------------: |
|   placa micro:bit *1    |        placa de expansión tipo T para micro:bit *1        |   cable micro USB *1    |
| ![Img](./media/A937.png) |              ![Img](./media/A944.png)              | ![Img](./media/A950.png) |
|       LED rojo *1       |                 resistor 220Ω *1                  |      cable de salto *2       |
| ![Img](./media/A017.png) |              ![Img](./media/A024.png)              | ![Img](./media/A952.png) |
|      protoboard *1      |soporte para batería *1 <br> (<span style="color: rgb(255, 76, 65);">pilas AA auto-proporcionadas *2</span>)|      tarjeta de alarma *1      |

#### 3. Conocimiento de Componentes

**Acelerómetro**

![Img](./media/A026.png)

La placa micro:bit cuenta con un sensor de aceleración integrado LSM303AGR (llamado acelerómetro) que incluye modos estándar, rápido, plus y de alta velocidad (100 kHz, 400 kHz, 1 MHz y 3.4 MHz) de interfaz de bus serial I2C y una interfaz estándar serial SPI para comunicación externa, con resolución de 8/10/12 bits y rango de ±2g, ±4g o ±8g.

Cuando la placa micro:bit está en reposo o en movimiento uniforme, el acelerómetro solo detecta la aceleración de la gravedad. Si se balancea ligeramente, la aceleración detectada es mucho menor que la de la gravedad, por lo que la diferencia puede ignorarse. Por lo tanto, principalmente detectamos el cambio de la aceleración gravitacional en los ejes x, y y z.

#### 4. Diagrama de Conexiones

![Img](./media/A219.png)

<span style="color: rgb(255, 76, 65);">El pin de control de la placa para el LED es P1 (el pin de la placa de expansión tipo T es digital 1).</span>

#### 5. Flujo del Código

![Img](./media/A4434.png)

#### 6. Código de Prueba

El archivo de código se encuentra en la carpeta Proyecto 08：Alarma Antirrobo, archivo Project-08-Burglar-Alarm\.py.

![Img](./media/A3743.png)

**Código completo:** 

<span style="color: rgb(255, 76, 65);">**Después de importar el código, si el zumbador sigue sonando aunque la protoboard no se haya movido; puede deberse a factores geográficos. Puede modificar el umbral en la condición -60 y 50 según las condiciones reales.**</span>

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

#### 7. Resultado de la Prueba

Haga clic en “<span style="color: rgb(255, 76, 65);">Flash</span>” para cargar el código en la placa micro:bit.

![Img](./media/A3757.png)

Después de descargar el código en la placa, **encienda mediante el cable micro USB o fuente de alimentación externa (mueva el interruptor DIP a ON)**, y presione el botón de reinicio en la placa.

![Img](./media/A455.png)

Después de descargar el código en la placa, mueva la protoboard. Si el valor de aceleración x＜-60 o x＞50, el altavoz en la placa emite alarma y el LED parpadea, y la matriz LED de micro:bit muestra ![Img](./media/A706.png). De lo contrario, el altavoz no emite sonido y el LED está apagado, y la matriz LED de micro:bit muestra ![Img](./media/A720.png).

<span style="color: rgb(255, 76, 65);">**ATENCIÓN:** Si el cableado es correcto pero no ve resultados, presione el botón de reinicio en la parte trasera de la placa.</span>

![Img](./media/A936.gif)
