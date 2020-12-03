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

shots = np.genfromtxt('shots_all.txt')


for i in range (0, len(shots)):
    shot = int(shots[i])

    print("Doing shot %s" %shot)
    # Go to the @shot folder
    try:
        path = path_to_shot(shot)
    except:
        continue
    # Check the .csv file size (too big will end with a kernel crash)
    if os.path.getsize("%s.csv" % shot)*1e-6 > 200:
        print("%s.csv is too big, going to the next shot" % shot)
        continue
    # Check if the needed hitmap exists: if yes, go on to the next shot
    os.chdir('Figures')
    if os.path.isfile("%s:Hitmap_time_sum.pdf" % shot) == True:
        print("%s: Hitmap_time_sum.pdf exists, going to the next shot" % shot)
        continue
    else:
        print("%s: No Hitmap_time_sum.pdf, working on it" % shot)
        os.chdir(path)
    
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
        print("%s: No 'ToA' in the list" %shot)
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
    
    # Separate the matrix signal into according to time intervals
    rows_sep = [[] for i in range(0,100)]
    cols_sep = [[] for i in range(0,100)]
    for i in range (0,len(rows_sep)):
        in_from = np.where(time[i] == time_new)[0][0]
        in_to = np.where(time[i+1] == time_new)[0][0]
        rows_sep[i] = row_total[in_from:in_to]
        cols_sep[i] = col_total[in_from:in_to]
    
        # Separate the matrix signal, each next combine the previous
    rows_sum = [[] for i in range(0,100)]
    cols_sum = [[] for i in range(0,100)]
    for i in range (0,len(rows_sum)):
        in_to = np.where(time[i+1] == time_new)[0][0]
        rows_sum[i] = row_total[0:in_to]
        cols_sum[i] = col_total[0:in_to]
    
    # Find the edges of the active window
    row_left = min(row_total)
    row_right = max(row_total)
    col_left = min(col_total)
    col_right = max(col_total)
    row_l = int(row_right-row_left)
    col_l = int(col_right-col_left)
    
    # Compute histograms separated by a step
    hists_sep = [[] for i in range(0,100)]
    xedges_sep = [[] for i in range(0,100)]
    yedges_sep = [[] for i in range(0,100)]
    for i in range (0,len(hists_sep)):
        # hists[i], xedges[i], yedges[i] = np.histogram2d(rows[i], cols[i], 256, [[0,255],[0,255]])
        hists_sep[i], xedges_sep[i], yedges_sep[i] = np.histogram2d(rows_sep[i], cols_sep[i],(row_l, col_l),[[row_left,row_right], [col_left, col_right]])
    
    # Compute histograms with a step adding one by one
    hists_sum = [[] for i in range(0,100)]
    xedges_sum = [[] for i in range(0,100)]
    yedges_sum = [[] for i in range(0,100)]
    for i in range (0,len(hists_sum)):
        hists_sum[i], xedges_sum[i], yedges_sum[i] = np.histogram2d(rows_sum[i], cols_sum[i],(row_l, col_l),[[row_left,row_right], [col_left, col_right]])
    
    # # Mask zeros to get a white color of the background
    # H1_masked = np.ma.masked_where(H1 == 0, H1)
    
    # Limits for the same colorbars
    vmin_sep = 0
    vmax_sep = np.max(hists_sep[0])
    vmin_sum = 0
    vmax_sum = np.max(hists_sum[-1])
    # =============================================================================
    # Plot
    # =============================================================================
    
    fig_sep, axes_sep = plt.subplots(10,10, figsize=(15,15))
    fig_sep.subplots_adjust(hspace = 0, wspace=0)
    # plt.rcParams.update({'font.size': 16})
    
    axes_sep=axes_sep.ravel()
    
    for i in range (0,len(rows_sep)):
        figs_sep = axes_sep[i].imshow(hists_sep[i], interpolation='none', origin='low', vmin=vmin_sep,vmax=vmax_sep)
        # fig.colorbar(figs, ax=axes[i], label="Hits", fraction=0.046, pad=0.04)
        # axes[i].set_title(int(time[i]))
        # axes[i].set_xlabel("Pixels, x axis")
        # axes[i].set_ylabel("Pixels, y axis")
        axes_sep[i].axis('off')
    
    # Go to the Figures folder
    try:
        os.chdir("%s/Figures" % path)
    except:
        print("No folder, creating one")
        os.mkdir("%s/Figures" % path)
        os.chdir("%s/Figures" % path)
    
    # fig.set_size_inches(20., 12., forward=True)
    plt.savefig('%s:Hitmap_time_sep.pdf' % shot, bbox_inches='tight')
    
    
    
    fig_sum, axes_sum = plt.subplots(10,10, figsize=(15,15))
    fig_sum.subplots_adjust(hspace = 0, wspace=0)
    # plt.rcParams.update({'font.size': 16})
    
    axes_sum=axes_sum.ravel()
    
    for i in range (0,len(rows_sum)):
        # figs_sum = axes_sum[i].imshow(hists_sum[i], interpolation='none', origin='low', vmin=vmin_sum,vmax=vmax_sum)
        figs_sum = axes_sum[i].imshow(hists_sum[i], interpolation='none', origin='low')
        # fig.colorbar(figs, ax=axes[i], label="Hits", fraction=0.046, pad=0.04)
        # axes[i].set_title(int(time[i]))
        # axes[i].set_xlabel("Pixels, x axis")
        # axes[i].set_ylabel("Pixels, y axis")
        axes_sum[i].axis('off')
    
    # Go to the Figures folder
    try:
        os.chdir("%s/Figures" % path)
    except:
        print("%s: No folder, creating one" %shot)
        os.mkdir("%s/Figures" % path)
        os.chdir("%s/Figures" % path)
    
    # fig.set_size_inches(20., 12., forward=True)
    plt.savefig('%s:Hitmap_time_sum.pdf' % shot, bbox_inches='tight')
    plt.close()
