import requests, json, time
from datetime import datetime

# version 1.01 of c2kbusstatuspost
# fixed variables to use until I figure out how to get them
bus_number = "bus0643"
bus_route = "Cicero-95th-103rd"
location = "lost in the woods"
status_uri = "http://imapex-c2k-c2klistener.green.browndogtech.com/api/v1.0/busses"
headers = {'Content-type': 'application/json'}

# echo the variables for testing purposes only - will be commented out
#print bus_number
#print bus_route
#print location
#print status_uri

# loop to generate status post every 60 seconds
# provides timestamp, bus name, location
# 1.01 logic corrected for POST via API
# future changes will add check for existing bus record before POST and use PUT for status update
# repeated POST creates new records for the same bus
while True:
    rightnow = datetime.now()
    ts = rightnow.strftime("%Y%m%d-%H%M%S")
    payload = {
    "id": "",
    "name": "bus0643",
    "last_checkin": ts,
    "last_location": location,
    "route": bus_route,
    "status": ""
    }
    r = requests.post(status_uri, data=json.dumps(payload), headers=headers)
    print r.status_code
    print r.text
    time.sleep(60)
