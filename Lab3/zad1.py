import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data#,img_as_ubyte

def applyLUT(img,LUT):
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            r = int(img[x,y,0])
            g = int(img[x,y,1])
            b = int(img[x,y,2])
            img[x,y] = [LUT[r],LUT[g],LUT[b]]

def scatterHist(ax,i,img):
    colors = ['r', 'g', 'b']
    for c, color in enumerate(colors):
        values, counts = np.unique(img[..., c], return_counts=True)
        probs = counts / counts.sum()
        ax[i, 2].scatter(values, probs, color=color,s = 1)
        ax[i, 2].legend(fontsize=8)
            
#if __name__ != "__main__":

#ZAD 1
#oiriginal
fig, ax = plt.subplots(6, 3, figsize=(9, 18))
#fig.subplots_adjust(wspace=0.05, hspace=0.15)
chelsea = data.cat()#img_as_ubyte(data.cat())
chelsea_ident = np.array(chelsea)
chelsea_neg = np.array(chelsea)
chelsea_edge = np.array(chelsea)
chelsea_sin = np.array(chelsea)
chelsea_gamma03 = np.array(chelsea)
chelsea_gamma3 = np.array(chelsea)

#LUTs
D = 8
L = 2**D

#generate LUTs
LUT_ident = np.zeros(shape = (L))
LUT_neg = np.zeros(shape = (L))   
LUT_edge = np.zeros(shape = (L)) 
LUT_sin = np.zeros(shape = (L))
LUT_gamma03 = np.zeros(shape = (L))
LUT_gamma3 = np.zeros(shape = (L))

dT = 2 * np.pi/L
G03_NORM =(L-1)/((L-1)**(0.3))
G3_NORM = (L-1)/((L-1)**(3))
for i in range(L):
    LUT_ident[i] = i
    LUT_neg[i] = L-i-1
    if(50<=i and i<150):
        LUT_edge[i] = L-1
    LUT_sin[i] = np.sin(dT*i) * (L-1)/2 +int((L-1)/2)
    LUT_gamma03[i] = LUT_ident[i]**(0.3) * G03_NORM
    LUT_gamma3[i] = LUT_ident[i]**(3) *G3_NORM

#apply LUTs
applyLUT(chelsea_ident,LUT_ident)
applyLUT(chelsea_neg, LUT_neg)
applyLUT(chelsea_edge, LUT_edge)
applyLUT(chelsea_sin, LUT_sin)
applyLUT(chelsea_gamma03, LUT_gamma03)
applyLUT(chelsea_gamma3, LUT_gamma3)

#genereate Hist for imgages
hist_ident = np.array(chelsea_ident[...,0])
#hist_neg = np.array(L,3)
#hist_edge = np.array(L,3)
#hist_sin = np.array(L,3)
#hist_gamma03 = np.array(L,3)
#hist_gamma3 = np.array(L,3)


#OUTPUT
ax[0,0].plot(LUT_ident)
ax[1,0].plot(LUT_neg)
ax[2,0].plot(LUT_edge)
ax[3,0].plot(LUT_sin)
ax[4,0].plot(LUT_gamma03)
ax[5,0].plot(LUT_gamma3)
ax[0,1].imshow(chelsea_ident)
ax[1,1].imshow(chelsea_neg)
ax[2,1].imshow(chelsea_edge)
ax[3,1].imshow(chelsea_sin)
ax[4,1].imshow(chelsea_gamma03)
ax[5,1].imshow(chelsea_gamma3)
scatterHist(ax,0,chelsea_ident)
scatterHist(ax,1,chelsea_neg)
scatterHist(ax,2,chelsea_edge)
scatterHist(ax,3,chelsea_sin)
scatterHist(ax,4,chelsea_gamma03)
scatterHist(ax,5,chelsea_gamma3)

fig.show()
input()