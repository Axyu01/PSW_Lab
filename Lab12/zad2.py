import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data
from scipy import ndimage
from sklearn.cluster import KMeans
import random
SIZE = 100
fig, ax = plt.subplots(1, 2)
image_shape = (SIZE,SIZE,3)
image = np.zeros(image_shape).astype(int)
ground_truth = np.zeros((SIZE,SIZE)).astype(int)
for i in range(3):
    radius = random.randint(10,40)
    center = (random.randint(radius,SIZE-radius),random.randint(radius,SIZE-radius))
    output = img.draw.disk(center=center,radius=radius)
    rand_value = random.randint(100,255)
    canal = random.randint(0,2)
    for pixel in range(len(output[0])):
        x = output[0][pixel]
        y = output[1][pixel]
        image[x,y,canal] += rand_value
        ground_truth[x,y] += rand_value
ground_truth = img.measure.label(ground_truth)
image += np.random.normal(0,32,image_shape).astype(int)
image = np.clip(image,a_min=0,a_max=255)

#clasterization
image_2 = np.reshape(image,newshape=(SIZE*SIZE,3))
coords = np.meshgrid(np.arange(SIZE),np.arange(SIZE))
coords = np.array(coords)
print(coords.shape)
#x,y/costam/costam

ground_truth_2 = np.reshape(ground_truth,newshape=(SIZE*SIZE))

X = np.zeros((SIZE*SIZE,5))
X[:,0:3] = image_2
for x in range(SIZE):
    for y in range(SIZE):
        X[x*SIZE +y,3] = x
        X[x*SIZE +y,4] = y

y = ground_truth_2

#normalizacja standardowa
for i in range(5):
    mean = np.mean(X[:,i])
    std = np.std(X[:,i])
    X[:,i] = (X[:,i] - mean)/std

#liczba klas
k = np.unique(ground_truth_2).shape[0]

#klasyfikacja
kmeans = KMeans(k)
clusters = kmeans.fit_predict(X)
print(clusters.shape)
clusters =  np.reshape(clusters,newshape=(SIZE,SIZE))

#show
ax[0].imshow(clusters)
ax[1].imshow(ground_truth)
fig.show()
input()
