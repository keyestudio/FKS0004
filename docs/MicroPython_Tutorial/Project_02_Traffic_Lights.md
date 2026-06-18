### プロジェクト 02: 信号機

#### 1. 概要

このプロジェクトでは、micro:bit ボード上の3つのLED（赤、黄、緑）、スピーカー、および5x5 LEDマトリックスを使って信号機のモデルを作成します。

#### 2. 部品

|              ![Img](./media/A850.png)              |       ![Img](./media/A858.png)       | ![Img](./media/A906.png) |
| :-----------------------------------------------: | :---------------------------------: | :---------------------: |
|                micro:bit ボード *1                 | micro:bit T型拡張ボード *1 |   micro USB ケーブル *1    |
|              ![Img](./media/A937.png)              |      ![Img](./media/A5652.png)       | ![Img](./media/A658.png) |
|                    赤色 LED *1                     |            黄色 LED *1            |      緑色 LED *1       |
|              ![Img](./media/A944.png)              |       ![Img](./media/A950.png)       | ![Img](./media/A017.png) |
|                 220Ω 抵抗 *3                  |             ジャンパーワイヤー              |      ブレッドボード *1      |
|              ![Img](./media/A024.png)              |       ![Img](./media/A020.png)       |                         |
| バッテリーホルダー *1 <br> (<span style="color: rgb(255, 76, 65);">自前の単三電池 *2</span>)|       信号機カード *1        |                         |

#### 3. 部品の知識

**スピーカー**

![Img](./media/A833.png)

Micro:bit にはスピーカーが内蔵されており、プロジェクトで簡単に音を出すことができます。

#### 4. 配線図

![Img](./media/A908.png)

<span style="color: rgb(255, 76, 65);">**注意:** micro:bit ボードは下図のようにT型拡張ボードに差し込む必要があります。micro:bit ボードのLEDマトリックスは拡張ボードのロゴと同じ側にしてください。</span>

![Img](./media/A940.png)

#### 5. コードの流れ

![Img](./media/A5956.png)

#### 6. テストコード

コードファイルはフォルダ Project 02：Traffic Lights 内のファイル Project-02-Traffic-Lights\.py にあります。

![Img](./media/A250.png)

**完成コード:** 

```python
'''
Function: traffic lights with countdowns and buzzes
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import microbit related libraries
from microbit import *

pin1.write_digital(0) # set P1 pin to low
pin2.write_digital(0) # set P2 pin to low
pin8.write_digital(0) # set P8 pin to low

import music # import music libraries

while True:
   pin1.write_digital(1)  # P1 pin to high
   display.show('6')  # LED matrixs shows 6
   sleep(1000)        # delay 1s
   display.show('5')
   sleep(1000)
   display.show('4')
   sleep(1000)
   display.show('3')
   sleep(1000)
   display.show('2')
   sleep(1000)
   display.show('1')
   sleep(1000)
   display.show('0')
   sleep(1000)
   pin1.write_digital(0)
   pin2.write_digital(1)
   music.play("C4:4")    # speaker plays C4 tone
   display.show('2')
   sleep(500)
   pin2.write_digital(0)
   music.reset()         # no tone
   sleep(500)
   pin2.write_digital(1)
   music.play("C4:4")
   display.show('1')
   sleep(500)
   pin2.write_digital(0)
   music.reset()
   sleep(500)
   pin2.write_digital(1)
   music.play("C4:4")
   display.show('0')
   sleep(500)
   pin2.write_digital(0)
   music.reset()
   sleep(500)
   pin8.write_digital(1)
   display.show('6')
   sleep(1000)
   display.show('5')
   sleep(1000)
   display.show('4')
   sleep(1000)
   display.show('3')
   sleep(1000)
   display.show('2')
   sleep(1000)
   display.show('1')
   sleep(1000)
   display.show('0')
   sleep(1000)
   pin8.write_digital(0)
```

#### 7. テスト結果

「<span style="color: rgb(255, 76, 65);">Flash</span>」をクリックしてコードをmicro:bit ボードに書き込みます。

![Img](./media/A353.png)

コードをボードにダウンロードした後、**micro USB ケーブルまたは外部電源で電源を入れ（DIPスイッチをONにしてください）**、ボードのリセットボタンを押します。

![Img](./media/A455.png)

緑色LEDが点灯し、5×5 LEDマトリックスが6秒のカウントダウンを表示します。緑色LEDが消えた後、黄色LEDが点滅し、マトリックスはスピーカーの音とともに3秒のカウントダウンを行います。最後に赤色LEDが点灯し、6秒のカウントダウンを表示します。これらの動作が繰り返されます。

<span style="color: rgb(255, 76, 65);">**注意:** 配線が正しいのに動作しない場合は、ボード裏面のリセットボタンを押してください。</span>

![Img](./media/A459.gif)

<span style="color: rgb(255, 76, 65);">**外部電源で電源を入れる場合は、DIPスイッチをONにしてください。**</span>

![Img](./media/A904.png)
