import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = np.zeros((512,512,3),np.uint8)
cv.line(img,(0,0),(511,511),(255,0,0),5)



font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500),font,4,(255,255,255),2,cv.LINE_AA)

plt.imshow(img,cmap = 'gray',interpolation = 'bicubic')
plt.xticks([]),plt.yticks([])
plt.show()
