import numpy as np
import matplotlib.pyplot as plt

mono = np.zeros((30,30))

mono[10:20,10:20] = 1

mono[15:25,5:15] = 2

fig, ax = fig, ax = plt.subplots(2,2, figsize=(7,7))
ax[0][0].set_title("obraz monochromatyczny")
ax[0][0].imshow(mono)
ax[0][1].imshow(mono,cmap='binary',)
ax[0][1].set_title("obraz monochromatyczny")
fig.tight_layout()
fig.savefig("Lab0/figure.png")



