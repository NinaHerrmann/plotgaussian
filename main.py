

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np


muesli = np.genfromtxt('/home/schredder/PycharmProjects/pythonProject1/muesli.csv', delimiter=';')
mueslitw_4 = muesli[np.where(muesli[:,0] == 16)]


fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

top = x + y
bottom = np.zeros_like(top)
width = depth = 1

newbottom = np.zeros_like(mueslitw_4[:,3])
ax1.bar3d(mueslitw_4[:,2], mueslitw_4[:,1], newbottom, width, 2, mueslitw_4[:,3], shade=True)
ax1.set_title('Shaded')
plt.savefig("barchart.svg", format="svg")

plt.show()