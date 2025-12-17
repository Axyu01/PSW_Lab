import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data
from scipy import ndimage

def fft(img):
    mono_fft = np.fft.fft2(img)
    print(mono_fft.shape)
    mono_fft_sh = np.fft.fftshift(mono_fft)
    mono_fft = mono_fft_sh
    return mono_fft

def inverse_fft(img):
    inverse = np.fft.ifft2(np.fft.ifftshift(img))
    inverse = np.real(np.fft.ifftshift(inverse))
    return inverse

fig, ax = plt.subplots(3, 2)
filtered_img = plt.imread("Lab9/filtered.png")
print(filtered_img.shape)
mono = filtered_img[:,:,0]
#mono = np.mean(mono,axis = 2)
mono_shape = mono.shape
print(mono_shape)
mono = mono[:mono_shape[0]-1,:mono_shape[1]]#obydwa musza byc nieparzyste
mono_shape = mono.shape
print(mono_shape)

h = np.ones((13,13))
h = h*(-1)
for i in range(13):
    h[i,i] = 9
h = h*(1/(-39))

#fourier transform
mono_fft = fft(mono)

h_padded = np.zeros(mono_shape)
h_padded[mono_shape[0]//2:mono_shape[0]//2+13,mono_shape[1]//2:mono_shape[1]//2+13] = h
h_padded_fft = fft(h_padded)

mono_fft_filtered = mono_fft/h_padded_fft

inverse = inverse_fft(mono_fft_filtered)

#show
ax[0,0].imshow(filtered_img,cmap = 'binary_r')
ax[0,1].imshow(np.abs(np.log(mono_fft)),cmap = 'magma')
ax[1,0].imshow(h_padded,cmap = 'binary_r')
ax[1,1].imshow(np.abs(h_padded_fft),cmap = 'magma')
ax[2,0].imshow(np.abs(np.log(mono_fft_filtered)),cmap = 'magma')
ax[2,1].imshow(inverse,cmap = 'binary_r')
fig.show()
input()
