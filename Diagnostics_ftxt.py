import os # for folder manipulations
import os.path
import numpy as np
import matplotlib.pyplot as plt
# Plot figures in external window:
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')

shot = input("Cislo vyboje:")

try:
    os.chdir(shot)
except:
    print("No folder, no data")

# =============================================================================
# Diagnostiky z tokamaku
## ============================================================================

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
else: print("Data_current is failed")
# HXR
if Data_HXR_all is not None:
    HXR_time = np.array([row[0] for row in Data_HXR_all]) 
    HXR_data = np.array([row[1] for row in Data_HXR_all])
else: print("Data_HXR is failed")
# SXR
if Data_SXR_all is not None:
    SXR_time = np.array([row[0] for row in Data_SXR_all]) 
    SXR_data = np.array([row[1] for row in Data_SXR_all])
else: print("Data_SXR is failed")
# Neutrony - HXR
if neutron_data_all is not None:
    neutron_time = np.array([row[0] for row in neutron_data_all]) 
    neutron_data = np.array([row[1] for row in neutron_data_all])
else: print("neutron_data is failed")
# gas puff
if gas_data_all is not None:
    gas_time = np.array([row[0] for row in gas_data_all]) 
    gas_data = np.array([row[1] for row in gas_data_all])
else: print("gas_data is failed")

# =============================================================================
# Find where current is positive
# =============================================================================
try:
    limits = np.where(np.diff(np.sign(current_data)) != 0 )[0] +1
except:
    pass
# =============================================================================
# Plot
# =============================================================================

# fig = plt.figure()
left,right = None, None

try:
    left = current_time[limits[0]]-10
    right = current_time[limits[-1]]+10
except:
    pass

if left is None:
    left = 920
    right = 1500

plt.subplots(4, 1, sharex='all')

if Data_current_all is not None:
    ax1 = plt.subplot(221)
    ax1.set_xlim(left,right)
    ax1.plot(current_time, current_data/1e3, color='red', label="current")
    ax2 = ax1.twinx()
    ax2.axes.get_yaxis().set_ticks([])
    ax2.plot(gas_time, gas_data, color='orange', label="gaspuff")
else: 
    ax1 = plt.subplot(221)
    ax1.set_xlim(left,right)
    ax1.plot(color='red', label="current")
    
if Data_SXR_all is not None:
    ax3 = plt.subplot(222)
    ax3.set_xlim(left,right)
    ax3.plot(SXR_time, SXR_data*-1, color='blue', label="SXR")
    ax3.axes.get_yaxis().set_ticks([])
    ax4 = ax3.twinx()
    ax4.axes.get_yaxis().set_ticks([])
    ax4.plot(gas_time, gas_data, color='orange', label="gaspuff")
else:
    ax3 = plt.subplot(222)
    ax3.set_xlim(left,right)
    ax3.plot(color='blue', label="SXR")

if Data_HXR_all is not None:
    ax5 = plt.subplot(223)
    ax5.set_xlim(left,right)
    ax5.plot(HXR_time, HXR_data*-1, color='green', label="HXR")
    ax6 = ax5.twinx()
    ax6.axes.get_yaxis().set_ticks([])
    ax6.plot(gas_time, gas_data, color='orange', label="gaspuff")
else:
    ax5 = plt.subplot(223)
    ax5.set_xlim(left,right)
    ax5.plot(color='green', label="HXR")

if neutron_data_all is not None:
    ax7 = plt.subplot(224)
    ax7.set_xlim(left,right)
    ax7.plot(neutron_time, neutron_data*-1, color='cyan', label="neutrons")
    ax8 = ax7.twinx()
    ax8.axes.get_yaxis().set_ticks([])
    ax8.plot(gas_time, gas_data, color='orange', label="gaspuff")
else:
    ax7 = plt.subplot(224)
    ax7.set_xlim(left,right)
    ax7.plot(color='cyan', label="neutrons")
    
ax1.set_xlabel("Time, [ms]",)
ax3.set_xlabel("Time, [ms]",)
ax5.set_xlabel("Time, [ms]",)
ax7.set_xlabel("Time, [ms]",)
ax1.set_ylabel("Ip, [kA]")
ax3.set_ylabel("[a.u.]")
ax5.set_ylabel("[a.u.]")
ax7.set_ylabel("[a.u.]")

# ax1.xaxis.label.set_size(14)
# ax1.yaxis.label.set_size(14)
# ax3.yaxis.label.set_size(14)
# ax5.yaxis.label.set_size(14)
# ax7.yaxis.label.set_size(14)

plt.rcParams.update({'font.size': 16})


ax1.tick_params(axis='x', labelsize = 14)
ax1.tick_params(axis='y', labelsize = 14)
#ax1.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
ax3.tick_params(axis='x', labelsize = 14)
ax3.tick_params(axis='y', labelsize = 14)
ax5.tick_params(axis='x', labelsize = 14)
ax5.tick_params(axis='y', labelsize = 14)
ax7.tick_params(axis='x', labelsize = 14)
ax7.tick_params(axis='y', labelsize = 14)
#ax3.tick_params(axis='y', colors="orange", labelsize=14)
#ax3.tick_params(axis='y', colors="orange", labelsize=14)

ax1.legend(loc="upper right")
ax3.legend(loc="upper left")
ax5.legend(loc="upper left")
ax7.legend(loc="upper left")
plt.show()

plt.savefig('%s:HXR_SXR_X-chip.pdf' % shot)
plt.show()
