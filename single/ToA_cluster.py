# =============================================================================
# Get the ToA data form the .csv file and plot it separating by the cluster
# size.
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
    index2 = row1.index('#Centroid')
    time_new = np.array([row[index1] for row in Data_tpx3_cent]) * 25/4096/1e6
    cent = np.array([row[index2] for row in Data_tpx3_cent])
except:
    print("No 'ToA' in the list")
    raise SystemExit

# Define the bins with the step of 1.5625
bins1 = np.arange(time_new[0], time_new[-1], 1.5625)

# Compute a histogram
a = np.histogram(time_new, bins = bins1)

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

# Prepair array for the data from time_new
ones_toa = np.zeros(len(ones))
twos_toa = np.zeros(len(twos))
threes_toa = np.zeros(len(threes))
fours_toa = np.zeros(len(fours))
fives_toa = np.zeros(len(fives))

# Fill the toa arrays with the data corresponding to the cluster size
for j in range (0, len(ones)):
    a = ones[j]
    ones_toa[j] = time_new[a]
    
a,j = 0,0
for j in range (0, len(twos)):
    a = twos[j]
    twos_toa[j] = time_new[a]

a,j = 0,0  
for j in range (0, len(threes)):
    a = threes[j]
    threes_toa[j] = time_new[a]

a,j = 0,0   
for j in range (0, len(fours)):
    a = fours[j]
    fours_toa[j] = time_new[a]
    
a,j = 0,0
for j in range (0, len(fives)):
    a = fives[j]
    fives_toa[j] = time_new[a]
    
# Prepair a tuple of arrays filled with toa clusters for stacked histogram
toa_multi = [ones_toa, twos_toa, threes_toa, fours_toa, fives_toa]
labels = ['1', '2', '3', '4', '5']

bins = int((time_new[-1] - time_new[0]) / 1.5625)
empty = np.zeros(len(time_new))

fig = plt.figure()
plt.rcParams.update({'font.size': 16})
plt.title("Shot %s: ToA by clusters" % shot)
plt.xlabel("Time, [ms]")
plt.ylabel("Hits, [a.u.]")
plt.plot(empty, color = 'white', label="Cluster size:")
a = plt.hist(toa_multi, bins, (time_new[0], time_new[-1]), histtype='step', stacked=True, fill=True, label = labels)

data = None
for i in range (0,4):
    if max(a[0][i+1]) > max(a[0][i]):
        data = a[0][i+1]
timee = a[1]

# Get rid off the noisy "ones" for an appropriate plot
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

plt.legend(loc="upper left")

# Go to the Figures folder
try:
    os.chdir("%s/Figures" % path)
except:
    print("No folder, creating one")
    os.mkdir("%s/Figures" % path)
    os.chdir("%s/Figures" % path)

print("Time of execution: %s seconds" % (time.time() - start_time))
fig.set_size_inches(20., 12., forward=True)
plt.savefig('%s:ToA_cluster.pdf' % shot)