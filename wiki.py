
import requests
from bs4 import BeautifulSoup

# Get Russian nouns

#url_nouns = "https://en.openrussian.org/list/nouns?start=%s"
#max_nouns = 22827
#
#file = open("ru-nouns.txt", "w") 
#
#nouns = []
#start = 0
#while start < max_nouns:
#    html = requests.get(url_nouns % start).text
#    soup = BeautifulSoup(html, 'html.parser')
#    rows = soup.find_all("i", {"class" : "icon icon-play play read auto"})
#    for row in rows:
#        noun = row["data-read"]
#        nouns.append(noun)
#        file.write("\n" + noun)
#    start += 50


# Get ipa

url_wiki = "https://en.wiktionary.org/wiki/%s#Pronunciation"
file = open("de-nouns.txt", "r+") 

text_new = ""
for noun in file:
    noun_stripped = noun.strip()
    html = requests.get(url_wiki % noun_stripped).text
    soup = BeautifulSoup(html, 'html.parser')
    element_ipa = soup.find("span", {"class" : "IPA"})
    if element_ipa is None:
        continue
    noun_ipa = element_ipa.text.replace("[", "").replace("]", "").replace("/", "")
    if soup.find("abbr", {"title" : "masculine gender"}) is not None:
        gender = "m"
    elif soup.find("abbr", {"title" : "feminine gender"}) is not None:
        gender = "f"
    elif soup.find("abbr", {"title" : "neuter gender"}) is not None:
        gender = "n"
    new_line = f"\n{noun_stripped} {noun_ipa} {gender}"
    print(new_line)
    text_new += new_line

file.write(text_new)

    
    
