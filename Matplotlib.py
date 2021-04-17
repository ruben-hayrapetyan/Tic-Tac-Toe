import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 1, 2, 3, 4])
ypoints = np.array([0, 123, 4132, 1343, 423, 766, 2534])

plt.plot(ypoints, '*-.b', ms=12.11, mfc = 'lightblue', mec = 'r')
plt.show()

