# 攻撃方法

まずは事前に ``python manage.py runserver`` を実行し、localhostの8000番ポートで攻撃対象のWebサイトを動かして置いて下さい。
その後、下記コマンドを実行します。

```
$ cd csrf_attack/
$ python -m http.server 8080
```

http://localhost:8080 にアクセスすると攻撃は完了です。
