### プロジェクト06：ミュージックパーティー

![Img](./media/A1317.png)

#### 1. 概要

手を叩くと、ボード上のマイクが音声信号を検出し、スピーカーが楽しい誕生日の歌を再生しながら、RGB LEDがまばゆい光を放ちます。

#### 2. 部品

| ![Img](./media/A850.png) |              ![Img](./media/A858.png)              | ![Img](./media/A906.png) |
| :---------------------: | :-----------------------------------------------: | :---------------------: |
|   micro:bit ボード *1   |        micro:bit T型拡張ボード *1                 |   micro USB ケーブル *1 |
| ![Img](./media/A500.png) |              ![Img](./media/A944.png)              | ![Img](./media/A950.png) |
|       赤色LED *1        |                 220Ω 抵抗 *3                       |      ジャンパーワイヤー *2       |
| ![Img](./media/A017.png) |              ![Img](./media/A024.png)              | ![Img](./media/A621.png) |
|      ブレッドボード *1  |バッテリーホルダー *1 <br> (<span style="color: rgb(255, 76, 65);">自前の単三電池 *2</span>)|       RGBカード *1       |

#### 3. 部品の知識

**マイクロフォン**

micro:bit V2 ボードの表面には高品質なデジタルマイクが内蔵されており、音声信号を検出します。マイクを制御・処理するチップは裏面にあります。

![Img](./media/A1317.png)

マイクはボード前面の小さな丸い穴にあり、周囲の音声信号を拾いやすくなっています。使用時はmicro:bitボードを表向きに置いてください。穴の隣にはマイクのLEDインジケーターがあり、音レベルを測定すると点灯します。

![Img](./media/A116.png)

**RGB LED**

![Img](./media/A2127.png)

RGB LEDは三原色（赤、緑、青）の交差点としてイメージされます。RGBの異なる比率でほとんどの色を合成できます。赤、緑、青のLEDは透明なプラスチックケースに封入されており、R、G、Bピンの入力電圧を変えることで光の色を発します。

![Img](./media/A137.png)

**三色説:**

![Img](./media/A150.png)

RGB LEDは共通アノード型と共通カソード型の2種類に分けられます：

共通カソードRGB LEDでは、3つのLEDが負極（カソード）を共有します；

共通アノードRGB LEDでは、3つのLEDが正極（アノード）を共有します。

![Img](./media/A209.png)

<span style="color: rgb(255, 76, 65);">**注意：ここでは共通カソードRGB LEDを使用しています。**</span>

**RGB LEDのピン:**

RGB LEDは4本のピンを持ちます：GND（最も長いピン）、R（赤）、G（緑）、B（青）。下図のようにRGB LEDを配置すると、左から右へピンは赤、GND、緑、青の順になります。

![Img](./media/A239.png)

#### 4. 配線図

![Img](./media/A308.png)

![Img](./media/A325.png)

#### 5. コードフロー

![Img](./media/A343.png)

#### 6. テストコード

コードファイルはフォルダ Project 06：Music Party 内の Project-06-Music-Party\.py にあります。

![Img](./media/A3523.png)

**完全なコード:**

```python
'''
Function: Clap your hands, the microbit microphone receives the sound signal, the music sounds, and the RGB emits a dazzling light to simulate a musical party
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from microbit import *
import music

display.clear() # clear LED matrix

while True:
    if microphone.current_event() == SoundEvent.LOUD:  # If the microphone picks up a loud signal
       music.play(["G3:4", "G3", "A4"]) # the speaker plays some tones
       pin1.write_analog(1023)      # P1 analog value is 1023,RGB is red
       pin2.write_analog(0)
       # pin3.write_analog(0)
       sleep(100)
       music.play(["G4:4", "C5", "B4"])
       pin1.write_analog(0)         # P1 analog value is 0,RGB is not red
       pin2.write_analog(1023)      # P2 analog value is 1023,RGB is green
       # pin3.write_analog(0)
       sleep(100)
       pin1.write_analog(10)
       pin2.write_analog(10)
       # pin3.write_analog(1023)      # P3 analog value is 1023,RGB is blue
       sleep(100)
       music.play(["G4:4", "D5", "C5"])
       pin1.write_analog(123)
       pin2.write_analog(123)
       # pin3.write_analog(0)
       sleep(100)
       music.play(["G4:4", "D5", "C5"])
       pin1.write_analog(1023)
       pin2.write_analog(400)
       # pin3.write_analog(1023)
       sleep(100)
       music.play(["G3:4", "G3", "G4"])
       pin1.write_analog(10)
       pin2.write_analog(1023)
       # pin3.write_analog(1023)
       sleep(100)
       pin1.write_analog(1023)
       pin2.write_analog(1023)
       # pin3.write_analog(1023)
       sleep(100)
       music.play(["E5:4", "C5", "B4", "A4"])
       pin1.write_analog(32)
       pin2.write_analog(184)
       # pin3.write_analog(336)
       sleep(100)
       pin1.write_analog(640)
       pin2.write_analog(328)
       # pin3.write_analog(180)
       sleep(100)
       music.play(["F5:4", "F5", "E5"])
       pin1.write_analog(552)
       pin2.write_analog(172)
       # pin3.write_analog(904)
       sleep(100)
       pin1.write_analog(1020)
       pin2.write_analog(796)
       # pin3.write_analog(560)
       sleep(100)
       music.play(["C5:4", "D5", "C5"])
       pin1.write_analog(136)
       pin2.write_analog(560)
       # pin3.write_analog(140)
       sleep(100)
       pin1.write_analog(0)
       pin2.write_analog(0)
       # pin3.write_analog(0)
       sleep(100)
if microphone.current_event() == SoundEvent.QUIET:  # If the microphone picks up a quie signal
       pin1.write_analog(0)
       pin2.write_analog(0)
```

#### 7. テスト結果

「<span style="color: rgb(255, 76, 65);">Flash</span>」をクリックしてコードをmicro:bitボードに書き込みます。

![Img](./media/A3540.png)

コードをボードにダウンロードした後、**micro USBケーブルまたは外部電源で電源を入れ（DIPスイッチをONにする）**、ボードのリセットボタンを押します。

![Img](./media/A455.png)

手を叩くと、ボード上のマイクが音声信号を検出し、スピーカーが楽しい誕生日の歌を再生しながら、RGB LEDがまばゆい光を放ちます。楽しい音楽パーティーの雰囲気が感じられませんか？

<span style="color: rgb(255, 76, 65);">**注意：** 配線が正しいのに結果が見えない場合は、ボード裏面のリセットボタンを押してください。</span>

![Img](./media/A757.gif)
