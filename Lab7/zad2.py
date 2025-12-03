import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data
from scipy import ndimage

def correlate(image,kernel):
    print(kernel)
    k_shape = kernel.shape
    x_offset = int(k_shape[0]/2)
    y_offset = int(k_shape[1]/2)
    shape = image.shape
    out = np.zeros((shape[0],shape[1]))
    for x in range (x_offset,shape[0]-x_offset):
        for y in range (y_offset,shape[1]-y_offset):
            out[x,y] = np.sum(np.sum(image[x-x_offset:x+x_offset+1,y-y_offset:y+y_offset+1]*kernel,axis=0),axis=0)/k_shape[0]/k_shape[1]
    return out

def applyNoise2(image,probability):
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if np.random.choice([0,1],p=[probability,1 - probability]) == 0:
                for c in range(3):
                    if np.random.choice([0,1],p=[0.5,0.5]) == 0:
                        image[x,y,c] = 255
                    else:
                        image[x,y,c] = 0

def applyNoise(image,probability):
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            for c in range(3):
                if np.random.choice([0,1],p=[probability,1 - probability]) == 0:
                    if np.random.choice([0,1],p=[0.5,0.5]) == 0:
                        image[x,y,c] = 255
                    else:
                        image[x,y,c] = 0


def undoNoise(image,kernelSize):
    shape = image.shape
    out = np.zeros((shape[0],shape[1],shape[2])).astype(int)
    x_offset = int(kernelSize/2)
    y_offset = int(kernelSize/2)
    for x in range (x_offset,shape[0]-x_offset):
        for y in range (y_offset,shape[1]-y_offset):
            for c in range(3):
                values = []
                for x_x in range (-x_offset,x_offset+1):
                    for y_y in range (-y_offset,y_offset+1):
                        values.append(image[x+x_offset,y+y_offset,c])
                values.sort()
                #print(values)
                out[x,y,c] = values[int((kernelSize*kernelSize)/2)]
    return out

def show(image,index,ax):
    ax[index,0].imshow(image,cmap = 'binary_r')
    ax[index,1].imshow(undoNoise(image,3),cmap = 'binary_r')
    ax[index,2].imshow(undoNoise(image,5),cmap = 'binary_r')
    ax[index,3].imshow(undoNoise(image,9),cmap = 'binary_r')

fig, ax = plt.subplots(3, 4)
chelsea = data.cat()
smol_chelsea = chelsea[::3,::3,:]
chelsea_noise_smoll = np.array(smol_chelsea)
chelsea_noise_avarage = np.array(smol_chelsea)
chelsea_noise_big = np.array(smol_chelsea)

applyNoise(chelsea_noise_smoll,0.1)
applyNoise(chelsea_noise_avarage,0.3)
applyNoise(chelsea_noise_big,0.45)


#S1 = [[1,1,1,],
#      [1,1,1,],
#      [1,1,1,]]

S1 = np.ones((9,9,3))
S1 = S1/(81*3)
#chelsea_noise = chelsea_noise.astype(float)
#chelsea_noise = chelsea_noise/255

#chelsea_mean = np.array(smol_chelsea.shape)
#chelsea_mean = ndimage.correlate(chelsea_noise,S1)



#corelation = ndimage.correlate(chelsea,S1_EX)
#convolution = ndimage.convolve(chelsea,S1_EX)
#corelation = ndimage.correlate(chelsea_grey,S1)
#convolution = ndimage.convolve(chelsea_grey,S1)
#show
#ax[0,0].imshow(smol_chelsea,cmap = 'binary_r')
show(chelsea_noise_smoll,0,ax)
show(chelsea_noise_avarage,1,ax)
show(chelsea_noise_big,2,ax)
#ax[1,0].imshow(chelsea_noise,cmap = 'binary_r')
#ax[2,0].imshow(chelsea_mean,cmap = 'binary_r')
fig.show()
input()
