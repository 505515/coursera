import urllib.request
import urllib.parse
import json

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url).read().decode('utf-8')

    js = json.loads(uh)

    #print(json.dumps(js, indent=4))

    if 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    place = js["results"][0]["place_id"]
    print(place)