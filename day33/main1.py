import requests
from datetime import datetime 

my_lat = 39.099728
my_log = -94.578568

parameters = {

    "lat" : my_lat,
    "lng" : my_log,
    "formatted" : 0
}



response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)

response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise.split("T")[1].split(":")[0])
print(sunset)
#print(data)
'''


longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)

'''