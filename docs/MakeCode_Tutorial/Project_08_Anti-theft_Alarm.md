### Proyecto 08: Alarma Antirrobo

#### 1. Resumen

Cuando la alarma antirrobo inteligente detecta que la caja antirrobo ha sido movida, el altavoz en la placa micro:bit emitirá una alarma y el LED rojo parpadeará.

#### 2. Componentes

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| placa micro:bit *1 | placa de expansión tipo T para micro:bit *1 | cable micro USB *1 |
| ![Img](./media/A937.png)| ![Img](./media/A944.png) | ![Img](./media/A950.png) |
| LED rojo *1 | resistencia 220Ω *1 | cable de conexión *2 |
| ![Img](./media/A017.png) | ![Img](./media/A024.png) | ![Img](./media/A952.png)  |
| protoboard *1 | portapilas *1 <br> (<span style="color: rgb(255, 76, 65);">pilas AA auto-proporcionadas *2</span>)| tarjeta de alarma *1 |

#### 3. Conocimiento de Componentes

**Acelerómetro**

![Img](./media/A026.png)

La placa micro:bit cuenta con un sensor de aceleración LSM303AGR incorporado (llamado acelerómetro) que incluye modos estándar, rápido, plus y de alta velocidad (100 kHz, 400 kHz, 1 MHz y 3.4 MHz) de interfaz de bus serial I2C y una interfaz estándar serial SPI para comunicación externa, con resolución de 8/10/12 bits y rango de ±2g, ±4g o ±8g.

Cuando la placa micro:bit está en reposo o en movimiento uniforme, el acelerómetro solo detecta la aceleración de la gravedad. Si se balancea ligeramente, la aceleración detectada es mucho menor que la gravedad, por lo que la diferencia puede ser ignorada. Por lo tanto, principalmente detectamos el cambio de la aceleración gravitacional en los ejes x, y y z.

#### 4. Diagrama de Conexiones

![Img](./media/A219.png)

<span style="color: rgb(255, 76, 65);">**El pin de control de la placa para el LED es P1 (el pin de la placa de expansión tipo T es digital 1).**</span>

#### 5. Flujo del Código

![Img](./media/A4434.png)

#### 6. Código de Prueba

El archivo de código se proporciona en la carpeta Proyecto 08：Alarma Antirrobo, archivo Project-08-Burglar-Alarm.hex.

![Img](./media/A4518.png)

**Cargar bloques de código:** 

<span style="color: rgb(255, 76, 65);">**Después de importar el código, si el zumbador sigue sonando aunque la protoboard no se haya movido; puede deberse a factores geográficos. Puedes modificar el umbral en la condición -60 y 50 según las condiciones reales.**</span>

![Img](./media/A611.png)

#### 7. Resultado de la Prueba

Después de descargar el código a la placa, mueve la protoboard. Si el valor de aceleración x＜-60 o x＞50, el altavoz en la placa emite una alarma y el LED parpadea, y la matriz de LED del micro:bit muestra ![Img](./media/A706.png). De lo contrario, el altavoz no emite sonido y el LED está apagado, y la matriz de LED del micro:bit muestra ![Img](./media/A720.png).

<span style="color: rgb(255, 76, 65);">**ATENCIÓN:** Si el cableado es correcto pero no ves resultados, presiona el botón de reinicio en la parte trasera de la placa.</span>

![Img](./media/A936.gif)
