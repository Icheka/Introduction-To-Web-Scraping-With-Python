from urllib.request import urlopen

html = urlopen("https://google.com")
print(html.read())
