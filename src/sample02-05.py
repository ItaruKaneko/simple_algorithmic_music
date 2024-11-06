# transportation of program8.sci
# stereo verseion
#
# to install simpleaudio
#    pip install simpleaudio
#
# audio playback using simpleaudio

import numpy as np
import simpleaudio as sa

fs=44100      # sampling frequency
l=20          # duration of sound
w = np.arange(fs*2)      # 2 sec window
t = w/fs                 # time offset in the window
x = np.zeros((l*fs,2))   # l*fs x 2ch array of floating zero
for ss in np.arange(5):      # 5 sections
  for v in np.arange(1,12,1): # 8 voices
    rand1=np.random.rand()   # random number
    rand2=np.random.rand()   # random number
    m1=np.random.rand()      # random number
    m2=np.random.rand()      # random number
    # produce attack shape using random number
    a=(1-np.exp(-t/pow(100,(-1-rand1)))) * np.exp(-t/(.5+rand2))*.2
    b1=(np.arange(64) % 8) + rand1 * 4
    b2=np.maximum(((pow(b1,2) % 5)-1).astype(int),0)
    for b in np.arange(0,16):  # 16 tones
      c1=(b % 2)
      p=int((b+ss*20)*fs/6)+w+1
      j=b-int(b/4/v)*4*v
      k=int(j/v)*(2+v)-v*7+14
      n=int(k/7*12+ss*3+12 + 0.4)-ss*5
      f=440*pow(2,(n/12)-3)
      m=np.sin(2 * np.pi * f * t) * np.sin(10 * t * m1) * v*m2
      x[p,c1]=x[p,c1]+a * np.sin(2* np.pi  * f*t+m)*0.2*b2[b]
    # end
  # end
# end

# audio playback
print(x.shape)
audio = x * 32767
audio = audio.astype(np.int16)
play_obj = sa.play_buffer(audio, 2, 2, fs)
play_obj.wait_done()
