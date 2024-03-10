#!/bin/bash

# This script sets up and deploys the ASKCOSv2 project.

# Step 1: Create a directory named ASKCOSv2
mkdir ASKCOSv2

# Step 2: Change directory to ASKCOSv2
cd ASKCOSv2

# Step 3: Clone the askcos2_core Git repository
git clone git@gitlab.com:mlpds_mit/askcosv2/askcos2_core.git

# Step 4: Change directory to askcos2_core
cd askcos2_core

# Step 5: Run the make deploy command to set up and deploy the project
make deploy

# After setup, the web app will be accessible at the host IP address, e.g., 0.0.0.0., or inter the FASTAPI using http://127.0.0.1:9100/docs#/ link, to confirm server availability
# You can access it in your browser and explore ASKCOSv2 as a guest without signup or login.
# Simply type the host IP address in your browser and follow the instructions on the welcome page.
#if you get a server error in the FASTAPI try: 
    #cd askcos2_core
    #git pull
    #make stop
    #make update
