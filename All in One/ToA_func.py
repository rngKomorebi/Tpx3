# =============================================================================
# Get the ToA data from the .csv file and plot it
# Defined as function for the "All_in_One.py" script
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import os

def ToA(shot):
    # Go to the @shot folder
    try:
        os.chdir("/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/%s" % shot)
    except:
        print("No folder, no data")
    
    # Get the data
    
    Data_tpx3_cent = np.genfromtxt('%s.csv' % shot, delimiter=',')
    
    try:
        cent = np.array([row[8] for row in Data_tpx3_cent])
        time_new = np.array([row[4] for row in Data_tpx3_cent]) * 25/4096/1e6
    except:
        time_new = np.array([row[2] for row in Data_tpx3_cent]) * 25/4096/1e6
    
    # Define the bins with the step of 1.5625
    bins1 = int((time_new[-1] - time_new[0]) / 1.5625)
    
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
    
    ones = np.where(data == 1)[0]
    
    for i in range (0, len(ones)):
        data[ones[i]] = 0
    
    # Define limits of x axis for an appropriate plot
    left, right = int(timee[np.nonzero(data)[0][0]]-10), int(timee[np.nonzero(data)[0][-1]]+10)
    
    # Show the result within the limits
    plt.xlim(left, right)
    plt.show()
    
    # Go to the Figures folder
    try:
        os.chdir("/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/%s/Figures" % shot)
    except:
        print("No folder, creating one")
        os.mkdir("/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/%s/Figures" % shot)
        os.chdir("/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/%s/Figures" % shot)

    fig.set_size_inches(20., 12., forward=True)
    plt.savefig('%s:ToA_plt.pdf' % shot)
    plt.close(fig)