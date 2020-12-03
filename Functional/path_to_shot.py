# =============================================================================
# A module with directions to the folder @shot
# =============================================================================
import os

def path_to_shot(shot):
    shot = int(shot)
    if 21077 <= shot <= 21085:
        try:
            os.chdir("/home/sjing/Documents/daisuki/COMPASS/12th_RE_18.11.2020/21077-21085: 18.11.20/%s" % shot)
            path = "/home/sjing/Documents/daisuki/COMPASS/12th_RE_18.11.2020/21077-21085: 18.11.20/%s" % shot
        except:
            print("No folder, no data")
    elif 21086 <= shot <= 21109:
        try:
            os.chdir("/home/sjing/Documents/daisuki/COMPASS/12th_RE_18.11.2020/21086-21109: 19.11.20/%s" % shot)
            path = "/home/sjing/Documents/daisuki/COMPASS/12th_RE_18.11.2020/21086-21109: 19.11.20/%s" % shot
        except:
            print("No folder, no data")
    elif 21110 <= shot <= 21125:
        try:
            os.chdir("/home/sjing/Documents/daisuki/COMPASS/12th_RE_18.11.2020/21110-21125: 20.11.20/%s" % shot)
            path = "/home/sjing/Documents/daisuki/COMPASS/12th_RE_18.11.2020/21110-21125: 20.11.20/%s" % shot
        except:
            print("No folder, no data")
    elif 21126 <= shot <= 21147:
        try:
            os.chdir("/home/sjing/Documents/daisuki/COMPASS/12th_RE_18.11.2020/21126-21147: 23.11.20/%s" % shot)
            path = "/home/sjing/Documents/daisuki/COMPASS/12th_RE_18.11.2020/21126-21147: 23.11.20/%s" % shot
        except:
            print("No folder, no data")
    elif 21148 <= shot <= 21169:
        try:
            os.chdir("/home/sjing/Documents/daisuki/COMPASS/12th_RE_18.11.2020/21148-21169: 24.11.20/%s" % shot)
            path = "/home/sjing/Documents/daisuki/COMPASS/12th_RE_18.11.2020/21148-21169: 24.11.20/%s" % shot
        except:
            print("No folder, no data")
    elif 21170 <= shot <= 21192:
        try:
            os.chdir("/home/sjing/Documents/daisuki/COMPASS/12th_RE_18.11.2020/21170-21192: 25.11.20/%s" % shot)
            path = "/home/sjing/Documents/daisuki/COMPASS/12th_RE_18.11.2020/21170-21192: 25.11.20/%s" % shot
        except:
            print("No folder, no data")
    elif 21193 <= shot <= 21214:
        try:
            os.chdir("/home/sjing/Documents/daisuki/COMPASS/12th_RE_18.11.2020/21193-21214: 01.12.20/%s" % shot)
            path = "/home/sjing/Documents/daisuki/COMPASS/12th_RE_18.11.2020/21193-21214: 01.12.20/%s" % shot
        except:
            print("No folder, no data")
    elif 21215 <= shot <= 21237:
        try:
            os.chdir("/home/sjing/Documents/daisuki/COMPASS/12th_RE_18.11.2020/21215-21237: 02.12.20/%s" % shot)
            path = "/home/sjing/Documents/daisuki/COMPASS/12th_RE_18.11.2020/21215-21237: 02.12.20/%s" % shot
        except:
            print("No folder, no data")

    return path