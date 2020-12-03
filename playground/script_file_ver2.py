import os
from datetime import datetime, time, timedelta, date
import time
import sys
import numpy as np

shot_number = 1000

while True:
    starttime = time.time()
    while True:

        os.chdir("/home/sjing/Documents/daisuki/COMPASS")
        file1 = open("run.sh")
        string_list = file1.read()
        print(string_list)
        
        file2 = open("shot.txt")
        shot = int(np.genfromtxt('shot.txt'))
        print(shot)
        
        if shot_number != shot:
            shot_number = shot
            file = open("run.sh", "w")
            file.write("./Tpx3daq -i 100 -m -p -1 -t 10 -s shot_%i" % shot_number)
        else:
            pass
        
        file = open("run.sh")
        string_list1 = file.readlines()
        
        file.close()
        
        print(string_list1)        

        time.sleep(6.0 - ((time.time() - starttime) % 6.0))


