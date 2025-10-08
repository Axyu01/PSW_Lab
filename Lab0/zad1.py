import numpy as np

mono = np.zeros((30,30))

mono[10:20,10:20] = 1

mono[15:25,5:15] = 2

print(mono)