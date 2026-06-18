### プロジェクト05：カー ダイヤル

#### 1. 概要

このプロジェクトでは、調整可能なポテンショメータ、サーボ、美しいダイヤルカードを組み合わせて、シンプルなカー ダイヤルモデルを作ります。

#### 2. 部品

| ![Img](./media/A850.png)  |              ![Img](./media/A858.png)              | ![Img](./media/A906.png) |
| :----------------------: | :-----------------------------------------------: | :---------------------: |
|    micro:bit ボード *1    |        micro:bit T型拡張ボード *1        |   micro USB ケーブル *1    |
| ![Img](./media/A350.png)  |              ![Img](./media/A309.png)              | ![Img](./media/A950.png) |
|     ポテンショメータ *1     |                     サーボ *1                      |       ジャンプワイヤー        |
| ![Img](./media/A017.png)  |              ![Img](./media/A024.png)              | ![Img](./media/A233.png) |
|      ブレッドボード *1       |バッテリーホルダー *1 <br> (<span style="color: rgb(255, 76, 65);">自前の単三電池 *2</span>)|  ポテンショメータカード *1  |
| ![Img](./media/A1326.png) |                                                   |                         |
|     カーダイヤルカード*1      |                                                   |                         |

#### 3. 部品の知識

**ポテンショメータ**

![Img](./media/A350.png)

ポテンショメータは3つの接点を持つ抵抗素子で、その抵抗値はある規則に従って調整可能です。

形状、サイズ、値は様々ですが、共通点は以下の通りです：

① 3つの端子（または接続点）。

② 可動ノブまたはスライダーがあり、中間端子と任意の外部端子間の抵抗を変えられる。

③ ノブを動かすと、中間端子と任意の外部端子間の抵抗が0Ωから最大値まで変化する。

ポテンショメータの回路記号：

![Img](./media/A654.png)

(1)\. 電圧分割器として

ポテンショメータは連続可変抵抗器です。スライダーを回転させると、可動接点が抵抗体上を移動します。この時、ポテンショメータにかかる電圧と可動スライダーの角度やストロークに応じて電圧を出力できます。

(2)\. 可変抵抗器として

ポテンショメータを可変抵抗器として使う場合、中間端子を回路内の2つの追加端子のいずれかに接続します。こうすることで、その範囲内で安定かつ連続的に変化する抵抗値を得られます。

(3)\. 電流制御器として

電流制御器として使う場合、可動接点を出力端子の一つとして接続します。

#### 4. 配線図

![Img](./media/A812.png)

<span style="color: rgb(255, 76, 65);">**サーボを使用する場合は、必ず外部電源を接続し、DIPスイッチをONにしてください。**</span>

![Img](./media/A902.png)

![Img](./media/A836.png)

#### 5. コードの流れ

![Img](./media/A0854.png)

#### 6. テストコード

コードファイルはフォルダ Project 05：Car Dial 内のファイル Project-05-Car-Dial\.py にあります。

![Img](./media/A3438.png)

**完成コード：**

```python
'''
Function: The potentiometer controls the servo to simulate the car dial
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import microbit related libraries
from microbit import *

display.show(Image.HAPPY)  # LED matrix displays a smile face
pin0.write_analog(25.6)    # set P0 pin analog to 25.6, servo initial angle to 0°
sleep(200)

# map function
def map(value,fromLow,fromHigh,toLow,toHigh):
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow

while True:
    value=pin2.read_analog()    # Read the analog value of the potentiometer (ADC value)
    pin0.set_analog_period(20)  # set servo frequency
    pin0.write_analog(map(value,0,1023,25.6,128))  # Map the analog value of the potentiometer to that of the servo
    sleep(20)
```

#### 7. テスト結果

「<span style="color: rgb(255, 76, 65);">Flash</span>」をクリックしてコードをmicro:bitボードに書き込みます。

![Img](./media/A3457.png)

コードをボードにダウンロードした後、**micro USBケーブルまたは外部電源で電源を入れ（DIPスイッチをONにする）、ボードのリセットボタンを押します。**

![Img](./media/A455.png)

ポテンショメータのノブを回すと、サーボがダイヤルのポインタを動かします。

<span style="color: rgb(255, 76, 65);">**注意：** 配線が正しいのに動作しない場合は、ボード裏面のリセットボタンを押してください。</span>

![Img](./media/A706.gif)
