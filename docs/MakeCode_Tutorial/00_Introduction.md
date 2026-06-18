# MakeCode_Tutorial

## 1. MakeCodeでのプログラミング

以下の手順はWindowsシステム向けですが、他のシステムを使用している場合の参考にもなります。

#### 1.1. クイックスタート

**ステップ1 micro:bitに接続**

USBケーブルでボードをコンピューターに接続します。

![Img](./media/A800.png)

ボードの裏側の赤いLEDが点灯していれば、ボードに電源が供給されています。コンピューターがUSBケーブル経由でメインボードと通信すると、黄色のLEDが点滅します。例えば、「.hex」ファイルを書き込むときに点滅します。

その後、Micro:bitメインボードは「MICROBIT」という名前のドライバーとしてコンピューターに表示されます。以下のように通常のUSBディスクではないことに注意してください。

![Img](./media/A849.png)

**ステップ2 heartbeatプログラムを書く**

リンクにアクセス：[Makecodeオンライン版](https://makecode.microbit.org/)

「<span style="color: rgb(255, 76, 65);">新しいプロジェクト</span>」をクリックすると「<span style="color: rgb(255, 76, 65);">プロジェクトを作成中</span>」が表示され、「<span style="color: rgb(255, 76, 65);">heartbeat</span>」と入力し、「<span style="color: rgb(255, 76, 65);">作成 √</span>」をクリックします。

<span style="color: rgb(255, 76, 65);">ここではGoogle Chromeでプログラムを書きます。</span>

![Img](./media/A021.png)

micro:bitのコードを書いてみましょう。

いくつかのブロックを編集エリアにドラッグし、下記のようにシミュレーターでプログラムを実行できます。ここでは<span style="color: rgb(255, 76, 65);">heartbeat</span>プログラムの編集方法を示します。

操作動画ガイド：

![Img](./media/A100.png)

**ステップ3 コードをダウンロード**

一般的に、Windows 10アプリ（[Windows 10アプリを入手](https://apps.microsoft.com/detail/9pjc7sv48lcx?hl=zh-CN&gl=CN#activetab=pivot:overviewtabdocx)）（クリック））では、「<span style="color: rgb(255, 76, 65);">ダウンロード</span>」をクリックするだけで、追加の手順なしにコードがmicro:bitボードに直接ダウンロードされます。

ブラウザの場合は：

エディター内の「<span style="color: rgb(255, 76, 65);">ダウンロード</span>」をクリックします。これにより、micro:bitボードが読み取れる形式の「hex」ファイルがダウンロードされます。その後、USBドライブにファイルをコピーするように、micro:bitボードにコピーしてください。Windowsでは、「<span style="color: rgb(255, 76, 65);">.hex</span>」ファイルを右クリックし、「**送る → MICROBIT**」を選択してmicro:bitボードにコピーすることもできます。

![Img](./media/A319.png)

![Img](./media/A449.png)

または、「<span style="color: rgb(255, 76, 65);">.hex</span>」ファイルを直接MICROBITにドラッグしても構いません。

![Img](./media/A341.png)

![Img](./media/A345.png)

「<span style="color: rgb(255, 76, 65);">.hex</span>」ファイルをMicro:bitにコピーしている間、ボードの裏側の黄色いLEDが点滅します。コピーが完了すると、LEDは点滅を止めて点灯したままになります。

**ステップ4 プログラムを実行**

プログラムがMicro:bitにアップロードされたら、USBケーブルまたは外部電源で電源を供給できます。すると5 x 5のLEDドットマトリックスにハートビートパターンが表示されます。

![Img](./media/A425.png)

<span style="color: rgb(255, 76, 65);">**注意：**</span> プログラムを実行するたびに、Micro:bitのドライバーは自動的に取り出されて戻るため、hexファイルは消えます。ボードはhexファイルにアクセスするだけで保存はしません。

#### 1.2. MakeCode

[Makecode Google Chromeオンライン版](https://makecode.microbit.org/)にアクセスします。これがメインインターフェースです。

![Img](./media/A637.png)

コード編集エリアには「**on start**」と「**forever**」のブロックがあります。<span style="color: rgb(255, 76, 65);">電源オン後、「on start」のコードは一度だけ実行され、「forever」のコードは繰り返し実行されます。</span>

「**JS JavaScript**」言語をクリック：

![Img](./media/A754.png)

「**Python**」言語に切り替え：

![Img](./media/A814.png)


#### 1.3. WebUSB機能の紹介

前述の通り、Windows 10のコンピューターでMakeCodeアプリをダウンロードしている場合、「<span style="color: rgb(255, 76, 65);">ダウンロード</span>」ボタンでコードを素早くボードにダウンロードできます。USB接続されたハードウェアデバイスにアクセスするために**<span style="color: rgb(255, 76, 65);">Google Chrome</span>**のwebUSBを使用しています。

**デバイスのペアリング：**

1\. USBケーブルでボードをコンピューターに接続。

![Img](./media/A951.png)

2\. 「<span style="color: rgb(255, 76, 65);">ダウンロード</span>」->「<span style="color: rgb(255, 76, 65);">...</span>」をクリックし、「<span style="color: rgb(255, 76, 65);">デバイスに接続</span>」。

![Img](./media/A028.png)

3\. 「<span style="color: rgb(255, 76, 65);">次へ</span>」。

![Img](./media/A046.png)

4\. 「<span style="color: rgb(255, 76, 65);">ペアリング</span>」。

![Img](./media/A104.png)

5\. 対応するデバイスを選択し、「<span style="color: rgb(255, 76, 65);">接続</span>」。

![Img](./media/A127.png)

6\. 「<span style="color: rgb(255, 76, 65);">完了</span>」。

![Img](./media/A144.png)

**プログラムのダウンロード：**

接続後、「<span style="color: rgb(255, 76, 65);">ダウンロード</span>」をクリックすると、![Img](./media/A212.png)が![Img](./media/A220.png)に変わります。プログラムがmicro:bitボードにダウンロードされます。

![Img](./media/A232.png)

選択用のデバイスが表示されない場合は、[WebUSBでのダウンロードのトラブルシューティング](https://makecode.microbit.org/device/usb/webusb/troubleshoot)を参照してください。micro:bitのファームウェア更新方法は[ユーザーガイド](https://microbit.org/guide/firmware/)をご覧ください。

#### 1.4. MakeCode拡張ライブラリ

**3.4.1 ライブラリ拡張のインポート**

Makecodeを開き、特定のプロジェクトに入り、![Img](./media/A806.png)をクリックして「**拡張機能**」を選択。

![Img](./media/A842.png)

または、Advancedの上にある「**拡張機能**」をクリック。

![Img](./media/A900.png)

欲しいライブラリを検索。

![Img](./media/A909.png)

各プロジェクトに必要なすべてを含むコードファイルを提供しているので、直接ロードできます。自分でコードブロックを作成したい場合は、以下の3つの拡張機能を追加してください。

<span style="color: rgb(0, 209, 0);">**OLED拡張:**</span>

1\. 「**拡張機能**」をクリックしてライブラリ拡張を追加。

![Img](./media/A236.png)

2\. 「**OLED**」を検索し、![Img](./media/A3257.png)をクリック。

![Img](./media/A306.png)

最初の**oled-ssd1306**をクリックし、追加されるのを待つ。

![Img](./media/A3316.png)

3\. 追加成功：

![Img](./media/A335.png)

<span style="color: rgb(0, 209, 0);">**超音波センサー拡張:**</span>

1\. 「**拡張機能**」をクリックしてライブラリ拡張を追加。

![Img](./media/A236.png)

2\. 「**sonar**」を検索し、![Img](./media/A3257.png)をクリックして「sonar」を見つけてロード。

![Img](./media/A506.png)

3\. 追加成功：

![Img](./media/A522.png)

<span style="color: rgb(0, 209, 0);">**DHT11センサー拡張:**</span>

1\. 「**拡張機能**」をクリックしてライブラリ拡張を追加。

![Img](./media/A236.png)

2\. 「**DHT11**」を検索し、![Img](./media/A3257.png)をクリックして「DHT11_DHT22」を見つけてロード。

![Img](./media/A616.png)

3\. 追加成功：

![Img](./media/A645.png)

**3.4.2 拡張機能の更新/削除**

1\. 「**JavaScript**」をクリックしてテキストコードに切り替え。

![Img](./media/A724.png)

2\. 「**エクスプローラー**」をクリック。

![Img](./media/A749.png)

3\. 「**OLED**」ライブラリを見つけ、![Img](./media/A813.png)をクリックして削除。

![Img](./media/A824.png)

4\. 「**削除**」。

![Img](./media/A727.png)

削除されました。

#### 1.5. MakeCodeにコードをインポートする方法

「**heartbeat**」プロジェクトを例にコードの読み込み方法を示します。

1\. MakecodeのWeb版またはWindows 10アプリMakecodeを開き、「<span style="color: rgb(255, 76, 65);">インポート</span>」をクリック。

![Img](./media/A956.png)

2\. 「<span style="color: rgb(255, 76, 65);">ファイルをインポート...</span>」

![Img](./media/A042.png)

3\. 「<span style="color: rgb(255, 76, 65);">ファイルを選択</span>」して読み込みたいファイルをインポート。

![Img](./media/A06.png)

4\. ここでは「<span style="color: rgb(255, 76, 65);">heartbeat.hex</span>」を読み込み。

![Img](./media/A28.png)

5\. 「<span style="color: rgb(255, 76, 65);">続行 √</span>」

![Img](./media/A149.png)

上記の方法に加え、テストコードをコード編集エリアにドラッグしても読み込めます。下記参照：

![Img](./media/A202.png)

読み込みを待ちます。

![Img](./media/A217.png)
