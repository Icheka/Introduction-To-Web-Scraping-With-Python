from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://webscraper.io/test-sites/e-commerce/allinone')
bsoup = BeautifulSoup(html.read(), 'html.parser')
print(bsoup.prettify())
