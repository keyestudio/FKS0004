### Proyecto 01: Pequeña lámpara con botón

#### 1. Resumen

Hay dos botones programables en la parte frontal de la placa micro:bit (A y B). Los combinamos con un LED rojo y una tarjeta de lámpara para construir una pequeña lámpara de escritorio. Cuando se presiona el botón A, el LED rojo se enciende; cuando se presiona B, se apaga.

#### 2. Componentes

| ![Img](./media/A850.png) |              ![Img](./media/A858.png)              | ![Img](./media/A906.png) |
| :---------------------: | :-----------------------------------------------: | :---------------------: |
|   placa micro:bit *1    |        placa de expansión tipo T para micro:bit *1        |   cable micro USB *1    |
| ![Img](./media/A937.png) |              ![Img](./media/A944.png)              | ![Img](./media/A950.png) |
|       LED rojo *1       |                 resistencia 220Ω *1                  |      cable puente *2       |
| ![Img](./media/A017.png) |              ![Img](./media/A024.png)              | ![Img](./media/A920.png) |
|      protoboard *1      | portapilas *1 <br> (<span style="color: rgb(255, 76, 65);">pilas AA auto-proporcionadas *2</span>) |      tarjeta de lámpara *1       |

#### 3. Conocimientos sobre componentes

**Botones**

Los botones pueden controlar el encendido y apagado del circuito. Cuando un botón está conectado a un circuito, el circuito está abierto cuando el botón no está presionado; el circuito se cierra al presionar el botón.

Hay tres botones en la placa micro:bit: un botón de reinicio en la parte trasera y dos botones programables (A y B) en la parte frontal.

![Img](./media/A230.png)

**Resistencias**

![Img](./media/A248.png)

Una resistencia es un componente electrónico que limita la corriente en una rama del circuito. La resistencia de una resistencia fija no puede ajustarse, mientras que la de un potenciómetro o resistencia variable sí puede.

Aquí hay dos símbolos comunes de circuito para resistencias. Si ves estos símbolos en un circuito, representan una resistencia.

![Img](./media/A303.png)

Ω es la unidad de resistencia, incluyendo Ω, KΩ, MΩ, etc. Se pueden expresar como: 1 MΩ=1000 KΩ, 1 KΩ =1000 Ω. En general, algunas resistencias están marcadas en la superficie.

Al usar una resistencia, primero necesitamos conocer su valor. Hay dos maneras: observar la banda de colores en ella, o medir su resistencia con un multímetro. Obviamente, la primera es más conveniente y rápida.

![Img](./media/A317.png)

Como se muestra en la tarjeta de resistencias, cada color representa un número.

![Img](./media/A3335.png)

Las resistencias de 4 y 5 bandas son las más comunes.

A menudo, cuando recibes una resistencia, puede ser difícil decidir por dónde empezar a leer el color.

**Por lo tanto, puedes observar la separación entre las dos bandas en un extremo; si es más ancha que cualquier otra separación de bandas, lee desde el extremo opuesto.**

<span style="color: rgb(255, 76, 65);">**Ten en cuenta que la separación entre la 4ª y 5ª banda (la 3ª y 4ª) es relativamente ancha en una resistencia de 5 bandas (4 bandas).**</span>

Veamos cómo leer la resistencia de una resistencia de 5 bandas, como se muestra a continuación:

![Img](./media/A426.png)

Para esta resistencia, el valor debe leerse de izquierda a derecha. El valor debe ser: 1ª banda 2ª banda 3ª banda x 10^multiplicador(Ω), ±tolerancia%.

Por lo tanto, la resistencia de esta resistencia es 2(rojo) 2(rojo) 0(negro) × 10^0 (negro)Ω = 220Ω, ±1%(marrón). Aprende más sobre [resistencia en Wiki](https://en.wikipedia.org/wiki/Resistor).

**LED**

LED, llamado completamente “diodo emisor de luz”, es un dispositivo electrónico hecho de materiales semiconductores (silicio, selenio, germanio, etc.). Es polar, con un polo positivo - el pin largo conectado a VCC (V o 3.3V o 5V o +), y un polo negativo - el pin corto conectado a GND (G o -). La corriente fluye del positivo al negativo, en un flujo unidireccional.

Símbolo electrónico y gráfico del LED:

![Img](./media/A515.png)

LED en varios tamaños y colores:

![Img](./media/A525.png)

Rojo, amarillo, azul, verde y blanco son los colores más comunes de LED, que coinciden con sus colores de apariencia. Raramente usamos LED transparentes, y la luz emitida puede no ser blanca. Hay cuatro tamaños de LED: 3mm, 5mm (el más común), 8mm y 10mm.

![Img](./media/A535.png)

El voltaje directo debe usarse cuando el LED está encendido. Es un parámetro muy importante al usar un LED, ya que determina cuánta energía usas y qué tan grande debe ser la resistencia limitadora de corriente. Para la mayoría de los LED rojos, amarillos, naranjas y verde claro, típicamente usan un voltaje entre 1.9V y 2.1V.

![Img](./media/A548.png)

Según la ley de Ohm, la corriente a través del circuito disminuye a medida que la resistencia aumenta, causando que el LED se atenúe.

I = (VP-Vl)/R

Para que el LED sea seguro y tenga el brillo adecuado, ¿qué resistencia debemos usar en el circuito?

Para el 99% de los LED de 5mm, la corriente recomendada es 20mA, que se puede ver en la columna de condiciones en su hoja de datos:

![Img](./media/A613.png)

Ahora convierte la fórmula anterior a la siguiente:

R = (VP-Vl)/I

Si VP = 5V, Vl (voltaje directo) = 2V, e I = 20mA, podemos decir que R es 150Ω. Por lo tanto, podemos hacer que el LED sea más brillante reduciendo la resistencia, pero la resistencia no debe ser inferior a 150Ω (este valor puede no ser exacto porque los LED proporcionados varían).

El voltaje directo y la longitud de onda de diferentes colores de LED se muestran a continuación para tu referencia:

![Img](./media/A629.png)

<span style="color: rgb(255, 76, 65);">**No conectes una resistencia con muy baja resistencia directamente a los dos polos de la fuente de alimentación, o los componentes electrónicos pueden dañarse debido a la corriente excesiva. Las resistencias no son polares.**</span>

**Protoboard**

Antes de completar cualquier circuito, se usa un protoboard para diseñar y probar circuitos rápidamente. Hay muchos agujeros en un protoboard donde se pueden insertar componentes del circuito (por ejemplo, resistencias). Un protoboard típico se muestra a continuación:

![Img](./media/A655.png)

Un protoboard tiene muchas tiras metálicas debajo para conectar los agujeros en la parte superior. Están dispuestas como se muestra a continuación.

<span style="color: rgb(255, 76, 65);">**Ten en cuenta que los agujeros de arriba y abajo están conectados horizontalmente, mientras que el resto de los agujeros están conectados verticalmente.**</span>

![Img](./media/A723.png)

Las dos primeras filas (superior) y las dos últimas (inferior) del protoboard se usan para los polos positivo (+) y negativo (-) de la fuente de alimentación, respectivamente. El diagrama de disposición conductiva se muestra a continuación:

![Img](./media/A730.png)

Al conectar componentes DIP (Dual In-line Packages), como circuitos integrados, microcontroladores, chips, etc., la ranura aísla las dos partes. Por lo tanto, los componentes DIP pueden conectarse como se muestra a continuación:

![Img](./media/A740.png)

![Img](./media/A747.png)

**Cable puente y cable DuPont**

Los cables puente y cables DuPont conectan dos terminales. Hay varios tipos, pero aquí nos enfocamos en los usados en protoboard. Transmiten señales eléctricas desde cualquier parte del protoboard a los pines de entrada/salida de un microcontrolador.

Al usarlos, inserta “dos pines” de los cables en el protoboard sin soldar. Varias filas paralelas están dispuestas bajo la superficie del protoboard, por lo que los cables solo necesitan insertarse en agujeros específicos en un prototipo particular.

Hay tres tipos de cables DuPont: F-F, M-M y M-F. En el cable, el pin se llama extremo macho (M), mientras que el agujero es hembra (F).

![Img](./media/A811.png)

Se pueden usar más de un tipo en un proyecto. Aunque los colores de los cables son diferentes, cumplen la misma función. Los colores se usan para distinguir circuitos.

#### 4. Diagrama de conexión

<span style="color: rgb(255, 76, 65);">Nota: la placa micro:bit debe insertarse en la placa de expansión tipo T como se muestra a continuación. La matriz LED de la placa micro:bit debe estar del mismo lado que el logo de la placa de expansión.</span>

![Img](./media/A156.png)

<span style="color: rgb(255, 76, 65);">**El pin de control de la placa para el LED es P0 (el pin de la placa de expansión tipo T es digital 0).**</span>

#### 5. Flujo del código

![Img](./media/A4323.png)

#### 6. Código de prueba

El archivo de código se proporciona en la carpeta Proyecto 01：Pequeña lámpara con botón, archivo Project-01-Small-Lamp-with-Button\.py.

![Img](./media/A100.png)

**Código completo:**

```python
'''
Function: microbit on-board buttons A&B control LED
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import microbit related libraries
from microbit import *

display.show(Image.HEART) # LED matrix displays ❤
pin0.write_digital(0) # set P0 pin to low

while True:
    if button_a.is_pressed():     # if A is pressed
        pin0.write_digital(1)     # P0 is high
        display.show(Image.HAPPY) # LED matrix displays a smile face
    elif button_b.is_pressed():   # or else B is pressed
        pin0.write_digital(0)     # P0 is low
        display.show(Image.SAD)   # LED matrix displays a crying face
```

#### 7. Resultado de la prueba

Haz clic en “<span style="color: rgb(255, 76, 65);">Flash</span>” para cargar el código en la placa micro:bit.

![Img](./media/A2156.png)

Después de descargar el código a la placa, **enciende mediante el cable micro USB o fuente de alimentación externa (gira el interruptor DIP a ON)**, y presiona el botón de reinicio en la placa.

![Img](./media/A455.png)

Podemos ver el fenómeno: la matriz LED 5x5 muestra ![Img](./media/A512.png). Presiona el botón A, y la matriz LED 5x5 muestra ![Img](./media/A518.png), el LED se enciende. Presiona el botón B, la matriz LED 5x5 muestra ![Img](./media/A527.png), el LED se apaga. ¿Parece una mini lámpara?

<span style="color: rgb(255, 76, 65);">**ATENCIÓN:** Si la conexión es correcta pero no ves resultados, presiona nuevamente el botón de reinicio en la parte trasera de la placa.</span>

![Img](./media/A359.gif)

<span style="color: rgb(255, 76, 65);">Cuando se alimenta mediante fuente externa, gira el interruptor DIP a ON.</span>

![Img](./media/A904.png)
