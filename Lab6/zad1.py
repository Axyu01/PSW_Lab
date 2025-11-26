import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data
from scipy import ndimage

fig, ax = plt.subplots(2, 3)
chelsea = data.cat()
POINT1 = (25,25)
POINT2 = (200,50)
POINT3 = (150,175)
DEAPTH1 = 10
DEAPTH2 = 100
DEAPTH3 = 200
img_data = np.load("Lab6/hsi_small.npy")
print(img_data.shape)

#show images
ax[0,0].imshow(img_data[:,:,DEAPTH1],cmap = 'binary_r')
ax[0,0].scatter(POINT1[0],POINT1[1],color = 'red')
ax[0,1].imshow(img_data[:,:,DEAPTH2],cmap = 'binary_r')
ax[0,1].scatter(POINT2[0],POINT2[1],color = 'red')
ax[0,2].imshow(img_data[:,:,DEAPTH3],cmap = 'binary_r')
ax[0,2].scatter(POINT3[0],POINT3[1],color = 'red')

#show pixel spectograms
deapth = img_data.shape[2]
x = np.linspace(0,deapth,num =deapth)
ax[1,0].plot(x,img_data[POINT1[0],POINT1[1],:],color = 'red')
ax[1,0].scatter(DEAPTH1,img_data[POINT1[0],POINT1[1],DEAPTH1],color = 'blue')
ax[1,1].plot(x,img_data[POINT2[0],POINT2[1],:],color = 'red')
ax[1,1].scatter(DEAPTH2,img_data[POINT2[0],POINT2[1],DEAPTH2],color = 'blue')
ax[1,2].plot(x,img_data[POINT3[0],POINT3[1],:],color = 'red')
ax[1,2].scatter(DEAPTH3,img_data[POINT3[0],POINT3[1],DEAPTH3],color = 'blue')
fig.show()
input()
