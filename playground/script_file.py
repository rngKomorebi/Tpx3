import os
from datetime import datetime, time, timedelta, date
import time
import sys

shot_number = ([1234, 1235, 1236, 1237])
i = 0

while True:
    starttime = time.time()
    while True:

        os.chdir("/home/sjing/Documents/daisuki/COMPASS")
        file = open("run.sh")
        string_list = file.readlines()
        print(string_list)
        
        file = open("run.sh", "w")
        file.write("./Tpx3daq -i 100 -m -p -1 -t 10 -s shot_%i" % shot_number[i])
        
        file = open("run.sh")
        string_list1 = file.readlines()
        
        file.close()
        i=i+1
        
        print(string_list1)        

        if i==4:
            sys.exit()
        time.sleep(6.0 - ((time.time() - starttime) % 6.0))


