import sys

print (sys.version)

import urllib.request
import urllib.parse


query = {"lat": 40.71, "lon": -74}
url = "http://api.open-notify.org/iss-pass.json"

query_string = urllib.parse.urlencode (query) 
url = url + "?" + query_string
with urllib.request.urlopen( url ) as response:
    response_text = response.read()        
    print( response_text )  