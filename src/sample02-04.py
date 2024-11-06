# transportation of program9.sci
# 
# fast version - optimized using array
#
# audio playback using simpleaudio
#   To install
#    pip install simpleaudio

import numpy as np
import simpleaudio as sa

# initial parameters
fs=44100      # sampling frequency
l=20          # duration of sound
x=np.arange(l*fs)*0.0   # initial sound data (silence)

# create melody pattern table
i=np.arange(97)
c=(i/16).astype(int)-(i/32).astype(int)*2
d= c/7*12-(c.astype(int)/7*12)

w=np.arange(fs)
t=w/44100
a=1-np.exp(-t/0.01)
# outer loop to produce multiple part
for kk in range(1,7,1) :
  r=np.exp(-t/0.1/kk)
  # innner loop to produce music note sequence for a part
  for i in range(1,96,kk) :
    s = int(i * fs / 6)   # sample position for a note
    k = i - int(i/4)*4    # pitch of a note
    m= k
    n=int(m/7*12 + 0.4 + d[i+1]-(kk*2))
    f=440*pow(2,(n/12))   # frequency
    m1=np.sin(2 * np.pi * f * t) * np.sin(20 * t) * (kk-0.9)  # tamper
    w1 = w + int(s) + 1   # window to add note
    x[w1] = x[w1] + a * r * np.sin(2 * np.pi * f * t + m1) * 0.2 # add a note
  # end
# end

# audio playback
audio = x * 32767
audio = audio.astype(np.int16)
play_obj = sa.play_buffer(audio, 1, 2, fs)
play_obj.wait_done()
