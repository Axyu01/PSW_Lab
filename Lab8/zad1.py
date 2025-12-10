import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data
from skimage.transform import resize 
from scipy import ndimage

zebra = plt.imread("Lab8/zebra.jpg")
zebra.astype(float)
print(zebra.shape)
zebra = np.mean(zebra,axis=2)#zebra[:,:,0]+zebra[:,:,1]+zebra[:,:,2]
print(zebra.shape)
MIN = np.min(zebra)
MAX = np.max(zebra)
zebra = (zebra-MIN)/(MAX-MIN)
w = np.array([2,5,9,-1,-4,-8])
w = w.astype(float)

w_normalized = w - np.mean(w)#(w-MIN)/(MAX-MIN)
print(np.mean(w_normalized))
#w_normalized = w - np.max(w_normalized)

w2_normalized = w_normalized[:,None]*w_normalized[None,:]
w2_normalized = w2_normalized- np.mean(w2_normalized)
print(w2_normalized)
w2_padded = np.zeros((10,10))
w2_padded[2:8,2:8] = w2_normalized
w2_resized = resize(w2_padded,(w2_padded.shape[0]*3,w2_padded.shape[1]*3))

print(w_normalized)

fig, ax = plt.subplots(3, 2)
ax[0][0].plot(w)
ax[0][1].plot(w_normalized)
ax[1][0].imshow(w2_padded,cmap = 'magma')
ax[1][1].imshow(w2_resized,cmap = 'magma')
ax[2][0].imshow(zebra,cmap = 'binary_r')
ax[2][0].imshow(zebra,cmap = 'magma')
ax[2][1].imshow(ndimage.correlate(zebra,w2_resized),cmap = 'magma')
#ax[2][0].imshow(zebra,cmap = 'binary_r')
fig.show()
input()