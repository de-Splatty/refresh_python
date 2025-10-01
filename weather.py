import requests
city = 'New york'
url = 'http://api.weatherapi.com/v1/current.json?key=174c4c5ed7a3426e92a152208252509&q=' + city + '&aqi=no'
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_c')

description = weather_json.get('current').get('condition').get('text')

print("Today's weather in", city, "is", description, "and", temp, "degrees")