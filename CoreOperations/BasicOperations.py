import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgPath = '../Assets/Pictures/logo.png'
img = cv.imread(imgPath,1)
# print(img[100,100])
# print(img[100,100,2])
# print('----------')
# img.itemset((100,100,2),100)
# print(img.item(100,100,2))
#
# print(img.shape)
# print(img.size)
# print(img.dtype)

# ball = img[470:1270, 860:1660]
# img[100:900, 300:1100] = ball

# b,g,r = cv.split(img)
# print(b)
# img = cv.merge((r,g,b))
# img[:,:,2] = 255

# plt.imshow(img,cmap = 'gray',interpolation = 'bicubic')
# plt.xticks([]),plt.yticks([])
# plt.show()

border = 10
replicate = cv.copyMakeBorder(img,border,border,border,border,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img,border,border,border,border,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img,border,border,border,border,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img,border,border,border,border,cv.BORDER_WRAP)
constant = cv.copyMakeBorder(img,border,border,border,border,cv.BORDER_CONSTANT, value = [255,0,0])

cmap = 'gray'
plt.subplot(231),plt.imshow(img,cmap),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,cmap),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,cmap),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,cmap),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,cmap),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,cmap),plt.title('CONSTANT')

plt.show()


