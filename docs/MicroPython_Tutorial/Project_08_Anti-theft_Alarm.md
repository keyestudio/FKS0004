### プロジェクト08：防犯アラーム

#### 1. 概要

スマート防犯アラームが防犯ボックスの移動を検知すると、micro:bitボードのスピーカーがアラームを鳴らし、赤色LEDが点滅します。

#### 2. 部品

| ![Img](./media/A850.png) |              ![Img](./media/A858.png)              | ![Img](./media/A906.png) |
| :---------------------: | :-----------------------------------------------: | :---------------------: |
|   micro:bitボード *1    |        micro:bit T型拡張ボード *1                 |   micro USBケーブル *1  |
| ![Img](./media/A937.png) |              ![Img](./media/A944.png)              | ![Img](./media/A950.png) |
|       赤色LED *1        |                 220Ω抵抗 *1                        |      ジャンパーワイヤー *2       |
| ![Img](./media/A017.png) |              ![Img](./media/A024.png)              | ![Img](./media/A952.png) |
|      ブレッドボード *1      |電池ホルダー *1 <br> (<span style="color: rgb(255, 76, 65);">自前の単三電池 *2</span>)|      アラームカード *1      |

#### 3. 部品の知識

**加速度センサー**

![Img](./media/A026.png)

micro:bitボードにはLSM303AGR加速度センサー（加速度計）が内蔵されており、標準、ファスト、プラス、高速モード（100 kHz、400 kHz、1 MHz、3.4 MHz）のI2CシリアルバスインターフェースとSPIシリアル標準インターフェースを備えています。分解能は8/10/12ビットで、測定範囲は±2g、±4g、または±8gです。

micro:bitボードが静止または等速運動中の場合、加速度計は重力加速度のみを検出します。わずかに揺らすと検出される加速度は重力加速度よりかなり小さいため、その差は無視できます。したがって、主にx、y、z軸の重力加速度の変化を検出します。

#### 4. 配線図

![Img](./media/A219.png)

<span style="color: rgb(255, 76, 65);">LEDのボード制御ピンはP1です（T型拡張ボードのピンはデジタル1）。</span>

#### 5. コードの流れ

![Img](./media/A4434.png)

#### 6. テストコード

コードファイルはフォルダ Project 08：Burglar Alarm 内のファイル Project-08-Burglar-Alarm\.py にあります。

![Img](./media/A3743.png)

**完成コード：**

<span style="color: rgb(255, 76, 65);">**コードをインポート後、ブレッドボードを動かしていないのにブザーが鳴り続ける場合は、地理的要因が原因かもしれません。条件内の閾値 -60 と 50 を実際の状況に合わせて調整してください。**</span>

```python
'''
Function: The accelerometer controls a buzzer and LED to simulate a anti-theft alarm
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from microbit import *
import music

display.show(Image.HAPPY) # LED matrix displays a smile face

while True:
    if accelerometer.get_x()<-60 or accelerometer.get_x()>50: # If the value of the accelerometer in the X direction is less than -60 or greater than 50
       music.play("C4:4")      # speaker plays C4 tone
       pin1.write_digital(1)   # P1 pin value is high, LED on
       sleep(200)
       pin1.write_digital(0)   # P1 pin value is low, LED off
       sleep(200)
       display.show(Image.NO)  # LED matrix shows X
    else:  # or
        display.show(Image.HAPPY) # LED matrix displays a smile face
        pin1.write_digital(0)
        music.reset()             # no tone
```

#### 7. テスト結果

「<span style="color: rgb(255, 76, 65);">Flash</span>」をクリックしてコードをmicro:bitボードに書き込みます。

![Img](./media/A3757.png)

コードを書き込んだ後、**micro USBケーブルまたは外部電源で電源を入れ（DIPスイッチをONにする）、ボードのリセットボタンを押します。**

![Img](./media/A455.png)

コードを書き込んだ後、ブレッドボードを動かします。加速度値 x＜-60 または x＞50 の場合、ボードのスピーカーがアラームを鳴らし、LEDが点滅し、micro:bitのLEDマトリックスに ![Img](./media/A706.png) が表示されます。そうでなければ、スピーカーは音を出さずLEDは消灯し、micro:bitのLEDマトリックスに ![Img](./media/A720.png) が表示されます。

<span style="color: rgb(255, 76, 65);">**注意：** 配線が正しいのに結果が見えない場合は、ボード裏面のリセットボタンを押してください。</span>

![Img](./media/A936.gif)
