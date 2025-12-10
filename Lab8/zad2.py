import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data
from skimage.transform import resize 
from scipy import ndimage

def show_img(ax,wavelet,x,y,x_w,y_w):
    wavelet2 = resize(wavelet,(x_w,y_w))
    wavelet2 = wavelet2 - np.mean(wavelet2)
    ax[x][y].imshow(ndimage.correlate(zebra,wavelet2),cmap = 'magma')

zebra = plt.imread("Lab8/zebra.jpg")
zebra.astype(float)
zebra = np.mean(zebra,axis=2)
MIN = np.min(zebra)
MAX = np.max(zebra)
zebra = (zebra-MIN)/(MAX-MIN)
w = np.array([2,5,9,-1,-4,-8])
w = w.astype(float)

w_normalized = w - np.mean(w)#(w-MIN)/(MAX-MIN)
print(np.mean(w_normalized))

w2_normalized = w_normalized[:,None]*w_normalized[None,:]
w2_normalized = w2_normalized- np.mean(w2_normalized)
print(w2_normalized)
w2_padded = np.zeros((10,10))
w2_padded[2:8,2:8] = w2_normalized
vals = np.linspace(start=4,stop=32,num=6)
vals.astype(int)

fig, ax = plt.subplots(6, 6)

for x in range(6):
    for y in range(6):
        show_img(ax,w2_padded,x,y,vals[x],vals[y])
    

print(w_normalized)


#ax[2][0].imshow(zebra,cmap = 'binary_r')
fig.show()
input()