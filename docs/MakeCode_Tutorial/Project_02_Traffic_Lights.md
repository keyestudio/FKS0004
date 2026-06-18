### プロジェクト 02: 信号機

#### 1. 概要

このプロジェクトでは、micro:bit ボード上の3つのLED（赤、黄、緑）、スピーカー、5x5 LEDマトリックスを使って信号機のモデルを作成します。

#### 2. 部品

| ![Img](./media/A850.png)| ![Img](./media/A858.png) | ![Img](./media/A906.png) |
| :--: | :--: | :--: |
| micro:bit ボード *1 | micro:bit T型拡張ボード *1 | micro USB ケーブル *1 |
| ![Img](./media/A937.png)| ![Img](./media/A5652.png) | ![Img](./media/A658.png) |
| 赤色LED *1 | 黄色LED *1 | 緑色LED *1 |
| ![Img](./media/A944.png) | ![Img](./media/A950.png) |![Img](./media/A017.png) |
| 220Ω抵抗 *3 | ジャンプワイヤー | ブレッドボード *1 |
|  ![Img](./media/A024.png) |  ![Img](./media/A020.png) |  |
| 電池ホルダー *1 <br> (<span style="color: rgb(255, 76, 65);">自分で用意した単3電池 *2</span>) | 信号機カード *1 | |

#### 3. 部品の知識

**スピーカー**

![Img](./media/A833.png)

Micro:bit にはスピーカーが搭載されており、プロジェクトで簡単に音を出すことができます。

#### 4. 配線図

![Img](./media/A908.png)

<span style="color: rgb(255, 76, 65);">**注意:** micro:bit ボードは下図のようにT型拡張ボードに差し込む必要があります。micro:bit ボードのLEDマトリックスは拡張ボードのロゴと同じ側にしてください。</span>

![Img](./media/A940.png)

#### 5. コードの流れ

![Img](./media/A5956.png)

#### 6. テストコード

コードファイルはフォルダ Project 02：Traffic Lights 内のファイル Project-02-Traffic-Lights.hex にあります。

![Img](./media/A0017.png)

**コードブロックの読み込み：**

![Img](./media/A605.png)

#### 7. テスト結果

Windows 10 アプリの場合、「<span style="color: rgb(255, 76, 65);">Download</span>」をクリックしてください。ブラウザの場合は、ダウンロードした「<span style="color: rgb(255, 76, 65);">.hex</span>」ファイルを micro:bit ボードに送信します。

コードをボードにダウンロードすると、緑色LEDが点灯し、5×5 LEDマトリックスが6秒のカウントダウンを表示します。緑色LEDが消えると黄色LEDが点滅し、マトリックスは3秒のカウントダウンを行い、スピーカーが鳴ります。最後に赤色LEDが点灯し、6秒のカウントダウンを行います。これらの動作が繰り返されます。

<span style="color: rgb(255, 76, 65);">**注意:** 配線が正しいのに結果が見えない場合は、ボード裏面のリセットボタンを押してください。</span>

![Img](./media/A459.gif)

<span style="color: rgb(255, 76, 65);">**外部電源で電源を入れる場合は、DIPスイッチをONにしてください。**</span>

![Img](./media/A904.png)
