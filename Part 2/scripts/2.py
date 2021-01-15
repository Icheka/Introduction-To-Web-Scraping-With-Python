from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/warandpeace.html"

html = urlopen(url)
bsoup = BeautifulSoup(html.read(), 'html.parser')
characters = bsoup.findAll('span', {'class': 'green'})
for character in characters:
    print(character.get_text())
