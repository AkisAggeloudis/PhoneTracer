import phonenumbers

import folium

from PhoneNumber import num
#from geopy.geocoders import Nominatim
from phonenumbers import geocoder

Number = phonenumbers.parse(num)

#get country

yourLocation = geocoder.description_for_number(Number, "en")
print(yourLocation)

#get service provider

from phonenumbers import carrier

service_prov = phonenumbers.parse(num)
print(carrier.name_for_number(service_prov, "en"))

#get the map info 1

Key = "eb94cdd82e4140f9abd140973e61b241"

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

query = str(yourLocation)

result = geocoder.geocode(query)
print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat, lng)

Map = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=yourLocation).add_to(Map)

#save map to html file

Map.save("myLocation.html")

#get location 2
#loc = Nominatim(user_agent="GetLoc")
#getLoc = loc.geocode(yourLocation)
#print(getLoc.address)
#print("Latitude = ", getLoc.latitude, "\n")
#print("Longitude = ", getLoc.longitude)