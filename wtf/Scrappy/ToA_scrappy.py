import numpy as np
import matplotlib.pyplot as plt
import os
import time
start_time = time.time() # Execution time
# Plot figures in external window:
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')

shot = input("Cislo vyboje:")

# Go to the @shot folder
try:
    os.chdir(shot)
except:
    print("No folder, no data")

# Get the data
Data_tpx3_cent = np.genfromtxt('shot_%s_W0020_J07-200204-111002-1_cent.csv' % shot, delimiter=',')

time_new = np.array([row[4] for row in Data_tpx3_cent]) * 25/4096
# time_new = time_tpx3 * 25/4096 # time in ms, 25 - ns, 4096 - binary
# del Data_tpx3_cent

# Define bin value - 1.5625; 30000 as max (30s)
# Range = (int(time_new[0])-5, int(time_new[-1])+5)

# bins1 = np.arange(0,30000,1.5625)
bins1 = np.arange(time_new[0], time_new[-1], 1.5625*100)

# Compute the histogram
# a = plt.hist(time_new, bins=bins1, range=Range, histtype='step')
# plt.show()

a = np.histogram(time_new, bins = bins1)
# del time_new
# del bins1
# Send data and time of the histogram into separate arrays
timee = a[1]
data = a[0]

# Get rid off the noisy "ones" for an appropriate plot
ones = np.where(data == 1)[0]

for i in range (0, len(ones)):
    data[ones[i]] = 0

# Define range for the plot
# left, right = int(np.nonzero(data)[0][0]), int(np.nonzero(data)[0][-1])
left, right = int(np.nonzero(data)[0][0]), int(np.nonzero(data)[0][-1])


fig = plt.figure()
plt.rcParams.update({'font.size': 16})

plt.plot(timee[left:right], data[left:right])

print("Time of execution: %s seconds" % (time.time() - start_time))
fig.set_size_inches(20., 12., forward=True)
# plt.savefig('%s:ToA_np1.pdf' % shot)