import numpy as np
import matplotlib.pyplot as plt
#Plot figures in external window:
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt') 

Data_tpx3_col_total = np.genfromtxt('shot_19970_W0020_J07-200128-170807-1_cent-0.csv', delimiter=',')

col_total = np.array([row[0] for row in Data_tpx3_col_total])
row_total = np.array([row[1] for row in Data_tpx3_col_total])

# =============================================================================
# Col
# =============================================================================

# Prepairing empty arrays for the indecies of particular clusters
col_ones_full = np.zeros(len(col_total))
col_twos_full = np.zeros(len(col_total))
col_threes_full = np.zeros(len(col_total))
col_fours_full = np.zeros(len(col_total))
col_fives_full = np.zeros(len(col_total))

# Fill the arrays with indecies
for i in range (0, len(col_total)):
    if col_total[i] == 1:
        col_ones_full[i] = i
    elif col_total[i] == 2:
        col_twos_full[i] = i
    elif col_total[i] == 3:
        col_threes_full[i] = i
    elif col_total[i] == 4:
        col_fours_full[i] = i
    else: col_fives_full[i] = i
    i += i

# Cut off the empty part, leaving an array of indecies of clusters
col_ones = col_ones_full[col_ones_full != 0]
col_twos = col_twos_full[col_twos_full != 0]
col_threes = col_threes_full[col_threes_full != 0]
col_fours = col_fours_full[col_fours_full != 0]
col_fives = col_fives_full[col_fives_full != 0]

# Transform float to integer for further manipulation
col_ones = col_ones.astype(int)
col_twos = col_twos.astype(int)
col_threes = col_threes.astype(int)
col_fours = col_fours.astype(int)
col_fives = col_fives.astype(int)

# Prepair array for data from col_total
col_ones_tot = np.zeros(len(col_ones))
col_twos_tot = np.zeros(len(col_twos))
col_threes_tot = np.zeros(len(col_threes))
col_fours_tot = np.zeros(len(col_fours))
col_fives_tot = np.zeros(len(col_fives))

# Fill the ToT arrays with the corresponding data
for j in range (0, len(col_ones)):
    a = col_ones[j]
    col_ones_tot[j] = col_total[a]
    j += j
    
a,j = 0,0
for j in range (0, len(col_twos)):
    a = col_twos[j]
    col_twos_tot[j] = col_total[a]
    j += j

a,j = 0,0  
for j in range (0, len(col_threes)):
    a = col_threes[j]
    col_threes_tot[j] = col_total[a]
    j += j

a,j = 0,0   
for j in range (0, len(col_fours)):
    a = col_fours[j]
    col_fours_tot[j] = col_total[a]
    j += j
    
a,j = 0,0
for j in range (0, len(col_fives)):
    a = col_fives[j]
    col_fives_tot[j] = col_total[a]
    j += j
    
# =============================================================================
# Row
# =============================================================================
# Prepairing empty arrays for the indecies of particular clusters
row_ones_full = np.zeros(len(row_total))
row_twos_full = np.zeros(len(row_total))
row_threes_full = np.zeros(len(row_total))
row_fours_full = np.zeros(len(row_total))
row_fives_full = np.zeros(len(row_total))

# Fill the arrays with indecies
for i in range (0, len(row_total)):
    if row_total[i] == 1:
        row_ones_full[i] = i
    elif row_total[i] == 2:
        row_twos_full[i] = i
    elif row_total[i] == 3:
        row_threes_full[i] = i
    elif row_total[i] == 4:
        row_fours_full[i] = i
    else: row_fives_full[i] = i
    i += i

# Cut off the empty part, leaving an array of indecies of clusters
row_ones = row_ones_full[row_ones_full != 0]
row_twos = row_twos_full[row_twos_full != 0]
row_threes = row_threes_full[row_threes_full != 0]
row_fours = row_fours_full[row_fours_full != 0]
row_fives = row_fives_full[row_fives_full != 0]

# Transform float to integer for further manipulation
row_ones = row_ones.astype(int)
row_twos = row_twos.astype(int)
row_threes = row_threes.astype(int)
row_fours = row_fours.astype(int)
row_fives = row_fives.astype(int)

# Prepair array for data from row_total
row_ones_tot = np.zeros(len(row_ones))
row_twos_tot = np.zeros(len(row_twos))
row_threes_tot = np.zeros(len(row_threes))
row_fours_tot = np.zeros(len(row_fours))
row_fives_tot = np.zeros(len(row_fives))

# Fill the ToT arrays with the corresponding data
for j in range (0, len(row_ones)):
    a = row_ones[j]
    row_ones_tot[j] = row_total[a]
    j += j
    
a,j = 0,0
for j in range (0, len(row_twos)):
    a = row_twos[j]
    row_twos_tot[j] = row_total[a]
    j += j

a,j = 0,0  
for j in range (0, len(row_threes)):
    a = row_threes[j]
    row_threes_tot[j] = row_total[a]
    j += j

a,j = 0,0   
for j in range (0, len(row_fours)):
    a = row_fours[j]
    row_fours_tot[j] = row_total[a]
    j += j
    
a,j = 0,0
for j in range (0, len(row_fives)):
    a = row_fives[j]
    row_fives_tot[j] = row_total[a]
    j += j
# =============================================================================
# 
# =============================================================================
plt.figure()

plt.hist2d(row_ones_tot,col_ones_tot,250,[[0,250],[0,250]])

plt.show()