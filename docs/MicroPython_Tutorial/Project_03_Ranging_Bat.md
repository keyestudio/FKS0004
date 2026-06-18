### プロジェクト03：距離測定バット

#### 1. 概要

超音波センサーをベースに、距離測定バットは障害物までの距離を検出し、OLEDにリアルタイムで表示します。距離が10cm未満になると、スピーカーが警報を鳴らします。

#### 2. 部品

| ![Img](./media/A850.png) |       ![Img](./media/A858.png)       |              ![Img](./media/A906.png)              |
| :---------------------: | :---------------------------------: | :-----------------------------------------------: |
|   micro:bit ボード *1    | micro:bit T型拡張ボード *1 |                micro USB ケーブル *1                 |
| ![Img](./media/A356.png) |       ![Img](./media/A406.png)       |              ![Img](./media/A415.png)              |
|  超音波センサー *1   |           OLED モジュール *1            |                   DuPont ワイヤー                    |
| ![Img](./media/A017.png) |       ![Img](./media/A950.png)       |              ![Img](./media/A024.png)              |
|      ブレッドボード *1      |             ジャンプワイヤー              | 電池ホルダー *1 <br> (<span style="color: rgb(255, 76, 65);">自前の単三電池 *2</span>)|
| ![Img](./media/A315.png) |       ![Img](./media/A557.png)       |                                                   |
|       バットカード *1       |            OLEDカード *1             |                                                   |

#### 3. 部品の知識

**超音波センサー**

超音波は障害物に当たると跳ね返ります。送信と受信の間の時間差を計測することで距離を測定します。空気中の音速は一定で v=340m/s なので、センサーと障害物間の距離は s=vt/2 で計算します。

![Img](./media/A846.png)

HC-SR04超音波モジュールは送信機と受信機を統合しています。送信機は電気信号（電気エネルギー）を高周波（人間の聴覚を超える）音波（機械エネルギー）に変換し、受信機はその逆を行います。

HC SR04の回路図：

![Img](./media/A642.png)

**ピン定義：**

![Img](./media/A702.png)

**パラメータ：**

- 動作電圧：5V
- 動作電流：12mA
- 最小測定距離：2cm
- 最大測定距離：200cm

**動作原理：**

Trigピンに10μs以上の高レベルパルスを出力すると、モジュールは超音波の送信を開始します。同時にEchoピンがプルアップされます。障害物に当たった超音波を受信すると、Echoピンはプルダウンされます。Echoピンの高レベルの継続時間は送信から受信までの合計時間であり、距離は s=vt/2 で計算されます。

![Img](./media/A728.png)

**OLEDモジュール**

OLED技術は豊かな色彩表現、高いコントラスト、広い視野角を特徴とし、特に黒色が際立った鮮明で生き生きとした画像を提供します。

OLEDディスプレイの各ピクセルは自発光でバックライトを必要としないため、比較的低消費電力です。小型で高解像度、低消費電力の0.9インチOLEDディスプレイはウェアラブルデバイスに非常に適しています。

![Img](./media/A636.png)

<span style="color: rgb(255, 76, 65);">**このプロジェクトでは、OLEDディスプレイモジュールのSDAインターフェースをピンP20に、SCLをピンP19に接続します。**</span>

**パラメータ：**

- 動作電圧：DC 3.3V-5V

- 動作電流：30mA

- インターフェース：ピンポート間隔2.54mm

- 通信方式：I2C

- 内蔵ドライバーチップ：SSD1306

- 解像度：128*64

- 視野角：150°以上

#### 4. 配線図

![Img](./media/A1849.png)

<span style="color: rgb(255, 76, 65);">**OLEDディスプレイと超音波センサーを使用する際は、外部電源を接続し、DIPスイッチをONにしてください。**</span>

![Img](./media/A902.png)

![Img](./media/A1906.png)

#### 5. ライブラリのインポート

必要なライブラリファイル（oled_ssd1306）をまだ追加していない場合は、[How Mu Import Library to Micro:bit](https://docs.keyestudio.com/projects/FKS0004/en/latest/docs/MicroPython_Tutorial/MicroPython_Tutorial.html#how-mu-import-library-to-micro-bit) を参照してインポートしてください。

#### 6. コードの流れ

![Img](./media/A924.png)

#### 7. テストコード

コードファイルはフォルダ Project 03：Ranging Bat 内のファイル Project-03-Ranging-Bat\.py にあります。

![Img](./media/A302.png)

**完成コード：** <span style="color: rgb(255, 76, 65);">**条件の10という閾値は実際の状況に応じて変更可能です。**</span>

```python
'''
Function: bat ranging
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from microbit import *
import ustruct
import machine
from time import sleep_us
import oled_ssd1306 as oled
import music

display.show(Image.HAPPY) # LED matrix displays a smile face
distance = 0              # set variable distance initial value to 0
lastEchoDuration = 0      # set variable lastEchoDuration initial value to 0

# initialize and clear oled
oled.initialize()
oled.clear_oled()

while True:
    # Ultrasonic sensor sends and receives signals
    pin1.write_digital(0)
    sleep_us(2)
    pin1.write_digital(1)
    sleep_us(15)
    pin1.write_digital(0)

    # measure the time interval between "when rising edge detected from the pin2" and "until the pin becomes low again"
    # unit is μs. Assign the interval to variable t.
    t = machine.time_pulse_us(pin2, 1, 35000)

    # a conditional statement, used to check whether the values of two variables t and lastechoduration satisfy specific conditions.
    # If both conditions are met, the block of code under the condition statement is executed.
    if (t <= 0 and lastEchoDuration >= 0):
        t = lastEchoDuration   # variable t = variable lastechoduration
    else:
        lastEchoDuration = t
    distance = int(t * 0.017)  # calculate distance
    oled.clear_oled()          # clear OLED
    oled.add_text(1, 0, str(distance) + 'cm')  # Display distance in the corresponding position of OLED
    sleep(200)
    if distance < 10:       # if distance < 10cm
        music.play("C4:4")  # speaker plays C4 tone
        sleep(200)          # delay 
        music.reset()       # no tone
        sleep(200)
```

#### 8. テスト結果

「<span style="color: rgb(255, 76, 65);">Flash</span>」をクリックしてコードをmicro:bitボードに書き込みます。

![Img](./media/A3323.png)

コードをボードにダウンロードした後、**micro USBケーブルまたは外部電源で電源を入れ（DIPスイッチをONにする）、ボードのリセットボタンを押します。**

![Img](./media/A455.png)

OLEDには超音波センサーと障害物間の距離がリアルタイムで表示されます。距離が10cm未満になると、micro:bitボードのスピーカーが警報を鳴らします。

<span style="color: rgb(255, 76, 65);"><span style="color: rgb(255, 76, 65);">**注意：** 配線が正しいのに結果が見えない場合は、ボード裏面のリセットボタンを押してください。</span></span>

![Img](./media/A605.gif)
