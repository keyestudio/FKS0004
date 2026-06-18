## 1. Muソフトウェアについて

### 1.1. MUのインストール

[Muソフトウェア公式サイト](https://codewith.mu/)をクリックしてアクセスしてください。

Muは、教師や学生など初心者プログラマー向けのPythonコードエディタです。Windows、Mac OSX、Linux用の公式インストーラーから入手できます（Muは32ビットWindowsをサポートしなくなりました）。推奨バージョンはMu 1.2.0です。

**ステップ1 - OSを確認してからMuインストーラーをダウンロード**

まず、コンピュータのOS（WindowsまたはMac OSX）を確認します。「**このPC**」を開き、「**プロパティ**」を見てください。

![Img](./media/A225.png)

システムの種類を確認します：64ビットか32ビットか。

![Img](./media/A253.png)

[MUをダウンロード](https://codewith.mu/en/download)。コンピュータのOSに合わせたバージョンをダウンロードしてください。

![Img](./media/A348.png)

<span style="color: rgb(255, 76, 65);">ここではWindowsシステムを例にしていますが、Mac OSXやLinuxの参考にもなります。</span>

![Img](./media/A422.png)

**ステップ2 - インストーラーを実行**

インストーラーをダブルクリックして実行します（おそらくダウンロードフォルダにあります）。

![Img](./media/A440.png)

Windows 10でMuをインストールするための追加手順を説明しています。他のバージョンもほぼ同様です。

[MacOS用Muインストーラー](https://codewith.mu/en/howto/1.1/install_macos)。

[Linux用Muインストーラー](https://codewith.mu/en/howto/1.2/install_linux)。

Windows 10の場合、Defenderが警告メッセージを表示します。「**詳細情報**」リンクをクリックしてください。

![Img](./media/A615.png)

メッセージが変わり、インストーラーの詳細情報と「**実行する**」ボタンが表示されます。「**実行する**」をクリック。

![Img](./media/A626.png)

**ステップ3 - ライセンス契約**

ライセンスを確認し、チェックボックスを選択して「**インストール**」をクリック。

![Img](./media/A1716.png)

**ステップ4 - インストール中**

Muがコンピュータにインストールされる間、コーヒーを一杯どうぞ。

![Img](./media/A1740.png)

**ステップ5 - 完了**

インストールが正常に完了しました。「**完了**」をクリックしてインストーラーを閉じます。

![Img](./media/A817.png)

**ステップ6 - Muを起動**

スタートメニューのアイコンをクリックするか、検索ボックスに「Mu」と入力して起動できます（下図の両方がハイライトされています）。初回起動は少し時間がかかる場合があります。

![Img](./media/A852.png)

起動後の画面は以下の通りです：

![Img](./media/A909.png)

### 1.2. モードとメニューバーの使い方

「<span style="color: rgb(255, 76, 65);">モード</span>」をBBC micro:bitに設定します。

メニューで「**Mode**」をクリックし、「**BBC micro：bit**」に設定してください。micro:bitモードはmicro:bitとの接続や操作方法を理解しています。

![Img](./media/A022.png)

[Muの始め方](https://codewith.mu/en/tutorials/1.1/start)をクリック。

Muの使い方に関する他のチュートリアルは、https://codewith.mu/en/tutorials/ をご覧ください。

### 1.3. Muでのプログラム

ここでは「<span style="color: rgb(255, 76, 65);">heartbeat\.py</span>」をMuに読み込みます。提供した「<span style="color: rgb(255, 76, 65);">Heart beat</span>」フォルダ内にあります。

![Img](./media/A200.png)

**方法1：**

Muを開き、「<span style="color: rgb(255, 76, 65);">Load</span>」をクリックして、コードをダウンロードしたパスを選択します。

![Img](./media/A341.png)

![Img](./media/A345.png)

正常に読み込まれました。下図の通りです：

![Img](./media/A354.png)

**方法2：**

「new」 ![Img](./media/A503.png)をクリックして新しいプログラムを作成し、「heartbeat\.py」をドラッグ＆ドロップします：

![Img](./media/A521.png)

正常に読み込まれました。下図の通りです：

![Img](./media/A533.png)

<span style="color: rgb(255, 76, 65);">他のコードを追加する場合も同様です。</span>

### 1.4. コードをMicro:bitにダウンロード

USBケーブルでボードをコンピュータに接続します。

![Img](./media/A252.png)

「<span style="color: rgb(255, 76, 65);">**Flash**</span>」をクリックしてコードをmicro:bitボードにダウンロードします。

![Img](./media/A3728.png)

その後、<span style="color: rgb(255, 76, 65);">**micro USBケーブルまたは外部電源で電源を入れます（DIPスイッチをONにしてください）**</span>。オンボードの5×5 LEDマトリックスが繰り返し ![Img](./media/A903.png) と ![Img](./media/A910.png) を表示します。

<span style="color: rgb(255, 76, 65);">**コードにエラーがあってもダウンロードは可能ですが、正常に動作しません。**</span>

<span style="color: rgb(0, 209, 0);">例えば、関数sleep()をsleeps()と書いてしまった場合、「**Flash**」をクリックしてmicro:bitにコードをロードしても、5×5 LEDマトリックスは乱れたアイコンを表示します。</span>

![Img](./media/A4003.png)

この場合、「**REPL**」をクリックし、ボード背面のリセットボタンを押します。エラーメッセージがREPL画面に表示されます。下図参照：

![Img](./media/A029.png)

![Img](./media/A033.png)

再度「**REPL**」をクリックしてREPLを閉じ、「<span style="color: rgb(255, 76, 65);">**Flash**</span>」をクリックします。

コードが正しいか確認するために、完了後「<span style="color: rgb(255, 76, 65);">**Check**</span>」をクリックすると、Muがコードのエラーを指摘します。

![Img](./media/A119.png)

エラーメッセージに従ってコードを修正し、再度「<span style="color: rgb(255, 76, 65);">**Check**</span>」をクリックします。Muがエラーを表示しなければOKです。

![Img](./media/A134.png)

[Muの特定の機能を説明する他のチュートリアル](https://codewith.mu/en/tutorials/)もご覧ください。

## 2. MuからMicro:bitへのライブラリのインポート方法

<span style="color: rgb(255, 76, 65);">ライブラリをインポートする前に、.pyコード（空のコードでも可）をmicro:bitボードにアップロードする必要があります。ここでは空のコードを例にします。</span>

USBケーブルでボードをコンピュータに接続し、Muを開いて「Flash」をクリックして.pyコード（空のコード）をボードにアップロードします。

![Img](./media/A252.png)

このチュートリアルではOLEDとDHT11モジュールを使用します。したがって、「<span style="color: rgb(255, 76, 65);">**oled_ssd1306\.py**</span>」と「<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>」のライブラリファイルをmicro:bitボードにインポートする必要があります。

Muがファイルを保存するデフォルトのディレクトリは、ユーザーディレクトリのルートにある「mu_code」です。

参考リンク：[https://codewith.mu/en/tutorials/1.0/files](https://codewith.mu/en/tutorials/1.0/files)

**ライブラリのインポート手順：**

1\. ディスク(C:)で「<span style="color: rgb(255, 76, 65);">mu_code</span>」フォルダを探します。

![Img](./media/A543.png)

![Img](./media/A550.png)

2\. 「<span style="color: rgb(255, 76, 65);">mu_code</span>」を開きます。

![Img](./media/A628.png)

3\. ライブラリファイル「<span style="color: rgb(255, 76, 65);">**oled_ssd1306\.py**</span>」と「<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>」を「<span style="color: rgb(255, 76, 65);">**Libraries**</span>」にコピー＆ペーストします。

![Img](./media/A4716.png)

4\. 下図のようになります：

![Img](./media/A735.png)

5\. Muを開き、「<span style="color: rgb(255, 76, 65);">**Files**</span>」をクリックします。ここで「<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>」ライブラリをmicro:bitにドラッグします。

![Img](./media/A816.png)

![Img](./media/A820.png)

6\. 「<span style="color: rgb(255, 76, 65);">**DHT11\.py**</span>」をインポートすると、左のボックスに表示されます。

![Img](./media/A841.png)

7\. 「<span style="color: rgb(255, 76, 65);">**oled_ssd1306\.py**</span>」も同様に行います。

![Img](./media/A916.png)

![Img](./media/A4920.png)

<span style="color: rgb(255, 76, 65);">**他のファイルをmicro:bitにアップロードすると元の内容が上書きされるため、次回使う際には再度インポートが必要です。**</span>
