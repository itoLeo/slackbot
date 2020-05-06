
import codecs
text = 'あいうえお'
# 最初に.opneで読み込む
# 上書きモード（w）、挿入モード(a)、読み込みモード(r)
target_file = codecs.open('read.text', "a", "utf_8")
# ファイルに記載する
target_file.write(text)
# 処理が終わったらcloseでファイルを閉じる
target_file.close()

# 読み込み作業。書き込みと同時は出来ない。多分ね
target_file = codecs.open('read.text', "r", "utf_8")
# ファイルを読み込む
text = target_file.read()
print(text)
target_file.close()
