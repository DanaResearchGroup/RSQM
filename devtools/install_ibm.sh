#!/bin/bash

# This script sets up and deploys the IBMRxn software

# Step 1: Create a directory named IBMRxn
mkdir IBMRxn

# Step 2: Change directory to IBMRxn
cd IBMRxn

# Step 3: Clone the ibmrxn Git repository
pip install git+https://github.com/rxn4chemistry/rxn4chemistry.git

echo "Installation complete. You can now use the 'IBMRxn' software."
