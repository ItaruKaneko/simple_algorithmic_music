# array を使って sin 波形 を生成する
import numpy as np
import matplotlib.pyplot as plt

fs = 10000 # サンプリング周波数 = 10000 サンプル/秒
f1 = 5       # 波形1の周波数 = 5Hz
 
# n = サンプル番号列, t=サンプル時刻列 の array を作る
n = np.arange(fs)
t = n / fs         # t には fs サンプル数分の時刻の一覧表ができる

# sin 波形の生成
wave = np.sin(2.0 * np.pi * f1 * t)      # 波形は array の sin 関数で作ることができる

# 波形を表示
plt.plot(wave)
plt.show()