import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen
#Plot figures in external window:
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')   

shot = input("Cislo vyboje:")

# =============================================================================
# Diagnostiky z tokamaku
## ============================================================================

Data_current = None
Data_HXR = None
Data_SXR = None
Data_neutron = None
Data_gas = None

try:
    url_current = 'https://webcdb.tok.ipp.cas.cz/data_signals/728/%s/data?variant=&revision=1&downsample=100' % (shot)
    ourl_current = urlopen(url_current)
    Data_current = np.loadtxt(ourl_current)
except Exception:
    pass

try:
    url_HXR = 'https://webcdb.tok.ipp.cas.cz/data_signals/1266/%s/data?variant=&revision=1&downsample=100' % (shot)
    ourl_HXR = urlopen(url_HXR)
    Data_HXR = np.loadtxt(ourl_HXR)
except Exception:
    pass

try:
    url_SXR = 'https://webcdb.tok.ipp.cas.cz/data_signals/1195/%s/data?variant=&revision=1&downsample=100' % (shot)
    ourl_SXR = urlopen(url_SXR)
    Data_SXR = np.loadtxt(ourl_SXR)
except Exception:
    pass

try:
    url_neutron = 'https://webcdb.tok.ipp.cas.cz/data_signals/2122/%s/data?variant=&revision=1&downsample=100' % (shot)
    ourl_neutron = urlopen(url_neutron)
    Data_neutron = np.loadtxt(ourl_neutron)
except Exception:
    pass

try:
    url_gas = 'https://webcdb.tok.ipp.cas.cz/data_signals/4789/%s/data?variant=&revision=1' % (shot)
    ourl_gas = urlopen(url_gas)
    Data_gas = np.loadtxt(ourl_gas)
except Exception:
    pass




# =============================================================================
# 
# =============================================================================

# HXR
if Data_HXR is not None:
    time_HXR = np.array([row[0] for row in Data_HXR])
    data_HXR = np.array([row[1] for row in Data_HXR])
else: print("Data_HXR is failed")
# Neutrony - HXR
if Data_neutron is not None:
    time_neutron = np.array([row[0] for row in Data_neutron])
    data_neutron = np.array([row[1] for row in Data_neutron])
else: print("Data_neutron is failed")
# SXR
if Data_SXR is not None:
    time_SXR = np.array([row[0] for row in Data_SXR])
    data_SXR = np.array([row[1] for row in Data_SXR])
else: print("Data_SXR is failed")
# gas puff
if Data_gas is not None:
    time_gas = np.array([row[0] for row in Data_gas])
    data_gas = np.array([row[1] for row in Data_gas])
else: print("Data_gas is failed")
# Current
if Data_current is not None:
    time_current = np.array([row[0] for row in Data_current])
    data_current = np.array([row[1] for row in Data_current])
else: print("Data_current is failed")

# =============================================================================
# Graf
# =============================================================================

#fig = plt.figure()

left = 920
right = 1500

plt.subplots(4, 1, sharex='all')

if Data_current is not None:
    ax1 = plt.subplot(221)
    ax1.set_xlim(left,right)
    ax1.plot(time_current, data_current/1e3, color='red', label="current")
    ax2 = ax1.twinx()
    ax2.axes.get_yaxis().set_ticks([])
else: 
    ax1 = plt.subplot(221)
    ax1.set_xlim(left,right)
    ax1.plot(color='red', label="current")
    
if Data_SXR is not None:
    ax3 = plt.subplot(222)
    ax3.set_xlim(left,right)
    ax3.plot(time_SXR, data_SXR*-1, color='blue', label="SXR")
    ax3.axes.get_yaxis().set_ticks([])
    ax4 = ax3.twinx()
    ax4.axes.get_yaxis().set_ticks([])
else:
    ax3 = plt.subplot(222)
    ax3.set_xlim(left,right)
    ax3.plot(color='blue', label="SXR")

if Data_HXR is not None:
    ax5 = plt.subplot(223)
    ax5.set_xlim(left,right)
    ax5.plot(time_HXR, data_HXR*-1, color='green', label="HXR")
    ax6 = ax5.twinx()
    ax6.axes.get_yaxis().set_ticks([])
    ax6.plot(time_gas, data_gas, color='orange', label="gaspuff")
else: 
    ax5 = plt.subplot(223)
    ax5.set_xlim(left,right)
    ax5.plot(color='green', label="HXR")
    
if Data_neutron is not None:
    ax7 = plt.subplot(224)
    ax7.set_xlim(left,right)
    ax7.plot(time_neutron, data_neutron*-1, color='cyan', label="neutrons")
    ax8 = ax7.twinx()
    ax8.axes.get_yaxis().set_ticks([])
    ax8.plot(time_gas, data_gas, color='orange', label="gaspuff")
else:
    ax7 = plt.subplot(224)
    ax7.set_xlim(left,right)
    ax7.plot(color='cyan', label="neutrons")
    
ax1.set_xlabel("Time, [ms]",)
ax1.set_ylabel("Ip, [kA]")
ax3.set_ylabel("[a.u.]")
ax5.set_ylabel("[a.u.]")
ax7.set_ylabel("[a.u.]")

ax1.xaxis.label.set_size(14)
ax1.yaxis.label.set_size(14)
ax3.yaxis.label.set_size(14)
ax5.yaxis.label.set_size(14)
ax7.yaxis.label.set_size(14)


ax1.tick_params(axis='x', labelsize = 14)
ax1.tick_params(axis='y', labelsize = 14)
#ax1.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
ax3.tick_params(axis='y', labelsize = 14)
ax5.tick_params(axis='y', labelsize=14)
ax7.tick_params(axis='y', labelsize=14)
#ax3.tick_params(axis='y', colors="orange", labelsize=14)
#ax3.tick_params(axis='y', colors="orange", labelsize=14)

ax1.legend(loc="upper right")
ax3.legend(loc="upper right")
ax5.legend(loc="upper right")
ax7.legend(loc="upper right")
plt.show()

#fig.savefig('19950:HXR_SXR_X-chip.pdf')
plt.show()