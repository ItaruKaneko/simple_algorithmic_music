# simpleaudio によるオーディオ再生
import simpleaudio
wav_obj = simpleaudio.WaveObject.from_wave_file("sample01-04.wav")
play_obj = wav_obj.play()
play_obj.wait_done()

# playsound によるオーディオ再生(参考)
# 以下のように playsound というライブラリも使える
# from playsound import playsound
# playsound('sample01-04.wav')
