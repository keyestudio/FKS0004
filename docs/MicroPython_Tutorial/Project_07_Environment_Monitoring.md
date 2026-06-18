### プロジェクト07：環境モニタリング

#### 1. 概要

OLEDには、DHT11センサーで検出した温度と湿度の値をリアルタイムで表示し、さらに基板上の光センサーで検出した周囲の明るさレベルの値も表示するスマート環境モニタリングシステムです。

#### 2. コンポーネント

|         ![Img](./media/A850.png)          |       ![Img](./media/A858.png)       |              ![Img](./media/A906.png)              |
| :--------------------------------------: | :---------------------------------: | :-----------------------------------------------: |
|            micro:bit ボード *1            | micro:bit T型拡張ボード *1 |                micro USB ケーブル *1                 |
|         ![Img](./media/A2637.png)         |       ![Img](./media/A406.png)       |              ![Img](./media/A415.png)              |
| XHT11 温湿度センサー *1 |           OLED モジュール *1            |                   DuPont ワイヤー                    |
|         ![Img](./media/A017.png)          |       ![Img](./media/A950.png)       |              ![Img](./media/A024.png)              |
|              ブレッドボード *1               |             ジャンプワイヤー              |バッテリーホルダー *1 <br> (<span style="color: rgb(255, 76, 65);">自前の単三電池 *2</span>)|
|         ![Img](./media/A0715.png)         |       ![Img](./media/A557.png)       |                                                   |
|              クラウドカード *1               |            OLEDカード *1             |                                                   |

#### 3. コンポーネント知識

**XHT11 温湿度センサー**

![Img](./media/A2637.png)

XHT11 温湿度センサーは、較正済みのデジタル信号出力を持つ複合センサーで、空気中の湿度と温度を検出できます。

**精度**：湿度 ±5%RH、温度 ±2℃

**検出範囲**：湿度 5%RH ~ 95%RH、温度 -25℃ ~ +60℃

このセンサーは特殊なデジタルモジュール取得と温湿度検知技術を使用しており、非常に高い信頼性と優れた長期安定性を保証します。抵抗式湿度検知素子とNTC温度検知素子を含み、比較的低精度かつリアルタイム性が求められる測定に非常に適しています。

**XHT11 通信方式：**

シングルバス通信を採用しています。つまり、システム内でデータ交換と制御に使用されるデータ線は1本だけです。

- シングルバスで送信されるデータビットの定義：

シングルバスデータフォーマット：40ビットのデータを一度に送信し、上位ビットが先に来ます。

8bit 湿度整数部 + 8bit 湿度小数部 + 8bit 温度整数部 + 8bit 温度小数部 + 8bit パリティビット（湿度の小数部は0）

- パリティビットの定義：

8bit 湿度整数部 + 8bit 湿度小数部 + 8bit 温度整数部 + 8bit 温度小数部。8bit パリティビット = 取得した結果の最後の8ビット

- データタイムライン：

ユーザーホスト（MCU）が開始信号を送信すると、XHT11は低電力モードから高速モードに切り替わります。開始信号の後、XHT11は応答信号と40ビットのデータを送信し、信号取得をトリガーします。

- 信号伝送は図の通りです：

![Img](./media/A229.png)

 **パラメータ**

- 動作電圧：DC 3.3V ～ 5V

- 動作電流：2.1mA

- 最大消費電力：0.0105W

- 温度範囲：-25℃ ～ +60℃ (± 2℃)

- 湿度範囲：5%RH ～ 95%RH (約25℃付近で精度 ±5%RH)

**Microbit 光センサー**

![Img](./media/A0335.png)

光センサーは外部光の明るさを測定する入力デバイスです。micro:bit ボードには内蔵光センサーはありません。LEDマトリクスが光の強度を繰り返し値に変換し、その後電圧減衰時間をサンプリングすることで周囲の明るさを検出・感知します。このため、<span style="color: rgb(255, 76, 65);">検出される明るさレベルは相対値です</span>。

#### 4. 配線図

![Img](./media/A409.png)

<span style="color: rgb(255, 76, 65);">**OLEDディスプレイを使用する場合は、必ず外部電源を接続し、DIPスイッチをONにしてください。**</span>

![Img](./media/A904.png)

![Img](./media/A554.png)

#### 5. ライブラリのインポート

必要なライブラリファイル（DHT11 と oled_ssd1306）をまだ追加していない場合は、[How Mu Import Library to Micro:bit](https://docs.keyestudio.com/projects/FKS0004/en/latest/docs/MicroPython_Tutorial/MicroPython_Tutorial.html#how-mu-import-library-to-micro-bit) を参照してインポートしてください。

#### 6. コードの流れ

![Img](./media/A638.png)


#### 7. テストコード

コードファイルはフォルダ Project 07：Environment Monitoring 中の Project-07-Environment-Monitoring\.py にあります。

![Img](./media/A3641.png)

**完成コード：**

```python
'''
Function: OLED displays temperature and humidity values and brightness level values in real time to simulate intelligent environment detection
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
import oled_ssd1306 as oled
from microbit import *
from DHT11 import *

val = Image("90900:""09090:""90009:""90009:""99999")  # Set pattern
display.show(val)   # LED matrix displays the set pattern

#initialize and clear oled
oled.initialize()
oled.clear_oled()

sensor = DHT11(pin1)  # set temperature and humidity pins

while True:
    oled.clear_oled() # clear oled
    sensor.read()     # read the temperature and humidity values
    T = sensor.temp   # store the temperature values in T
    H = sensor.humid  # store the humidity values in H
    L = display.read_light_level()  # read the brightness level value of the light and store it in L
    oled.add_text(1, 0, 'T:' + str(T) + 'C')   # Display the temperature value at the corresponding position of the OLED
    oled.add_text(1, 1, 'H:' + str(H) + '%')   # Display the humidity value at the corresponding position of the OLED
    oled.add_text(1, 2, 'L:' + str(L))         # Display the brightness level value at the corresponding position of the OLED
    sleep(2000)
```

#### 8. テスト結果

「<span style="color: rgb(255, 76, 65);">Flash</span>」をクリックしてコードをmicro:bitボードに書き込みます。

![Img](./media/A3710.png)

コードをボードにダウンロードした後、**micro USBケーブルまたは外部電源で電源を入れ（DIPスイッチをONにする）、ボードのリセットボタンを押します。**

![Img](./media/A455.png)

OLEDに温度・湿度の値と光の明るさレベルがリアルタイムで表示されます。

<span style="color: rgb(255, 76, 65);">**注意：** 配線が正しいのに結果が表示されない場合は、ボード裏面のリセットボタンを押してください。</span>

![Img](./media/A838.gif)
