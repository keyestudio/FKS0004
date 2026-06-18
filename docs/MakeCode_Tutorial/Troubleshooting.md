## 3. Solución de Problemas

#### MAINTENANCE: El código no se descarga en Micro:bit

**1. Problema**

Recientemente, muchos usuarios encuentran el problema de que la placa Micro:bit no responde al descargar el código.

Si la forma en que operas es correcta, tal vez presionaste accidentalmente el botón de reinicio y entraste en modo MAINTENANCE o el firmware se perdió debido a una mala operación.

Conecta la placa Micro:bit, aparece la unidad “<span style="color: rgb(255, 76, 65);">MAINTENANCE</span>”, lo que significa que el programa no se puede descargar.

![Img](./media/A158.png)

**2. Soluciones**

(1) Descarga el archivo <span style="color: rgb(255, 76, 65);">.hex</span> desde esta página a tu computadora.

Descarga [el firmware más reciente de micro:bit-0255](https://www.microbit.org/get-started/user-guide/firmware/). Si no deseas descargarlo desde este sitio web, también lo proporcionamos en nuestro tutorial.

(2) Después de descargar el firmware más reciente, arrastra Firmware para V2.20_V2.21 a la unidad “<span style="color: rgb(255, 76, 65);">MAINTENANCE</span>” para que Micro:bit vuelva al modo normal.

<span style="color: rgb(255, 76, 65);">Instalamos diferentes firmwares según los modelos de placa micro:bit. Aquí es Firmware para V2.20_V2.21.</span>

![Img](./media/A326.png)

![Img](./media/A331.png)

**3. Evitar entrar en “MAINTENANCE”**

(1) Asegúrate de no presionar el botón de reinicio al conectar la placa con el cable USB.

![Img](./media/A228.png)

(2) No desconectes el cable repentinamente durante la descarga del programa micro:bit, de lo contrario, el firmware se perderá y micro:bit entrará en modo “MAINTENANCE”.

(3) En el experimento, una conexión incorrecta también puede causar un cortocircuito o pérdida del firmware.

#### Solución de problemas de descargas con WebUSB

Haz clic: [Solución de problemas de descargas con WebUSB](https://makecode.microbit.org/device/usb/webusb/troubleshoot)

¿Tienes problemas para emparejar tu micro:bit con WebUSB? ¡Vamos a intentar descubrir por qué!

**Paso 1: Verifica tu cable**

Asegúrate de que tu micro:bit esté conectado a tu computadora con un cable micro USB. Por ejemplo, en el Explorador de Windows deberías ver que aparece una unidad **MICROBIT** cuando está conectado.

![Img](./media/A321.png)

Si puedes ver la unidad MICROBIT, pasa al paso 2. Si no puedes ver la unidad:

(1) Asegúrate de que el cable USB funcione.

¿Funciona el cable en otra computadora? Si no, busca otro cable para usar. Algunos cables solo proporcionan conexión de energía y no transfieren datos realmente.

(2) Prueba otro puerto USB en tu computadora.

¿El cable está bien pero aún no ves la unidad MICROBIT? Hmm, podrías tener un problema con tu micro:bit.

Prueba los pasos adicionales descritos en la [página de solución de problemas en microbit.org](https://support.microbit.org/support/solutions/articles/19000024000-fault-finding-with-a-micro-bit). Si esto no ayuda, puedes [crear un ticket de soporte](https://support.microbit.org/support/tickets/new) para notificar a la Fundación Micro:bit del problema. Omite los pasos restantes de solución de problemas.

**Paso 2: Verifica la versión de tu firmware**

Si tus descargas aún no funcionan, es posible que la versión del firmware en el micro:bit necesite una actualización. Vamos a comprobarlo:

1. Ve a la unidad **MICROBIT**;

2. Abre el archivo <span style="color: rgb(255, 76, 65);">DETAILS.TXT</span>;

![Img](./media/A0452.png)

3. Encuentra el número de versión del firmware; Busca una línea en el archivo que diga el número de versión. Debe decir Version:

![Img](./media/A501.png)

Si la versión es 0234, 0241, 0243 NECESITAS actualizar el firmware de tu micro:bit. Ve al Paso 3 y sigue las instrucciones de actualización.

Si la versión es 0249, 0250 o superior, tienes el firmware correcto, pasa al paso 4.

**Paso 3: Actualiza el firmware**

(1) Pon tu micro:bit en modo MAINTENANCE.

Para hacer esto, desconecta el cable USB del micro:bit y luego vuelve a conectar el cable USB mientras mantienes presionado el botón de reinicio. Una vez que insertes el cable, puedes soltar el botón de reinicio.

Ahora deberías ver una unidad MAINTENANCE en lugar de la unidad MICROBIT como antes. Además, un LED amarillo permanecerá encendido junto al botón de reinicio.

![maintenance](./media/maintenance.gif)

(2) Descarga el [archivo .hex del firmware](https://microbit.org/guide/firmware/).

<span style="color: rgb(255, 76, 65);">Instalamos diferentes firmwares según los modelos de placa micro:bit. Aquí es Firmware para V2.20_V2.21.</span>

![Img](./media/A0629.png)

(3) Arrastra y suelta ese archivo en la unidad **MAINTENANCE**.

(4) Observa el LED parpadeante.

El LED amarillo parpadeará mientras se copia el archivo HEX. Cuando la copia termine, el LED se apagará y el micro:bit se reiniciará. La unidad MAINTENANCE ahora cambia de nuevo a MICROBIT.

(5) Actualización completa.

¡La actualización está completa! Puedes abrir el archivo <span style="color: rgb(255, 76, 65);">DETAILS.TXT</span> para verificar que la versión del firmware cambió y coincide con la versión del archivo HEX que copiaste.

Si quieres saber más sobre cómo conectar la placa, el modo MAINTENANCE y la actualización del firmware, léelo en la [Guía de Firmware](https://microbit.org/guide/firmware/).

**Paso 4: Verifica la versión de tu navegador**

WebUSB es una función bastante nueva y puede requerir que actualices tu navegador. Verifica que la versión de tu navegador coincida con una de las siguientes: versiones de navegador para Android, Chrome OS, Linux, macOS y Chrome 65+ para Windows 10.

**Paso 5: Emparejar dispositivo**

Una vez que hayas actualizado el firmware, abre el navegador Chrome, ve al editor y haz clic en Emparejar dispositivo en el menú del engranaje. Consulta [WebUSB(/device/usb/webusb)](https://microbit.org/get-started/user-guide/web-usb/) para instrucciones de emparejamiento.

¡Disfruta de descargas rápidas!
