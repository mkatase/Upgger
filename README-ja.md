# Google BloggerのためのHTMLアップローダ
Google BloggerのためのHTMLアップローダ。Pythonにて実装。

## 環境
* Python 3
* pip (Python module)
* Googleアカウント

## ID作成 (ラフ)
* Blog ID:
 - GoogleアカウントでBloggerの設定を行い, URLバーに表示されるblogIDを保持
* Client IDとClient Secret ID:
 - Google Developers Consoleにログインをし, 新規Projectを作成
 - Blogger API v3を有効化
 - 「認証情報」から、「OAuth同意画面」タブを選択し、必須事項を記入後、「保存」をクリック
 - 「認証情報」から、「認証情報」タブから「認証情報を作成」から「OAuthクライアントID」選択
 - 「アプリケーションの種類」から、「その他」を選択、「名前」を適宜入力し、「作成」クリック
 - ポップアップ表示される「クライアントIDとクライアントシークレット」を保持
* 保持した3つのIDをScriptの以下を書き換えます
```
CLIENT_ID     = 'INPUT CLIENT ID'
CLIENT_SECRET = 'INPUT CLIENT SECRET'
BLOG_ID       = 'INPUT BLOG ID'
```

## Pythonモジュールのインストール
```
$ pip install google--api-python-client oauth2client
```

## 使用方法
実行初回時、ブラウザ上で、「認証」や「許可」を行ってください。成功すれば「upgger.dat」ファイルが作成されます
* 標準 (-iオプションは必須)
```
$ python3 upgger.py -i hello.html
```
上記の場合、タイトルはファイル名(hello.html)、ラベルは無し、ステータスはLIVE（公開）

* -tもしくは--titleオプションを追加
```
$ python3 upgger.py -i hello.html -t hello
```
上記の場合、タイトルは「hello」、ラベルは無し、ステータスはLIVE（公開）
```
$ python3 upgger.py -i hello.html -t "Hello World"
$ python3 upgger.py -i hello.html -t Hello\ World
```
タイトルに半角スペースがある場合、ダブルコーテーションかバックスラッシュを使用する。この場合、タイトルは「Hello World」、ラベルは無し、ステータスはLIVE（公開）

* -lもしくは-labelオプションを追加
```
$ python3 upgger.py -i hello.html -l abc,def
```
上記の場合、タイトルはファイル名、ラベルは「abc」と「def」、ステータスは公開（LIVE）  
ラベルが複数の場合、カンマを用いて、文字を連結

* -dもしくは--draftオプションを追加
```
$ python3 upgger.py - hello.html -d
```
上記の場合、タイトルはファイル名、ラベルは無し、ステータスはDRAFT（下書き）

## 制限
* 画像ファイルはアップロードできない
* スケジュールは設定できない
* パーマリンクは設定できない

## バージョン
* v0.10 2018/08/30 新規作成
