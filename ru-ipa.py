from selenium import webdriver

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

#baseurl = "https://easypronunciation.com/en/russian-phonetic-transcription-converter#phonetic_transcription"
#mydriver = webdriver.Firefox()
#mydriver.get(baseurl)

file = open("ru-nouns.txt", "r+") 
lines = [line.replace("masculine", "m").replace("feminine", "f").replace("neuter", "n") for line in file]
text = "".join(lines)
file.write(text)
