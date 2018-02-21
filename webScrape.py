from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'

# Scrape the HTML
uClient = uReq(my_url)
pageHtml = uClient.read()
uClient.close()

# Parse html with soup
pageSoup = soup(pageHtml, "html.parser")

# Grabs each product
containers = pageSoup.findAll("div",{"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")
headers = "Brand, Product Name, Shipping\n"
f.write(headers)


for container in containers:
    brand = container.div.div.a.img["title"]

    productName = container.findAll("a",{"class":"item-title"})[0].text

    shipping = container.findAll("li",{"class":"price-ship"})[0].text.strip()

    print("Brand: " + brand)
    print("Name: " + productName)
    print("Shipping: " + shipping)

    f.write(brand.replace(",", " ") + "," + productName.replace(",", "|") + "," + shipping + "\n")

f.close()