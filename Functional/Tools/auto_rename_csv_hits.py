# =============================================================================
# A script for autorename of the .csv files without centroids (clusters)
# which can be later used for getting the number of hits in particular shots
# May need to change the name of the file in line 18
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
        continue
    for file in glob.glob("*1-0.csv"):
        print(file)
        os.rename(r'%s' %file, r'%s_hits.csv' %shot)
