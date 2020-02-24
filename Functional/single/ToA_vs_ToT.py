# =============================================================================
# Get the ToT and ToA data from the .csv file and plot it as histogram
# ToT vs ToA. This gives a number of hits of specific energies at the
# exact time.
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import os
import time
from path_to_shot import *
start_time = time.time() # Execution time
# Plot figures in external window:
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')

shot = int(input("Shot number:"))

# Go to the @shot folder
path = path_to_shot(shot)

# Get the data

Data_tpx3_cent = np.genfromtxt('%s.csv' % shot, delimiter=',')

try:
    cent = np.array([row[8] for row in Data_tpx3_cent])
    time_new = np.array([row[4] for row in Data_tpx3_cent]) * 25/4096/1e6
    tot = np.array([row[6] for row in Data_tpx3_cent])
except:
    time_new = np.array([row[2] for row in Data_tpx3_cent]) * 25/4096/1e6
    tot = np.array([row[4] for row in Data_tpx3_cent])

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
l_lim, r_lim = int(np.nonzero(data)[0][0]), int(np.nonzero(data)[0][-1])
left, right = timee[l_lim]-10, timee[r_lim]+10
y, x = np.meshgrid(yedges,xedges)

data_masked = np.ma.masked_where(H == 0, H)

# =============================================================================
# Plot
# =============================================================================

fig = plt.figure()
fig1 = plt.gca()
plt.rcParams.update({'font.size': 16})
plt.xlim(left, right)
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
