# Name

ダンベル交換所

# DEMO

![スクリーンショット 2023-06-16 140331](https://github.com/dyoshino88/Django-app/assets/130971236/5c76b66f-e18e-4f18-aa07-43a62f4461ad)

# Features
ダンベルをユーザー間で交換できる掲示板<br>
ジモティーではアイテム数が多く探しにくさを感じ、簡易版として作成<br>
差別点：「ダンベル」「交換」に特化しているため探しやすい、決済トラブルがない<br>
<table>
  <caption>技術選定と選定理由</caption>
  <thead>
    <tr>
      <th>技術</th> <th>選定理由</th>
    </tr>
  </thead>
  <tr>
    <td> Django </td> <td>ユーザー認証、セキュリティ面、フルスタック</td>
  </tr>
  <tr>
    <td> Python </td> <td>書きやすい、ライブラリが豊富、機械学習に興味があった</td>
  </tr>
  <tr>
    <td> HEROKU </td> <td>gitと連携でき自動デプロイ可能、コンテナ（Dyno）でOS、サーバ、DBの機能を一括で提供してくれる</td>
  </tr>
  <tr>
    <td> PostgreSQL </td> <td>DB設定はHeroku Postgresが推奨されていた</td>
  </tr>
  <tr>
    <td> HTML </td> <td>WEBアプリには必須</td>
  </tr>
  <tr>
    <td> CSS </td> <td>HTMLと同様</td>
  </tr>
</table>

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

# Usage

1. 会員登録ボタンより必要情報入力の上、会員登録<br>
2. 登録したメールアドレスに認証メールが届くので、そのメールに記載のURLからログイン<br>
3. ログイン後、新規作成ボタンより掲示板を作成<br>
4. ユーザー間にて条件すり合わせの上、取引条件を決定<br>

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

