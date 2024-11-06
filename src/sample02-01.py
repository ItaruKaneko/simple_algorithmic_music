# sample02-02.py
# audio sample program2.sci
# audio playback using simpleaudio
import numpy as np
import simpleaudio as sa

# initial parameters
fs=44100      # sampling frequency
l=20          # duration of sound
x=np.arange(l*fs)*0.0   # initial sound data (silence)

# w: 音符1つ分のインデックス, t: その開始からの相対時間
w=np.arange(8192)
# t=w/fs

# 128個の音符を生成
for i in np.arange(128):
  a=.001
  r=.1
  s=i*fs/16
  n=i - int(i/8) * 8
  f=440 * pow(2 , (int(n/7*12+.8)/24))
  #
  # 1つの音符の 8192 個のサンプルを生成する
  for w1 in range(8192) :
    t1=w1/fs    # 音符の開始時刻からの相対時間
    xw =  (1-np.exp(-t1/a)) * np.exp(-t1/r) * (np.sin(2* np.pi*f*t1)*.2)  # 音符を生成
    x[w1+int(s)+1] = x[w1+int(s)+1] + xw  # その音を配列 x に合成
  # end
#end

# playback audio
audio = x * 32767
audio = audio.astype(np.int16)
play_obj = sa.play_buffer(audio, 1, 2, fs)
play_obj.wait_done()
