from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/warandpeace.html"

html = urlopen(url)
bsoup = BeautifulSoup(html.read(), 'html.parser')
characters = bsoup.findAll('span', {'class': 'green'})
    
for i in range(len(characters)):
    print("{}: {}".format(i + 1, characters[i].get_text()))

print("========")
print("The count is: {}".format(len(characters)))
