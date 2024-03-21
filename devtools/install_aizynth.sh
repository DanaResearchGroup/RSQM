#!/bin/bash

# Instructions for installing aizynthfinder software

# Step 1: Create a directory named aizynth
mkdir aizynth

# Step 2: Change directory to aizynth
cd aizynth

# Step 3: Create a Conda environment named 'aizynth-env' with Python version between 3.8 and 3.10
conda create 'python>=3.8,<3.10' -n aizynth-env

# Step 4: Activate the Conda environment
conda activate aizynth-env

# Step 5: Install the 'aizynthfinder' package using pip

python -m pip install aizynthfinder[all]

echo "Installation complete. You can now use the 'aizynthfinder' software."

