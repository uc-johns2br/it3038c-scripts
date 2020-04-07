import requests
import json

print('Please enter your zip code: ')
zip = input()

r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=cincinnati,us&appid=c9f9d9c417905bea604deda930a10184')
#print(r.content)
data = r.json()
#print(type(data))
print(data['weather'][0]['description'])