import numpy as np
import matplotlib.pyplot as plt

fig, ax = fig, ax = plt.subplots(3,3, figsize=(10,10))
#sin
y = np.linspace(0,np.pi*4,num = 40)
y = np.sin(y)
ax[0][0].plot(y)
#sin squered
y2 = y[:, np.newaxis]*y[np.newaxis, :]
value_min = np.min(y2)
value_max = np.max(y2)
ax[0][1].imshow(y2,cmap = 'magma')
ax[0][1].set_title('min: %.3f, max: %.3f' % (value_min, value_max))
#sin squered normalized
y2 -= value_min
y2 /= value_max-value_min
value_min = np.min(y2)
value_max = np.max(y2)
ax[0][2].imshow(y2,cmap = 'magma')
ax[0][2].set_title('min: %.3f, max: %.3f' % (value_min, value_max))
#sin squered quantized 2 bit
y2q = y2*(2**2)
y2q = np.rint(y2q)
value_min_q = np.min(y2q)
value_max_q = np.max(y2q)
ax[1][0].imshow(y2q,cmap = 'magma')
ax[1][0].set_title('min: %.3f, max: %.3f' % (value_min_q, value_max_q))
#sin squered quantized 4 bit
y2q = y2*(2**4)
y2q = np.rint(y2q)
value_min_q = np.min(y2q)
value_max_q = np.max(y2q)
ax[1][1].imshow(y2q,cmap = 'magma')
ax[1][1].set_title('min: %.3f, max: %.3f' % (value_min_q, value_max_q))
#sin squered quantized 8 bit
y2q = y2*(2**8)
y2q = np.rint(y2q)
value_min_q = np.min(y2q)
value_max_q = np.max(y2q)
ax[1][2].imshow(y2q,cmap = 'magma')
ax[1][2].set_title('min: %.3f, max: %.3f' % (value_min_q, value_max_q))



#show fig
fig.tight_layout()
fig.show()
input()