# Name

ダンベル交換所

# DEMO

![two-dumbells-slider](https://github.com/dyoshino88/Django-app/assets/130971236/39053698-1194-4696-b763-6f0b181a8963)

# Features
自分のトレーニング強度に合わないダンベルをユーザー間で交換できる掲示板
ジモティーのアイテム特化型の掲示板として作成
差別点：「ダンベル」「交換」に特化しているため探しやすい、決済トラブルがない

# Requirement

* dj-database-url==0.5.0
* Django==3.2.4
* django-on-heroku==1.1.2
* gunicorn==20.1.0
* psycopg2-binary==2.9.6
* whitenoise==6.4.0
* django-environ==0.10.0
* django-heroku==0.3.1

# Installation

[](Requirementで列挙したライブラリなどのインストール方法を説明する

```bash
pip install huga_package
```)

# Usage

1.会員登録ボタンより必要情報入力の上、会員登録
2.登録したメールアドレスに認証メールが届くので、そのメールに記載のURLからログイン
3.ログイン後、新規作成ボタンより掲示板を作成
4.ユーザー間にて条件すり合わせの上、取引条件を決定

```bash
git clone https://github.com/hoge/~
cd examples
python demo.py
```

# Note

注意点などがあれば書く

# Author

* dyoshino88


# License
[](ライセンスを明示する

"hoge" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).

社内向けなら社外秘であることを明示してる

"hoge" is Confidential.)
