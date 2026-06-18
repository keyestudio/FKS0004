## 3. トラブルシューティング

#### メンテナンス：コードがMicro:bitにダウンロードできない

**1. 問題**

最近、多くのユーザーがMicro:bitボードにコードをダウンロードしても反応しない問題に直面しています。

操作方法が正しい場合でも、誤ってリセットボタンを押してメンテナンスモードに入ってしまったり、誤操作によりファームウェアが消失している可能性があります。

Micro:bitボードを接続すると、「<span style="color: rgb(255, 76, 65);">MAINTENANCE</span>」ドライブが表示され、プログラムがダウンロードできないことを意味します。

![Img](./media/A158.png)

**2. 解決策**

(1) このページから<span style="color: rgb(255, 76, 65);">.hex</span>ファイルをコンピューターにダウンロードします。

[最新のmicro:bitファームウェア-0255](https://www.microbit.org/get-started/user-guide/firmware/)をダウンロードしてください。このウェブサイトからのダウンロードを希望しない場合は、チュートリアル内でも提供しています。

(2) 最新のファームウェアをダウンロードしたら、「<span style="color: rgb(255, 76, 65);">MAINTENANCE</span>」にFirmware for V2.20_V2.21をドラッグしてMicro:bitを通常モードに戻します。

<span style="color: rgb(255, 76, 65);">micro:bitボードのモデルに応じて異なるファームウェアをインストールしています。ここではFirmware for V2.20_V2.21です。</span>

![Img](./media/A326.png)

![Img](./media/A331.png)

**3. 「MAINTENANCE」に入らないようにする**

(1) USBケーブルでボードを接続する際にリセットボタンを押さないように注意してください。

![Img](./media/A228.png)

(2) micro:bitプログラムのダウンロード中にケーブルを突然抜かないでください。そうしないとファームウェアが消失し、micro:bitが「MAINTENANCE」モードに入ります。

(3) 実験中の誤配線もショートやファームウェア消失の原因となります。

#### WebUSBでのダウンロードのトラブルシューティング

クリック：[WebUSBでのダウンロードのトラブルシューティング](https://makecode.microbit.org/device/usb/webusb/troubleshoot)

micro:bitをWebUSBでペアリングする際に問題がありますか？原因を探ってみましょう！

**ステップ1：ケーブルを確認する**

micro:bitがマイクロUSBケーブルでコンピューターに接続されていることを確認してください。例えば、Windowsエクスプローラーでは接続時に**MICROBIT**ドライブが表示されるはずです。

![Img](./media/A321.png)

MICROBITドライブが見える場合はステップ2へ進んでください。見えない場合は：

(1) USBケーブルが正常に動作しているか確認してください。

別のコンピューターでケーブルが動作しますか？動作しない場合は別のケーブルを使用してください。中には電源供給のみでデータ転送ができないケーブルもあります。

(2) コンピューターの別のUSBポートを試してください。

ケーブルは良好でもMICROBITドライブが見えない場合、micro:bitに問題がある可能性があります。

[microbit.orgの故障診断ページ](https://support.microbit.org/support/solutions/articles/19000024000-fault-finding-with-a-micro-bit)に記載されている追加手順を試してください。これでも解決しない場合は、[サポートチケットを作成](https://support.microbit.org/support/tickets/new)してMicro:bit Foundationに問題を通知できます。残りのトラブルシューティング手順はスキップしてください。

**ステップ2：ファームウェアのバージョンを確認する**

ダウンロードがまだうまくいかない場合、micro:bitのファームウェアバージョンが更新を必要としている可能性があります。確認しましょう：

1. **MICROBIT**ドライブにアクセスします；

2. <span style="color: rgb(255, 76, 65);">DETAILS.TXT</span>ファイルを開きます；

![Img](./media/A0452.png)

3. ファームウェアのバージョン番号を探します；ファイル内に「Version:」と記載された行を見つけてください。

![Img](./media/A501.png)

バージョンが0234、0241、0243の場合はmicro:bitのファームウェアを更新する必要があります。ステップ3に進み、アップグレード手順に従ってください。

バージョンが0249、0250以上の場合は適切なファームウェアがインストールされています。ステップ4に進んでください。

**ステップ3：ファームウェアをアップグレードする**

(1) micro:bitをMAINTENANCEモードにします。

これを行うには、micro:bitのUSBケーブルを抜き、リセットボタンを押しながらUSBケーブルを再接続します。ケーブルを挿入したらリセットボタンを離してください。

以前のMICROBITドライブの代わりにMAINTENANCEドライブが表示されるはずです。また、リセットボタンの隣に黄色のLEDが点灯します。

![maintenance](./media/maintenance.gif)

(2) [ファームウェアの.hexファイル](https://microbit.org/guide/firmware/)をダウンロードします。

<span style="color: rgb(255, 76, 65);">micro:bitボードのモデルに応じて異なるファームウェアをインストールしています。ここではFirmware for V2.20_V2.21です。</span>

![Img](./media/A0629.png)

(3) そのファイルを**MAINTENANCE**ドライブにドラッグ＆ドロップします。

(4) LEDの点滅を確認します。

HEXファイルがコピーされている間、黄色のLEDが点滅します。コピーが完了するとLEDは消灯し、micro:bitがリセットされます。MAINTENANCEドライブは再びMICROBITに変わります。

(5) アップグレード完了。

アップグレードが完了しました！<span style="color: rgb(255, 76, 65);">DETAILS.TXT</span>ファイルを開いて、ファームウェアのバージョンがコピーしたHEXファイルのバージョンに変わっていることを確認できます。

ボードの接続、MAINTENANCEモード、ファームウェアのアップグレードについてさらに知りたい場合は、[ファームウェアガイド](https://microbit.org/guide/firmware/)を参照してください。

**ステップ4：ブラウザのバージョンを確認する**

WebUSBは比較的新しい機能であり、ブラウザのアップデートが必要な場合があります。以下のいずれかのバージョンにブラウザが対応しているか確認してください：Android、Chrome OS、Linux、macOS、Windows 10用Chrome 65以上。

**ステップ5：デバイスをペアリングする**

ファームウェアを更新したら、Chromeブラウザを開き、エディターにアクセスして歯車メニューの「Pair Device」をクリックします。ペアリング手順は[WebUSB(/device/usb/webusb)](https://microbit.org/get-started/user-guide/web-usb/)を参照してください。

高速ダウンロードをお楽しみください！
