import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data
from scipy import ndimage

def correlate(image,kernel):
    print(kernel)
    k_shape = kernel.shape
    x_offset = int(k_shape[0]/2)
    y_offset = int(k_shape[1]/2)
    shape = image.shape
    out = np.zeros((shape[0],shape[1]))
    for x in range (x_offset,shape[0]-x_offset):
        for y in range (y_offset,shape[1]-y_offset):
            out[x,y] = np.sum(np.sum(image[x-x_offset:x+x_offset+1,y-y_offset:y+y_offset+1]*kernel,axis=0),axis=0)/k_shape[0]/k_shape[1]
    return out
def convolve(image,kernel):
    #kernel = np.swapaxes(kernel,axis1=0,axis2=1)
    kernel = np.flip(kernel)
    return correlate(image,kernel)

def diff(image1,image2):
    shape = image1.shape
    diff_image = np.zeros(shape)
    for x in range (0,shape[0]):
        for y in range (0,shape[1]):
           diff_image[x,y] = np.abs(image1[x,y]-image2[x,y]) 
    diff_sum = np.sum(np.sum(diff_image,axis=0),axis=0)
    return diff_image,diff_sum
    
           

fig, ax = plt.subplots(3, 2)
chelsea = data.cat()

S1 = [[-1,0,1,],
      [-2,0,2,],
      [-1,0,1,]]
S1 = np.array(S1)
chelsea_grey = np.sum(chelsea,axis = 2)/3

#show
blurred = correlate(chelsea_grey,np.ones((7,7)))
mask = chelsea_grey-blurred
with_mask = chelsea_grey+mask
ax[0,0].imshow(chelsea_grey,cmap = 'binary_r')
ax[0,1].imshow(blurred,cmap = 'binary_r')
ax[1,0].imshow(mask,cmap = 'binary_r')
ax[1,1].imshow(with_mask,cmap = 'binary_r',vmin = 0,vmax =255)

#diff_image,diff_sum = diff(corelation,corelation_custom)
#ax[2,0].imshow(diff_image,cmap = 'binary_r')
#ax[2,0].set_title(f"Sum {diff_sum}",fontdict = {'fontsize':8})

#diff_image,diff_sum = diff(convolution,convolution_custom)
#ax[2,1].imshow(diff_image,cmap = 'binary_r')
#ax[2,1].set_title(f"Sum {diff_sum}",fontdict = {'fontsize':8})

fig.show()
input()
