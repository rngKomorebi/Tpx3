import numpy as np
import os
import sys
import matplotlib.pyplot as plt

os.chdir("/home/sjing/Documents/daisuki/COMPASS/Codes/pixels_window")

Trim_dacs = None

try:
    Trim_dacs = np.genfromtxt('W0020_J07_trimdacs_template.txt')
except:
    pass

if Trim_dacs is not None:
    row = np.array([row[0] for row in Trim_dacs]) 
    col = np.array([row[1] for row in Trim_dacs])
    c1 = np.array([row[2] for row in Trim_dacs]) # f_it
    c2 = np.array([row[3] for row in Trim_dacs]) # 1-masked, 0-active
    c3 = np.array([row[4] for row in Trim_dacs]) # always 0
else: print("FU")
#  # not all pixels are active in the template file - correct it
# for i in range (0,len(c2)):
#     c2[i] = 1

# define the limits of the needed window
col_min = input("left column: ")
col_max = input("right column: ")
row_min = input("bottom row: ")
row_max = input("top row: ")

# activate the pixels within the given window
cc2 = np.ones(len(c2))
ac_pixels = 0
for i in range (int(col_min),int(col_max)):
    for j in range (int(row_min), int(row_max)):
        index = np.where(np.logical_and(col==i, row==j))
        cc2[index] = 0
        ac_pixels = ac_pixels+1


# plt.scatter(row,col,cc2) # for control

# create one array for np.savetxt
new_content = np.column_stack((row,col,c1,cc2,c3))
# create new txt with the generated active window; last two arguments for integer, other way
# the txt will be full of floats
np.savetxt("W0020_J07_trimdacs%s.txt" % ac_pixels, new_content.astype(int), fmt='%i')
