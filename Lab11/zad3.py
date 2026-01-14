import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data
from scipy import ndimage

def otsu(image):
    shape = image.shape
    ALL_PIXELS_COUNT = shape[0]*shape[1]
    v_arr = []
    for threshold in range(0,255):
        CLASS_0_COUNT = 0
        CLASS_0_AVG =0
        CLASS_1_COUNT = 0
        CLASS_1_AVG = 0
        IMAGE_AVG = 0
        for x in range(shape[0]):
            for y in range(shape[1]):
                val = image[x,y]
                if val<threshold:
                    CLASS_0_COUNT += 1
                    CLASS_0_AVG += val
                else:
                    CLASS_1_COUNT += 1
                    CLASS_1_AVG += val
                IMAGE_AVG += val

        IMAGE_AVG /=ALL_PIXELS_COUNT
        if(CLASS_0_COUNT == 0):
            CLASS_0_COUNT = 1
        if(CLASS_1_COUNT == 0):
            CLASS_1_COUNT = 1
        
        CLASS_0_AVG /=CLASS_0_COUNT
        CLASS_1_AVG /=CLASS_1_COUNT

        P_0 = CLASS_0_COUNT/ALL_PIXELS_COUNT
        P_1 = CLASS_1_COUNT/ALL_PIXELS_COUNT

        v = P_0*((CLASS_0_AVG - IMAGE_AVG)**2)+P_1*((CLASS_1_AVG - IMAGE_AVG)**2)
        v_arr.append(v)
    return v_arr
        

fig, ax = plt.subplots(2, 2)
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

#normalizacja
mono_edge -= np.min(mono_edge)
mono_edge /= np.max(mono_edge)

#forma 8 bit
mono_edge = mono_edge *(2**8-1)
mono_edge = mono_edge.astype(int)
unique,counts = np.unique(mono_edge,return_counts=True)
print(unique)
print(counts)

#Otsu
v_arr = otsu(mono_edge)
threshold = np.argmax(v_arr)
mono_edge_t = mono_edge.copy()
mono_edge_t[mono_edge_t>=threshold] = 255
mono_edge_t[mono_edge_t<threshold] = 0


#show
#ax[0,0].imshow(mono,cmap = 'binary_r')
ax[0,0].imshow(mono_edge,cmap = 'binary')
ax[0,1].bar(unique,counts)
ax[0,1].set_yscale('log')
ax[1,0].plot(v_arr)
ax[1,0].vlines(threshold,0,v_arr[threshold],color = "red",linestyles = "dotted")
ax[1,1].imshow(mono_edge_t,cmap = 'binary')
fig.show()
input()
