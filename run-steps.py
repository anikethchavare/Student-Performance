# Student Performance - Run Steps

''' Run this program if you're setting up Student Performance. '''

''' STEP 1 - Download the latest version of Python. The system should be 64-bit. '''
''' STEP 2 - Run this Python file. '''

# Imports
import os
import time

# Set the Directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Start
print("\nInstalling and upgrading the necessary packages and tools required for Student Performance.\n")

time.sleep(5)

# Packages and Tools
os.system("python -m pip install --upgrade pip")

os.system("pip install --upgrade pandas")
os.system("pip install --upgrade matplotlib")
os.system("pip install --upgrade numpy")