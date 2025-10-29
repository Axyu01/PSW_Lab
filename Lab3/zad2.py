import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data

def applyLUT(img,LUT):
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            v = int(img[x,y])
            img[x,y] = LUT[v]
D = 8
L = 2**D
fig, ax = plt.subplots(2, 3)
moon = data.moon()

#OUTPUT
ax[0,0].imshow(moon,cmap = 'binary_r')
#histogram
values, counts = np.unique(moon, return_counts=True)
probs = counts / counts.sum()
ax[0,1].bar(values,probs,color = 'black')
#dystrybuanta
probsCum = np.cumsum(probs)
ax[0,2].scatter(values,probsCum,s = 1,color = 'black')

LUT = (np.zeros(L))
x = np.arange(0,L)
vIterator = 0
for i in range(values[0]):
    LUT[i] = 0

for i in range(values[0],L):
    while(i>values[vIterator]):
        vIterator+=1
    LUT[i] = probsCum[vIterator]*L

    #LUT[values[i]] = probsCum[i]
ax[1,0].scatter(x,LUT,s = 1,color = 'black')


moonAfterLUT = np.array(moon)
applyLUT(moonAfterLUT,LUT)
ax[1,1].imshow(moonAfterLUT,cmap = 'binary_r')

#histogram po LUT
values, counts = np.unique(moonAfterLUT, return_counts=True)
print(values)
probs = counts / counts.sum()
ax[1,2].bar(values,probs,color = 'black',width = 1)
ax[1, 2].set_xlim(0, 255)

fig.show()
input()