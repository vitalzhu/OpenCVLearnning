import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgPath = '../../Assets/Pictures/Contours.jpg'
img = cv.imread(imgPath)

imgray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh = cv.threshold(imgray,127,255,0)

contours,hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

print(len(contours))
cnt = contours[0]
dr = cv.drawContours(imgray,cnt,0,(245,0,0),3)

plt.subplot(121),plt.imshow(img),plt.title('Orignal')
plt.xticks([]),plt.yticks([])

plt.subplot(122),plt.imshow(dr),plt.title('DR')
plt.xticks([]),plt.yticks([])

plt.show()
