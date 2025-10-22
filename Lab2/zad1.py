import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data

#ZAD 1
#oiriginal
fig, ax = fig, ax = plt.subplots(2,2, figsize=(7,7))
chelsea = data.cat()
print(chelsea.shape)
ax[0][0].imshow(chelsea)
#scaled
chelsea = chelsea.mean(axis = 2)
chelsea = chelsea[::8,::8]
print(chelsea.shape)
ax[0][1].imshow(chelsea,cmap = 'binary_r')
#scaled + rotated
angle = np.deg2rad(-15)
cos_a, sin_a = np.cos(angle), np.sin(angle)
R = np.array([[cos_a, -sin_a, 0],
             [sin_a, cos_a, 0],
             [0, 0, 1]])
chelseaR = img.transform.warp(chelsea,R,clip=False)
ax[1][0].imshow(chelseaR,cmap = 'binary_r')
#scaled + 3d rotated
shearX = -0.5
shearY = 0
cos_a, sin_a = np.cos(angle), np.sin(angle)
R = np.array([[1, shearX, 0],
             [shearY, 1, 0],
             [0, 0, 1]])
chelseaR = img.transform.warp(chelsea,R,clip=False)
ax[1][1].imshow(chelseaR,cmap = 'binary_r')
#OUTPUT
fig.show()
input()