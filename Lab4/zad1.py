import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data
from scipy import ndimage

fig, ax = plt.subplots(1, 2)
chelsea = data.cat()

S1 = [[-1,0,1,],
      [-2,0,2,],
      [-1,0,1,]]
S1_EX = [[[-1,0,1,],
      [-2,0,2,],
      [-1,0,1,]],
[[-1,0,1,],
      [-2,0,2,],
      [-1,0,1,]],[[-1,0,1,],
      [-2,0,2,],
      [-1,0,1,]]]
chelsea_grey = np.sum(chelsea,axis = 2)/3



#corelation = ndimage.correlate(chelsea,S1_EX)
#convolution = ndimage.convolve(chelsea,S1_EX)
corelation = ndimage.correlate(chelsea_grey,S1)
convolution = ndimage.convolve(chelsea_grey,S1)
#show
ax[0].imshow(corelation,cmap = 'binary_r')
ax[1].imshow(convolution,cmap = 'binary_r')
fig.show()
input()
