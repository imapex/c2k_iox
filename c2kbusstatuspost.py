import requests, json, time
from datetime import datetime

# version 1.02 of c2kbusstatuspost
# fixed variables to use until I figure out how to get them
bus_number = "bus0648"
bus_route = "Pulaski-87th-95th"
location = "GPS Temporarily Unavailable"
listener_url  = "http://imapex-c2k-c2klistener.green.browndogtech.com/api/v1.0/busses"
headers = {'Content-type': 'application/json'}

# loop to generate status every 60 seconds
# provides timestamp, bus name, location
# 1.01 logic corrected for POST via API
# 1.02 logic adds check for existing bus record before POST and use PUT for status update
# repeated POST creates new records for the same bus
while True:
    r = requests.get(listener_url + '/' + bus_number)
    if r.status_code == 200 :
        payload = {
        "last_checkin": datetime.now().strftime("%Y%m%d" + "-" + "%H%M%S"),
        "last_location": location
        }
        r = requests.put(listener_url + '/' + bus_number, data=json.dumps(payload), headers=headers)
        print r.status_code
        print r.text
    else:
        payload = {
        "id": "",
        "name": bus_number,
        "last_checkin": datetime.now().strftime("%Y%m%d" + "-" + "%H%M%S"),
        "last_location": location,
        "route": bus_route,
        "status": ""
        }
        r = requests.post(listener_url, data=json.dumps(payload), headers=headers)
        print r.status_code
        print r.text
    time.sleep(60)
