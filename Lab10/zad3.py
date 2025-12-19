import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data,draw
from scipy import ndimage
import random

def apply_ovals(img):
    np.random.seed = 1299
    shape = img.shape
    for i in range(100):
        x = random.randint(0,shape[0])
        y = random.randint(0,shape[1])
        rr,cc = draw.disk(center = (x,y),radius =random.randint(2,6),shape=shape)
        img[rr,cc] = 1

def match(img,element):
    img_shape = img.shape
    element_shape = element.shape
    eroded_img = np.zeros(img_shape)

    for x in range(img_shape[0]):
        for y in range(img_shape[1]):
            isObject = True

            for B_x in range(element_shape[0]):
                R_x = x - element_shape[0]//2 + B_x
                if(isObject == False):
                    break
                if(R_x<0 or img_shape[0]<=R_x):
                    continue

                for B_y in range(element_shape[1]):
                    R_y = y - element_shape[0]//2 + B_y
                    if(isObject == False):
                        break
                    if(R_y<0 or img_shape[1]<=R_y):
                        continue
                    if(img[R_x,R_y] != element[B_x,B_y] and element[B_x,B_y] >0):
                        isObject = False

            if(isObject):
                eroded_img[x,y] = 1

    return eroded_img

def hit_or_miss(img,o_element,b_element):
    o_img = match(img,o_element)
    b_img = match(np.ones(img.shape)-img,b_element)

    return o_img * b_img

mono_shape = (100,100)
#chelsea = data.cat()
mono = np.zeros(mono_shape)
apply_ovals(mono)
#mono[500:520, 460:550] = 1

B1 = np.zeros((9,9))
rr,cc = draw.disk(center = (9//2,9//2),radius = (9//2),shape = B1.shape)
B1[rr,cc] = 1

B2 = np.zeros((9,9))
rr,cc = draw.disk(center = (9//2,9//2),radius = (9//2+1),shape = B2.shape)
B2[rr,cc] = 1
B2 = B2-B1

product = hit_or_miss(mono,B1,B2)

#show
fig, ax = plt.subplots(1, 4)
ax[0].imshow(B1,cmap = 'binary_r')
ax[1].imshow(B2,cmap = 'binary_r')
ax[2].imshow(mono,cmap = 'binary_r')
ax[3].imshow(product,cmap = 'binary_r')
fig.show()
input()
