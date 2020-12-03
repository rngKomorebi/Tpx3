import os
os.chdir('/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020')

for i in range (20024, 20077):
    if 20024 <= i <= 20049:
        try:
            i = str(i)
            os.chdir("/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/20024-20049: 03.02.20/%s" %i) 
        except:
            os.mkdir("/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/20024-20049: 03.02.20/%s" %i) 
    else:
        print("Loh")
        raise SystemExit