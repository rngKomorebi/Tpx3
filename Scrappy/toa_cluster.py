import numpy as np
import matplotlib.pyplot as plt
import os
# Plot figures in external window:
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')

shot = input("Cislo vyboje:")

try:
    os.chdir(shot)
except:
    print("No folder, no data")

Data_tpx3_cent = np.genfromtxt('shot_%s_W0020_J07-200128-170807-1_cent-0.csv' % shot, delimiter=',')

time_tpx3 = np.array([row[2] for row in Data_tpx3_cent])
cent = np.array([row[5] for row in Data_tpx3_cent])
time_new = time_tpx3 * 25/4096/1e6

toa_full = np.zeros(len(cent))
# Fill the arrays with indices
for i in range (0, len(cent)):
    if cent[i] == 1:
        toa_full[i] = i
    
# Cut off the empty part, leaving an array of indices of clusters
toa = toa_full[toa_full != 0]

# Transform float to integer for further manipulation
toa = toa.astype(int)

# Prepair array for data from ToT_total
toa_tot = np.zeros(len(toa))

# Fill the ToT arrays with the corresponding data
for j in range (0, len(toa)):
    a = toa[j]
    toa_tot[j] = time_new[a]
    j += j
    
plt.figure()
plt.rcParams.update({'font.size': 16})
plt.hist(toa_tot, 128, (14400, 14600), histtype='step', fill=False)
# plt.legend()

plt.show()