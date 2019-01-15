import tensorflow as tf
import keras
import numpy as np

characters_all = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜß".lower()
articles_all = ["der", "die", "das"]

lines = tuple(open("list_nouns_german", "r"))
articles, nouns = zip(*[(line.lower().rstrip().split(" ")) for line in lines])

articles_indexes = [[int(article in articles_all[0]), int(article in articles_all[1]), int(article in articles_all[2])] for article in articles]
nouns_indexes = [[characters_all.index(c) for c in noun] for noun in nouns]
length_max = max(len(noun) for noun in nouns)

nouns_indexes = keras.preprocessing.sequence.pad_sequences(nouns_indexes,
                                                        value=0,
                                                        padding='post',
                                                        maxlen=length_max)

mean = int((len(characters_all) + len(articles_all)) / 2)

model = keras.Sequential()
model.add(keras.layers.Dense(len(characters_all), activation=tf.nn.sigmoid))
model.add(keras.layers.Dense(mean, activation=tf.nn.relu))
model.add(keras.layers.Dense(len(articles_all), activation=tf.nn.softmax))

model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='mean_squared_error',
              metrics=['accuracy'])

articles_indexes = np.array(articles_indexes)
nouns_indexes = np.array(nouns_indexes)

history = model.fit(nouns_indexes,
                    articles_indexes,
                    epochs=250,
                    verbose=1)


# convert to characters
#nouns_chars = ["".join([characters_all[i] for i in noun_index]) for noun_index in nouns_indexes]
#print(nouns_chars)