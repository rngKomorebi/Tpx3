# =============================================================================
# This script is used for getting number of hits in particular shots and 
# saves them as 'shot-hits' in two columns for future analysis.
# =============================================================================
import numpy as np
import os
import sys
import csv
import matplotlib.pyplot as plt
sys.path.insert(1, '/home/sjing/Documents/daisuki/COMPASS/Codes/Functional')
from path_to_shot import *
# from_ = input("Shots from: ")
# to_ = input("to: ")
shots = np.genfromtxt("shots:21215-21237.txt")

hits = np.zeros(int(len(shots)))
for i in range (0, len(shots)):
    shot = int(shots[i])
    print("Doing shot %s" %shot)

    # Go to the @shot folder
    try:
        path = path_to_shot(shot)
    except:
        continue
    
    # Get the data
    Data_tpx3_cent = np.genfromtxt('%s_hits.csv' %shot, delimiter=',')
    # Read the first row in the .csv file and get index of the required signal
    with open('%s_hits.csv' % shot, newline='') as f:
        reader = csv.reader(f)
        row1 = next(reader) 
    
    index = row1.index('#ToA')
    time_new = np.array([row[index] for row in Data_tpx3_cent])
    hits[i] = len(time_new)
    
# create one array of several columns for np.savetxt
new_content = np.column_stack((shots,hits))
# create new txt with the generated active window; last two arguments for integer, other way
# the txt will be full of floats

# Go to the directory with the shots and save under an appropriate name
os.chdir(path[:78])
name = path[70:76]
np.savetxt("Shot_vs_Hits_%s.txt" %name, new_content, fmt='%i')

plt.plot(shots,hits,'o')
