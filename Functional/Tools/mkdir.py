# =============================================================================
# A script for automatic generation of multiple folders. Checks if the folder
# exists, creates one if negative.
# =============================================================================
import os
os.chdir('/home/sjing/Documents/daisuki/COMPASS/12th_RE_18.11.2020')

for i in range (21215, 21237):
    if 21215 <= i <= 21237:
        try:
            i = str(i)
            os.chdir("/home/sjing/Documents/daisuki/COMPASS/12th_RE_18.11.2020/21215-21237: 02.12.20/%s" %i) 
        except:
            os.mkdir("/home/sjing/Documents/daisuki/COMPASS/12th_RE_18.11.2020/21215-21237: 02.12.20/%s" %i) 
    else:
        print("Loh")
        raise SystemExit