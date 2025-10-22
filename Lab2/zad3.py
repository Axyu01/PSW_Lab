import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data

#ZAD 3
#oiriginal
fig, ax = fig, ax = plt.subplots(1,3, figsize=(9,6),sharex = 50,sharey = 50)
chelsea = data.cat()
print(chelsea.shape)
#ax[0].imshow(chelsea)
#scaled
chelsea = chelsea.mean(axis = 2)
chelsea = chelsea[::8,::8]
print(chelsea.shape)

#scatter original
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

#scatter random
RAND_COUNT = 1000
randCoordsIndicies = np.random.choice(SIZE,RAND_COUNT)
randCoords = np.zeros((RAND_COUNT,2))
randColors = np.zeros((RAND_COUNT))
for i in range(0,RAND_COUNT):
    tIndex = randCoordsIndicies[i] #translated Index
    randCoords[i][0] = coords[tIndex][0]
    randCoords[i][1] = coords[tIndex][1]
    randColors[i] = colors[tIndex]

ax[1].scatter(randCoords[:,0],randCoords[:,1],c = randColors,cmap = 'binary')

#scatter interpolate
INTER_X = 400# * 3
INTER_Y = 300# * 3
INTER_SIZE = INTER_X*INTER_Y
interCoords = np.zeros((INTER_SIZE,2))
interColors = np.zeros((INTER_SIZE))
print(INTER_SIZE)

#RAND_COUNT = 4
for i in range(0,INTER_SIZE):
    iy = int(i / INTER_X)*SIZE_Y/INTER_Y
    ix = (i % INTER_X)*SIZE_X/INTER_X
    best_distance = float('inf')
    best_coord = 0
    for j in range(0,RAND_COUNT):
        x = randCoords[j][0]
        y = randCoords[j][1]
        distance = ((x-ix)**2 + (y-iy)**2)**(0.5)
        if(best_distance > distance):
            best_distance = distance
            best_coord = j
    interCoords[i][0] = ix
    interCoords[i][1] = iy
    #print(interCoords[i])
    interColors[i] = randColors[best_coord]
    #print(best_coord)
        
ax[2].scatter(interCoords[:,0],interCoords[:,1],c = interColors,cmap = 'binary')
#OUTPUT
fig.show()
input()