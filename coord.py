import requests
import urllib.parse

address = 'Ampere - Lavoisier'

url = 'https://nominatim.openstreetmap.org/search.php?q=' + urllib.parse.quote_plus(address) +'&format=jsonv2'

response = requests.get(url).json()
print(response[0]["lat"])
print(response[0]["lon"])