from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np

lowlevel = np.genfromtxt('/home/schredder/PycharmProjects/pythonProject1/LL_Gaussian1000.csv', delimiter=';')
muesli = np.genfromtxt('/home/schredder/PycharmProjects/pythonProject1/Gaussian_HL.csv', delimiter=';')

lowlevel_8 = lowlevel[np.where(lowlevel[:, 3] == 8)]
lowlevel_16 = lowlevel[np.where(lowlevel[:, 3] == 16)]
lowlevel_32 = lowlevel[np.where(lowlevel[:, 3] == 32)]
lowlevel_12 = lowlevel[np.where(lowlevel[:, 3] == 12)]

highlevel_8 = muesli[np.where(muesli[:, 0] == 8)]
highlevel_16 = muesli[np.where(muesli[:, 0] == 16)]
highlevel_32 = muesli[np.where(muesli[:, 0] == 32)]
highlevel_12 = muesli[np.where(muesli[:, 0] == 12)]

lowlevel_8_8 = lowlevel_8[np.where(lowlevel_8[:, 4] == 8)]
lowlevel_16_8 = lowlevel_16[np.where(lowlevel_16[:, 4] == 8)]
lowlevel_12 = lowlevel_12[np.where(lowlevel_12[:, 4] == 1)]

highlevel_8_8 = highlevel_8[np.where(highlevel_8[:, 2] == 8)]
highlevel_16_8 = highlevel_16[np.where(highlevel_16[:, 2] == 8)]
highlevel_12 = highlevel_12[np.where(highlevel_12[:, 2] == 1)]
print(lowlevel_8_8[:, 0])
print(highlevel_8_8[:, 3])
plt.set_cmap("gist_rainbow")
plt.plot(lowlevel_16_8[:, 5], lowlevel_16_8[:, 0], label="16 Tile Width", linestyle='-', marker='o')
plt.plot(lowlevel_8_8[:, 5], lowlevel_8_8[:, 0], label="32 Tile Width", linestyle='-', marker='o')
plt.plot(lowlevel_12[:, 5], lowlevel_12[:, 0], label="GM", linestyle='-', marker='o')
plt.plot(highlevel_16_8[:, 1], highlevel_16_8[:, 3], label="16 Tile Width", linestyle=':', marker='o', color="blue")
plt.plot(highlevel_8_8[:, 1], highlevel_8_8[:, 3], label="32 Tile Width", linestyle=':', marker='o', color="blue")
plt.plot(highlevel_12[:, 1], highlevel_12[:, 3], label="GM", linestyle=':', marker='o', color="blue")
plt.savefig("linechart.svg", format="svg")

plt.show()
