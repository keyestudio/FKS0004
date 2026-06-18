## 1. Programación en MakeCode

Las siguientes instrucciones se aplican al sistema Windows pero también pueden servir como referencia si usas un sistema diferente.

#### 1.1. Inicio rápido

**Paso 1 Conectar al micro:bit**

Conecta la placa al ordenador mediante un cable USB.

![Img](./media/A800.png)

Si el LED rojo en la parte trasera de la placa está encendido, significa que la placa está alimentada. Cuando tu ordenador se comunica con la placa principal a través del cable USB, el LED amarillo parpadea. Por ejemplo, parpadea cuando cargas un archivo “.hex”.

Luego, la placa principal Micro:bit aparecerá en tu ordenador como un dispositivo llamado “MICROBIT”. Ten en cuenta que no es un disco USB ordinario como se muestra a continuación.

![Img](./media/A849.png)

**Paso 2 Escribir programa heartbeat**

Entra en el enlace: [versión online de Makecode](https://makecode.microbit.org/)

Haz clic en “<span style="color: rgb(255, 76, 65);">Nuevo Proyecto</span>” y verás “<span style="color: rgb(255, 76, 65);">Creando un proyecto</span>”, escribe “<span style="color: rgb(255, 76, 65);">heartbeat</span>” y haz clic en “<span style="color: rgb(255, 76, 65);">Crear √</span>”.

<span style="color: rgb(255, 76, 65);">Aquí escribimos programas en Google Chrome.</span>

![Img](./media/A021.png)

Vamos a escribir un código para micro:bit.

Puedes arrastrar algunos bloques al área de edición y luego ejecutar tu programa en el simulador como se muestra a continuación. Aquí demostramos cómo editar el programa <span style="color: rgb(255, 76, 65);">heartbeat</span>.

Video guía de operación:

![Img](./media/A100.png)

**Paso 3 Descargar códigos**

Generalmente, para la APP de Windows 10 ([Obtener la APP de Windows 10](https://apps.microsoft.com/detail/9pjc7sv48lcx?hl=zh-CN&gl=CN#activetab=pivot:overviewtabdocx))(Haz clic), simplemente hacer clic en “<span style="color: rgb(255, 76, 65);">Descargar</span>” descargará directamente el código a la placa micro:bit sin pasos adicionales.

Para navegadores, por favor:

Haz clic en “<span style="color: rgb(255, 76, 65);">Descargar</span>” en el editor. Esto descargará un archivo “hex”, que es un formato que la placa micro:bit puede leer. Después, cópialo a tu placa micro:bit como si copiaras un archivo a una unidad USB. En Windows, también puedes hacer clic derecho en el archivo “<span style="color: rgb(255, 76, 65);">.hex</span>” y seleccionar “**Enviar a → MICROBIT**” para copiar el archivo a la placa micro:bit.

![Img](./media/A319.png)

![Img](./media/A449.png)

O bien, puedes arrastrar directamente el archivo “<span style="color: rgb(255, 76, 65);">.hex</span>” a MICROBIT.

![Img](./media/A341.png)

![Img](./media/A345.png)

Durante la copia del archivo “<span style="color: rgb(255, 76, 65);">.hex</span>” al Micro:bit, el LED amarillo en la parte trasera de la placa parpadea. Cuando la copia termina, el LED deja de parpadear y permanece encendido.

**Paso 4 Ejecutar programa**

Después de que el programa se haya cargado en el Micro:bit, puedes alimentarlo mediante el cable USB o una fuente de alimentación externa. Entonces, la matriz de puntos LED 5 x 5 muestra un patrón de latido del corazón.

![Img](./media/A425.png)

<span style="color: rgb(255, 76, 65);">**Precaución:**</span> Cada vez que programas, el controlador del Micro:bit se expulsará automáticamente y volverá, por lo que los archivos hex desaparecerán. La placa solo tiene acceso a archivos hex pero no los guarda.

#### 1.2. MakeCode

Entra en la [versión online de Makecode Google Chrome](https://makecode.microbit.org/). Aquí está su interfaz principal.

![Img](./media/A637.png)

Hay bloques “**on start**” y “**forever**” en el área de edición de código. <span style="color: rgb(255, 76, 65);">Después de encender, el código en “on start” se ejecuta solo una vez, mientras que el código en “forever” se ejecuta cíclicamente.</span>

Haz clic en el lenguaje “**JS JavaScript**”:

![Img](./media/A754.png)

Cámbialo a “**Python**”:

![Img](./media/A814.png)


#### 1.3. Introducción a las funciones WebUSB

Como se mencionó antes, si tu ordenador es Windows 10 y has descargado la APP MakeCode, puedes descargar rápidamente los códigos a la placa con el botón “<span style="color: rgb(255, 76, 65);">Descargar</span>”. Usamos el webUSB de **<span style="color: rgb(255, 76, 65);">Google Chrome</span>** para acceder al dispositivo hardware conectado por USB.

**Emparejamiento de dispositivos:**

1\. Conecta la placa al ordenador mediante un cable USB.

![Img](./media/A951.png)

2\. Haz clic en “<span style="color: rgb(255, 76, 65);">Descargar</span>” -> “<span style="color: rgb(255, 76, 65);">...</span>” y “<span style="color: rgb(255, 76, 65);">Conectar dispositivo</span>”.

![Img](./media/A028.png)

3\. “<span style="color: rgb(255, 76, 65);">Siguiente</span>”.

![Img](./media/A046.png)

4\. “<span style="color: rgb(255, 76, 65);">Emparejar</span>”.

![Img](./media/A104.png)

5\. Luego selecciona el dispositivo correspondiente y “<span style="color: rgb(255, 76, 65);">Conectar</span>”.

![Img](./media/A127.png)

6\. “<span style="color: rgb(255, 76, 65);">Hecho</span>”.

![Img](./media/A144.png)

**Descargar programa:**

Después de la conexión, haz clic en “<span style="color: rgb(255, 76, 65);">Descargar</span>” y verás que ![Img](./media/A212.png) se convierte en ![Img](./media/A220.png). El programa se descarga a la placa micro:bit.

![Img](./media/A232.png)

Si no aparece ningún dispositivo para seleccionar, consulta [Solución de problemas de descargas con WebUSB](https://makecode.microbit.org/device/usb/webusb/troubleshoot). Consulta [la guía del usuario](https://microbit.org/guide/firmware/) para saber cómo actualizar el firmware de micro:bit.

#### 1.4. Biblioteca de extensiones MakeCode

**3.4.1 Importar extensiones de biblioteca**

Abre Makecode para entrar en un proyecto determinado, haz clic en ![Img](./media/A806.png) para elegir “**Extensiones**”.

![Img](./media/A842.png)

O haz clic en “**Extensiones**” encima de Avanzado.

![Img](./media/A900.png)

Busca la biblioteca que deseas.

![Img](./media/A909.png)

Proporcionamos los archivos de código para cada proyecto que contienen todo lo necesario para ejecutar un proyecto, por lo que puedes cargarlos directamente. Si quieres construir bloques de código tú mismo, recuerda añadir las siguientes tres extensiones.

<span style="color: rgb(0, 209, 0);">**Extensión OLED:**</span>

1\. Haz clic en “**Extensiones**” para añadir extensiones de biblioteca.

![Img](./media/A236.png)

2\. Busca “**OLED**” y haz clic en ![Img](./media/A3257.png).

![Img](./media/A306.png)

Haz clic en el primer **oled-ssd1306** y espera a que se añada.

![Img](./media/A3316.png)

3\. Añadido con éxito:

![Img](./media/A335.png)

<span style="color: rgb(0, 209, 0);">**Extensión sensor ultrasónico:**</span>

1\. Haz clic en “**Extensiones**” para añadir extensiones de biblioteca.

![Img](./media/A236.png)

2\. Busca “**sonar**” y haz clic en ![Img](./media/A3257.png) para encontrar y cargar “sonar”.

![Img](./media/A506.png)

3\. Añadido con éxito:

![Img](./media/A522.png)

<span style="color: rgb(0, 209, 0);">**Extensión sensor DHT11:**</span>

1\. Haz clic en “**Extensiones**” para añadir extensiones de biblioteca.

![Img](./media/A236.png)

2\. Busca “**DHT11**” y haz clic en ![Img](./media/A3257.png) para encontrar y cargar “DHT11_DHT22”.

![Img](./media/A616.png)

3\. Añadido con éxito:

![Img](./media/A645.png)

**3.4.2 Actualizar/Eliminar extensiones**

1\. Haz clic en “**JavaScript**” para cambiar al código de texto.

![Img](./media/A724.png)

2\. Haz clic en “**Explorador**”.

![Img](./media/A749.png)

3\. Encuentra la biblioteca “**OLED**” y haz clic en ![Img](./media/A813.png) para eliminarla.

![Img](./media/A824.png)

4\. “**Eliminar**”.

![Img](./media/A727.png)

Se ha eliminado.

#### 1.5. Cómo importar códigos a MakeCode

Tomemos el proyecto “**heartbeat**” como ejemplo para mostrar cómo cargar el código.

1\. Abre la versión web de Makecode o la app Windows 10 Makecode y haz clic en “<span style="color: rgb(255, 76, 65);">Importar</span>”.

![Img](./media/A956.png)

2\. “<span style="color: rgb(255, 76, 65);">Importar archivo...</span>”

![Img](./media/A042.png)

3\. “<span style="color: rgb(255, 76, 65);">Elegir archivo</span>” para importar el archivo que deseas cargar.

![Img](./media/A06.png)

4\. Aquí cargamos “<span style="color: rgb(255, 76, 65);">heartbeat.hex</span>”.

![Img](./media/A28.png)

5\. “<span style="color: rgb(255, 76, 65);">Continuar √</span>”

![Img](./media/A149.png)

Además del método anterior, también puedes arrastrar el código de prueba al área de edición de código, como se muestra a continuación:

![Img](./media/A202.png)

Espera a que cargue.

![Img](./media/A217.png)
