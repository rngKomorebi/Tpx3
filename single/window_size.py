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

shot1 = int(input("Shot number:"))
shot2 = int(input("Shot number:"))
shot3 = int(input("Shot number:"))

# Go to the @shot folder
try:
    path = path_to_shot(shot1)
except:
    raise SystemExit

# Get the data
Data_tpx3_cent1 = np.genfromtxt('%s.csv' % shot1, delimiter=',')
# Read the first row in the .csv file and get index of the required signal
with open('%s.csv' % shot1, newline='') as f1:
    reader1 = csv.reader(f1)
    row1 = next(reader1) 
    
# Go to the @shot folder
try:
    path = path_to_shot(shot2)
except:
    raise SystemExit
    
    # Get the data
Data_tpx3_cent2 = np.genfromtxt('%s.csv' % shot2, delimiter=',')
# Read the first row in the .csv file and get index of the required signal
with open('%s.csv' % shot2, newline='') as f2:
    reader2 = csv.reader(f2)
    row2 = next(reader2)
    
# Go to the @shot folder
try:
    path = path_to_shot(shot3)
except:
    raise SystemExit
    
    # Get the data
Data_tpx3_cent3 = np.genfromtxt('%s.csv' % shot3, delimiter=',')
# Read the first row in the .csv file and get index of the required signal
with open('%s.csv' % shot3, newline='') as f3:
    reader3 = csv.reader(f3)
    row3 = next(reader3) 

try:
    index11 = row1.index('#Col')
    index21 = row1.index('#Row')
    index31 = row1.index('#Centroid')
    col_total1 = np.array([row[index11] for row in Data_tpx3_cent1])
    row_total1 = np.array([row[index21] for row in Data_tpx3_cent1])
    cent = np.array([row[index31] for row in Data_tpx3_cent1])
except:
    print("No 'ToA' in the list")
    raise SystemExit
    

try:
    index12 = row2.index('#Col')
    index22 = row2.index('#Row')
    index32 = row2.index('#Centroid')
    col_total2 = np.array([row[index12] for row in Data_tpx3_cent2])
    row_total2 = np.array([row[index22] for row in Data_tpx3_cent2])
    cent2 = np.array([row[index32] for row in Data_tpx3_cent2])
except:
    print("No 'ToA' in the list")
    raise SystemExit
    
try:
    index13 = row3.index('#Col')
    index23 = row3.index('#Row')
    index33 = row3.index('#Centroid')
    col_total3 = np.array([row[index13] for row in Data_tpx3_cent3])
    row_total3 = np.array([row[index23] for row in Data_tpx3_cent3])
    cent3 = np.array([row[index33] for row in Data_tpx3_cent3])
except:
    print("No 'ToA' in the list")
    raise SystemExit
    

# Compute histograms
H1, xedges, yedges = np.histogram2d(row_total1, col_total1, 255, [[0,255],[0,255]])
H2, xedges, yedges = np.histogram2d(row_total2, col_total2, 255, [[0,255],[0,255]])
H3, xedges, yedges = np.histogram2d(row_total3, col_total3, 255, [[0,255],[0,255]])

# Mask zeros to get a white color of the background
H1_masked = np.ma.masked_where(H1 == 0, H1)
H2_masked = np.ma.masked_where(H2 == 0, H2)
H3_masked = np.ma.masked_where(H3 == 0, H3)

# Limits for the same colorbars
vmin = 0
vmax1 = np.max(H1)
vmax2 = np.max(H2)
vmax3 = np.max(H3)
# =============================================================================
# Plot
# =============================================================================

fig, axes = plt.subplots(1,3)
fig.subplots_adjust(hspace=0.6, wspace=0.6)
plt.rcParams.update({'font.size': 19})

fig1 = axes[0].imshow(H1_masked, interpolation='none', origin='low', vmin=vmin,vmax=vmax1)
# fig.colorbar(fig1, ax=axes[0], label="Hits", fraction=0.046, pad=0.04)
axes[0].set_title("Fully active window")
axes[0].set_xlabel("Pixels, x axis", fontsize=19)
axes[0].set_ylabel("Pixels, y axis", fontsize=19)
axes[0].axis('scaled')

fig2 = axes[1].imshow(H2_masked, interpolation='none', origin='low', vmin=vmin,vmax=vmax2)
# fig.colorbar(fig2, ax=axes[1], label="Hits", fraction=0.046, pad=0.04)
axes[1].set_title("\u2248 12000 active pixels")
axes[1].set_xlabel("Pixels, x axis", fontsize=19)
axes[1].set_ylabel("Pixels, y axis", fontsize=19)

fig3 = axes[2].imshow(H3_masked, interpolation='none', origin='low', vmin=vmin,vmax=vmax3)
# fig.colorbar(fig3, ax=axes[2], label="Hits", fraction=0.046, pad=0.04)
axes[2].set_title("\u2248 1600 active pixels")
axes[2].set_xlabel("Pixels, x axis", fontsize=19)
axes[2].set_ylabel("Pixels, y axis", fontsize=19)

fig.set_size_inches(14., 5., forward=True)
plt.savefig('Window_size1.pdf')
