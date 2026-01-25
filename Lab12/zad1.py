import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data
from scipy import ndimage
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

#show
ax[0].imshow(image)
ax[1].imshow(ground_truth)
fig.show()
input()
