import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data
from sklearn import decomposition
from scipy import ndimage

def normalize(image):
    min = np.min(image)
    max = np.max(image)
    image = (image - min)/(max-min)

    return image

fig, ax = plt.subplots(1, 2)
chelsea = data.cat()

POINT1 = (25,25)
POINT2 = (200,50)
POINT3 = (150,175)

DEAPTH_R = 100
DEAPTH_G = 50
DEAPTH_B = 7

img_data = np.load("Lab6/hsi_small.npy")
IMG_X = img_data.shape[0]
IMG_Y = img_data.shape[1]
IMG_Z = img_data.shape[2]
print(img_data.shape)

#RGB
red_normalized = img_data[:,:,DEAPTH_R]
red_normalized = normalize(red_normalized)
print(np.min(red_normalized))
print(np.max(red_normalized))
green_normalized = img_data[:,:,DEAPTH_G]
green_normalized = normalize(green_normalized)
blue_normalized = img_data[:,:,DEAPTH_B]
blue_normalized = normalize(blue_normalized)
img_rgb = np.zeros((IMG_X,IMG_Y,3))
img_rgb[:,:,0] = red_normalized
img_rgb[:,:,1] = green_normalized
img_rgb[:,:,2] = blue_normalized

#PCA
PCA = decomposition.PCA(n_components=3)
img_data_flat = np.zeros((IMG_X*IMG_Y,IMG_Z))
for y in range(IMG_Y):
    for x in range(IMG_X):
        img_data_flat[x + y*IMG_X,:] = img_data[x,y,:]

PCA.fit(img_data_flat)
pca_out = PCA.transform(img_data_flat)
print(pca_out.shape)

img_rgb_pca = np.zeros((IMG_X,IMG_Y,3))
for y in range(IMG_Y):
    for x in range(IMG_X):
        img_rgb_pca[x,y,:] = pca_out[x + y*IMG_X,:]

print(np.min(img_rgb_pca[:,:,0]))
print(np.max(img_rgb_pca[:,:,0]))
img_rgb_pca[:,:,0] = normalize(img_rgb_pca[:,:,0])
print(np.min(img_rgb_pca[:,:,0]))
print(np.max(img_rgb_pca[:,:,0]))
img_rgb_pca[:,:,1] = normalize(img_rgb_pca[:,:,1])
img_rgb_pca[:,:,2] = normalize(img_rgb_pca[:,:,2])

#show images
ax[0].imshow(img_rgb,cmap = 'binary_r')
ax[1].imshow(img_rgb_pca,cmap = 'binary_r')

fig.show()
input()
