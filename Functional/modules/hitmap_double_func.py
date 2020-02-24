# =============================================================================
# Get the hits by col and row coordinates and plot it as histogram. Plot full
# window in the first row, adjusted window (unmasked pixels) in the second row.
# Defined as function for the "All_in_One" script.
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import os
from modules.path_to_shot import *

def hitmap_double(shot):

# Go to the @shot folder
    path = path_to_shot(shot)
    
    # Get data from the .csv file
    Data_tpx3_cent = np.genfromtxt('%s.csv'% shot, delimiter=',')
    
    # Row and col coordinates, cent = cluster size
    try:
        col_total = np.array([row[2] for row in Data_tpx3_cent])
        row_total = np.array([row[3] for row in Data_tpx3_cent])
        cent = np.array([row[8] for row in Data_tpx3_cent])
    except:
        col_total = np.array([row[0] for row in Data_tpx3_cent])
        row_total = np.array([row[1] for row in Data_tpx3_cent])
        cent = np.array([row[5] for row in Data_tpx3_cent])
    
    # Prepare arrays for the cluster separation
    col_ones = np.zeros(len(col_total))
    row_ones = np.zeros(len(row_total))
    col_noones = np.zeros(len(col_total))
    row_noones = np.zeros(len(row_total))
    
    # Fill the arrays with appropriate data defined by the cluster size
    for i in range (0, len(col_total)):
        if cent[i] == 1:
            col_ones[i] = col_total[i]
            row_ones[i] = row_total[i]
            col_noones[i] = 0
            row_noones[i] = 0
        else:
            col_ones[i] = 0
            row_ones[i] = 0
            col_noones[i] = col_total[i]
            row_noones[i] = row_total[i]
    
    # Compute histograms: H - all data, H1 - with particular cluster size
    H, xedges, yedges = np.histogram2d(row_total, col_total, 255, [[0,255],[0,255]])
    H1, xedges1, yedges1 = np.histogram2d(row_ones, col_ones, 255, [[0,255],[0,255]])
    H2, xedges2, xedges2 = np.histogram2d(row_noones, col_noones, 255, [[0,255],[0,255]])
    
    row_left = min(row_total)
    row_right = max(row_total)
    col_left = min(col_total)
    col_right = max(col_total)
    row_l = int(row_right-row_left)
    col_l = int(col_right-col_left)
    
    H_, xedges_, yedges_ = np.histogram2d(row_total, col_total, (row_l, col_l),[[row_left,row_right], [col_left, col_right]])
    H_1, xedges_1, yedges_1 = np.histogram2d(row_ones, col_ones, (row_l, col_l),[[row_left,row_right], [col_left, col_right]])
    H_2, xedges_2, ydeges_2 = np.histogram2d(row_noones, col_noones, (row_l, col_l),[[row_left,row_right], [col_left, col_right]])
    
    # Mask zeros to get a white color of the background
    H_masked = np.ma.masked_where(H == 0, H)
    H1_masked = np.ma.masked_where(H1 == 0, H1)
    H2_masked = np.ma.masked_where(H2 == 0, H2)
    H__masked = np.ma.masked_where(H_ ==0, H_)
    H_1_masked = np.ma.masked_where(H_1 == 0, H_1)
    H_2_masked = np.ma.masked_where(H_2 == 0, H_2)
    # Limits for the same colorbars
    vmin = 0
    vmax = np.max(H)
    # =============================================================================
    # Plot
    # =============================================================================
    
    fig, axes = plt.subplots(2,3)
    fig.subplots_adjust(hspace=0.6, wspace=0.6)
    plt.rcParams.update({'font.size': 16})
    
    fig1 = axes[0,0].imshow(H_masked, interpolation='none', origin='low', vmin=vmin,vmax=vmax)
    fig.colorbar(fig1, ax=axes[0,0], label="Hits", fraction=0.046, pad=0.04)
    axes[0,0].set_title("Shot %s: Hitmap" % shot)
    axes[0,0].set_xlabel("Pixels, x axis")
    axes[0,0].set_ylabel("Pixels, y axis")
    
    fig2 = axes[0,1].imshow(H1_masked, interpolation='none', origin='low', vmin=vmin,vmax=vmax)
    fig.colorbar(fig2, ax=axes[0,1], label="Hits", fraction=0.046, pad=0.04)
    axes[0,1].set_title("Hitmap, cluster=1")
    axes[0,1].set_xlabel("Pixels, x axis")
    axes[0,1].set_ylabel("Pixels, y axis")
    
    fig3 = axes[0,2].imshow(H2_masked, interpolation='none', origin='low', vmin=vmin,vmax=vmax)
    fig.colorbar(fig3, ax=axes[0,2], label="Hits", fraction=0.046, pad=0.04)
    axes[0,2].set_title("Hitmap, cluster>1")
    axes[0,2].set_xlabel("Pixels, x axis")
    axes[0,2].set_ylabel("Pixels, y axis")
    
    fig4 = axes[1,0].imshow(H__masked, interpolation='none', origin='low', vmin=vmin,vmax=vmax)
    fig.colorbar(fig4, ax=axes[1,0], label="Hits", fraction=0.046, pad=0.04)
    axes[1,0].set_title("Hitmap")
    axes[1,0].set_xlabel("Pixels, x axis")
    axes[1,0].set_ylabel("Pixels, y axis")
    
    fig5 = axes[1,1].imshow(H_1_masked, interpolation='none', origin='low', vmin=vmin,vmax=vmax)
    fig.colorbar(fig5, ax=axes[1,1], label="Hits", fraction=0.046, pad=0.04)
    axes[1,1].set_title("Hitmap, cluster=1")
    axes[1,1].set_xlabel("Pixels, x axis")
    axes[1,1].set_ylabel("Pixels, y axis")
    
    fig6 = axes[1,2].imshow(H_2_masked, interpolation='none', origin='low', vmin=vmin,vmax=vmax)
    fig.colorbar(fig6, ax=axes[1,2], label="Hits", fraction=0.046, pad=0.04)
    axes[1,2].set_title("Hitmap, cluster>1")
    axes[1,2].set_xlabel("Pixels, x axis")
    axes[1,2].set_ylabel("Pixels, y axis")
    
    # Go to the Figures folder
    try:
        os.chdir("%s/Figures" % path)
    except:
        print("No folder, creating one")
        os.mkdir("%s/Figures" % path)
        os.chdir("%s/Figures" % path)
    
    fig.set_size_inches(20., 12., forward=True)
    plt.savefig('%s:Hitmap_double.pdf' % shot)
    plt.close(fig)
