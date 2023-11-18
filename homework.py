from math import radians, cos, sin, asin, sqrt
import requests

def distance(lat1, lat2, lon1, lon2):
     
    # Modul matematika bermuat fungsi bernama
    # radian yang mengonversi dari derajat ke radian.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    # formula Haversine
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a))
    
    # Radius bumi dalam kilometer. Gunakan 3956 untuk mil
    r = 6371
      
    # kalkulasikan hasil
    return(c * r)

url_launches = "https://api.spacexdata.com/v4/launches"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url_launches, headers=headers)
launches = data.json()

launches = launches[:20]

long = -122.420679
lat = 37.772537
access_token = 'pk.eyJ1IjoibGlsd3J6bWFuIiwiYSI6ImNsZmd6eGN0czAwM3kzcHIweWxnazdidTgifQ.3zuzm6Cx74mVBpVNAFr2Uw'

for launch in launches: 
    launchpad_id = launch['launchpad']
    url_launchpad = f'https://api.spacexdata.com/v4/launchpads/{launchpad_id}'
    data = requests.get(url_launchpad, headers=headers)
    launchpad = data.json()

    full_name = launchpad['full_name']
    lon1 = launchpad['longitude']
    lat1 = launchpad['latitude']

    geo_url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{full_name}.json?proximity={long},{lat}&access_token={access_token}"
    geo_response = requests.get(geo_url)
    geo_json = geo_response.json()
    center = geo_json['features'][0]['center']
    lon2 = center[0]
    lat2 = center[1]

    dist = distance(lat1,lat2,lon1,lon2)

    print(full_name, dist)