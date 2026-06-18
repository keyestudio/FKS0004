### Proyecto 04: Estacionamiento Inteligente

#### 1. Visión General

Los estacionamientos inteligentes están en todas partes. ¿Podemos también crear un estacionamiento inteligente? Por supuesto. Podemos usar un sensor ultrasónico para detectar si hay vehículos adelante. Cuando se detecta que un vehículo (o cosa) se acerca, controlamos el servo para levantar la barra de elevación; si se detecta que se aleja, el servo bajará la barra de elevación.

#### 2. Componentes

| ![Img](./media/A850.png) |       ![Img](./media/A858.png)       |              ![Img](./media/A906.png)              |
| :---------------------: | :---------------------------------: | :-----------------------------------------------: |
|   placa micro:bit *1    | placa de expansión tipo T para micro:bit *1 |                cable micro USB *1                 |
| ![Img](./media/A356.png) |       ![Img](./media/A309.png)       |              ![Img](./media/A415.png)              |
|  sensor ultrasónico *1  |              servo *1               |                   cables DuPont                    |
| ![Img](./media/A017.png) |       ![Img](./media/A950.png)       |              ![Img](./media/A024.png)              |
|      protoboard *1      |             cables puente           |soporte para baterías *1 <br> (<span style="color: rgb(255, 76, 65);">baterías AA auto-proporcionadas *2</span>)|
| ![Img](./media/A336.png) |       ![Img](./media/A131.png)       |                                                   |
|       tarjeta bat *1    |          tarjeta barra de elevación *1           |                                                   |

#### 3. Conocimiento de los Componentes

**Servo**

El servo es un actuador de posición. Podemos usar el servo para controlar la posición exacta o para entregar alto torque. Usualmente se usa en robots, autos de control remoto e incluso modelos de aeronaves. Hay muchas especificaciones, pero todos los servos tienen tres cables: señal (naranja), positivo (rojo) y negativo (marrón). El color puede variar según la marca del servo.

![Img](./media/A5525.png)

**Diagrama de estructura interna:**

![Img](./media/A5534.png)

① Señal: recibe señales de control del microcontrolador;

② potenciómetro: se puede medir la posición del eje de salida, que pertenece a la parte de retroalimentación de todo el servo;

③ Controlador interno: la placa embebida procesa señales de control externas, acciona el motor y señales de retroalimentación de posición, que es el núcleo de todo el servo;

④ Motor DC: actúa como un actuador para entregar velocidad, torque y posición;

⑤ Transmisión / mecanismo del servo: el mecanismo amplifica el recorrido de salida del motor al ángulo final de salida según una cierta relación de transmisión.

**Conducción del servo**

Se envían señales PWM a la línea de señal del servo para controlar su salida. El ciclo de trabajo del PWM determina directamente la posición del eje de salida. El período suele ser de 20 milisegundos y típicamente se configura para generar pulsos a una frecuencia de 50Hz.

<span style="color: rgb(255, 0, 0);">Por ejemplo (servo de 180°):</span>

Cuando enviamos un ancho de pulso de 1.5 milisegundos (ms) al servo de 180°, el eje de salida del servo se moverá a la posición media (90 grados);

Si el ancho de pulso es de 0.5ms, el eje de salida se moverá a 0 grados;

Si el ancho de pulso es de 2.5ms, el eje de salida se moverá a 180 grados;

![Img](./media/A5545.png)

**Parámetros:**

- Voltaje de operación: DC 3.3V~5V

- Temperatura de operación: -10°C ~ +50°C

- Dimensiones: 32.25mm x 12.25mm x 30.42mm

- Interfaz: interfaz de 3 pines con un espaciado de 2.54mm

#### 4. Diagrama de Conexiones

![Img](./media/A606.png)

<span style="color: rgb(255, 76, 65);">**Al usar el sensor ultrasónico y el servo, debemos conectar una fuente de alimentación externa y poner el interruptor DIP en ON.**</span>

![Img](./media/A902.png)

![Img](./media/A701.png)

#### 5. Flujo del Código

![Img](./media/A716.png)

#### 6. Código de Prueba

El archivo de código se proporciona en la carpeta Proyecto 04：Smart-Parking, archivo Project-04-Smart-Parking\.py.

![Img](./media/A3345.png)

**Código completo:** <span style="color: rgb(255, 76, 65);">El umbral en la condición 10 puede modificarse según las condiciones reales.</span>

```python
'''
Function: smart parking
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from microbit import *
import ustruct
import machine
from time import sleep_us

distance = 0              # set variable distance initial value to 0
lastEchoDuration = 0      # set variable lastEchoDuration initial value to 0

val = Image("09990:""09090:""09990:""09000:""09000")  # set iamge
display.show(val)        # LED matrix shows image
pin0.write_analog(25.6)    # set P0 pin analog to 25.6, servo angle to 0°
sleep(200)

while True:
    pin0.set_analog_period(20) # set servo frequency
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
    if distance < 10:          # if distance < 10cm
       pin0.write_analog(77)   # servo rotate to 90°
       sleep(2000)
    else:  # or
       sleep(2000)
       pin0.write_analog(25.6)
       sleep(2000)
```

#### 7. Resultado de la Prueba

Haga clic en “<span style="color: rgb(255, 76, 65);">Flash</span>” para cargar el código en la placa micro:bit.

![Img](./media/A3400.png)

Después de descargar el código a la placa, **encienda mediante el cable micro USB o fuente de alimentación externa (ponga el interruptor DIP en ON)**, y presione el botón de reinicio en la placa.

![Img](./media/A455.png)

Cuando el sensor ultrasónico detecta un vehículo (o cosa) acercándose, el servo controla la barra de elevación para subirla; si el sensor detecta que se aleja, el servo bajará la barra de elevación.

<span style="color: rgb(255, 76, 65);">**ATENCIÓN:** Si el cableado es correcto pero no ve resultados, presione el botón de reinicio en la parte trasera de la placa.</span>

![Img](./media/A021.gif)
