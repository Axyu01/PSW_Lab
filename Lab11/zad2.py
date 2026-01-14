import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data
from scipy import ndimage

def adaptive_threshold(image):
    print(image)
    median_image = np.zeros(image.shape)
    end_image = np.zeros(image.shape)
    shape = median_image.shape
    print(shape)
    size = 21

    for x in range(shape[0]):
        for y in range(shape[1]):
            chunk = np.array(image[max(0,x-size//2):min(shape[0],x+size//2+1),max(0,y-size//2):min(shape[1],y+size//2+1)])
            
            median_image[x,y] = np.median(chunk)#np.sum(chunk)/chunk.shape[0]/chunk.shape[1]
    for x in range(shape[0]):
        for y in range(shape[1]):
            if image[x,y] > median_image[x,y]:
                end_image[x,y] = 1
            else:
                end_image[x,y] = 0
    
    
    return end_image

fig, ax = plt.subplots(2, 4)
mono = data.cat()
mono = np.mean(mono,axis = 2)
mono_shape = mono.shape
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
      [1,1,1,]]
mono_px = ndimage.correlate(mono_gausian,PX)
mono_py = ndimage.correlate(mono_gausian,PY)
mono_px[mono_px<0] = 0
mono_py[mono_py<0] = 0
mono_m = np.abs(mono_py) + np.abs(mono_px)


#normalizacja
mono_m -= np.min(mono_m)
mono_m /= np.max(mono_m)

mono_edge -= np.min(mono_edge)
mono_edge /= np.max(mono_edge)

#progrowanie
threshold = 0.1
mono_m_t = np.array(mono_m)
mono_m_t[mono_m_t>=threshold] = 1
mono_m_t[mono_m_t<threshold] = 0
mono_edge_t = np.array(mono_edge)
mono_edge_t[mono_edge>=threshold] = 1
mono_edge_t[mono_edge<threshold] = 0

#filtracja medianowa
#MEDIAN_FILTER = np.ones((21,21))/(21*21)
mono_m_median = ndimage.median_filter(mono_m,size = 21)
mono_edge_median = ndimage.median_filter(mono_edge,size = 21)

#progowanie adaptacyjne
mono_m_ad = adaptive_threshold(mono_m)
mono_edge_ad = adaptive_threshold(mono_edge)

#show
#ax[0].imshow(mono,cmap = 'binary_r')
ax[0,0].imshow(mono_edge,cmap = 'binary')
ax[1,0].imshow(mono_m,cmap = 'binary')
ax[0,1].imshow(mono_edge_t,cmap = 'binary')
ax[1,1].imshow(mono_m_t,cmap = 'binary')
ax[0,2].imshow(mono_edge_median,cmap = 'binary')
ax[1,2].imshow(mono_m_median,cmap = 'binary')
ax[0,3].imshow(mono_edge_ad,cmap = 'binary')
ax[1,3].imshow(mono_m_ad,cmap = 'binary')
fig.show()
input()
