### Proyecto 02: Semáforos

#### 1. Resumen

En este proyecto, utilizamos tres LEDs (rojo, amarillo y verde), un altavoz en la placa micro:bit y una matriz LED 5x5 para hacer un modelo de semáforo.

#### 2. Componentes

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| placa micro:bit *1 | placa de expansión tipo T para micro:bit *1 | cable micro USB *1 |
| ![Img](./media/A937.png)| ![Img](./media/A5652.png) | ![Img](./media/A658.png) |
| LED rojo *1 | LED amarillo *1 | LED verde *1 |
| ![Img](./media/A944.png) | ![Img](./media/A950.png) |![Img](./media/A017.png) |
| resistencia 220Ω *3 | cables de salto | protoboard *1 |
|  ![Img](./media/A024.png) |  ![Img](./media/A020.png) |  |
| portapilas *1 <br> (<span style="color: rgb(255, 76, 65);">pilas AA auto-proporcionadas *2</span>) | tarjeta de semáforo *1 | |

#### 3. Conocimiento de Componentes

**Altavoz**

![Img](./media/A833.png)

Micro:bit viene con un altavoz, lo que facilita hacer sonido en tu proyecto.

#### 4. Diagrama de Conexiones

![Img](./media/A908.png)

<span style="color: rgb(255, 76, 65);">**Nota:** la placa micro:bit debe insertarse en la placa de expansión tipo T como se muestra a continuación. La matriz LED de la placa micro:bit debe estar del mismo lado que el logo de la placa de expansión.</span>

![Img](./media/A940.png)

#### 5. Flujo del Código

![Img](./media/A5956.png)

#### 6. Código de Prueba

El archivo de código se proporciona en la carpeta Proyecto 02：Semáforos, archivo Project-02-Traffic-Lights.hex.

![Img](./media/A0017.png)

**Cargar bloques de código:**

![Img](./media/A605.png)

#### 7. Resultado de la Prueba

Para la aplicación de Windows 10, haga clic en “<span style="color: rgb(255, 76, 65);">Descargar</span>”. Para navegadores, envíe el archivo “<span style="color: rgb(255, 76, 65);">.hex</span>” descargado a la placa micro:bit.

Después de descargar el código a la placa, el LED verde se enciende y la matriz LED 5×5 cuenta regresivamente 6 segundos. Después de que el LED verde se apaga, el LED amarillo parpadea y la matriz cuenta regresivamente 3s con el altavoz sonando. Finalmente, el LED rojo se enciende con una cuenta regresiva de 6s. Estas acciones se repiten.

<span style="color: rgb(255, 76, 65);">**ATENCIÓN:** Si el cableado es correcto pero no ves los resultados, presiona el botón de reinicio en la parte trasera de la placa.</span>

![Img](./media/A459.gif)

<span style="color: rgb(255, 76, 65);">**Al alimentar mediante fuente de alimentación externa, encienda el interruptor DIP.**</span>

![Img](./media/A904.png)
