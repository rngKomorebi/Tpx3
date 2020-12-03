# =============================================================================
# Get data from the tokamak's diagnostics and plot it
# =============================================================================
import os # for folder manipulations
import os.path
import csv
import numpy as np
import matplotlib.pyplot as plt
from path_to_shot import *
# Plot figures in external window:
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')

shots = np.genfromtxt('shots:21215-21237.txt')

for i in range (0, len(shots)):
    shot = int(shots[i])
    print("Doing shot %s" %shot)
    # Go to the @shot folder
    try:
        path = path_to_shot(shot)
    except:
        continue
    # Check the .csv file size (too big will end with a kernel crash)
    if os.path.getsize("%s.csv" % shot)*1e-6 > 600:
        print("%s.csv is too big, going to the next shot" % shot)
        continue
    # =============================================================================
    # Check and read the data from the tokamak's diagnostics
    # ============================================================================
    
    Data_current_all = None
    Data_HXR_all = None
    Data_SXR_all = None
    neutron_data_all = None
    gas_data_all = None
    
    try:
        Data_current_all = np.genfromtxt('I_plasma_Rogowski_coil_RAW-%s.txt' % shot)
    except:
        pass
    try:
        Data_HXR_all = np.genfromtxt('hard_X_rays-%s.txt' % shot)
    except:
        pass
    try:
        Data_SXR_all = np.genfromtxt('SXR_A_1-%s.txt' % shot)
    except:
        pass
    try:
        neutron_data_all = np.genfromtxt('neutron_detection_scintillator-%s.txt' % shot)
    except:
        pass
    try:
        gas_data_all = np.genfromtxt('MARTE_NODE.FeedbackDataCollection.GasPuffAnalogueOutputSecondGasPuff-%s.txt' % shot)
    except:
        pass
    
    # Current
    if Data_current_all is not None:
        current_time = np.array([row[0] for row in Data_current_all]) 
        current_data = np.array([row[1] for row in Data_current_all])
    else: print("%s: Data_current is failed" %shot)
    # HXR
    if Data_HXR_all is not None:
        HXR_time = np.array([row[0] for row in Data_HXR_all]) 
        HXR_data = np.array([row[1] for row in Data_HXR_all])
    else: print("%s: Data_HXR is failed" %shot)
    # SXR
    if Data_SXR_all is not None:
        SXR_time = np.array([row[0] for row in Data_SXR_all]) 
        SXR_data = np.array([row[1] for row in Data_SXR_all])
    else: print("%s: Data_SXR is failed" %shot)
    # Neutrony - HXR
    if neutron_data_all is not None:
        neutron_time = np.array([row[0] for row in neutron_data_all]) 
        neutron_data = np.array([row[1] for row in neutron_data_all])
    else: print("%s: neutron_data is failed" %shot)
    # gas puff
    if gas_data_all is not None:
        gas_time = np.array([row[0] for row in gas_data_all]) 
        gas_data = np.array([row[1] for row in gas_data_all])
    else: print("%s: gas_data is failed" %shot)
    
    # =============================================================================
    # Find where current is positive/negative (depends on the direction of plasma
    # current)
    # =============================================================================
    try:
        limits = np.where(np.diff(np.sign(current_data)) != 0 )[0] +1
    except:
        pass
    
    # =============================================================================
    # Check, if current is negative or positive (depending on the direction)
    # =============================================================================
    current_data1 = current_data[9000:20000]
    
    current_min = min(current_data1)
    current_max = max(current_data1)
    
    if current_min > 0 and current_max > 0:
        current_data_fin = current_data
    elif current_min < 0 and current_max < 0:
        current_data_fin = current_data*-1
    elif current_max > 0 and current_min < 0:
        if current_min*-1 > current_max:
            current_data_fin = current_data*-1
        else:
            current_data_fin = current_data
    
# =============================================================================
# Get the ToA signal
# =============================================================================
    
    # Get the data
    Data_tpx3_cent = np.genfromtxt('%s.csv' % shot, delimiter=',')
    # Read the first row in the .csv file and get index of the required signal
    with open('%s.csv' % shot, newline='') as f:
        reader = csv.reader(f)
        row1 = next(reader) 
    # Get the time from triger: 912 ms from the start of the discharge
    p = None
    try:
        index = row1.index('#Trig-ToA[arb]')
        time_new = np.array([row[index] for row in Data_tpx3_cent]) * 25/4096/1e6 + 912
        p = 1
    except:
        print("No 'Trig-ToA' in the list")
        index = row1.index('#ToA')
        time_new = np.array([row[index] for row in Data_tpx3_cent]) * 25/4096/1e6
    
    # Define the bins with the step of 1.5625
    bins1 = int((time_new[-1] - time_new[0]) / 1.5625 *4)
    
    
    # # =============================================================================
# Plot
# =============================================================================

    fig = plt.figure()
    fig.subplots_adjust(top=0.9, bottom=0.1, hspace = 0.4, wspace=0)
    # fig.subplots_adjust(hspace=0, wspace=0)
    left,right = None, None
    
    try:
        left = current_time[limits[0]]-10
        right = current_time[limits[-1]]+10
    except:
        pass
    
    if left is None or left<900:
        left = 920
        right = 1500
    
    # Check if data is not None. If not, then plot it. If there is no data,
    # plot an empty graph.
    
    if Data_current_all is not None:
        ax1 = fig.add_subplot(511)
        ax1.set_xlim(left,right)
        ax1.plot(current_time, current_data_fin/1e3, color='red', label="current")
        ax2 = ax1.twinx()
        ax2.axes.get_yaxis().set_ticks([])
        ax2.plot(gas_time, gas_data, color='orange', label="gaspuff")
    else: 
        ax1 = fig.add_subplot(511)
        ax1.set_xlim(left,right)
        ax1.plot(color='red', label="current")
        
    if Data_SXR_all is not None:
        ax3 = fig.add_subplot(512)
        ax3.set_xlim(left,right)
        ax3.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        ax3.plot(SXR_time, SXR_data*-1, color='blue', label="SXR")
        # ax3.axes.get_yaxis().set_ticks([])
        ax4 = ax3.twinx()
        ax4.axes.get_yaxis().set_ticks([])
        ax4.plot(gas_time, gas_data, color='orange', label="gaspuff")
    else:
        ax3 = fig.add_subplot(512)
        ax3.set_xlim(left,right)
        ax3.plot(color='blue', label="SXR")
    
    if Data_HXR_all is not None:
        ax5 = fig.add_subplot(513)
        ax5.set_xlim(left,right)
        ax5.plot(HXR_time, HXR_data*-1, color='green', label="HXR")
        ax6 = ax5.twinx()
        ax6.axes.get_yaxis().set_ticks([])
        ax6.plot(gas_time, gas_data, color='orange', label="gaspuff")
    else:
        ax5 = fig.add_subplot(513)
        ax5.set_xlim(left,right)
        ax5.plot(color='green', label="HXR")
    
    if neutron_data_all is not None:
        ax7 = fig.add_subplot(514)
        ax7.set_xlim(left,right)
        ax7.plot(neutron_time, neutron_data*-1, color='cyan', label="neutrons")
        ax8 = ax7.twinx()
        ax8.axes.get_yaxis().set_ticks([])
        ax8.plot(gas_time, gas_data, color='orange', label="gaspuff")
    else:
        ax7 = fig.add_subplot(514)
        ax7.set_xlim(left,right)
        ax7.plot(color='cyan', label="neutrons")
        
    # Prepare figure and compute the histogram
    ax9 = fig.add_subplot(515)
    if p == 1:
        ax9.set_xlim(left,right)
        ax9.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    else:
        # Define limits of x axis for an appropriate plot
        try:
            left_, right_ = int(timee[np.nonzero(data)[0][0]]-10), int(timee[np.nonzero(data)[0][-1]]+10)
            plt.xlim(left_, right_)
        except:
                print("Probably no data at all or just a weak signal")
                pass
    
    a = plt.hist(time_new, bins1, (time_new[0], time_new[-1]), histtype='step', fill=False, label="Timepix3:ToA")
    # plt.xlabel("Time, [ms]")
    # plt.ylabel("Hits, [a.u.]")
    # Get rid off the noisy "ones" for an appropriate plot
    data = a[0]
    timee = a[1]
    
    ones = np.where(data < 10)[0]
    
    for i in range (0, len(ones)):
        data[ones[i]] = 0
    
    
    
    ax1.set_xlabel("Time [ms]",)
    ax3.set_xlabel("Time [ms]",)
    ax5.set_xlabel("Time [ms]",)
    ax7.set_xlabel("Time [ms]",)
    ax9.set_xlabel("Time [ms]")
    ax1.set_ylabel("Ip [kA]")
    ax3.set_ylabel("[a.u.]")
    ax5.set_ylabel("[a.u.]")
    ax7.set_ylabel("[a.u.]")
    ax9.set_ylabel("Hits [a.u.]")
    
    plt.rcParams.update({'font.size': 22})
    
    # ax1.tick_params(axis='x', labelsize = 16)
    # ax1.tick_params(axis='y', labelsize = 16)
    # ax3.tick_params(axis='x', labelsize = 16)
    # ax3.tick_params(axis='y', labelsize = 16)
    # ax5.tick_params(axis='x', labelsize = 16)
    # ax5.tick_params(axis='y', labelsize = 16)
    # ax7.tick_params(axis='x', labelsize = 16)
    # ax7.tick_params(axis='y', labelsize = 16)
    # ax9.tick_params(axis='x', labelsize = 16)
    # ax9.tick_params(axis='y', labelsize = 16)
    
    ax1.legend(loc="upper right")
    ax3.legend(loc="upper left")
    ax5.legend(loc="upper left")
    ax7.legend(loc="upper left")
    ax9.legend(loc="upper left")
    
    # Go to the Figures folder
    try:
        os.chdir("%s/Figures" % path)
    except:
        print("No folder, creating one")
        os.mkdir("%s/Figures" % path)
        os.chdir("%s/Figures" % path)
    
    fig.set_size_inches(18., 20., forward=True)
    plt.savefig('%s:Diag_ToA.pdf' % shot)
    plt.show()
    plt.close(fig)
