# =============================================================================
# A module with directions to the folder @shot
# =============================================================================
import os

def path_to_shot(shot):
    shot = int(shot)
    if 19933 <= shot <= 19950:
        try:
            os.chdir("/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/19933-19950: 27.01.20/%s" % shot)
            path = "/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/19933-19950: 27.01.20/%s" % shot
        except:
            print("No folder, no data")
    elif 19951 <= shot <= 19975:
        try:
            os.chdir("/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/19951-19975: 28.01.20/%s" % shot)
            path = "/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/19951-19975: 28.01.20/%s" % shot
        except:
            print("No folder, no data")
    elif 19976 <= shot <= 19992:
        try:
            os.chdir("/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/19976-19992: 29.01.20/%s" % shot)
            path = "/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/19976-19992: 29.01.20/%s" % shot
        except:
            print("No folder, no data")
    elif 19993 <= shot <= 20010:
        try:
            os.chdir("/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/19993-20010: 30.01.20/%s" % shot)
            path = "/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/19993-20010: 30.01.20/%s" % shot
        except:
            print("No folder, no data")
    elif 20011 <= shot <= 20023:
        try:
            os.chdir("/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/20011-20023: 31.01.20/%s" % shot)
            path = "/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/20011-20023: 31.01.20/%s" % shot
        except:
            print("No folder, no data")
    elif 20024 <= shot <= 20049:
        try:
            os.chdir("/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/20024-20049: 03.02.20/%s" % shot)
            path = "/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/20024-20049: 03.02.20/%s" % shot
        except:
            print("No folder, no data")
    else:
        try:
            os.chdir("/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/20050-20077: 4.02.20/%s" % shot)
            path = "/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/20050-20077: 4.02.20/%s" % shot
        except:
            print("No folder, no data")

    return path