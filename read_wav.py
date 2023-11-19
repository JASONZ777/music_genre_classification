import librosa
import librosa.display
import librosa.feature
import os
import numpy as np
import matplotlib.image as mping
path = "E:/ZHOU/dsp_project/gtzan"
folders = os.listdir(path)
num = 0  # file iterator
cat = 0
for f in folders:
    new_path = os.path.join(path, f)
    for file in os.listdir(new_path):
        wav, sr = librosa.load(os.path.join(new_path, file))
        mel = librosa.feature.melspectrogram(y=wav, sr=sr)
        mel = librosa.power_to_db(mel, ref=np.max)
        librosa.display.specshow(mel, y_axis='mel', x_axis='time')
        mping.imsave('mel_spectrum_jpg/'+str(cat)+'/'+str(num)+'.jpg', mel)
        num += 1
    cat += 1
    num = 0