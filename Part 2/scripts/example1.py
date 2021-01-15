from urllib.request import urlopen
from bs4 import BeautifulSoup

war = "http://www.pythonscraping.com/pages/warandpeace.html"
ecomm1 = "https://webscraper.io/test-sites/e-commerce/allinone"

html = urlopen(war)
bsoup = BeautifulSoup(html.read(), 'html.parser')
print(bsoup.prettify())
