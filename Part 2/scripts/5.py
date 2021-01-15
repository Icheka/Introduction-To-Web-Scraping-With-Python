from urllib.request import urlopen
from bs4 import BeautifulSoup
# we'll use the datetime module to get today's date
from datetime import date

url = "our_fictional_url"

html = urlopen(url)

bsoup = BeautifulSoup(html.read(), 'html.parser')
products = bsoup.findAll('div', {'class': {'product-name', 'featured'}})
    
for product in products:
    product_name = product.get_text()
    # save product to a file
    with open('featured-products-file.txt', 'a+') as f:
        msg = "{}: The featured product is {}\n".format(date.today(), product_name)
        f.write(msg)
print("File saved.")
