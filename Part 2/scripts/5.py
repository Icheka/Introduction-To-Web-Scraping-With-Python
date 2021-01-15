from urllib.request import urlopen
from bs4 import BeautifulSoup
# we'll use the datetime module to get today's date
from datetime import date

#url = "our_fictional_url"

#html = urlopen(url)
html = """<div class="product featured" data-featured-product="pr/123456">
    <img src="some_long_path_to_an_image_of_a_cup" alt="product:123456" />
    <div class="product-name">Gold-plated Cups!</div>
</div>
<div class="product last-featured">
    <img src="some_long_path_to_an_image_of_a_spoon" alt="product:123457" />
    <div class="product-name">Gold-plated Spoons</div>
</div>
<div class="product">
    <img src="some_long_path_to_an_image_of_a_doorknob" alt="product:123456" />
    <div class="product-name">Gold-plated Doorknobs</div>
</div>"""

bsoup = BeautifulSoup(html, 'html.parser')
products = bsoup.findAll('div', {'class': 'product-name'})
    
for product in products:
    product_name = product.get_text()
    # save product to a file
    with open('featured-products-file.txt', 'a+') as f:
        msg = "{}: The featured product is {}\n".format(date.today(), product_name)
        f.write(msg)
print("File saved.")
