from selenium import webdriver

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

baseurl = "https://easypronunciation.com/en/russian-phonetic-transcription-converter#phonetic_transcription"

mydriver = webdriver.Firefox()
mydriver.get(baseurl)