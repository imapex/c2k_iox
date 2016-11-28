# Cisco Kiddie Kounter (C2K): IoX App

Cisco Kiddie Kounter (C2K) is a sample demonstration applicaiton that illustrates how several technologies from Cisco can be b$

## Demo Application Background

The initial problem to be solved is to to count the kids on the school bus.  Additional capabilities include tracking school b$

The total application consists of the following services:
* [c2k_demo](https://github.com/imapex/c2k_demo) - Full Demo Application Setup and Details
* [c2k_iox](https://github.com/imapex/c2k_iox) - Details on the Cisco IOx Client Application
* [c2k_listener](https://github.com/imapex/c2k_listener) - Centralized services for receiving bus updates from IoX and maintai$
* [c2k_msg](https://github.com/imapex/c2k_msg) - Messaging services via Cisco Spark or Tropo

# c2k_iox 

This repository provides the code and details for the Cisco IOx Application that monitors GPS Location and WLAN clients on a Cisco 829 IoX Router in a school bus and periodically reports status to the C2K Listener.

### Table of Contents 

* [Setup and PreRequisites](#setup-and-prerequisites)
* [Loading Demo Application](#loading-demo-application)
* [Connecting the Arduino and Router](#connecting-the-arduino-and-router)

# Setup and PreRequisites 

To build and replicate this demonstraiton you'll need access to an IOx device. The original demonstration was created using a Cisco 829 router.

## IOx Router/Host 

[Cisco DevNet IOx Community](https://developer.cisco.com/site/iox/index.gsp) is the best place for resources on developing with IOx.  Before beginning this, or any other IOx app project, you can find information on preparing your router.  This includes: 

* installing the correct IOS image 
* configuing IOS to enable IOx 
* loading the neccessary cartridges for running applications

This demonstration runs as a Python PaaS application, so follow the [PaaS QuickStart](https://developer.cisco.com/media/iox-dev-guide-7-12-16/getstarted/quickstart-paas/) preperation for that demonstration.  

# Loading Demo Application

Begin by cloning the c2k_iox repository to your local machine.  

```
git clone https://github.com/imapex/c2k_iox

# Change to the gbos_iox directory
cd c2k_iox/

# View the contents of the repo, you should see something similar
ls
LICENSE     resources        README.md      iox_app

```

## IOx PaaS Application

Follow these steps to properly package and deploy c2k_iox to your device.  This assumes you already have installed and setup ioxclient on your local machine.  For information on how to do that, see [ioxclient-reference](https://developer.cisco.com/media/iox-dev-guide-7-12-16/ioxclient/ioxclient-reference/) on DevNet.  

*All of these steps will be accomplished from a terminal on your workstation*

1. Enter the iox_app directory.  You should see the following files.  

	```
	cd iox_app/
	```
	
	| File | Description |
	| --- | --- | 
	| package.yaml | YAML formated description of the IOx application |
	| sample_package_config.ini | Application configuration file (empty) | 
	| device_mapping.json | Host Router Device Mapping (ie network and serial) | 
	| requirements.txt | Python requirements list | 
	| main.py | Python code to run for application | 
	

2. The `sample_package_config.ini` file is a template for the required configuraiton file for the IOx application.  Make a copy of this file that you will customize for your deployment.  

    ```
    cp sample_package_config.ini package_config.ini
    ```
    

