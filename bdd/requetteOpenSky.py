import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta

# Définir les informations d'identification
username = 'your_username'
password = 'your_password'
icao = "JFK"
end_time = datetime.utcnow()
start_time = end_time - timedelta(hours=1)
start_timestamp = int(start_time.timestamp())
end_timestamp = int(end_time.timestamp())


urlGeneral="https://opensky-network.org/api/flights/arrival?airport="+icao+"&begin=1702219200&end=1702222800"
urlGeneralBis= f"https://opensky-network.org/api/flights/arrival?airport={icao}&begin={start_timestamp}&end={end_timestamp}"
url = "https://opensky-network.org/api/flights/arrival?airport=LFPG&begin=1702219200&end=1702222800"
print(urlGeneral==urlGeneralBis)
#print(url)
print(urlGeneral)
# Faire une requête GET avec les identifiants pour récupérer les données
response = requests.get(urlGeneral)

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




