## 1. Programming On MakeCode

The following instructions are applied for Windows system but can also serve as a reference if you are using a different system.

#### 1.1. Fast Start

**Step 1 Connect to micro:bit**

Connect the board to computer via USB cable. 

![Img](./media/A800.png)

If the red LED on the back of the board is on, that means the board is powered. When your computer communicates with the main board via the USB cable, the yellow LED on it will flashes. For example, it will flash when you burn a “.hex” file.

Then Micro: bit main board will appear on your computer as a driver named “MICROBIT”. Please note that it is not an ordinary USB disk as shown below.

![Img](./media/A849.png)

**Step 2 Write heartbeat program**

Enter the link：[online version of Makecode](https://makecode.microbit.org/)

Click “<span style="color: rgb(255, 76, 65);">New Project</span>” and you will see a “<span style="color: rgb(255, 76, 65);">Creating a project</span>”, fill it with “<span style="color: rgb(255, 76, 65);">heartbeat</span>” and click “<span style="color: rgb(255, 76, 65);">Create √</span>”.

<span style="color: rgb(255, 76, 65);">Here we write programs on Google Chrome.</span>

![Img](./media/A021.png)

Let’s write a micro:bit code. 

You can drag some Blocks to the editing area and then run your program in Simulator as shown below. Here we demonstrate how to edit <span style="color: rgb(255, 76, 65);">heartbeat</span> program. 

Operation video guide:

![Img](./media/A100.png)

**Step3 Download codes**

Generally, for Windows 10 APP ([Get Windows 10 App](https://apps.microsoft.com/detail/9pjc7sv48lcx?hl=zh-CN&gl=CN#activetab=pivot:overviewtabdocx))(Click), simply clicking the  “<span style="color: rgb(255, 76, 65);">Download</span>” will directly download the code to the micro:bit board without any additional steps.

Yet for browsers, please:

Click “<span style="color: rgb(255, 76, 65);">Download</span>” in the editor. This will download a “hex” file, which is a format that the micro:bit board can read. After that, copy it to your micro:bit board just like you would copy a file to a USB drive. On Windows, you can also right-click on the “<span style="color: rgb(255, 76, 65);">.hex</span>” file and select “**Send to → MICROBIT**” to copy the file to the micro:bit board.

![Img](./media/A319.png)

![Img](./media/A449.png)

Or, you may directly drag the “<span style="color: rgb(255, 76, 65);">.hex</span>” file into MICROBIT.

![Img](./media/A341.png)

![Img](./media/A345.png)

During copying the “<span style="color: rgb(255, 76, 65);">.hex</span>” file to the Micro: bit, the yellow LED on the back of the board flashes. When the duplication is completed, the LED will stop flashing and remain on.

**Step 4 Run porgram**

After the program is uploaded to the Micro: bit, you can power it via USB cable or an external power. Then the 5 x 5 LED dot matrix displays a heartbeat pattern.

![Img](./media/A425.png)

<span style="color: rgb(255, 76, 65);">**Caution:**</span> When you programs each time, the driver of Micro: bit will automatically eject and return so the hex files will disappear. The board only has access to hex files rather than save them.

#### 1.2. MakeCode

Enter [Makecode Google Chrome online version](https://makecode.microbit.org/) . Here is its main interface.

![Img](./media/A637.png)

There are blocks “**on start**” and “**forever**”in the code editing area. <span style="color: rgb(255, 76, 65);">After powering on, codes in “on start” only executes once, while those in “forever” runs cyclically.</span>

Click “**JS JavaScript**” language:

![Img](./media/A754.png)

Switch it to “**Python**” language:

![Img](./media/A814.png)


#### 1.3. Introduction to WebUSB Functions

As mentioned before, if your computer is Windows 10 and you have downloaded the APP MakeCode, you can quickly download codes to the board by “<span style="color: rgb(255, 76, 65);">Download</span>” button. We use the webUSB of **<span style="color: rgb(255, 76, 65);">Google Chrome</span>** to access the hardware device connected by USB. 

**Devices Pairing:**

1\. Connect the board to computer via USB cable.

![Img](./media/A951.png)

2\. Click “<span style="color: rgb(255, 76, 65);">Download</span>” -> “<span style="color: rgb(255, 76, 65);">...</span>” , and “<span style="color: rgb(255, 76, 65);">Connect device</span>”.

![Img](./media/A028.png)

3\.  “<span style="color: rgb(255, 76, 65);">Next</span>”.

![Img](./media/A046.png)

4\.  “<span style="color: rgb(255, 76, 65);">Pair</span>” .

![Img](./media/A104.png)

5\. Then select the corresponding device and  “<span style="color: rgb(255, 76, 65);">Connect</span>” . 

![Img](./media/A127.png)

6\. “<span style="color: rgb(255, 76, 65);">Done</span>”.

![Img](./media/A144.png)

**Download Program:**

After connection, click “<span style="color: rgb(255, 76, 65);">Download</span>” and you will see the ![Img](./media/A212.png) becomes ![Img](./media/A220.png). The program is downloaded to the micro:bit board. 

![Img](./media/A232.png)

If no device shows up for selection, please refer to [Troubleshooting downloads with WebUSB](https://makecode.microbit.org/device/usb/webusb/troubleshoot). Browse [the user guide](https://microbit.org/guide/firmware/) to know how to update micro:bit firmware. 

#### 1.4. MakeCode Extensions Library

**3.4.1 Import Library Extensions**

Open makecode to enter a certain project, click ![Img](./media/A806.png) to choose “**Extensions**”.

![Img](./media/A842.png)

Or click “**Extensions**”  above the Advanced.

![Img](./media/A900.png)

Search the library you want.

![Img](./media/A909.png)

We provide the code files for each project containing everything you need to run a project, so you can load it directly. If you want to build code blocks by yourself, remember to add the following three extensions.

<span style="color: rgb(0, 209, 0);">**OLED Extension:**</span>

1\. Click “**Extensions**” to add library extensions.

![Img](./media/A236.png)

2\. Search “**OLED**” and click ![Img](./media/A3257.png).

![Img](./media/A306.png)

Click the first **oled-ssd1306** and wait for it to be added.

![Img](./media/A3316.png)

3\. Add successful:

![Img](./media/A335.png)

<span style="color: rgb(0, 209, 0);">**Ultrasonic sensor extension:**</span>

1\. Click “**Extensions**” to add library extensions.

![Img](./media/A236.png)

2\. Search “**sonar**” and click![Img](./media/A3257.png) to find and load “sonar”.

![Img](./media/A506.png)

3\. Add successful:

![Img](./media/A522.png)

<span style="color: rgb(0, 209, 0);">**DHT11 sensor extension:**</span>

1\. Click “**Extensions**” to add library extensions.

![Img](./media/A236.png)

2\. Search “**DHT11**” and click ![Img](./media/A3257.png) to find and load “DHT11_DHT22”.

![Img](./media/A616.png)

3\. Add successful:

![Img](./media/A645.png)

**3.4.2 Update/Delete Extensions**

1\. Click “**JavaScript**” to switch to text code.

![Img](./media/A724.png)

2\. Click “**Explorer**”.

![Img](./media/A749.png)

3\. Find the “**OLED**” library and click ![Img](./media/A813.png) to delete it.

![Img](./media/A824.png)

4\.  “**Remove it**”.

![Img](./media/A727.png)

It is removed.

#### 1.5. How to Import Codes to MakeCode

Let’s take the “**heatbeat**” project as an example to show how to load the code. 

1\. Open the Web version of Makecode or the Windows 10 App Makecode, and click “<span style="color: rgb(255, 76, 65);">Import</span>” .

![Img](./media/A956.png)

2\. “<span style="color: rgb(255, 76, 65);">Import File...</span>”

![Img](./media/A042.png)

3\. “<span style="color: rgb(255, 76, 65);">Choose File</span>”  to import the file you want to load.

![Img](./media/A06.png)

4\. Here we load “<span style="color: rgb(255, 76, 65);">heartbeat.hex</span>” .

![Img](./media/A28.png)

5\. “<span style="color: rgb(255, 76, 65);">Go ahead √</span>”

![Img](./media/A149.png)

In addition to the above method, you can also drag the the test code into the code editing area, as shown below:

![Img](./media/A202.png)

Wait for loading.

![Img](./media/A217.png)
