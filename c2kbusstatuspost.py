import requests, json, time
from datetime import datetime

# version 1.0 of c2kbusstatuspost
# fixed variables to use until I figure out how to get them
bus_number = "bus505"
bus_route = "Cicero-95th-103rd"
location = "lost in the woods"
status_uri = "http://imapex-c2k-c2klistener.green.browndogtech.com/api/v1.0/busses/" + bus_number

# echo the variables for testing purposes only - will be commented out
#print bus_number
#print bus_route
#print location
#print status_uri

# loop to generate status post every 60 seconds
# provides timestamp, bus name, location
while True:
    rightnow = datetime.now()
    ts = rightnow.strftime("%Y%m%d-%H%M%S")
    r = requests.post(status_uri, data={"last_checkin":ts, "name":bus_number, "last_location":location, "route":bus_route})
    print r.status_code
    print r.text
    time.sleep(60)
