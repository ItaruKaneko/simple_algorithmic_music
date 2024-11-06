import numpy as np
import matplotlib.pyplot as plt

fs = 10000 # サンプリング周波数 = 10000 サンプル/秒
f1 = 30      # 波形1の周波数 = 30Hz
a1 = 1       # 波形1の振幅   = 1
f2 = 5       # 波形2の周波数 = 5Hz
a2 = 3       # 波形2の振幅   = 3
l  = 1       # 継続時間      = 1 秒

n = np.arange(fs)
t = n / fs         # t には fs サンプル数分の時刻の一覧表ができる
 
# 2種類の周波数のサイン波を生成
wave = a1 * np.sin(2.0 * np.pi * f1 * t)      # 波形1
wave = wave + a2 * np.sin(2.0 * np.pi * f2 * t)  # 波形2

# 波形を表示
plt.plot(wave[0:10000])
plt.show()

# FFT の計算と表示
spectrum=2*np.fft.fft(wave)/fs
plt.plot(np.abs(spectrum[0:50]))
plt.show()