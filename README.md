# Pythonでテストを書く

## 環境構築(とりあえず動かしたい人向け)

```
pipenv sync
pipenv run test
```

ソースを直すたびに勝手にテストが走るようになります。


## テストのためのライブラリ

- unittest
  - 標準ライブラリなのでインストール不要
  - クラスベースなのでLambdaとちょっと合わない？
- pytest
  - サードパーティライブラリなので要インストール
  - 人気がある模様
  - テストが関数ベースでも書ける
- nose
  - サードパーティライブラリなので要インストール
  - かつて人気があった

今回は**pytest**を使ってみる

## セットアップ

```
pipenv --python 3.8
pipenv install -d pytest pytest-watch
```

`Pipfile`に以下を追記。
以降、`pipenv run test`でテストが自動で走るようになる

```
[scripts]
test = "ptw -- -vv"
```

## テストコードのファイルを作る

ソースコードとテストコードが1:1になるようにします。

どのソースに対してのテストコードなのかをわかりやすくするために、
`handler.py`のテストは`test_handler.py`のようにしています。

`test_`から始まるファイルにするのは、`pytest`が自動的に探し出して、テストコードとして実行してくれるためです。


## テストコードを書く

テストコード内でソースコードをテストします。

```py
from first import * # point1

def test_add():
    assert add(1, 2) == 3 # point2
```

**point1**では他のファイルの関数を呼べるようにしています。
**point2**では`assert`文を使って、テストしています。




## 参考

- [Pythonのpytest-watchモジュールでテスト駆動開発が捗った - Qiita](https://qiita.com/kai_kou/items/2a494289f6b28da3361a)
  - pytest-watchの紹介
- [pytestのとりあえず知っておきたい使い方 - Qiita](https://qiita.com/kg1/items/4e2cae18e9bd39f014d4)
  - 細かいオプション
  - ディレクトリ構成の例