import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgPath = 'Assets/Pictures/test.jpg'
img = cv.imread(imgPath)

imgPath2 = 'Assets/Pictures/Contours.jpg'
img2 = cv.imread(imgPath2)

print(img.shape)
print(img.ndim)

print(img2.shape)
print(img2.ndim)


if img is None:
    print("Read Picture Error!")
    exit()


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
plt.hist(gray.ravel(),bins=256,range=[0,256])


bgrColor = ('b','g','r')

for cidx,color in enumerate(bgrColor):

    cHist = cv.calcHist([img],[cidx],None,[256],[0,256])
    plt.plot(cHist,color = color)

plt.xlim([0,256])
plt.show()
