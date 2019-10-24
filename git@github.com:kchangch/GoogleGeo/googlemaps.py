import googlemaps
from datetime import datetime

fileName = open('key.txt', 'r')
apiKey = fileName.read()
gmaps = googlemaps.Client(key = apiKey)

# stdin = input("Enter address: ")
# geocode_result = gmaps.geocode(stdin)
# print(geocode_result)
now = datetime.now()
directions_result = gmaps.directions("4107 Frances Street, Burnaby",
                                     "SFU Burnaby",
                                     mode="transit",
                                     departure_time=now)

