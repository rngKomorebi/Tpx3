import numpy as np
import matplotlib.pyplot as plt
# Plot figures in external window:
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt') 

Data_tpx3 = np.genfromtxt('shot_19970_W0020_J07-200128-170807-1-0.csv', delimiter=',')
Data_tpx3_cent = np.genfromtxt('shot_19970_W0020_J07-200128-170807-1_cent-0.csv', delimiter=',')

time_tpx3 = np.array([row[2] for row in Data_tpx3])
time_new = time_tpx3 * 25/4096/1e6
data_tpx3 = np.array([row[3] for row in Data_tpx3])
tot_total = np.array([row[4] for row in Data_tpx3_cent])

col = np.array([row[0] for row in Data_tpx3])
row = np.array([row[1] for row in Data_tpx3])

# =============================================================================
# Plot
# =============================================================================

fig1 = plt.figure(1)

#plt.plot(time_new, data_tpx3)
#plt.plot(time_new)
plt.xlabel("t, [ms]")
plt.ylabel(",[-]")

plt.hist(data_tpx3, 300, (0, 7500), histtype='step')
ToT = np.histogram(data_tpx3, 300, (0, 7500))

fig2 = plt.figure(2)

plt.hist(time_new, 128, (14400, 14600), histtype='step')

fig3 = plt.figure(3)

plt.hist(tot_total, 1000, (0, 25000), histtype='step')

fig4 = plt.figure(4)
plt.plot(time_new, data_tpx3)

