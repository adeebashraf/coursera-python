# networking-json-api.py

import urllib
import json

location = raw_input("Enter location: ")
url = 'http://python-data.dr-chuck.net/geojson'
param = { "sensor": "false", "address": location}
url = url + '?' + urllib.urlencode(param)

print 'Retrieving', url
response = urllib.urlopen(url)
text = response.read()
print "Retrieved", len(text), 'characters'

js = json.loads(text)
print 'Place id', js['results'][0]['place_id']
