# =============================================================================
# Get the hits by col and row coordinates and plot it as histogram. Plot full
# window in the first row, adjusted window (unmasked pixels) in the second row
# Output is 10 frames, trigger is used
# Used for plotting the window with exact edges read from the file
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import os
import csv
import sys
sys.path.insert(1, '/home/sjing/Documents/daisuki/COMPASS/Codes/Functional')

from path_to_shot import *
# Plot figures in external window:
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt') 

shotss = np.genfromtxt('shots:21215-21237.txt')
# from_ = input("Execute for shots from:")
# to_ = input("to:")

for i in range (0, len(shotss)):
    shot = int(shotss[i])
    print("Doing shot %s" %shot)

    os.chdir("/home/sjing/Documents/daisuki/COMPASS/12th_RE_18.11.2020")
    Data_pixels = np.genfromtxt("12th RE Tpx3 active pixels.csv", delimiter=',',skip_header=0)
    
    with open('12th RE Tpx3 active pixels.csv', newline='') as f:
        reader = csv.reader(f)
        row1 = next(reader) 
    
    try:
        index_shot = row1.index('Shot')
        index_brow = row1.index('Bottom row')
        index_trow = row1.index('Top row')
        index_lcol = row1.index('Left col')
        index_rcol = row1.index('Right col')
        index_pixels = row1.index('N of pixels')
        
        shots = np.array([row[index_shot] for row in Data_pixels])
        rows_bottom = np.array([row[index_brow] for row in Data_pixels])
        rows_top = np.array([row[index_trow] for row in Data_pixels])
        cols_left = np.array([row[index_lcol] for row in Data_pixels])
        cols_right = np.array([row[index_rcol] for row in Data_pixels])
        N_pixels = np.array([row[index_pixels] for row in Data_pixels])
    except:
        print("Error while getting data from csv")
        
    try:
        index_current_shot = np.where(shots==shot)[0][0]
        row_bottom = rows_bottom[index_current_shot]
        row_top = rows_top[index_current_shot]
        col_left = cols_left[index_current_shot] 
        col_right = cols_right[index_current_shot]
        row_l = int(row_top-row_bottom)
        col_l = int(col_right-col_left)
        N_pixels_cur = int(N_pixels[index_current_shot])
    except:
        print("Error while getting edges")
    
        
    # Go to the @shot folder
    try:
        path = path_to_shot(shot)
    except:
        continue
        
    if os.path.isfile("Figures/%s:Hitmap_time_sum_fin.pdf" %shot):
        print("%s: figures already exist" %shot)
        continue
    else:
        pass
    
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
        # index4 = row1.index('#ToA')
        col_total = np.array([row[index1] for row in Data_tpx3_cent])
        row_total = np.array([row[index2] for row in Data_tpx3_cent])
        cent = np.array([row[index3] for row in Data_tpx3_cent])
        # time_new = np.array([row[index4] for row in Data_tpx3_cent]) * 25/4096/1e6
    except:
        print("No 'ToA' in the list")
        raise SystemExit
    
    try:
        index4 = row1.index('#Trig-ToA[arb]')
        time_new = np.array([row[index4] for row in Data_tpx3_cent]) * 25/4096/1e6 + 912
        p=1
    except:
        print("No 'Trig-ToA' in the list")
        index4 = row1.index('#ToA')
        time_new = np.array([row[index4] for row in Data_tpx3_cent]) * 25/4096/1e6
    
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
    
    # Separate the matrix signal according to time intervals
    rows_sep = [[] for i in range(0,100)]
    cols_sep = [[] for i in range(0,100)]
    for i in range (0,len(rows_sep)):
        in_from = np.where(time[i] == time_new)[0][0]
        in_to = np.where(time[i+1] == time_new)[0][0]
        rows_sep[i] = row_total[in_from:in_to]
        cols_sep[i] = col_total[in_from:in_to]
    
    # Separate the matrix signal, each next combines the previous
    rows_sum = [[] for i in range(0,100)]
    cols_sum = [[] for i in range(0,100)]
    for i in range (0,len(rows_sum)):
        in_to = np.where(time[i+1] == time_new)[0][0]
        rows_sum[i] = row_total[0:in_to]
        cols_sum[i] = col_total[0:in_to]    
    
    # Compute histograms separated by a step
    hists_sep = [[] for i in range(0,100)]
    xedges_sep = [[] for i in range(0,100)]
    yedges_sep = [[] for i in range(0,100)]
    for i in range (0,len(hists_sep)):
        # hists[i], xedges[i], yedges[i] = np.histogram2d(rows[i], cols[i], 256, [[0,255],[0,255]])
        hists_sep[i], xedges_sep[i], yedges_sep[i] = np.histogram2d(rows_sep[i], cols_sep[i],(row_l, col_l),[[row_bottom,row_top], [col_left, col_right]])
    
    # Compute histograms with a step adding one by one
    hists_sum = [[] for i in range(0,100)]
    xedges_sum = [[] for i in range(0,100)]
    yedges_sum = [[] for i in range(0,100)]
    for i in range (0,len(hists_sum)):
        hists_sum[i], xedges_sum[i], yedges_sum[i] = np.histogram2d(rows_sum[i], cols_sum[i],(row_l, col_l),[[row_bottom,row_top], [col_left, col_right]])
    
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
    
    rows=3
    cols=5
    
    fig_sep, axes_sep = plt.subplots(rows,cols, figsize=(15,10))
    fig_sep.subplots_adjust(hspace = 0.2, wspace=0)
    plt.rcParams.update({'font.size': 22})
    fig_sep.suptitle("Total pixels: {N_pixels}, Rows: {row_bottom}-{row_top}, Cols: {col_left}-{col_right}".format(N_pixels=N_pixels_cur, row_bottom=int(row_bottom), row_top=int(row_top), col_left=int(col_left), col_right=int(col_right)))
    
    axes_sep=axes_sep.ravel()
    
    for i in range (0, rows*cols):
        figs_sep = axes_sep[i].imshow(hists_sep[i], interpolation='none', origin='low', vmin=vmin_sep,vmax=vmax_sep)
        # fig.colorbar(figs, ax=axes[i], label="Hits", fraction=0.046, pad=0.04)
        time_step = int(time[i+1])-int(time[i])
        axes_sep[i].set_title('%i ms' % time_step)
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
    plt.savefig('%s:Hitmap_time_sep_fin.pdf' % shot, bbox_inches='tight')
    
    
    
    fig_sum, axes_sum = plt.subplots(rows,cols, figsize=(15,10))
    fig_sum.subplots_adjust(hspace = 0.2, wspace=0)
    plt.rcParams.update({'font.size': 22})
    fig_sum.suptitle("Total pixels: {N_pixels}, Rows: {row_bottom}-{row_top}, Cols: {col_left}-{col_right}".format(N_pixels=N_pixels_cur, row_bottom=int(row_bottom), row_top=int(row_top), col_left=int(col_left), col_right=int(col_right)))

    
    axes_sum=axes_sum.ravel()
    
    for i in range (0, rows*cols):
        # figs_sum = axes_sum[i].imshow(hists_sum[i], interpolation='none', origin='low', vmin=vmin_sum,vmax=vmax_sum)
        figs_sum = axes_sum[i].imshow(hists_sum[i], interpolation='none', origin='low')
        # fig.colorbar(figs, ax=axes[i], label="Hits", fraction=0.046, pad=0.04)
        time_step = int(time[i])
        axes_sum[i].set_title('%i ms' % time_step)
        # axes[i].set_xlabel("Pixels, x axis")
        # axes[i].set_ylabel("Pixels, y axis")
        axes_sum[i].axis('off')
    
    # Go to the Figures folder
    try:
        os.chdir("%s/Figures" % path)
    except:
        print("No folder, creating one")
        os.mkdir("%s/Figures" % path)
        os.chdir("%s/Figures" % path)
    
    # fig.set_size_inches(20., 12., forward=True)
    plt.savefig('%s:Hitmap_time_sum_fin.pdf' % shot, bbox_inches='tight')
    plt.close(fig_sum)
    plt.close(fig_sep)
