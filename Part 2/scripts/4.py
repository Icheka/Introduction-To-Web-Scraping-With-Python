from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "our_fictional_url"

html = urlopen(url)
bsoup = BeautifulSoup(html.read(), 'html.parser')
products = bsoup.findAll('div', {'class': 'product-name'})
    
for product in products:
    product_name = product.get_text()
    # save product_name to database
    # we'll learn how to save data to databases soon
