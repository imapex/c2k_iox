#!/usr/bin/env python

# IoX/CAF standard imports
import os
import sys
import logging
import time
import signal
import caf.handlers
from logging.handlers import RotatingFileHandler
from caf.static import ENV_VARS

# Project specific imports


# Signal handlers, primarily used for multi threaded applications
signal.signal(signal.SIGTERM, caf.handlers.handle_signal)
signal.signal(signal.SIGINT, caf.handlers.handle_signal)

logger = logging.getLogger("myapp")

# Get hold of the configuration file (package_config.ini)
moduledir = os.path.abspath(os.path.dirname(__file__))
BASEDIR = os.getenv("CAF_APP_PATH", moduledir)

# If we are not running with CAF, use the BASEDIR to get cfg file
tcfg = os.path.join(BASEDIR, "package_config.ini")

CONFIG_FILE = os.getenv("CAF_APP_CONFIG_FILE", tcfg)


def dump_caf_env():
    logger.info("Printing CAF ENV VARIABLES")
    for l in ENV_VARS:
        logger.info("%s: %s" % (l, os.getenv(l)))


def setup_logging(cfg):
    """
    Setup logging for the current module and dependent libraries based on
    values available in config.
    :param cfg:  SafeConfigParser instance
    :return:
    """
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Set log level based on what is defined in package_config.ini file
    loglevel = cfg.getint("logging", "log_level")
    logger.setLevel(loglevel)

    # Create a console handler only if console logging is enabled
    ce = cfg.getboolean("logging", "console")
    if ce:
        console = logging.StreamHandler()
        console.setLevel(loglevel)
        console.setFormatter(formatter)
        # add the handler to the root logger
        logger.addHandler(console)

    # The default is to use a Rotating File Handler
    log_file_dir = os.getenv("CAF_APP_LOG_DIR", "/tmp")
    log_file_path = os.path.join(log_file_dir, "app.log")

    # Lets cap the file at 1MB and keep 3 backups
    rfh = RotatingFileHandler(log_file_path, maxBytes=1024*1024, backupCount=3)
    rfh.setLevel(loglevel)
    rfh.setFormatter(formatter)
    logger.addHandler(rfh)

    return logger

if __name__ == '__main__':

    from ConfigParser import SafeConfigParser
    cfg = SafeConfigParser()
    cfg.read(CONFIG_FILE)
    setup_logging(cfg)
    dump_caf_env()

    # Log env variables

    # Main program routing below here...

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

