# =============================================================================
# Get the ToA data from the .csv file and plot it
# Purposed for manual plotting the ToA figures in case auto plotting is
# flawed. Uses limits for the plots prescribed in the appropriate .csv file
# Plotting for a single input shot
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import os
import csv
import time
import sys
sys.path.insert(1, '/home/sjing/Documents/daisuki/COMPASS/Codes/Functional')
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

###------------------------------------###
# 25 ns, 1.5625 ns - clocks in the FPGA  #
# *25/4096 -> from binary to ns          #
# /1e6 -> ns to ms                       #
# +912 ms -> trigger                     #
###------------------------------------###

# try:
#     index = row1.index('#ToA')
#     time_new = np.array([row[index] for row in Data_tpx3_cent]) * 25/4096/1e6
# except:
#     print("No 'ToA' in the list")
#     raise SystemExit

try:
    index = row1.index('#Trig-ToA[arb]')
    time_new = np.array([row[index] for row in Data_tpx3_cent]) * 25/4096/1e6 + 912
    p=1
except:
    print("No 'Trig-ToA' in the list")
    index = row1.index('#ToA')
    time_new = np.array([row[index] for row in Data_tpx3_cent]) * 25/4096/1e6

# Define the bins with the step of 1.5625 ms
bins1 = int((time_new[-1] - time_new[0]) / 1.5625*4)

# =============================================================================
# Plot
# =============================================================================

# Prepare figure and compute the histogram
fig = plt.figure()
plt.rcParams.update({'font.size': 22})
plt.title("Shot %s: ToA" % shot)
plt.xlabel("Time [ms]")
plt.ylabel("Hits [-]")
a = plt.hist(time_new, bins1, (time_new[0], time_new[-1]), histtype='step', fill=False)
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

# ### This section is dedicated for limitting the plot using the predefined borders from a
# # .csv file ###
# os.chdir("/home/sjing/Documents/daisuki/COMPASS/12th_RE_18.11.2020")
# Data_limits = np.genfromtxt("12th RE Tpx3 plot limits.csv", delimiter=',',skip_header=0)

# with open('12th RE Tpx3 plot limits.csv', newline='') as f:
#     reader = csv.reader(f)
#     row1 = next(reader) 

# try:
#     index_shot = row1.index('Shot')
#     index_left = row1.index('Left')
#     index_right = row1.index('Right')

#     shots = np.array([row[index_shot] for row in Data_limits])
#     lefts = np.array([row[index_left] for row in Data_limits])
#     rights = np.array([row[index_right] for row in Data_limits])
# except:
#     print("Error while getting data from csv")
    
# try:
#     index_current_shot = np.where(shots==shot)[0][0]
#     left = lefts[index_current_shot]
#     right = rights[index_current_shot]
# except:
#     print("Error while getting limits")
    
# plt.xlim(left,right)

# # Manual plot limits manipulation
# if right > 1350:
#     right = 1350
#     plt.xlim(left,right)

# # Ask for the predefined plot limits
# left = input("Left: ")
# # right = input("Right: ")
# plt.xlim(int(left),int(right))

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
plt.savefig('%s:ToA_plt_test.pdf' % shot)