### Proyecto 05: Dial de Coche

#### 1. Resumen

En este proyecto, combinamos un potenciómetro ajustable, un servo y una hermosa tarjeta de dial para hacer un modelo simple de dial de coche.

#### 2. Componentes

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| placa micro:bit *1 | placa de expansión tipo T para micro:bit *1 | cable micro USB *1 |
| ![Img](./media/A350.png)| ![Img](./media/A309.png)| ![Img](./media/A950.png) |
| potenciómetro *1 | servo *1 | cables de conexión |
|![Img](./media/A017.png)  | ![Img](./media/A024.png) |![Img](./media/A233.png) |
|protoboard *1 |portapilas *1 <br> (<span style="color: rgb(255, 76, 65);">pilas AA auto-proporcionadas *2</span>)| tarjeta de potenciómetro *1 |
|![Img](./media/A1326.png) |  |  |
|tarjeta de dial de coche*1| |  |

#### 3. Conocimiento de Componentes

**potenciómetro**

![Img](./media/A350.png)

Un potenciómetro es también un elemento resistor con tres contactos, cuyo valor de resistencia puede ajustarse según cierta regularidad.

Vienen en todas las formas, tamaños y valores, pero todos tienen en común lo siguiente:

① Tres terminales (o puntos de conexión).

② Una perilla o deslizador móvil que puede cambiar la resistencia entre el terminal intermedio y cualquier terminal externo.

③ Al mover la perilla, la resistencia entre el terminal intermedio y cualquier terminal externo varía desde 0Ω hasta su máximo.

El símbolo del circuito del potenciómetro:

![Img](./media/A654.png)

(1)\. Como divisor de voltaje

El potenciómetro es un resistor ajustable continuamente. Cuando giras su deslizador, el contacto móvil se desliza a lo largo del resistor. En este punto, se puede obtener una salida de voltaje según el voltaje aplicado al potenciómetro y el ángulo o recorrido de rotación del deslizador móvil.

(2)\. Como resistor variable

Cuando el potenciómetro se usa como resistor variable, conecta su terminal intermedio a uno de los dos terminales adicionales en el circuito. De esta manera, puedes obtener un valor de resistencia estable y continuamente variable dentro de su rango.

(3)\. Como controlador de corriente

Cuando se usa como controlador de corriente, el contacto móvil debe conectarse como uno de los terminales de salida.

#### 4. Diagrama de Conexiones

![Img](./media/A812.png)

<span style="color: rgb(255, 76, 65);">Al usar el servo, debemos conectar una fuente de alimentación externa y poner el interruptor DIP en ON.</span>

![Img](./media/A902.png)

![Img](./media/A836.png)

#### 5. Flujo del Código

![Img](./media/A0854.png)

#### 6. Código de Prueba

El archivo de código se proporciona en la carpeta Proyecto 05：Dial de Coche, archivo Project-05-Car-Dial.hex.

![Img](./media/A922.png)

**Cargar bloques de código:**

![Img](./media/A942.png)

#### 7. Resultado de la Prueba

Después de descargar el código a la placa, gira la perilla del potenciómetro y el servo mueve la aguja en el dial.

<span style="color: rgb(255, 76, 65);">**ATENCIÓN:** Si el cableado es correcto pero no ves resultados, presiona el botón de reinicio en la parte trasera de la placa.</span>

![Img](./media/A706.gif)
