import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data,draw
from scipy import ndimage
import random

def apply_ovals(img):
    shape = img.shape
    for i in range(100):
        x = random.randint(0,shape[0])
        y = random.randint(0,shape[1])
        rr,cc = draw.disk(center = (x,y),radius = (random.random()*8+2),shape=shape)
        img[rr,cc] = 1

def erode(img,element):
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
                    if(img[R_x,R_y] != element[B_x,B_y]):
                        isObject = False

            if(isObject):
                eroded_img[x,y] = 1

    return eroded_img

def dilatate(img,element):
    img_shape = img.shape
    element_shape = element.shape
    dilatated_img = np.zeros(img_shape)
    new_element = element#np.ones(element_shape) - element

    for x in range(img_shape[0]):
        for y in range(img_shape[1]):
            isObject = False

            for B_x in range(element_shape[0]):
                R_x = x - element_shape[0]//2 + B_x
                if(isObject == True):
                    break
                if(R_x<0 or img_shape[0]<=R_x):
                    continue

                for B_y in range(element_shape[1]):
                    R_y = y - element_shape[0]//2 + B_y
                    if(isObject == True):
                        break
                    if(R_y<0 or img_shape[1]<=R_y):
                        continue
                    if(img[R_x,R_y] == new_element[B_x,B_y]):
                        isObject = True

            if(isObject):
                dilatated_img[x,y] = 1

    return dilatated_img

def opening(img,element):
    return dilatate(erode(img,element),element)

def closing(img,element):
    return erode(dilatate(img,element),element)


mono_shape = (100,100)
#chelsea = data.cat()
mono = np.zeros(mono_shape)
apply_ovals(mono)
#mono[500:520, 460:550] = 1

B = [[ 1,1,1,],
      [1,1,1,],
      [1,1,1,]]
B = np.array(B)
print(B)
eroded = erode(mono,B)
dilatated = dilatate(mono,B)
opened = opening(mono,B)
closed = closing(mono,B)

#show
fig, ax = plt.subplots(2, 2)
ax[0,0].imshow(eroded,cmap = 'binary_r')
ax[0,1].imshow(dilatated,cmap = 'binary_r')
ax[1,0].imshow(opened,cmap = 'binary_r')
ax[1,1].imshow(closed,cmap = 'binary_r')
fig.show()
input()
