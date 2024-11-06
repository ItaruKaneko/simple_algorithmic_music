# sample09.py
# audio sample program9.sci
#
# veeeery slow - not optimized
#
# audio playback using simpleaudio
import os
import numpy as np
import math
import simpleaudio as sa

# initial parameters
fs=44100      # sampling frequency
l=20          # duration of sound
t1= np.arange(l*fs)
x=t1 * 0.0                       # initial sound data (silence)
w=np.arange(8192)                # unit sound window
# t=w / fs                         # unit sound sample time


# ????
i=np.arange(97)
c=i
d=i
for i1 in i :
  c1=int(i1/16)-int(i1/32)*2
  c[i1]=c1
  d[i1]= c1/7*12-int(c1/7*12)
#end

w=np.arange(44100)
t=w/44100
a=w*0.1    # make array with size w
r=w*0.1    # make array with size w
x1=w*0.1   # make array wwith size w
m1=w*0.1   # make array wwith size w
for w1 in w :
  a[w1]=1-np.exp(-t[w1]/0.01)
# end
# ??????
for kk in range(1,6,1) :
  for w1 in w :
    r[w1]=np.exp(-t[w1]/0.1/kk)
  #end
  # ??????
  for i in range(1,96,kk) :
    s = int(i * fs / 6)
    k = i - int(i/4)*4
    m= k
    n=int(m/7*12 + 0.4 + d[i+1]-(kk*2))
    f=440*pow(2,(n/12))
    for w1 in w:
      m1[w1]=np.sin(2 * np.pi * f * t[w1]) * np.sin(20 * t[w1]) * (kk-0.9) 
    # end
    for w1 in w:
      x1[w1] =np.sin(2 * np.pi * f * t[w1] + m1[w1]) * 0.2
    # end
    w1 = w + int(s) + 1
    x[w1] = x[w1] + a * r * x1
  # end
# end
audio = x * 32767
audio = audio.astype(np.int16)
play_obj = sa.play_buffer(audio, 1, 2, fs)
play_obj.wait_done()
