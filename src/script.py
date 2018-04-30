import sys
import numpy as np
import file_loader
import matplotlib
array = file_loader.read_pgm("../res/faces_4/cheyer/cheyer_left_angry_open_4.pgm")


print(array.shape)

plt.subplot(10,10,i+1)
plt.imshow(-Xorig[i,:].reshape((28,28)),interpolation='nearest',cmap='gray')
plt.axis('off')
plt.title(str(Torig[i][0]))