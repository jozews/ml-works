
import tensorflow as tf
import keras
import numpy as np

# ˈ strong accent counts 2
# ˌ soft accent counts 1.5
# () optional counts 0.5
# ː counts 2

genders = ["m", "f", "n"]
chars_all_ipa = "t͡ɕɪlɐˈvʲekɡorməʊadɛsʐɨznuɔbʃɫɵiːäʂɯ̞.äjpʒɑɑæ⁽⁾xf()ɤʉˌ"
chars_sonorous = "t͡ɕɪlɐvekɡorməʊadɛsʐɨznuɔbʃɫɵiäʂɯ̞äjpʒɑɑæxfɤʉ"
chars_non_sonorous = "ˈː.⁽⁾ˌ"
chars_vowels_ipa = "ɪɐeoəaɛɨuɔɵiääɑɑæ"

len_in = len(chars_sonorous)
len_out = len(genders)

file_nouns = open("ru-nouns.txt", "r+") 
chars = ""

list_in = []
list_out = []

for line in file_nouns:
    _, noun_ipa, gender = line.split()
    in_ = [noun_ipa.count(char) for char in chars_sonorous]
    out = [int(gender == g) for g in genders]
    list_in.append(in_)
    list_out.append(out)

model = keras.Sequential()
model.add(keras.layers.Dense(len_in))
model.add(keras.layers.Dense(int(len_in + len_out/2), activation=tf.nn.relu))
model.add(keras.layers.Dense(len_out, activation=tf.nn.softmax))

model.compile(optimizer=tf.train.AdamOptimizer(), loss='mean_squared_error', metrics=['accuracy'])

history = model.fit(np.array(list_in), np.array(list_out), epochs=75, verbose=1)