# =============================================================================
# Get the ToT data from .csv file and plot it separating by clusters
# Defined as function for the "All_in_One.py" script.
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import os
import csv
import sys

sys.path.insert(1, '/home/sjing/Documents/daisuki/COMPASS/Codes/Functional')
from path_to_shot import *

def ToT_cluster(shot):
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
        index1 = row1.index('#ToTtotal[arb]')
        index2 = row1.index('#Centroid')
        tot_total = np.array([row[index1] for row in Data_tpx3_cent]) # Total ToT
        cent = np.array([row[index2] for row in Data_tpx3_cent])
    except:
        print("No 'ToA' in the list")
        raise SystemExit
    
    
    # Prepare empty arrays for the indices of particular clusters
    ones_full = np.zeros(len(cent))
    twos_full = np.zeros(len(cent))
    threes_full = np.zeros(len(cent))
    fours_full = np.zeros(len(cent))
    fives_full = np.zeros(len(cent))
    
    # Fill the arrays with indices
    for i in range (0, len(cent)):
        if cent[i] == 1:
            ones_full[i] = i
        elif cent[i] == 2:
            twos_full[i] = i
        elif cent[i] == 3:
            threes_full[i] = i
        elif cent[i] == 4:
            fours_full[i] = i
        else: fives_full[i] = i
    
    # Cut off the empty part, leaving an array of indices of clusters
    ones = ones_full[ones_full != 0]
    twos = twos_full[twos_full != 0]
    threes = threes_full[threes_full != 0]
    fours = fours_full[fours_full != 0]
    fives = fives_full[fives_full != 0]
    
    # Transform float to integer for further manipulation
    ones = ones.astype(int)
    twos = twos.astype(int)
    threes = threes.astype(int)
    fours = fours.astype(int)
    fives = fives.astype(int)
    
    # Prepair array for the data from ToT_total
    ones_tot = np.zeros(len(ones))
    twos_tot = np.zeros(len(twos))
    threes_tot = np.zeros(len(threes))
    fours_tot = np.zeros(len(fours))
    fives_tot = np.zeros(len(fives))
    
    # Fill the ToT arrays with the corresponding data
    for j in range (0, len(ones)):
        a = ones[j]
        ones_tot[j] = tot_total[a]
        
    a,j = 0,0
    for j in range (0, len(twos)):
        a = twos[j]
        twos_tot[j] = tot_total[a]
    
    a,j = 0,0  
    for j in range (0, len(threes)):
        a = threes[j]
        threes_tot[j] = tot_total[a]
    
    a,j = 0,0   
    for j in range (0, len(fours)):
        a = fours[j]
        fours_tot[j] = tot_total[a]
        
    a,j = 0,0
    for j in range (0, len(fives)):
        a = fives[j]
        fives_tot[j] = tot_total[a]
        
    # Prepair a tuple of arrays filled with ToT clusters for stacked histogram
    tot_multi = [ones_tot, twos_tot, threes_tot, fours_tot, fives_tot]
    labels = ['1', '2', '3', '4', '5']
    
    # To add some text to the legend
    empty = np.zeros(len(tot_multi))
    # Bin value==25
    # bins1 = np.arange(0,25000,1000)
    # Comptute a histogram
    # hist = np.histogram(tot_multi, bins=bins1)
    # timee = hist[0]
    # data = hist[1]
    # =============================================================================
    # Plot
    # =============================================================================
    
    fig = plt.figure()
    plt.rcParams.update({'font.size': 16})
    plt.title("Shot %s: ToT by clusters" % shot)
    plt.xlabel("ToT, [a.u.]")
    plt.ylabel("Hits, [a.u.]")
    plt.plot(empty, color = 'white', label="Cluster size:")
    plt.hist(tot_multi, 1000, (0, 25000), histtype='step', stacked=True, fill=False, label = labels)
    # plt.plot(timee, data)
    plt.legend()
    
# Go to the Figures folder
    try:
        os.chdir("%s/Figures" % path)
    except:
        print("No folder, creating one")
        os.mkdir("%s/Figures" % path)
        os.chdir("%s/Figures" % path)
    
    fig.set_size_inches(20., 12., forward=True)
    plt.savefig('%s:ToT_cluster.pdf' % shot)
    plt.close(fig)
