import requests
from requests.auth import HTTPBasicAuth

# Définir les informations d'identification
username = 'your_username'
password = 'your_password'

# URL de l'API OpenSky
url = 'https://opensky-network.org/api/states/all'

# Faire une requête GET avec les identifiants pour récupérer les données
response = requests.get(url, auth=HTTPBasicAuth("majeurSmith", "9f196160"))

print("tarte au citron")
data = response.json()
print("chocolat")
print(data)
for flight in data['states']:
   print(f"Flight {flight[1]} is at latitude {flight[6]} and longitude {flight[5]}")

