# =============================================================================
# A script for automatic renaming of the *cent.csv files (with clusters) 
# which are later used in data analysis
# =============================================================================
import os
import glob
import numpy as np
os.chdir('/home/sjing/Documents/daisuki/COMPASS/Codes/Functional')
shots = np.genfromtxt('shots:21215-21237.txt')

for i in range (0, len(shots)):
    shot = int(shots[i])
    try:
        os.chdir("/home/sjing/Documents/daisuki/COMPASS/12th_RE_18.11.2020/21215-21237: 02.12.20/%s"%shot)
    except:
        pass
    for file in glob.glob("*1_cent-0.csv"):
        print(file)
        os.rename(r'%s' %file, r'%s.csv' %shot)
