# =============================================================================
# Get the ToA data from the .csv file and plot it
# Defined as function for the "All_in_One.py" script
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import os
import csv
import sys

sys.path.insert(1, '/home/sjing/Documents/daisuki/COMPASS/Codes/Functional')
from path_to_shot import *


def ToA(shot):
    # Go to the @shot folder
    try:
        path = path_to_shot(shot)
    except:
        raise SystemExit
    
    # Get the data
    Data_tpx3_cent = np.genfromtxt('%s.csv' % shot, delimiter=',')
    # Read the first row in the .csv file and get index of the required signal
    with open('%s.csv' % shot, newline='') as f:
        reader = csv.reader(f)
        row1 = next(reader) 
    
    try:
        index = row1.index('#Trig-ToA[arb]')
        time_new = np.array([row[index] for row in Data_tpx3_cent]) * 25/4096/1e6 + 912
        p=1
    except: 
        print("No 'Trig-ToA' in the list")
        index = row1.index('#ToA')
        time_new = np.array([row[index] for row in Data_tpx3_cent]) * 25/4096/1e6
    
    # try:
    #     index = row1.index('#ToA')
    #     time_new = np.array([row[index] for row in Data_tpx3_cent]) * 25/4096/1e6
    # except:
    #     print("No 'ToA' in the list")
    
    # Define the bins with the step of 1.5625
    bins1 = int((time_new[-1] - time_new[0]) / 1.5625*4)
    
    # Prepare figure and compute the histogram
    fig = plt.figure()
    plt.rcParams.update({'font.size': 16})
    plt.title("Shot %s: ToA" % shot)
    plt.xlabel("Time, [ms]")
    plt.ylabel("Hits, [a.u.]")
    a = plt.hist(time_new, bins1, (time_new[0], time_new[-1]), histtype='step', fill=False)
    # Get rid off the noisy "ones" for an appropriate plot
    data = a[0]
    timee = a[1]
    
    ones = np.where(data < 10)[0]
    
    for i in range (0, len(ones)):
        data[ones[i]] = 0
    
    # Define limits of x axis for an appropriate plot
    try:
        left, right = int(timee[np.nonzero(data)[0][0]]-10), int(timee[np.nonzero(data)[0][-1]]+10)
        plt.xlim(left, right)
    except:
        print("Probably no data at all or just a weak signal")
        pass
    
    # Show the result within the limits
    plt.show()
    
    # Go to the Figures folder
    try:
        os.chdir("%s/Figures" % path)
    except:
        print("No folder, creating one")
        os.mkdir("%s/Figures" % path)
        os.chdir("%s/Figures" % path)

    fig.set_size_inches(20., 12., forward=True)
    fig.savefig('%s:ToA_plt.pdf' % shot)
    plt.close(fig)