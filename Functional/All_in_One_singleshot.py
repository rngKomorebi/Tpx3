# =============================================================================
# Import modules and execute them at once for a single shot
# =============================================================================
from modules.ToA_func import *
from modules.hitmap_double_func import *
from modules.ToA_cluster_func import *
from modules.ToT_cluster_func import *
from modules.ToT_vs_ToA_func import *

shot = input("Shot number:")

ToA(shot)
ToA_cluster(shot)
ToT_vs_ToA(shot)
hitmap_double(shot)
ToT_cluster(shot)