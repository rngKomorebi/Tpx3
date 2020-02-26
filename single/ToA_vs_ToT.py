# =============================================================================
# Get the ToT and ToA data from the .csv file and plot it as histogram
# ToT vs ToA. This gives a number of hits of specific energies at the
# exact time.
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
    index1 = row1.index('#ToA')
    index2 = row1.index('#ToTtotal[arb]')
    time_new = np.array([row[index1] for row in Data_tpx3_cent]) * 25/4096/1e6
    tot = np.array([row[index2] for row in Data_tpx3_cent])
except:
    print("No 'ToA' or 'ToT' in the list")
    raise SystemExit

bins1 = np.arange(time_new[0], time_new[-1], 1.5625)
bins2 = np.arange(0, 25000, 25)

H, xedges, yedges = np.histogram2d(time_new, tot, [bins1,bins2])
a = np.histogram(time_new, bins = bins1)

# Time and data from the histogram
timee = a[1]
data = a[0]

# Get rid off the noisy "ones" for an appropriate plot
ones = np.where(data == 1)[0]

for i in range (0, len(ones)):
    data[ones[i]] = 0

# Define the range limits for the appropriate plot
try:
    l_lim, r_lim = int(np.nonzero(data)[0][0]), int(np.nonzero(data)[0][-1])
    left, right = timee[l_lim]-10, timee[r_lim]+10
except:
    print("Could not compute 'left' and 'right'")

y, x = np.meshgrid(yedges,xedges)

data_masked = np.ma.masked_where(H == 0, H)

# =============================================================================
# Plot
# =============================================================================

fig = plt.figure()
fig1 = plt.gca()
plt.rcParams.update({'font.size': 16})
try:
    plt.xlim(left, right)
except:
    pass
yticks = fig1.yaxis.get_major_ticks() 
yticks[0].label1.set_visible(False)
# plt.pcolormesh(x, y, H)
plt.pcolormesh(x, y, data_masked)
plt.colorbar(label="Hits")
plt.title("Shot %s: ToT vs ToA" % shot)
plt.xlabel("ToA, [ms]")
plt.ylabel("ToT, [a.u.]")

# Go to the Figures folder
try:
    os.chdir("%s/Figures" % path)
except:
    print("No folder, creating one")
    os.mkdir("%s/Figures" % path)
    os.chdir("%s/Figures" % path)

fig.set_size_inches(20., 12., forward=True)
fig.savefig('%s:ToTvsToA.png' % shot) # OS freeze while saving .pdf
