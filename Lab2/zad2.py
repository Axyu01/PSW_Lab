import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data

#ZAD 2
#oiriginal
fig, ax = fig, ax = plt.subplots(1,2, figsize=(9,6),sharex = 50,sharey = 50)
chelsea = data.cat()
print(chelsea.shape)
#ax[0].imshow(chelsea)
#scaled
chelsea = chelsea.mean(axis = 2)
chelsea = chelsea[::8,::8]
print(chelsea.shape)

#manual
SIZE_X = chelsea.shape[0]
SIZE_Y = chelsea.shape[1]
SIZE = SIZE_X * SIZE_Y
coords = np.zeros((SIZE,3))
colors = np.zeros((SIZE))
for x in range(0,SIZE_X):
    for y in range(0,SIZE_Y): 
        element = x *SIZE_Y + y
        coords[element,0] = x
        coords[element,1] = y
        coords[element,2] = 1
        colors[element] = 1-chelsea[x,y]

ax[0].scatter(coords[:,0],coords[:,1],c = colors,cmap = 'binary')

angle = np.deg2rad(15)
cos_a, sin_a = np.cos(angle), np.sin(angle)
R = np.array([[cos_a, -sin_a, 0],
             [sin_a, cos_a, 0],
             [0, 0, 1]])
newCoords = coords @ R
ax[1].scatter(newCoords[:,0],newCoords[:,1],c = colors,cmap = 'binary')
#OUTPUT
fig.show()
input()