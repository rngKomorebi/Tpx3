import numpy as np
import matplotlib.pyplot as plt

a = [10,11,10,5,9,10]
b = [2,2,10,4,5,2]


hist = np.histogram2d(a,b, bins=1, range=[[0,20], [0,20]])

plt.figure()

plt.hist2d(a,b,20,[[0, 20], [0, 20]])