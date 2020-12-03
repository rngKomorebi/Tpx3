# =============================================================================
# Get the hits by col and row coordinates and plot it as histogram.
# Defined as function for the "All_in_One.py" script.
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import os

def hitmap(shot):
    # Go to the @shot folder
    try:
        os.chdir("/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/%s" % shot)
    except:
        print("No folder, no data")
    
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
    
    # Mask the zeroes to get a white color of the background
    H_masked = np.ma.masked_where(H == 0, H)
    H1_masked = np.ma.masked_where(H1 == 0, H1)
    H2_masked = np.ma.masked_where(H2 == 0, H2)
    # Limits for the same colorbars
    vmin = 0
    vmax = np.max(H)
    # =============================================================================
    # Plot
    # =============================================================================
    
    fig, (ax1,ax2,ax3) = plt.subplots(1,3)
    fig.subplots_adjust(wspace=0.6)
    plt.rcParams.update({'font.size': 16})
    
    fig1 = ax1.imshow(H_masked, interpolation='none', origin='low', vmin=vmin,vmax=vmax)
    fig.colorbar(fig1, ax=ax1, label="Hits", fraction=0.046, pad=0.04)
    ax1.set_title("Shot %s: Hitmap" % shot)
    ax1.set_xlabel("Pixels, x axis")
    ax1.set_ylabel("Pixels, y axis")
    
    fig2 = ax2.imshow(H1_masked, interpolation='none', origin='low', vmin=vmin,vmax=vmax)
    fig.colorbar(fig2, ax=ax2, label="Hits", fraction=0.046, pad=0.04)
    ax2.set_title("Hitmap, cluster=1")
    ax2.set_xlabel("Pixels, x axis")
    ax2.set_ylabel("Pixels, y axis")
    
    fig3 = ax3.imshow(H2_masked, interpolation='none', origin='low', vmin=vmin,vmax=vmax)
    fig.colorbar(fig3, ax=ax3, label="Hits", fraction=0.046, pad=0.04)
    ax3.set_title("Hitmap, cluster>1")
    ax3.set_xlabel("Pixels, x axis")
    ax3.set_ylabel("Pixels, y axis")
    
    # Go to the Figures folder
    try:
        os.chdir("/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/%s/Figures" % shot)
    except:
        print("No folder, creating one")
        os.mkdir("/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/%s/Figures" % shot)
        os.chdir("/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/%s/Figures" % shot)
    
    fig.set_size_inches(20., 12., forward=True)
    plt.savefig('%s:Hitmap_masked.pdf' % shot)
    plt.close(fig)
