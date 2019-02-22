import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgPath = '../Assets/Pictures/test.jpg'
img = cv.imread(imgPath)

cows = 9

# kernel = np.ones((cows,cows),np.float32)/(cows*cows)
# dst = cv.filter2D(img,-1,kernel)

# dst = cv.blur(img,(cows,cows))

# dst = cv.GaussianBlur(img,(cows,cows),10,50)

# dst = cv.medianBlur(img,cows)

dst = cv.bilateralFilter(img,9,75,75)

plt.subplot(121),plt.imshow(img),plt.title('Orignal')
plt.xticks([]),plt.yticks([])

plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]),plt.yticks([])


plt.show()
