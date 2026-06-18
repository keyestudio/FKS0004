## 1. Sobre el software Mu

### 1.1. Instalar MU

Haz clic para visitar la [página oficial del software Mu](https://codewith.mu/).

Mu es un editor de código Python para programadores principiantes, como profesores y estudiantes. Podemos obtenerlo mediante el instalador oficial para Windows, Mac OSX o Linux (Mu ya no soporta Windows de 32 bits). La versión recomendada es Mu 1.2.0.

**Paso 1 - Asegúrate de tu sistema operativo y luego descarga el instalador de Mu**

Primero averigua el sistema operativo de tu computadora (Windows o Mac OSX). Abre “**Este equipo**” para ver “**Propiedades**”.

![Img](./media/A225.png)

Verifica el tipo de sistema: 64 bits o 32 bits.

![Img](./media/A253.png)

[Descargar MU](https://codewith.mu/en/download). Descarga la versión según el sistema operativo de tu computadora.

![Img](./media/A348.png)

<span style="color: rgb(255, 76, 65);">Aquí tomamos el sistema Windows como ejemplo, que puede servir de referencia para Mac OSX y Linux.</span>

![Img](./media/A422.png)

**Paso 2 - Ejecutar el instalador**

Haz doble clic en el instalador (probablemente esté en tu carpeta de Descargas) para ejecutarlo.

![Img](./media/A440.png)

Hemos detallado los pasos adicionales necesarios para ayudar a Windows a instalar Mu en Windows 10. Otras versiones serán similares.

[Instalador Mu para MacOS](https://codewith.mu/en/howto/1.1/install_macos).

[Instalador Mu para sistema Linux](https://codewith.mu/en/howto/1.2/install_linux).

Para Windows 10, Defender mostrará un mensaje de advertencia. Debes hacer clic en el enlace “**Más información**”.

![Img](./media/A615.png)

El mensaje cambiará proporcionando más información sobre el instalador y mostrará un botón “**Ejecutar de todas formas**”. Haz clic en “**Ejecutar de todas formas**”.

![Img](./media/A626.png)

**Paso 3 - Acuerdo de licencia**

Revisa la licencia, selecciona la casilla y haz clic en “**Instalar**”.

![Img](./media/A1716.png)

**Paso 4 - Instalando**

Ve a prepararte una taza de café mientras Mu se instala en tu computadora.

![Img](./media/A1740.png)

**Paso 5 - Completar**

La instalación se ha completado con éxito, haz clic en “**Finalizar**” para cerrar el instalador.

![Img](./media/A817.png)

**Paso 6 - Iniciar Mu**

Puedes iniciar Mu haciendo clic en el icono en el menú Inicio o escribiendo “Mu” en el cuadro de búsqueda (ambos resaltados abajo). En el primer inicio, puede tardar un poco.

![Img](./media/A852.png)

Así es como se ve:

![Img](./media/A909.png)

### 1.2. Usar Modos y Barra de Menú

Configura el “<span style="color: rgb(255, 76, 65);">Modo</span>” a BBC micro:bit.

En el menú, haz clic en “**Modo**” para configurarlo a “**BBC micro：bit**”. El modo micro:bit entiende cómo interactuar y conectarse con un micro:bit.

![Img](./media/A022.png)

Haz clic para [Comenzar con Mu](https://codewith.mu/en/tutorials/1.1/start).

Para más tutoriales sobre el uso de Mu, visita: https://codewith.mu/en/tutorials/

### 1.3. Programar en Mu

Aquí cargamos el “<span style="color: rgb(255, 76, 65);">heartbeat\.py</span>” en Mu. Encuéntralo en la carpeta “<span style="color: rgb(255, 76, 65);">Heart beat</span>” que proporcionamos.

![Img](./media/A200.png)

**Método uno:**

Abre Mu y haz clic en “<span style="color: rgb(255, 76, 65);">Cargar</span>” para elegir la ruta donde descargaste el código.

![Img](./media/A341.png)

![Img](./media/A345.png)

Cargado exitosamente, como se muestra a continuación:

![Img](./media/A354.png)

**Método dos:**

Haz clic en “nuevo” ![Img](./media/A503.png) para crear un nuevo programa y arrastra “heartbeat\.py” dentro de él:

![Img](./media/A521.png)

Cargado exitosamente, como se muestra a continuación:

![Img](./media/A533.png)

<span style="color: rgb(255, 76, 65);">Lo mismo aplica para agregar otros códigos.</span>

### 1.4. Descargar código a Micro:bit

Conecta la placa a la computadora mediante un cable USB.

![Img](./media/A252.png)

Haz clic en “<span style="color: rgb(255, 76, 65);">**Flash**</span>” para descargar el código a la placa micro:bit.

![Img](./media/A3728.png)

Después, <span style="color: rgb(255, 76, 65);">**enciende con el cable micro USB o fuente de alimentación externa (gira el interruptor DIP a ON)**</span>. Verás que la matriz LED 5×5 integrada muestra repetidamente ![Img](./media/A903.png) y luego ![Img](./media/A910.png).

<span style="color: rgb(255, 76, 65);">**Ten en cuenta que si hay un error en tu código, también puede descargarse pero no funcionará correctamente.**</span>

<span style="color: rgb(0, 209, 0);">Por ejemplo, la función sleep() está escrita como sleeps() en el código. Haz clic en “**Flash**” para cargar el código al micro:bit. Sin embargo, la matriz LED 5×5 muestra íconos desordenados.</span>

![Img](./media/A4003.png)

En este caso, haz clic en “**REPL**” y presiona el botón de reinicio en la parte trasera de la placa. El mensaje de error se mostrará en la interfaz REPL, como se muestra a continuación:

![Img](./media/A029.png)

![Img](./media/A033.png)

Haz clic en “**REPL**” nuevamente para cerrar REPL. Luego haz clic en “<span style="color: rgb(255, 76, 65);">**Flash**</span>”.

Para asegurarte de que el código es correcto, haz clic en “<span style="color: rgb(255, 76, 65);">**Comprobar**</span>” después de terminar, y Mu señalará el error en el código.

![Img](./media/A119.png)

Modifica el código según el mensaje de error y haz clic en “<span style="color: rgb(255, 76, 65);">**Comprobar**</span>” de nuevo. Mu no mostrará error.

![Img](./media/A134.png)

Consulta [más tutoriales que explican aspectos específicos de Mu](https://codewith.mu/en/tutorials/).

## 2. Cómo Mu importa librerías a Micro:bit

<span style="color: rgb(255, 76, 65);">Antes de importar librerías, necesitamos subir un código .py (un código vacío también está bien) a la placa micro:bit. Aquí tomamos un código vacío como ejemplo.</span>

Conecta la placa a la computadora mediante un cable USB. Abre Mu y haz clic en “Flash” para subir el código .py (código vacío) a la placa.

![Img](./media/A252.png)

En este tutorial, se usan los módulos OLED y DHT11. Por lo tanto, los archivos de librería “<span style="color: rgb(255, 76, 65);">**oled_ssd1306\.py**</span>” y “<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>” deben importarse a la placa micro:bit.

El directorio predeterminado donde Mu guarda archivos es “mu_code” en el directorio raíz del usuario.

Enlace de referencia: [https://codewith.mu/en/tutorials/1.0/files](https://codewith.mu/en/tutorials/1.0/files)

**Instrucciones para importar librerías:**

1\. Busca la carpeta “<span style="color: rgb(255, 76, 65);">mu_code</span>” en el Disco (C:).

![Img](./media/A543.png)

![Img](./media/A550.png)

2\. Abre “<span style="color: rgb(255, 76, 65);">mu_code</span>”.

![Img](./media/A628.png)

3\. Copia y pega los archivos de librería “<span style="color: rgb(255, 76, 65);">**oled_ssd1306\.py**</span>” y “<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>” en “<span style="color: rgb(255, 76, 65);">**Libraries**</span>”.

![Img](./media/A4716.png)

4\. Como se muestra a continuación:

![Img](./media/A735.png)

5\. Abre Mu y haz clic en “<span style="color: rgb(255, 76, 65);">**Archivos**</span>”. Aquí arrastramos la librería “<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>” al micro:bit.

![Img](./media/A816.png)

![Img](./media/A820.png)

6\. Después de importar “<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>”, la verás en el cuadro a la izquierda.

![Img](./media/A841.png)

7\. Hagamos lo mismo con “<span style="color: rgb(255, 76, 65);">**oled_ssd1306\.py**</span>”.

![Img](./media/A916.png)

![Img](./media/A4920.png)

<span style="color: rgb(255, 76, 65);">**Ten en cuenta que cuando subes otros archivos al micro:bit, sobrescribirán el contenido original, por lo que necesitas reimportarlos para la próxima vez que los uses.**</span>
