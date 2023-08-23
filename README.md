# Name

ダンベル交換所<br>
dkoukan.com

# DEMO

![FireShot Capture 025 - ダンベル交換所 - dkoukan com](https://github.com/dyoshino88/bulletinboard/assets/130971236/8ed13045-0fd8-495d-8dd6-f5cd6f5fadc2)



# Features
ダンベルをユーザー間で交換できる掲示板<br>
ジモティーではアイテム数が多く探しにくさを感じ、簡易版として作成<br>
差別点：「ダンベル」「交換」に特化しているため探しやすい、決済トラブルがない<br>
フロントエンド：HTML、TailwindCSS、Bootstrap、JQuery、JavaScript<br>
バックエンド：Python<br>
フレームワーク：Django<br>
データベース：Postgresql<br>
インフラ：Heroku、Docker（予定）<br>

<table>
  <caption>技術選定と選定理由</caption>
  <thead>
    <tr>
      <th>技術</th> <th>選定理由</th>
    </tr>
  </thead>
  <tr>
    <td> TailwindCSS </td> <td>スタイル変更の効率化を図るため</td>
  </tr>
  <tr>
    <td> Bootstrap </td> <td>Djangoの仕様上、フォーム周りが簡素になってしまうので最低限のスタイリングを実現するため</td>
  </tr>
  <tr>
    <td> JQuery、JavaScript </td> <td>ハンバーガメニュー、アラートなどUIを高めるため</td>
  </tr>
  <tr>
    <td> Django </td> <td>デフォルトで認証機能をもち、セキュリティ面も強いこと、将来的に機械学習も勉強したいため、Pythonとセットでフレームワークを学習したかったため</td>
  </tr>
  <tr>
    <td> Python </td> <td>書きやすい、ライブラリが豊富、機械学習に興味があったため</td>
  </tr>
  <tr>
    <td> HEROKU </td> <td>Djangoアプリを比較的容易にデプロイ可能なため</td>
  </tr>
  <tr>
    <td> PostgreSQL </td> <td>HerokuがサポートしているのがPostgresqlだったため</td>
  </tr>

</table>

# Requirement

asgiref==3.6.0
dj-database-url==2.0.0
Django==4.2.3
django-debug-toolbar==4.0.0
django-heroku==0.3.1
django-on-heroku==1.1.2
environ==1.0
gunicorn==20.1.0
psycopg2==2.9.6
psycopg2-binary==2.9.6
pycodestyle==2.10.0
virtualenv==20.23.0
whitenoise==6.5.0
django-environ~=0.4.5
django-sendgrid-v5~=1.1.1
django-widget-tweaks==1.4.12

# Installation

# Usage

1. 会員登録ボタンより必要情報入力の上、会員登録<br>
2. 登録したメールアドレスに認証メールが届くので、そのメールに記載のURLからログイン<br>
3. ログイン後、新規作成ボタンより掲示板を作成<br>
4. ユーザー間にて条件すり合わせの上、取引条件を決定（任意の相手と個別チャットができるチャットルーム機能を実装予定）<br>

# Note

1. メールでのやり取りで気をつけるポイント<br>
・個人情報の開示は慎重に行う<br>
・やり取りは掲示板内のみで行う（ダンベル交換所外でのやり取りを避ける）<br>
・連絡先を聞いた場合、その連絡先が正しいことを確認する（携帯電話に実際に連絡してみるなど）<br>
2. トラブルの起こりやすい投稿<br>
・決済を伴う取引※原則交換での取引<br>
・次のような取引には十分ご注意ください！ <br>
・手渡しを拒否する<br>
・駅のロッカーを使った受け渡し<br>
3. 手渡しで取引を行う際に気をつけるポイント<br>
・人気のない場所での取引は行わない<br>
・「誰と・いつ・どこで」会うか家族や知人と共有する<br>
・家に呼ぶ際は家族の方などに同席をしてもらう<br>

# Author

* dyoshino88


# License

