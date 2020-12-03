# =============================================================================
# Import modules and execute them at once
# =============================================================================
from modules.ToA_func import *
from modules.hitmap_double_func import *
from modules.ToA_cluster_func import *
from modules.ToT_cluster_func import *
from modules.ToT_vs_ToA_func import *
import numpy as np

shots = np.genfromtxt('shots:21215-21237.txt')
# from_ = input("Execute for shots from:")
# to_ = input("to:")

for i in range (0, len(shots)):
    shot = int(shots[i])
    print("Doing shot %s" %shot)
# for i in range (int(from_), int(to_)+1):
#     shot = i
    try:
        ToA(shot)
    except:
        pass
    try:
        ToA_cluster(shot)
    except:
        pass
    try:
        ToT_vs_ToA(shot)
    except:
        pass
    try:
        hitmap_double(shot)
    except:
        pass
    try:
        ToT_cluster(shot)
    except:
        pass
