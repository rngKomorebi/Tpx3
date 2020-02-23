# =============================================================================
# Import modules and execute them at once
# =============================================================================
from ToA_func import *
from ToA_cluster_func import *
from ToT_vs_ToA_func import *
from hitmap_func import *
from ToT_cluster_func import *

shot = input("Shot number:")

ToA(shot)
ToA_cluster(shot)
ToT_vs_ToA(shot)
hitmap(shot)
ToT_cluster(shot)