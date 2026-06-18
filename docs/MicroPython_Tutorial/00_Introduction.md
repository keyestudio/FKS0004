## 1. About Mu Software

### 1.1. Install MU

Click to visit [Mu software official website](https://codewith.mu/).

Mu is a Python code editor for beginner programmers, like teachers and students. We can get it by the official installer for Windows, Mac OSX or Linux (Mu no longer supports 32-bit Windows). The recommended version is Mu 1.2.0. 

**Step 1 - Make sure your OS so then download Mu Installer**

First find out your computer operating system (Windows or Mac OSX). Open “**This PC**” to see  “**Properties**”.

![Img](./media/A225.png)

Check the system type: 64-bit or 32-bit.

![Img](./media/A253.png)

[Download MU](https://codewith.mu/en/download). Download the version according to your computer operating system.

![Img](./media/A348.png)

<span style="color: rgb(255, 76, 65);">Here we take the Windows system as an example, which can be a reference for Mac OSX and Linux.</span>

![Img](./media/A422.png)

**Step 2 - Run the installer**

Double-click the installer (it is probably in your Downloads folder) to run it.

![Img](./media/A440.png)

We’ve outlined the extra steps needed to help Windows install Mu for Windows 10. Other versions will be similar. 

[Mu installer for MacOS](https://codewith.mu/en/howto/1.1/install_macos). 

[Mu installer for Linux system](https://codewith.mu/en/howto/1.2/install_linux). 

 

For Windows 10, the Defender will pop up with a warning message. You should click on the “**More info**” link.

![Img](./media/A615.png)

The message will change giving you more information about the installer and display a “**Run anyway**” button. Click “**Run anyway**”.

![Img](./media/A626.png)

**Step 3 - License Agreement**

Review the license, select the check box and click “**Install**” .

![Img](./media/A1716.png)

**Step 4 - Installing**

Go make a cup of coffee as Mu installs on your computer.

![Img](./media/A1740.png)

**Step 5 - Complete**

The installation has completed successfully, click “**Finish**” to close the installer.

![Img](./media/A817.png)

**Step 6 - Start Mu**

You can start Mu by clicking on the icon in the Start menu or by typing “Mu” into the search box (both highlighted below). On first start, this may take some time.

![Img](./media/A852.png)

Here’s what it looks like:

![Img](./media/A909.png)

### 1.2. Using Modes & Menu Bar

Set  “<span style="color: rgb(255, 76, 65);">Mode</span>” to BBC micro:bit .

On the menu, click “**Mode**” to set it to “**BBC micro：bit**”. The micro:bit mode understands how to interact with and connect to a micro:bit.

![Img](./media/A022.png)

Click to [Start with Mu](https://codewith.mu/en/tutorials/1.1/start). 

For more tutorials on using Mu, please visit: https://codewith.mu/en/tutorials/

### 1.3. Program on Mu

Here we load the “<span style="color: rgb(255, 76, 65);">heartbeat\.py</span>” to Mu. Find it in the folder “<span style="color: rgb(255, 76, 65);">Heart beat</span>” we provided.

![Img](./media/A200.png)

**Method one:**

Open the Mu and click “<span style="color: rgb(255, 76, 65);">Load</span>”  to choose the path where you downloaded the code.

![Img](./media/A341.png)

![Img](./media/A345.png)

Loaded successfully, as shown below:

![Img](./media/A354.png)

**Method two:** 

Click “new” ![Img](./media/A503.png)to create a new program and drag “heartbeat\.py” into it:

![Img](./media/A521.png)

Loaded successfully, as shown below:

![Img](./media/A533.png)

<span style="color: rgb(255, 76, 65);">The same is true for adding other codes.</span>

### 1.4. Download Code to Mciro:bit

Connect the board to computer via USB cable.

![Img](./media/A252.png)

Click “<span style="color: rgb(255, 76, 65);">**Flash**</span>” to download the code to the micro:bit board.

![Img](./media/A3728.png)

After that, <span style="color: rgb(255, 76, 65);">**power on by the micro USB cable or external power supply (turn DIP switch to ON)**</span>. You will see the on-board 5×5 LED matrix repeatedly shows ![Img](./media/A903.png) and then ![Img](./media/A910.png).

<span style="color: rgb(255, 76, 65);">**Note that if there is an error in your code, it can also be able to download yet it will not work properly.**</span>

<span style="color: rgb(0, 209, 0);">For example, the function sleep() is written as sleeps() in the code. Click “**Flash**” to load code to micro:bit. However, the 5×5 LED matrix shows messy icons. </span>

![Img](./media/A4003.png)

In this case, click “**REPL**”  and press the reset button on the board on its back. The error message will be displayed in the REPL interface, as shown below:

![Img](./media/A029.png)

![Img](./media/A033.png)

Click “**REPL**” again to close REPL. And then click “<span style="color: rgb(255, 76, 65);">**Flash**</span>”.

To ensure that the code is correct, click “<span style="color: rgb(255, 76, 65);">**Check**</span>” after completing, and Mu will point out the error in the code.

![Img](./media/A119.png)

Modify the code according to the error message, and click “<span style="color: rgb(255, 76, 65);">**Check**</span>” again. Mu does not show an error.

![Img](./media/A134.png)

See [more tutorials explaining specific aspects of Mu](https://codewith.mu/en/tutorials/). 

## 2. How Mu Import Library to Micro:bit

<span style="color: rgb(255, 76, 65);">Before importing libraries, we need to upload a .py code (empty code is also ok) to the micro:bit board. Here we take an empty code as an example.</span>

Connect the board to computer via USB cable. Open the Mu and click “Flash” to upload the .py code (empty code) to the board.

![Img](./media/A252.png)

In this tutorial, OLED and DHT11 modules are used. Therefore, the “<span style="color: rgb(255, 76, 65);">**oled_ssd1306\.py**</span>” and “<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>” library files need to be imported into the micro:bit board. 

The default directory for Mu to save files is “mu_code”in the root directory of the user’s directory. 

References link: [https://codewith.mu/en/tutorials/1.0/files](https://codewith.mu/en/tutorials/1.0/files)

**Instructions for importing libraries:**

1\. Search for the “<span style="color: rgb(255, 76, 65);">mu_code</span>” folder on the Disk(C:).

![Img](./media/A543.png)

![Img](./media/A550.png)

2\. Open “<span style="color: rgb(255, 76, 65);">mu_code</span>”.

![Img](./media/A628.png)

3\. Copy and paste the library files “<span style="color: rgb(255, 76, 65);">**oled_ssd1306\.py**</span>” and “<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>” to “<span style="color: rgb(255, 76, 65);">**Libraries**</span>”.

![Img](./media/A4716.png)

4\. As shown below:

![Img](./media/A735.png)

5\. Open the Mu and click “<span style="color: rgb(255, 76, 65);">**Files**</span>”. Here we drag  “<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>” library into micro:bit.

![Img](./media/A816.png)

![Img](./media/A820.png)

6\. After importing “<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>”, you'll see it in the box on the left.

![Img](./media/A841.png)

7\. Let’s do the same thing to the “<span style="color: rgb(255, 76, 65);">**oled_ssd1306\.py**</span>”.

![Img](./media/A916.png)

![Img](./media/A4920.png)

<span style="color: rgb(255, 76, 65);">**Note that when you upload other files to the micro:bit, they will overwrite the original content so you need to re-import it for the next time you use.**</span>
