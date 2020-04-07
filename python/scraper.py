import requests, re
from  bs4 import BeautifulSoup

try:
    data = requests.get("https://darksky.net/forecast/39.1712,-84.5489/us12/en").text
    soup = BeautifulSoup(data, "lxml")
    span = soup.find("span", {"class":"summary swap"})
    tempAndConditions = span.text
    span = soup.find("span", {"class":"currently__summary next swap"})
    f = span.text
    forecast = f.strip()
    print('Current temp and weather is: %s Forecast is: %s' % (tempAndConditions,forecast))
except:
    print("An error occurred.")