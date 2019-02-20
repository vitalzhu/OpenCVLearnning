import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgPath = '../Assets/Pictures/test.jpg'
img = cv.imread(imgPath,0)

rows,cols = img.shape

#Translation Matrix
# M = np.float32([[1,0,100],[0,1,50]]

#Rotation
# M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)

# dst = cv.warpAffine(img,M,(cols,rows))


# cv.imshow('img',dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

#---------Affine Transformation--------------

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv.getAffineTransform(pts1,pts2)

dst = cv.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('input')
plt.subplot(122),plt.imshow(dst),plt.title('output')
plt.show()
