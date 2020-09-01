# =============================================================================
# Get the ToA data from the .csv file and plot it
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
Data_tpx3_cent = np.genfromtxt('%s.csv' % shot, delimiter=',')
# Read the first row in the .csv file and get index of the required signal
with open('%s.csv' % shot, newline='') as f:
    reader = csv.reader(f)
    row1 = next(reader) 

try:
    index = row1.index('#ToTtotal[arb]')
    tot_total = np.array([row[index] for row in Data_tpx3_cent])
except:
    print("No 'ToT' in the list")
    raise SystemExit


# =============================================================================
# Plot
# =============================================================================

# Prepare figure and compute the histogram
fig = plt.figure()
plt.rcParams.update({'font.size': 22})
plt.title("Shot %s: ToT" % shot)
plt.xlabel("ToT [a.u.]")
plt.ylabel("Hits [-]")
a = plt.hist(tot_total, 1000, (0, 25000), histtype='step', fill=False)
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

print("Time of execution: %s seconds" % (time.time() - start_time))
fig.set_size_inches(20., 12., forward=True)
plt.savefig('%s:ToT_plt.pdf' % shot)