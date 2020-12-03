# =============================================================================
# This script is used for generating a .txt file with number of shots which
# is later used in other scripts for automatic data analysis . Type in
# from and to which shot you require a .txt
# =============================================================================
import os
os.chdir('/home/sjing/Documents/daisuki/COMPASS/Codes/Functional')
text_file = open("shots.txt", "w")
from_ = input("Shots from: ")
to_ = input("to: ")
for i in range(int(from_),int(to_)+1):
    n = text_file.write('%i\n' % i)
text_file.close()
name='{}-{}'.format(from_, to_)
os.rename(r'shots.txt', r'shots:%s.txt' %name)