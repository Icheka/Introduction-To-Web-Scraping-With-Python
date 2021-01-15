from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")
bsoup = BeautifulSoup(html.read(), 'html.parser')
print(bsoup)
