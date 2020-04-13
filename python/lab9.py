import requests
import json

#Get data from API server
r = requests.get('http://localhost:3000')

#Set variable equal to JavaScript Object Notation value of get request. This creates a list of dictionaries
data = r.json()

#Loop to print output
for i in data:
    nameOfWidget = i['name']
    nameOfColor = i['color']
    print("%s is %s." % (nameOfWidget.capitalize(),nameOfColor))
