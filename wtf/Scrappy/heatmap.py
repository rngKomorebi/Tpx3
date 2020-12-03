import numpy as np
import matplotlib.pyplot as plt

# here are the three lists
# for example, you could do random values to demo
x = np.random.randn(8873)
y = np.random.randn(8873)
weights = np.random.rand(8873)

heatmap, _, _ = np.histogram2d(x, y, weights=weights)

plt.clf()
plt.imshow(heatmap)
plt.show()