import numpy as np
import matplotlib.pyplot as plt

fs = 10000 # サンプリング周波数 = 10000 サンプル/秒
f1 = 5       # 波形1の周波数 = 5Hz
a1 = 3       # 波形1の振幅   = 3
wave=[]
 
# 2種類の周波数のサイン波を生成
for n in np.arange(fs):       # サンプル数分だけ繰り返す
   x = a1 * np.sin(2.0 * np.pi * f1 * n / fs)      # サンプル値を計算する
   wave.append(x)                                  # サンプルを wave に追加していく

# 波形を表示
plt.plot(wave)
plt.show()