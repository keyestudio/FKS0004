### Proyecto 07: Monitoreo del Ambiente

#### 1. Resumen

En el OLED, el sistema inteligente de monitoreo ambiental muestra en tiempo real los valores de temperatura y humedad detectados por el sensor DHT11, así como el valor del nivel de brillo de la luz ambiental detectado por el sensor de luz incorporado.

#### 2. Componentes

|         ![Img](./media/A850.png)          |       ![Img](./media/A858.png)       |              ![Img](./media/A906.png)              |
| :--------------------------------------: | :---------------------------------: | :-----------------------------------------------: |
|            placa micro:bit *1             | placa de expansión tipo T para micro:bit *1 |                cable micro USB *1                 |
|         ![Img](./media/A2637.png)         |       ![Img](./media/A406.png)       |              ![Img](./media/A415.png)              |
| sensor de temperatura y humedad XHT11 *1 |           módulo OLED *1            |                   cables DuPont                    |
|         ![Img](./media/A017.png)          |       ![Img](./media/A950.png)       |              ![Img](./media/A024.png)              |
|              protoboard *1               |             cables de salto          |soporte para baterías *1 <br> (<span style="color: rgb(255, 76, 65);">pilas AA auto-proporcionadas *2</span>)|
|         ![Img](./media/A0715.png)         |       ![Img](./media/A557.png)       |                                                   |
|              tarjeta nube *1              |            tarjeta OLED *1           |                                                   |

#### 3. Conocimiento del Componente

**Sensor de temperatura y humedad XHT11**

![Img](./media/A2637.png)

El sensor de temperatura y humedad XHT11 es un sensor compuesto con salida de señal digital calibrada, que puede detectar la humedad y la temperatura en el aire.

**Precisión**: humedad ±5%RH, temperatura ±2℃

**Rango de detección**: humedad 5%RH ~ 95%RH, temperatura -25℃ ~ +60℃

El sensor utiliza un módulo digital especial para la adquisición y tecnología de detección de temperatura y humedad para asegurar una fiabilidad extremadamente alta y una excelente estabilidad a largo plazo. Incluye un elemento resistivo de detección de humedad y un elemento NTC de detección de temperatura, siendo muy adecuado para mediciones con precisión relativamente baja y requisitos en tiempo real.

**Modo de comunicación XHT11:**

Se adopta comunicación de bus único. Esto significa que hay solo una línea de datos para el intercambio y control de datos en el sistema.

- Definición de bits de datos transmitidos por bus único:

Formato de datos de bus único: se transmiten 40 bits de datos a la vez, con el bit alto primero.

8 bits de humedad entera + 8 bits de humedad decimal + 8 bits de temperatura entera + 8 bits de temperatura decimal + 8 bits de bit de paridad (La parte decimal de la humedad es 0)

- Definición del bit de paridad:

8 bits de humedad entera + 8 bits de humedad decimal + 8 bits de temperatura entera + 8 bits de temperatura decimal. 8 bits de bit de paridad = los últimos 8 bits del resultado obtenido

- Línea de tiempo de datos:

Después de que el host usuario (MCU) envía una señal de inicio, el XHT11 cambia de modo de bajo consumo a modo de alta velocidad. Después de la señal de inicio, el XHT11 envía una señal de respuesta y 40 bits de datos, y activa una adquisición de señal.

- La transmisión de señal se muestra en la figura:

![Img](./media/A229.png)

 **Parámetros**

- Voltaje de operación: DC 3.3V a 5V

- Corriente de operación: 2.1mA

- Potencia máxima: 0.0105W

- Rango de temperatura: -25℃ ~ +60℃ (± 2℃)

- Rango de humedad: 5%RH ~ 95%RH (precisión ±5%RH alrededor de 25 °C)

**Sensor de Luz Microbit**

![Img](./media/A0335.png)

Un sensor de luz es un dispositivo de entrada que mide el brillo de la luz externa. La placa micro:bit no incluye un sensor de luz incorporado. Detecta y percibe el brillo ambiental mediante una matriz de LED que convierte repetidamente la intensidad de luz en un valor de entrada, y luego se muestrea el tiempo de atenuación del voltaje. De esta manera, <span style="color: rgb(255, 76, 65);">el nivel de brillo detectado es un valor relativo</span>.

#### 4. Diagrama de Conexiones

![Img](./media/A409.png)

<span style="color: rgb(255, 76, 65);">**Al usar la pantalla OLED, debemos conectar una fuente de alimentación externa y poner el interruptor DIP en ON.**</span>

![Img](./media/A904.png)

![Img](./media/A554.png)

#### 5. Importar Biblioteca

Si aún no ha agregado los archivos de biblioteca requeridos (DHT11 y oled_ssd1306), por favor impórtelos refiriéndose a [Cómo Mu Importa Biblioteca a Micro:bit](https://docs.keyestudio.com/projects/FKS0004/en/latest/docs/MicroPython_Tutorial/MicroPython_Tutorial.html#how-mu-import-library-to-micro-bit).

#### 6. Flujo del Código

![Img](./media/A638.png)


#### 7. Código de Prueba

El archivo de código se proporciona en la carpeta Proyecto 07：Monitoreo del Ambiente中找文件Project-07-Environment-Monitoring\.py.

![Img](./media/A3641.png)

**Código completo:**

```python
'''
Function: OLED displays temperature and humidity values and brightness level values in real time to simulate intelligent environment detection
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
import oled_ssd1306 as oled
from microbit import *
from DHT11 import *

val = Image("90900:""09090:""90009:""90009:""99999")  # Set pattern
display.show(val)   # LED matrix displays the set pattern

#initialize and clear oled
oled.initialize()
oled.clear_oled()

sensor = DHT11(pin1)  # set temperature and humidity pins

while True:
    oled.clear_oled() # clear oled
    sensor.read()     # read the temperature and humidity values
    T = sensor.temp   # store the temperature values in T
    H = sensor.humid  # store the humidity values in H
    L = display.read_light_level()  # read the brightness level value of the light and store it in L
    oled.add_text(1, 0, 'T:' + str(T) + 'C')   # Display the temperature value at the corresponding position of the OLED
    oled.add_text(1, 1, 'H:' + str(H) + '%')   # Display the humidity value at the corresponding position of the OLED
    oled.add_text(1, 2, 'L:' + str(L))         # Display the brightness level value at the corresponding position of the OLED
    sleep(2000)
```

#### 8. Resultado de la Prueba

Haga clic en “<span style="color: rgb(255, 76, 65);">Flash</span>” para cargar el código en la placa micro:bit.

![Img](./media/A3710.png)

Después de descargar el código a la placa, **encienda mediante el cable micro USB o fuente de alimentación externa (ponga el interruptor DIP en ON)**, y presione el botón de reinicio en la placa.

![Img](./media/A455.png)

El OLED muestra en tiempo real los valores de temperatura y humedad y el nivel de brillo de la luz.

<span style="color: rgb(255, 76, 65);">**ATENCIÓN:** Si el cableado es correcto pero no puede ver los resultados, presione el botón de reinicio en la parte trasera de la placa.</span>

![Img](./media/A838.gif)
