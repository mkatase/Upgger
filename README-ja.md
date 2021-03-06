# Upgger - Google BloggerのためのHTMLアップローダ
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
	- 「認証情報」から、「認証情報」タブを選択し、当該プロジェクトから「SECRET ID」をダウンロード
	- ダウンロードした「SECRET ID」ファイル(JSON形式)を「secret_id.json」にリネームする
	- 「secret_id.json」ファイルを「.uppger.conf」ディレクトリに移動する
* BLOG_IDを書き換えます
	- 「.upgger.conf」ディレクトリに移動し、「upgger.yaml」を開きます
	- Blogger編集画面のURLアドレスバーに表示されているBLOG_IDを書き込みます
```
blog_id: 'INPUT BLOG ID'
```
* 「.upgger.conf」ディレクトリを確認してください
```
$ ls -a .upgger.conf
. .. secret_id.json upgger.yaml
```

## Pythonモジュールのインストール
```
$ pip install google-api-python-client oauth2client　PyYAML
```

## 使用方法
実行初回時、ブラウザ上で、「認証」や「許可」を行ってください。成功すれば「upgger.json」ファイルが「.uppger.conf」ディレクトリに作成されます
```
$ ls -a .upgger.conf
. .. secret_id.json upgger.json upgger.yaml
```

* 標準 (-iオプションは必須)
```
$ python3 upgger.py -i hello.html
```
上記の場合、タイトルはファイル名(hello.html)、ラベルは無し、スケジュールは無し、ステータスはLIVE（公開）

* -tもしくは--titleオプションを追加
```
$ python3 upgger.py -i hello.html -t hello
```
上記の場合、タイトルは「hello」、ラベルは無し、スケジュールは無し、ステータスはLIVE（公開）
```
$ python3 upgger.py -i hello.html -t "Hello World"
$ python3 upgger.py -i hello.html -t Hello\ World
```
タイトルに半角スペースがある場合、ダブルコーテーションかバックスラッシュを使用する。この場合、タイトルは「Hello World」、ラベルは無し、スケジュールは無し、ステータスはLIVE（公開）

* -lもしくは-labelオプションを追加
```
$ python3 upgger.py -i hello.html -l abc,def
```
上記の場合、タイトルはファイル名、ラベルは「abc」と「def」、スケジュールは無し、ステータスは公開（LIVE）  
ラベルが複数の場合、カンマを用いて、文字を連結

* -pもしくは-pubオプションを追加
```
$ python3 upgger.py -i hello.html -p 20XX-YY-ZZ
```
上記の場合、タイトルはファイル名、ラベルは無し、スケジュールは「20XX-YY-ZZ」、ステータスは公開（効果なし）

* -dもしくは--draftオプションを追加
```
$ python3 upgger.py -i hello.html -d
```
上記の場合、タイトルはファイル名、ラベルは無し、ステータスはDRAFT（下書き）

## 制限
*  ~~画像ファイルはアップロードできない~~
*  ~~スケジュールは設定できない~~
* パーマリンクは設定できない

## 開発環境
* OS: Fedora 32 (5.6.7-300) on x86_64
* Python: 3.8.2
* google-api-python-client: 1.8.2
* oauth2client: 4.1.3

## バージョン
* v0.50 2018/09/03 タイムゾーンを削除
* v0.40 2018/09/02 スケジュールオプションを追加
* v0.30 2018/09/01 body内のkind/idを削除。flagsの変更。
* v0.20 2018/08/31 json及びyamlの読み込み部分の修正・追加
* v0.10 2018/08/30 新規作成
