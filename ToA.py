import numpy as np
import matplotlib.pyplot as plt
import os
import time
start_time = time.time() # Execution time
# Plot figures in external window:
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')

shot = input("Shot number:")

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
bins1 = np.arange(time_new[0], time_new[-1], 1.5625)

# Compute a histogram
a = np.histogram(time_new, bins = bins1)

# Time and data from the histogram
timee = a[1]
data = a[0]

# Get rid off the noisy "ones" for an appropriate plot
ones = np.where(data == 1)[0]

for i in range (0, len(ones)):
    data[ones[i]] = 0

# Define the range limits for the appropriate plot
left, right = int(np.nonzero(data)[0][0]), int(np.nonzero(data)[0][-1])

fig = plt.figure()
plt.rcParams.update({'font.size': 16})
plt.title("ToA")
plt.xlabel("Time, [ms]")
plt.ylabel("Hits, [a.u.]")
plt.plot(timee[left:right], data[left:right])

# Go to the Figures folder
try:
    os.chdir("/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/%s/Figures" % shot)
except:
    print("No folder, creating one")
    os.mkdir("/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/%s/Figures" % shot)
    os.chdir("/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/%s/Figures" % shot)

print("Time of execution: %s seconds" % (time.time() - start_time))
fig.set_size_inches(20., 12., forward=True)
plt.savefig('%s:ToA.pdf' % shot)