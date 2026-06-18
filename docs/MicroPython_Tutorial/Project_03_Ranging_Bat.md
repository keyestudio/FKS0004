### Proyecto 03: Murciélago Medidor de Distancia

#### 1. Resumen

Basado en un sensor ultrasónico, el murciélago medidor detecta la distancia de los obstáculos y la muestra en tiempo real en un OLED. Cuando es menor a 10cm, el altavoz emite una alarma.

#### 2. Componentes

| ![Img](./media/A850.png) |       ![Img](./media/A858.png)       |              ![Img](./media/A906.png)              |
| :---------------------: | :---------------------------------: | :-----------------------------------------------: |
|   placa micro:bit *1    | placa de expansión tipo T para micro:bit *1 |                cable micro USB *1                 |
| ![Img](./media/A356.png) |       ![Img](./media/A406.png)       |              ![Img](./media/A415.png)              |
|  sensor ultrasónico *1   |           módulo OLED *1            |                   cables DuPont                    |
| ![Img](./media/A017.png) |       ![Img](./media/A950.png)       |              ![Img](./media/A024.png)              |
|      protoboard *1      |             cables de salto              | portapilas *1 <br> (<span style="color: rgb(255, 76, 65);">pilas AA auto-proporcionadas *2</span>)|
| ![Img](./media/A315.png) |       ![Img](./media/A557.png)       |                                                   |
|       tarjeta bat *1       |            tarjeta OLED *1             |                                                   |

#### 3. Conocimiento de Componentes

**sensor ultrasónico**

Las ondas ultrasónicas rebotan cuando golpean un obstáculo. Medimos la distancia calculando el intervalo de tiempo entre el envío y la recepción de las ondas. Dado que la velocidad de propagación del sonido en el aire es constante v=340m/s, calculamos la distancia entre el sensor y el obstáculo: s=vt/2.

![Img](./media/A846.png)

El módulo ultrasónico HC-SR04 integra un transmisor y un receptor. El primero convierte señales eléctricas (energía eléctrica) en ondas sonoras de alta frecuencia (más allá del oído humano) (energía mecánica), mientras que el segundo hace lo contrario.

El diagrama esquemático del HC SR04:

![Img](./media/A642.png)

**Definición de pines:**

![Img](./media/A702.png)

**Parámetros:**

- Voltaje de operación: 5V
- Corriente de operación: 12mA
- Distancia mínima de medición: 2cm
- Distancia máxima de medición: 200cm

**Principio de funcionamiento:**

Se emite un pulso de nivel alto de al menos 10us en el pin Trig, y el módulo comienza a transmitir ondas ultrasónicas. Al mismo tiempo, el pin Echo se pone en alto. Cuando el módulo recibe una onda ultrasónica de vuelta al encontrar un obstáculo, el pin Echo se pone en bajo. La duración del nivel alto del pin Echo es el tiempo total de la onda desde el envío hasta la recepción: s=vt/2.

![Img](./media/A728.png)

**Módulo OLED**

La tecnología OLED ofrece un rendimiento de color rico, alto contraste y amplio ángulo de visión, proporcionando imágenes claras y vívidas, especialmente destacadas en el color negro.

Cada píxel de la pantalla OLED emite luz por sí mismo sin retroiluminación, por lo que consume relativamente poca energía. Con tamaño pequeño, alta resolución y bajo consumo, la pantalla OLED de 0.9 pulgadas es muy adecuada para dispositivos portátiles.

![Img](./media/A636.png)

<span style="color: rgb(255, 76, 65);">**En este proyecto, el módulo de pantalla OLED conecta la interfaz SDA al pin P20 y SCL al pin P19.**</span>

**Parámetros:**

- Voltaje de operación: DC 3.3V-5V

- Corriente de operación: 30mA

- Interfaz: Puertos de pines con un espaciado de 2.54mm

- Modo de comunicación: I2C

- Chip controlador interno: SSD1306

- Resolución: 128*64

- Ángulo de visión: mayor a 150°

#### 4. Diagrama de Conexiones

![Img](./media/A1849.png)

<span style="color: rgb(255, 76, 65);">**Al usar la pantalla OLED y el sensor ultrasónico, debemos conectar una fuente de alimentación externa y poner el interruptor DIP en ON.**</span>

![Img](./media/A902.png)

![Img](./media/A1906.png)

#### 5. Importar Biblioteca

Si aún no has agregado los archivos de biblioteca requeridos (oled_ssd1306), por favor impórtala refiriéndote a [Cómo Mu importa biblioteca a Micro:bit](https://docs.keyestudio.com/projects/FKS0004/en/latest/docs/MicroPython_Tutorial/MicroPython_Tutorial.html#how-mu-import-library-to-micro-bit).

#### 6. Flujo del Código

![Img](./media/A924.png)

#### 7. Código de Prueba

El archivo de código se proporciona en la carpeta Proyecto 03：Murciélago Medidor de Distancia, archivo Project-03-Ranging-Bat\.py.

![Img](./media/A302.png)

**Código completo:** <span style="color: rgb(255, 76, 65);">**El umbral en la condición 10 puede modificarse según las condiciones reales.**</span>

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

#### 8. Resultado de la Prueba

Haz clic en “<span style="color: rgb(255, 76, 65);">Flash</span>” para cargar el código en la placa micro:bit.

![Img](./media/A3323.png)

Después de descargar el código a la placa, **enciende mediante el cable micro USB o fuente de alimentación externa (pon el interruptor DIP en ON)**, y presiona el botón de reinicio en la placa.

![Img](./media/A455.png)

El OLED muestra la distancia entre el sensor ultrasónico y el obstáculo en tiempo real. Cuando el valor de la distancia es menor a 10cm, el altavoz en la placa micro:bit emite una alarma.

<span style="color: rgb(255, 76, 65);"><span style="color: rgb(255, 76, 65);">**ATENCIÓN:** Si el cableado es correcto pero no ves resultados, presiona el botón de reinicio en la parte trasera de la placa.</span></span>

![Img](./media/A605.gif)
