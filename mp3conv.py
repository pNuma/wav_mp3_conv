#参考：hhttps://algorithm.joho.info/programming/python/pydub-mp3-wav/
#先にpydubをインストールしておく：https://mackro.blog.jp/archives/13141447.html?ref=foot_btn_prev&id=8145773
#実行環境　Ubuntu20.04.1LTS

import pydub

#wav→mp3
DIR="/home/user/wavファイルがあるフォルダ名/"
 
# 入力
sound = pydub.AudioSegment.from_wav(DIR+"変換対象ファイル.wav")

# 音量を N dbだけ上げる
N = 0
loud_sound = sound + N

# 出力
loud_sound.export(DIR+"変換後ファイル.mp3", format="mp3")
 
print("complete")


