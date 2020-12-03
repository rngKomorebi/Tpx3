# =============================================================================
# Get the hits by col and row coordinates and plot it as histogram. Plot full
# window in the first row, adjusted window (unmasked pixels) in the second row
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import os
import csv
from path_to_shot import *
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
    index1 = row1.index('#Col')
    index2 = row1.index('#Row')
    index3 = row1.index('#Centroid')
    index4 = row1.index('#ToA')
    col_total = np.array([row[index1] for row in Data_tpx3_cent])
    row_total = np.array([row[index2] for row in Data_tpx3_cent])
    cent = np.array([row[index3] for row in Data_tpx3_cent])
    time_new = np.array([row[index4] for row in Data_tpx3_cent]) * 25/4096/1e6
except:
    print("No 'ToA' in the list")
    raise SystemExit

# Calculate a step for 10 hitmaps
# step = (time_new[-1] - time_new[0]) / 10
step = int(len(time_new) / 101)

# Separate time interval into 10 intervals for different hitmaps
# time = np.zeros(10)
# for i in range (0,len(time)):
#     time[i] = time_new[0]+step*(i+1)
time = np.zeros(101)
for i in range (0,len(time)):
    step_new = step*i
    time[i] = time_new[step_new]

# Separate the matrix signal into ten according to time intervals
rows = [[] for i in range(100)]
cols = [[] for i in range(100)]
for i in range (0,len(rows)):
    in_from = np.where(time[i] == time_new)[0][0]
    in_to = np.where(time[i+1] == time_new)[0][0]
    rows[i] = row_total[in_from:in_to]
    cols[i] = col_total[in_from:in_to]

# Find the edges of the active window
row_left = min(row_total)
row_right = max(row_total)
col_left = min(col_total)
col_right = max(col_total)
row_l = int(row_right-row_left)
col_l = int(col_right-col_left)

# Compute histograms with a step: H - all data
hists = [[] for i in range(100)]
xedges = [[] for i in range(100)]
yedges = [[] for i in range(100)]
for i in range (0,len(hists)):
    # hists[i], xedges[i], yedges[i] = np.histogram2d(rows[i], cols[i], 256, [[0,255],[0,255]])
    hists[i], xedges[i], yedges[i] = np.histogram2d(rows[i], cols[i],(row_l, col_l),[[row_left,row_right], [col_left, col_right]])

# # Mask zeros to get a white color of the background
# H1_masked = np.ma.masked_where(H1 == 0, H1)

# Limits for the same colorbars
vmin = 0
vmax = np.max(hists[0])
# =============================================================================
# Plot
# =============================================================================

fig, axes = plt.subplots(10,10, figsize=(15,15))
fig.subplots_adjust(hspace = 0, wspace=0)
# plt.rcParams.update({'font.size': 16})

axes=axes.ravel()

for i in range (0,len(rows)):
    figs = axes[i].imshow(hists[i], interpolation='none', origin='low', vmin=vmin,vmax=vmax)
    # fig.colorbar(figs, ax=axes[i], label="Hits", fraction=0.046, pad=0.04)
    # axes[i].set_title(int(time[i]))
    # axes[i].set_xlabel("Pixels, x axis")
    # axes[i].set_ylabel("Pixels, y axis")
    axes[i].axis('off')

# Go to the Figures folder
try:
    os.chdir("%s/Figures" % path)
except:
    print("No folder, creating one")
    os.mkdir("%s/Figures" % path)
    os.chdir("%s/Figures" % path)

# fig.set_size_inches(20., 12., forward=True)
plt.savefig('%s:Hitmap_time.pdf' % shot, bbox_inches='tight')


