### Proyecto 06: Fiesta de Música

![Img](./media/A1317.png)

#### 1. Resumen

Cuando aplaudimos, el micrófono en la placa capta señales de sonido, y el altavoz reproduce una alegre canción de cumpleaños mientras el LED RGB emite una luz deslumbrante.

#### 2. Componentes

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| placa micro:bit *1 | placa de expansión tipo T para micro:bit *1 | cable micro USB *1 |
| ![Img](./media/A500.png)| ![Img](./media/A944.png) | ![Img](./media/A950.png) |
| LED rojo *1 | resistencia 220Ω *3 | cable de conexión *2 |
| ![Img](./media/A017.png) | ![Img](./media/A024.png) | ![Img](./media/A621.png)  |
| protoboard *1 | soporte para baterías *1 <br> (<span style="color: rgb(255, 76, 65);">pilas AA auto-proporcionadas *2</span>)| tarjeta RGB *1 |

#### 3. Conocimiento de los Componentes

**Micrófono**

Un micrófono digital de alta calidad está integrado en el lado frontal de la placa micro:bit V2 para detectar señales de sonido y audio. El chip que controla y procesa el micrófono está en la parte trasera.

![Img](./media/A1317.png)

El micrófono está en un pequeño orificio redondo en la parte frontal de la placa, lo que facilita captar las señales de sonido circundantes. Simplemente coloque la placa micro:bit con la cara hacia arriba al usarla. Junto al orificio hay un indicador LED del micrófono. Cuando el micro:bit mide niveles de sonido, el indicador se ilumina.

![Img](./media/A116.png)

**LED RGB**

![Img](./media/A2127.png)

El LED RGB se representa en la intersección de tres colores primarios (RGB): rojo, verde y azul. La mayoría de los colores pueden sintetizarse con RGB en diferentes proporciones. Los LEDs rojo, verde y azul están empaquetados en una carcasa plástica transparente para emitir colores de luz cambiando el voltaje de entrada en los pines R, G y B.

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

El archivo de código se proporciona en la carpeta Proyecto 06：Fiesta de Música, archivo Project-06-Music-Party.hex.

![Img](./media/A423.png)

**Cargar bloques de código:**

![Img](./media/A445.png)

#### 7. Resultado de la Prueba

Después de descargar el código a la placa, cuando aplaudimos, el micrófono en la placa capta señales de sonido, y el altavoz reproduce una alegre canción de cumpleaños mientras el LED RGB emite una luz deslumbrante. ¿No es la fiesta de música un ambiente feliz y alegre?

<span style="color: rgb(255, 76, 65);">**ATENCIÓN:** Si el cableado es correcto pero no ves resultados, presiona el botón de reinicio en la parte trasera de la placa.</span>

![Img](./media/A757.gif)
