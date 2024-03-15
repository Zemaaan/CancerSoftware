import os
import PIL.Image
import tensorflow as tf
import numpy
from sklearn.model_selection import train_test_split
mnist = tf.keras.datasets.mnist

SeznamRakSlik = numpy.zeros(shape=(84, 320, 320, 3))
SeznamNeRakSlik = numpy.zeros(shape=(204, 320, 320, 3))

LabelsRak = numpy.ones(SeznamRakSlik.shape[0]).astype(int)
LabelsNeRak = numpy.zeros(SeznamNeRakSlik.shape[0]).astype(int)

Indeks = 0

DirektorijCancer = r"C:\Users\Hrvoje\OneDrive - Univerza v Mariboru\Namizje\Cancer\Skin_Data\Cancer\Testing"
DirektorijNeCancer = r"C:\Users\Hrvoje\OneDrive - Univerza v Mariboru\Namizje\Cancer\Skin_Data\Non_Cancer\Training"

for SlikaRaka in os.listdir(DirektorijCancer):
	PopolnaPot = DirektorijCancer + "\\" + SlikaRaka
	Slika = PIL.Image.open(PopolnaPot)

	Slika = Slika.resize((320, 320))
	SeznamRakSlik[Indeks] = Slika
	Indeks += 1

Indeks = 0
for SlikaNeRaka in os.listdir(DirektorijNeCancer):
	PopolnaPot = DirektorijNeCancer + "\\" + SlikaNeRaka
	Slika = PIL.Image.open(PopolnaPot)

	Slika = Slika.resize((320, 320))
	SeznamNeRakSlik[Indeks] = Slika
	Indeks += 1

print(SeznamRakSlik.shape)
print(SeznamNeRakSlik.shape)
print(LabelsRak.shape)
print(LabelsNeRak.shape)

Features = numpy.concatenate((SeznamRakSlik, SeznamNeRakSlik))
Labels = numpy.concatenate((LabelsRak, LabelsNeRak))

model = tf.keras.models.Sequential([
	tf.keras.layers.Flatten(input_shape=(320, 320, 3)),
	tf.keras.layers.Dense(128, activation='sigmoid'),
	tf.keras.layers.Dropout(0.2),
	tf.keras.layers.Dense(256, activation='sigmoid'),
	tf.keras.layers.Dropout(0.2),
	tf.keras.layers.Dense(10)
])

X_train, X_test, y_train, y_test = train_test_split(Features, Labels, test_size=0.33, random_state=42)

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])
model.fit(X_train, y_train, epochs=50)
