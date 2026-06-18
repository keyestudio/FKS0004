### Proyecto 07: Monitoreo del Ambiente

#### 1. Resumen

En el OLED, el sistema inteligente de monitoreo ambiental muestra en tiempo real los valores de temperatura y humedad detectados por el sensor DHT11, así como el valor del nivel de brillo de la luz ambiental detectado por el sensor de luz integrado.

#### 2. Componentes

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| placa micro:bit *1 | placa de expansión tipo T para micro:bit *1 | cable micro USB *1 |
| ![Img](./media/A2637.png)| ![Img](./media/A406.png)| ![Img](./media/A415.png) |
| sensor de temperatura y humedad XHT11 *1 | módulo OLED *1 | cables DuPont |
|![Img](./media/A017.png) | ![Img](./media/A950.png) | ![Img](./media/A024.png) |
| protoboard *1 | cables de salto | soporte para batería *1 <br> (<span style="color: rgb(255, 76, 65);">pilas AA auto-proporcionadas *2</span>)|
|![Img](./media/A0715.png) |![Img](./media/A557.png)  | |
| tarjeta nube *1| tarjeta OLED *1 | |

#### 3. Conocimiento de los Componentes

**Sensor de temperatura y humedad XHT11**

![Img](./media/A2637.png)

El sensor de temperatura y humedad XHT11 es un sensor compuesto con salida de señal digital calibrada, que puede detectar la humedad y temperatura en el aire.

**Precisión**: humedad ±5%RH, temperatura ±2℃

**Rango de detección**: humedad 5%RH ~ 95%RH, temperatura -25℃ ~ +60℃

El sensor utiliza un módulo digital especial para adquisición y tecnología de detección de temperatura y humedad para asegurar una fiabilidad extremadamente alta y una excelente estabilidad a largo plazo. Incluye un elemento resistivo de detección de humedad y un elemento NTC de detección de temperatura, siendo muy adecuado para mediciones con precisión relativamente baja y requisitos en tiempo real.

**Modo de comunicación XHT11:**

Se adopta comunicación de bus único. Esto significa que solo hay una línea de datos para el intercambio de datos y control en el sistema.

- Definición de bits de datos transmitidos por bus único:

Formato de datos de bus único: se transmiten 40 bits de datos a la vez, con el bit alto primero.

8bit entero de humedad + 8bit decimal de humedad + 8bit entero de temperatura + 8bit decimal de temperatura + 8bit bit de paridad (La parte decimal de la humedad es 0)

- Definición del bit de paridad

8bit entero de humedad + 8bit decimal de humedad + 8bit entero de temperatura + 8bit decimal de temperatura. 8bit bit de paridad = los últimos 8 bits del resultado obtenido

- Línea de tiempo de datos:

Después de que el host usuario (MCU) envía una señal de inicio, el XHT11 cambia de modo de bajo consumo a modo de alta velocidad. Tras la señal de inicio, XHT11 envía una señal de respuesta y 40bit de datos, y activa una adquisición de señal.

- La transmisión de señal se muestra en la figura:

![Img](./media/A229.png)

 **Parámetros**

- Voltaje de operación: DC 3.3V a 5V

- Corriente de operación: 2.1mA

- Potencia máxima: 0.0105W

- Rango de temperatura: -25℃ ~ +60℃ (± 2℃)

- Rango de humedad: 5%RH ~ 95%RH (precisión ±5%RH alrededor de 25 ° C)

**Sensor de Luz Microbit**

![Img](./media/A0335.png)

Un sensor de luz es un dispositivo de entrada que mide el brillo de la luz externa. La placa micro:bit no incluye un sensor de luz incorporado. Detecta y percibe el brillo ambiental mediante una matriz de LED que convierte repetidamente la intensidad de la luz en un valor de entrada, y luego se muestrea el tiempo de atenuación del voltaje. De esta manera, <span style="color: rgb(255, 76, 65);">el nivel de brillo detectado es un valor relativo</span>.

#### 4. Diagrama de Conexiones

![Img](./media/A409.png)

<span style="color: rgb(255, 76, 65);">Al usar la pantalla OLED, debemos conectar una fuente de alimentación externa y poner el interruptor DIP en ON.</span>

![Img](./media/A904.png)

![Img](./media/A554.png)

#### 5. Flujo del Código

![Img](./media/A638.png)


#### 6. Código de Prueba

El archivo de código se proporciona en la carpeta Proyecto 07：Monitoreo del Ambiente, archivo Project-07-Environment-Monitoring.hex.

![Img](./media/A656.png)

**Cargar bloques de código:**

![Img](./media/A715.png)

#### 7. Resultado de la Prueba

Después de descargar el código a la placa, el OLED muestra en tiempo real los valores de temperatura y humedad y el nivel de brillo de la luz.

<span style="color: rgb(255, 76, 65);">**ATENCIÓN:** Si el cableado es correcto pero no puede ver los resultados, presione el botón de reinicio en la parte trasera de la placa.</span>

![Img](./media/A838.gif)
