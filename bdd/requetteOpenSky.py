import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta, timezone

# Définir les informations d'identification
username = 'your_username'
password = 'your_password'
icao = "LFPG"

local_time = datetime.now()

# Convertir l'heure locale en UTC
utc_time = local_time.astimezone(timezone.utc)


end_time = utc_time
start_time = end_time - timedelta(hours=1)

start_timestamp = int(start_time.timestamp())
end_timestamp = int(end_time.timestamp())



urlGeneralBis= f"https://opensky-network.org/api/flights/arrival?airport={icao}&begin={start_timestamp}&end={end_timestamp}"
url = "https://opensky-network.org/api/flights/arrival?airport=LFPG&begin=1734020112&end=1734023712"
url = "https://opensky-network.org/api/flights/arrival?airport=JFK&begin=1734024464&end=1734028064"
print(end_timestamp)
print(start_timestamp)
print(urlGeneralBis)

print("je suis la avant le get")
# Faire une requête GET avec les identifiants pour récupérer les données
response = requests.get(urlGeneralBis,auth=HTTPBasicAuth('majeurSmith', 'azerty'))

print("tarte au citron")
if response.status_code==200:
   data = response.json()
   print("chocolat")
   print(data)
   """
   for flight in data['states']:
      print(f"Flight {flight[1]} is at latitude {flight[6]} and longitude {flight[5]}")
   """
else : 
   print(f"Erreur: {response.status_code}")
   print(response.text)




