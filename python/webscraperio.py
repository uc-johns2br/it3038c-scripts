import requests, re
from bs4 import BeautifulSoup

r = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/phones").content
soup = BeautifulSoup(r, "lxml")

tags = soup.findAll("div", {"class":re.compile('(ratings)')})

for p in tags:
    a = p.findAll("p",{"class":"pull-right"})
    print(type(a[0].string))
    print(a[0].string)