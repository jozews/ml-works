
import tensorflow as tf
import keras
import numpy as np

# ˈ strong accent counts 2
# ˌ soft accent counts 1.5
# () optional counts 0.5

chars_ipa = "t͡ɕɪlɐˈvʲekɡorməʊadɛsʐɨznuɔbʃɫɵiːäʂɯ̞.äjpʒɑɑæ⁽⁾xf()ɤʉˌ"
chars_vowels_ipa = "ɪɐeoəaɛɨuɔɵiä.äɑɑæ"

file_nouns = open("ru-nouns.txt", "r+") 
chars = ""

for line in file_nouns:
    noun_ipa = line.split()[1]
    chars_new = [char for char in noun_ipa if char not in chars]
    chars += "".join(chars_new)

print(chars)