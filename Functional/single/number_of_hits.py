# =============================================================================
# This script is solely aimed at getting the number of hits
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import os
import csv
import time
from path_to_shot import *
start_time = time.time() # Execution time
# Plot figures in external window:
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')

shot = int(input("Shot number:"))

# Go to the @shot folder
try:
    path = path_to_shot(shot)
except:
    raise SystemExit

# Get the data
Data_tpx3_cent = np.genfromtxt('shot_21185W0020_J07-201125-161718-1-0.csv', delimiter=',')
# Read the first row in the .csv file and get index of the required signal
with open('shot_21185W0020_J07-201125-161718-1-0.csv', newline='') as f:
    reader = csv.reader(f)
    row1 = next(reader) 

index = row1.index('#ToA')
time_new = np.array([row[index] for row in Data_tpx3_cent]) * 25/4096/1e6
