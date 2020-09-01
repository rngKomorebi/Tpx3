import os
os.chdir('/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/Codes/Functional')
text_file = open("shots.txt", "w")
for i in range(19976,19992):
    n = text_file.write('%i\n' % i)
text_file.close()