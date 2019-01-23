import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

print(cv.__version__)


img = cv.imread('logo.png',0)
print(img.shape)

plt.imshow(img,cmap = 'gray',interpolation = 'bicubic')
plt.xticks([]),plt.yticks([])
plt.show()

