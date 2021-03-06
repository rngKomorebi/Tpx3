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
    os.chdir(shot)
except:
    print("No folder, no data")

# Get the data
try:
    Data_tpx3_cent = np.genfromtxt('shot_%s_W0020_J07-200128-170807-1_cent-0.csv' % shot, delimiter=',')
    txt = 'shot_%s_W0020_J07-200128-170807-1_cent-0.csv' % shot
except:
    Data_tpx3_cent = np.genfromtxt('shot_%s_W0020_J07-200204-111002-1_cent.csv' % shot, delimiter=',')
    txt = 'shot_%s_W0020_J07-200204-111002-1_cent.csv' % shot

if txt == 'shot_%s_W0020_J07-200204-111002-1_cent.csv' % shot:
    cent = np.array([row[8] for row in Data_tpx3_cent]) # Clusters
    tot_total = np.array([row[6] for row in Data_tpx3_cent]) # Total ToT
else:
    cent = np.array([row[5] for row in Data_tpx3_cent]) # Clusters
    tot_total = np.array([row[3] for row in Data_tpx3_cent]) # Total ToT

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

empty = np.zeros(len(tot_multi))
# bins1 = np.arange()
# =============================================================================
# On y axis are hits, on x - time. cent==1 for photons, bigger clusters
# are for electrons and heavier particles
# =============================================================================
fig = plt.figure()
plt.rcParams.update({'font.size': 16})
plt.title("ToT by clusters")
plt.xlabel("Time, [ms]")
plt.ylabel("Hits, [a.u.]")
plt.plot(empty, color = 'white', label="Cluster size:")
plt.hist(tot_multi, 1000, (0, 25000), histtype='step', stacked=True, fill=False, label = labels)
# hist= np.histogram(tot_multi, bins = bins1)
plt.legend()

print("Time of execution: %s seconds" % (time.time() - start_time))

# Go to the Figures folder
try:
    os.chdir("Figures")
except:
    print("No folder, creating one")
    os.mkdir("Figures")
    os.chdir("Figures")

fig.set_size_inches(20., 12., forward=True)
plt.savefig('%s:ToT_cluster.pdf' % shot)
