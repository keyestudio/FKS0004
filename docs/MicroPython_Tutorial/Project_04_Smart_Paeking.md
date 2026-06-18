### プロジェクト04：スマート駐車

#### 1. 概要

スマート駐車場はどこにでもあります。私たちもスマート駐車場を作ることができるでしょうか？もちろんです。超音波センサーを使って前方に車両があるかどうかを検出します。車両（または物）が近づいてくるのを検出したら、サーボを制御してリフトロッドを上げます。離れていくのを検出したら、サーボはリフトロッドを下げます。

#### 2. 部品

| ![Img](./media/A850.png) |       ![Img](./media/A858.png)       |              ![Img](./media/A906.png)              |
| :---------------------: | :---------------------------------: | :-----------------------------------------------: |
|   micro:bit ボード *1    | micro:bit T型拡張ボード *1 |                micro USB ケーブル *1                 |
| ![Img](./media/A356.png) |       ![Img](./media/A309.png)       |              ![Img](./media/A415.png)              |
|  超音波センサー *1   |              サーボ *1               |                   DuPont ワイヤー                    |
| ![Img](./media/A017.png) |       ![Img](./media/A950.png)       |              ![Img](./media/A024.png)              |
|      ブレッドボード *1      |             ジャンプワイヤー              |バッテリーホルダー *1 <br> (<span style="color: rgb(255, 76, 65);">自前の単三電池 *2</span>)|
| ![Img](./media/A336.png) |       ![Img](./media/A131.png)       |                                                   |
|       バットカード *1       |          リフトロッドカード *1           |                                                   |

#### 3. 部品の知識

**サーボ**

サーボは位置駆動装置です。サーボを使って正確な位置制御や高トルク出力が可能です。通常、ロボット、リモコンカー、さらには航空機モデルで使われます。多くの仕様がありますが、すべてのサーボは3本の線を持っています：信号線（オレンジ）、正極（赤）、負極（茶色）。色はサーボのブランドによって異なります。

![Img](./media/A5525.png)

**内部構造図：**

![Img](./media/A5534.png)

① 信号線：マイコンからの制御信号を受け取る；

② ポテンショメーター：出力軸の位置を測定し、サーボ全体のフィードバック部分に属する；

③ 内部コントローラー：組み込み基板が外部制御からの信号を処理し、モーターと位置フィードバック信号を駆動する。サーボ全体のコア；

④ DCモーター：速度、トルク、位置を出力するアクチュエーター；

⑤ 伝達機構／サーボ機構：モーターのストローク出力を一定の伝達比で最終出力角度に拡大する機構。

**サーボの駆動**

PWM信号をサーボの信号線に送って出力を制御します。PWMのデューティ比が出力軸の位置を直接決定します。周期は通常20ミリ秒で、50Hzの周波数でパルスを生成するように設定されます。

<span style="color: rgb(255, 0, 0);">例えば（180°サーボ）：</span>

180°サーボに1.5ミリ秒（ms）のパルス幅を送ると、サーボの出力軸は中間位置（90度）に移動します；

パルス幅が0.5msなら、出力軸は0度に移動します；

パルス幅が2.5msなら、出力軸は180度に移動します；

![Img](./media/A5545.png)

**パラメータ：**

- 動作電圧：DC 3.3V～5V

- 動作温度：-10°C ～ +50°C

- 寸法：32.25mm x 12.25mm x 30.42mm

- インターフェース：ピッチ2.54mmの3ピンインターフェース

#### 4. 配線図

![Img](./media/A606.png)

<span style="color: rgb(255, 76, 65);">**超音波センサーとサーボを使用する場合は、必ず外部電源を接続し、DIPスイッチをONにしてください。**</span>

![Img](./media/A902.png)

![Img](./media/A701.png)

#### 5. コードフロー

![Img](./media/A716.png)

#### 6. テストコード

コードファイルはフォルダ Project 04：Smart-Parking 内のファイル Project-04-Smart-Parking\.py にあります。

![Img](./media/A3345.png)

**完成コード：** <span style="color: rgb(255, 76, 65);">条件10の閾値は実際の状況に応じて変更可能です。</span>

```python
'''
Function: smart parking
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from microbit import *
import ustruct
import machine
from time import sleep_us

distance = 0              # set variable distance initial value to 0
lastEchoDuration = 0      # set variable lastEchoDuration initial value to 0

val = Image("09990:""09090:""09990:""09000:""09000")  # set iamge
display.show(val)        # LED matrix shows image
pin0.write_analog(25.6)    # set P0 pin analog to 25.6, servo angle to 0°
sleep(200)

while True:
    pin0.set_analog_period(20) # set servo frequency
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
    if distance < 10:          # if distance < 10cm
       pin0.write_analog(77)   # servo rotate to 90°
       sleep(2000)
    else:  # or
       sleep(2000)
       pin0.write_analog(25.6)
       sleep(2000)
```

#### 7. テスト結果

「<span style="color: rgb(255, 76, 65);">Flash</span>」をクリックしてコードをmicro:bitボードに書き込みます。

![Img](./media/A3400.png)

コードをボードにダウンロードした後、**micro USBケーブルまたは外部電源で電源を入れ（DIPスイッチをONにする）、ボードのリセットボタンを押します。**

![Img](./media/A455.png)

超音波センサーが車両（または物）が近づいてくるのを検出すると、サーボがリフトロッドを上げます。センサーが離れていくのを検出すると、サーボはリフトロッドを下げます。

<span style="color: rgb(255, 76, 65);">**注意：** 配線が正しいのに結果が見えない場合は、ボードの裏側のリセットボタンを押してください。</span>

![Img](./media/A021.gif)
