import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data
from scipy import ndimage

fig, ax = plt.subplots(1, 3)
mono = data.cat()
mono = np.mean(mono,axis = 2)
mono_shape = mono.shape
print(mono_shape)
#mono = mono[:mono_shape[0]-1,:mono_shape[1]]#obydwa musza byc nieparzyste
mono_shape = mono.shape


#GAUSIAN
mono_gausian = ndimage.gaussian_filter(input = mono,sigma= 1)

#EDGE DETECTION L
L = [[1,1,1,],
      [1,-8,1,],
      [1,1,1,]]
L = np.array(L)
mono_edge = ndimage.correlate(mono_gausian,L)
mono_edge[mono_edge<0] = 0
#EDGE DETECTION M
PX = [[-1,0,1,],
      [-1,0,1,],
      [-1,0,1,]]
PY = [[-1,-1,-1,],
      [ 0,0,0,],
      [-1,1,1,]]
mono_px = ndimage.correlate(mono_gausian,PX)
mono_py = ndimage.correlate(mono_gausian,PY)
mono_px[mono_px<0] = 0
mono_py[mono_py<0] = 0
mono_m = np.abs(mono_py) + np.abs(mono_px)




#show
ax[0].imshow(mono,cmap = 'binary_r')
ax[1].imshow(mono_edge,cmap = 'binary')
ax[2].imshow(mono_m,cmap = 'binary')
fig.show()
input()
