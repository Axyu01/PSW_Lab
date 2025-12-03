import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data
from scipy import ndimage

def applyNoise(image,probability):
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            for c in range(3):
                if np.random.choice([0,1],p=[probability,1 - probability]) == 0:
                    if np.random.choice([0,1],p=[0.5,0.5]) == 0:
                        image[x,y,c] = 255
                    else:
                        image[x,y,c] = 0

def undoNoise(imageOg,kernelSize):
    image = np.array(imageOg)
    S = np.ones((kernelSize,kernelSize))
    S = S/(kernelSize*kernelSize)
    for c in range(3):
        image[:,:,c] = ndimage.correlate(image[:,:,c],S)
    print(f"{np.min(image)} | {np.max(image)}")
    return image

fig, ax = plt.subplots(1, 3)
chelsea = data.cat()
smol_chelsea = chelsea[::3,::3,:]
chelsea_noise = np.array(smol_chelsea)
applyNoise(chelsea_noise,0.2)

chelsea_mean = undoNoise(chelsea_noise,9)

#show
ax[0].imshow(smol_chelsea,cmap = 'binary_r')
ax[1].imshow(chelsea_noise,cmap = 'binary_r')
ax[2].imshow(chelsea_mean,cmap = 'binary_r')
fig.show()
input()
