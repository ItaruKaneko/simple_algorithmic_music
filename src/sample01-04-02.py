# オーディオファイルの再生
# wav フォーマットでない 16 bit のPCM ファイルである場合
# read 16 bit PCM file
# Play back it as 44100, monral signal

import numpy as np
import simpleaudio as sa

num_ch = 1               # チャンネル数 モノラル=1, ステレオ=2
fs=44100                 # サンプリング周波数
file_name='sample01-04.wav' # ファイル名

# ファイルを開き、pcm_data に int16 で読み込む
with open(file_name, 'rb') as f:
    buf = f.read()
    pcm_data = np.frombuffer(buf, dtype='int16')

# pcm_data の構造を確認のため printする。1次元配列
print(pcm_data.shape)
# ステレオとして再生する
play_obj = sa.play_buffer(pcm_data, num_ch, 2, fs)
play_obj.wait_done()
# 左チャンネルのみ再生
# value error になる。
# header は読み飛ばす必要があるようだ
# L = pcm_data[::2]
# R = pcm_data[1::2]
# play_obj = sa.play_buffer(L, 1, 2, fs)
# play_obj.wait_done()