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

mono_shape = (1000,1000)
fig, ax = plt.subplots(3, 2)
#chelsea = data.cat()
mono = np.zeros(mono_shape)
#mono[500:520, 460:550] = 1
mono = data.cat()
mono = np.mean(mono,axis = 2)
mono_shape = mono.shape
print(mono_shape)
mono = mono[:mono_shape[0]-1,:mono_shape[1]]#obydwa musza byc nieparzyste
mono_shape = mono.shape
print(mono_shape)

#fourier transform
mono_fft = fft(mono)
#Sobel operator
S1 = [[-1,0,1,],
      [-2,0,2,],
      [-1,0,1,]]
S1 = np.array(S1)
S1_padded = np.zeros(mono_shape)

S1_padded[mono_shape[0]//2:mono_shape[0]//2+3,mono_shape[1]//2:mono_shape[1]//2+3] = S1
S1_padded_fft = fft(S1_padded)

mono_fft_filtered = S1_padded_fft * mono_fft


#inverse = np.fft.ifft2(np.fft.ifftshift(mono_fft_filtered))
#inverse = np.real(np.fft.ifftshift(inverse))
inverse = inverse_fft(mono_fft_filtered)

#show
ax[0,0].imshow(mono,cmap = 'binary_r')
ax[0,1].imshow(np.abs(np.log(mono_fft)),cmap = 'magma')
ax[1,0].imshow(S1_padded,cmap = 'binary_r')
ax[1,1].imshow(np.abs(S1_padded_fft),cmap = 'magma')
ax[2,0].imshow(np.abs(np.log(mono_fft_filtered)),cmap = 'magma')
ax[2,1].imshow(inverse,cmap = 'binary_r')
fig.show()
input()
