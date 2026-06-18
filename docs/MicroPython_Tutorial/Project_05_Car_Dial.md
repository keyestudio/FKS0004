### Proyecto 05: Dial de Coche

#### 1. Resumen

En este proyecto, combinamos un potenciómetro ajustable, un servo y una hermosa tarjeta de dial para hacer un modelo simple de dial de coche.

#### 2. Componentes

| ![Img](./media/A850.png)  |              ![Img](./media/A858.png)              | ![Img](./media/A906.png) |
| :----------------------: | :-----------------------------------------------: | :---------------------: |
|    placa micro:bit *1    |        placa de expansión tipo T para micro:bit *1        |   cable micro USB *1    |
| ![Img](./media/A350.png)  |              ![Img](./media/A309.png)              | ![Img](./media/A950.png) |
|     potenciómetro *1     |                     servo *1                      |       cables de salto        |
| ![Img](./media/A017.png)  |              ![Img](./media/A024.png)              | ![Img](./media/A233.png) |
|      protoboard *1       |soporte para baterías *1 <br> (<span style="color: rgb(255, 76, 65);">baterías AA auto-proporcionadas *2</span>)|  tarjeta de potenciómetro *1  |
| ![Img](./media/A1326.png) |                                                   |                         |
|     tarjeta de dial de coche*1      |                                                   |                         |

#### 3. Conocimiento de Componentes

**potenciómetro**

![Img](./media/A350.png)

Un potenciómetro es también un elemento resistivo con tres contactos, cuyo valor de resistencia puede ajustarse según cierta regularidad.

Vienen en todas las formas, tamaños y valores, pero todos tienen en común lo siguiente:

① Tres terminales (o puntos de conexión).

② Una perilla o deslizador móvil que puede cambiar la resistencia entre el terminal intermedio y cualquier terminal externo.

③ A medida que se mueve la perilla, la resistencia entre el terminal intermedio y cualquier terminal externo varía desde 0Ω hasta su máximo.

El símbolo de circuito del potenciómetro:

![Img](./media/A654.png)

(1)\. Como divisor de voltaje

El potenciómetro es una resistencia ajustable continuamente. Cuando giras su deslizador, el contacto móvil se desliza a lo largo de la resistencia. En este punto, se puede obtener un voltaje de salida según el voltaje aplicado al potenciómetro y el ángulo o recorrido de rotación del deslizador móvil.

(2)\. Como resistencia variable

Cuando el potenciómetro se usa como resistencia variable, conecta su terminal intermedio a uno de los dos terminales adicionales en el circuito. De esta manera, puedes obtener un valor de resistencia estable y continuamente variable dentro de su rango.

(3)\. Como controlador de corriente

Cuando se usa como controlador de corriente, el contacto móvil debe conectarse como uno de los terminales de salida.

#### 4. Diagrama de Conexiones

![Img](./media/A812.png)

<span style="color: rgb(255, 76, 65);">**Al usar el servo, debemos conectar una fuente de alimentación externa y poner el interruptor DIP en ON.**</span>

![Img](./media/A902.png)

![Img](./media/A836.png)

#### 5. Flujo del Código

![Img](./media/A0854.png)

#### 6. Código de Prueba

El archivo de código se proporciona en la carpeta Proyecto 05：Dial de Coche, archivo Project-05-Car-Dial\.py.

![Img](./media/A3438.png)

**Código completo:**

```python
'''
Function: The potentiometer controls the servo to simulate the car dial
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import microbit related libraries
from microbit import *

display.show(Image.HAPPY)  # LED matrix displays a smile face
pin0.write_analog(25.6)    # set P0 pin analog to 25.6, servo initial angle to 0°
sleep(200)

# map function
def map(value,fromLow,fromHigh,toLow,toHigh):
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow

while True:
    value=pin2.read_analog()    # Read the analog value of the potentiometer (ADC value)
    pin0.set_analog_period(20)  # set servo frequency
    pin0.write_analog(map(value,0,1023,25.6,128))  # Map the analog value of the potentiometer to that of the servo
    sleep(20)
```

#### 7. Resultado de la Prueba

Haz clic en “<span style="color: rgb(255, 76, 65);">Flash</span>” para cargar el código en la placa micro:bit.

![Img](./media/A3457.png)

Después de descargar el código a la placa, **enciende mediante el cable micro USB o fuente de alimentación externa (pon el interruptor DIP en ON)**, y presiona el botón de reinicio en la placa.

![Img](./media/A455.png)

Gira la perilla del potenciómetro y el servo mueve la aguja en el dial.

<span style="color: rgb(255, 76, 65);">**ATENCIÓN:** Si el cableado es correcto pero no ves resultados, presiona el botón de reinicio en la parte trasera de la placa.</span>

![Img](./media/A706.gif)
