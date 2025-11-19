import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data
from scipy import ndimage

def calc(img):
    img_shape = img.shape

mono_shape = (1000,1000)
fig, ax = plt.subplots(2, 3)
#chelsea = data.cat()
mono = np.zeros(mono_shape)
#mono[500:520, 460:550] = 1
xv,yv=np.meshgrid(np.linspace(0,16,num = 1000),np.linspace(0,16,num = 1000),)

A = [9.2,2.3,5.4,7.5,0.6]
angles = [0.2,4.3,0.4,2.5,7.6]
lengths = [1.2,8.3,3.4,1.5,4.6]

for amp,angle,length in zip(A,angles,lengths):
    mono = mono + amp *np.sin(2*np.pi*(xv*np.cos(angle)+yv*np.sin(angle)/length))

mono_fft = np.fft.fft2(mono)
mono_fft_sh = np.fft.fftshift(mono_fft)
mono_fft_R = np.real(mono_fft_sh)
mono_fft_R  = np.abs(mono_fft_R)
mono_fft_R = mono_fft_R + np.ones(mono_shape)
mono_fft_R = np.log(mono_fft_R)

mono_fft_I = np.imag(mono_fft_sh)
mono_fft_I  = np.abs(mono_fft_I)
mono_fft_I = mono_fft_I + np.ones(mono_shape)
mono_fft_I = np.log(mono_fft_I)

phase_shift =np.arctan2(np.imag(mono_fft_sh),np.real(mono_fft_sh))
magnitude = np.abs(mono_fft_sh)
magnitude = magnitude + np.ones(mono_shape)
magnitude = np.log(magnitude)

inverse = np.fft.ifft2(np.fft.ifftshift(mono_fft_sh))
inverse = np.real(inverse)

#show
ax[0,0].imshow(mono,cmap = 'magma')
ax[0,1].imshow(mono_fft_R,cmap = 'magma')
ax[0,2].imshow(mono_fft_I,cmap = 'magma')
ax[1,0].imshow(phase_shift,cmap = 'magma')
ax[1,1].imshow(magnitude,cmap = 'magma')
ax[1,2].imshow(inverse,cmap = 'magma')
fig.show()
input()
