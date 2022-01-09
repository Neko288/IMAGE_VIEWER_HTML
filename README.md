# IMAGE VIEWER.html

### ブラウザで使う画像ビューアです。

## 使い方
html(Viewer)フォルダの中のindex.htmlをクリックして起動できます。

### 任意のフォルダを開く
write_txt_image.pyをクリックしてビューアで見たい画像があるフォルダの完全パスを入力してください。Enterで実行するとhtml(Viewer)フォルダの中に「1641695438.2284553-index.html」こんな感じのファイルができてると思うのでそれをクリックしてください。クリックしたらビューアを起動できます。


## ちなみに
html(Viewer)フォルダの中にあるmediaフォルダと最初から入っているindex.htmlは削除してもらって構いません。

## 必要なもの

Python(3)
ブラウザ(FirefoxとEdgeのみ動作確認)

## 注意点
あまりにも画像が多いフォルダを画像ビューアで見ようとすると、ブラウザがとんでもなく重たくなり、表示されるまで数分かかることもあります。

## 仕組み
画像があるフォルダ内の画像のパスをすべてPythonで集めます。それを.htmlに書き込むことによって画像ビューアのように振舞わせることができます。