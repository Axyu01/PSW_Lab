import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data
from scipy import ndimage

def correlate(image,kernel):
    print(kernel)
    shape = image.shape
    out = np.zeros((shape[0],shape[1]))
    for x in range (1,shape[0]-1):
        for y in range (1,shape[1]-1):
            out[x,y] = np.sum(np.sum(image[x-1:x+2,y-1:y+2]*kernel,axis=0),axis=0)
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
print(f"shapes:{corelation.shape},{chelsea_grey.shape}")
convolution = ndimage.convolve(chelsea_grey,S1)
corelation_custom = correlate(chelsea_grey,S1)
convolution_custom = convolve(chelsea_grey,S1)
print(convolution_custom.shape)
#show
ax[0,0].imshow(corelation,cmap = 'binary_r')
ax[0,1].imshow(convolution,cmap = 'binary_r')
ax[1,0].imshow(corelation_custom,cmap = 'binary_r')
ax[1,1].imshow(convolution_custom,cmap = 'binary_r')

diff_image,diff_sum = diff(corelation,corelation_custom)
ax[2,0].imshow(diff_image,cmap = 'binary_r')
ax[2,0].set_title(f"Sum {diff_sum}",fontdict = {'fontsize':8})

diff_image,diff_sum = diff(convolution,convolution_custom)
ax[2,1].imshow(diff_image,cmap = 'binary_r')
ax[2,1].set_title(f"Sum {diff_sum}",fontdict = {'fontsize':8})

fig.show()
input()
