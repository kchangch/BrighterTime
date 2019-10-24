import requests
import json
import sys

def get_lat_lng(address, apiKey):
    """
    Returns the latitude and longitude of a location using the Google Maps Geocoding API. 
    API: https://developers.google.com/maps/documentation/geocoding/start

    # INPUT -------------------------------------------------------------------
    apiKey                  [str]
    address                 [str]

    # RETURN ------------------------------------------------------------------
    lat                     [float] 
    lng                     [float] 
    """
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(address.replace(' ','+'), apiKey))
    try:
        response = requests.get(url)
        resp_json_payload = response.json()
        lat = resp_json_payload['results'][0]['geometry']['location']['lat']
        lng = resp_json_payload['results'][0]['geometry']['location']['lng']
    except:
        print('ERROR: {}'.format(address))
        lat = 0
        lng = 0
    return lat, lng

if __name__ == '__main__':
    #get key
    fileName = open('key.txt', 'r')
    apiKey = fileName.read()
    # get coordinateste
    address = '4107 Frances Street, Burnaby, BC'
    lat, lng = get_lat_lng(address, apiKey)
    get_lat_lng(address, apiKey)
    print('{} Coordinates:\nLatitude:  {}°\nLongitude: {}°'.format(address,lat, lng))