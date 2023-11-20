# music_genre_classification
This project is based on the GTZAN dataset. Two files are broken including jz00054 and reggae00086, so we replace .wav files by copying intact songs from the same music genre. To expand the dataset, each song is cut into 10 equal-length segment, thus creating 10000 samples from 10 different music genres.

read_wav.py: read .wav audio files and create the Mel spectrum for each song which lasts for 30s.

basic_model.ipyb: include data pre-processing, training and test dataset splitting, LSTM and CNN models, and training process.

cnn_lstm.ipyb: for each segment, we conduct windowing operation without overlapping to further divide each segment into many time-related images. For each image, CNN is used to extract feature vectors, and then a LSTM network is performed for classification.  

pitch_mel_cnn_lstm.ipyb

Confusion matrix comparision:

LSTM: 85.7% ![confusion_matrix](https://github.com/JASONZ777/music_genre_classification/assets/94668646/348a7975-8f24-4c9b-9e17-8884604b4957)

CNN: 85.8% ![confusion matrix](https://github.com/JASONZ777/music_genre_classification/assets/94668646/14b548ef-01a4-436e-a681-ace86a1ba88c)

CNN+LSTM: 91.8% ![confusion_matrix](https://github.com/JASONZ777/music_genre_classification/assets/94668646/9cc39713-a43a-4d90-a91a-9c8ce00c46d7)

