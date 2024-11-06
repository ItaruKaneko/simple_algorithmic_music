# sample08.py
# audio sample program2.sci
# optimized
# audio playback using simpleaudio
import numpy as np
import simpleaudio as sa

# initial parameters
fs=44100      # サンプリング周波数
l=20          # トータルの再生時間
x=np.zeros(l*fs)                 # 無音のデータ l 秒分を作成
w=np.arange(fs)                  # 一音の中の相対時間
t=w / fs                         # 一音の中の相対時間
for i in np.arange(128):         # 音の回数
  a=.01                         # 音の立ち上がり 小=鋭い
  r=.01                           # 音の減衰 小=速い
  s=int(i*fs/16)  + 44100        # 音のタイミング
  n=i % 3 + (i % 5) * 3                      # n は音階 8 音ずつくりかえす
  f=440 * pow(2 , (int(n/7*12+.8)/24)) # 音階を周波数に変換
  x[w+s] = x[w+s] + (1-np.exp(-t/a)) * np.exp(-t/r) * (np.sin(2* np.pi*f*t)*.2) 

# 波形 x を 16 bit の PCM データ, audio に変換する
audio = x * 32767
audio = audio.astype(np.int16)
# 再生
play_obj = sa.play_buffer(audio, 1, 2, fs)
play_obj.wait_done()
