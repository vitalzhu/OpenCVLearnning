import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgPath = '../../Assets/Pictures/Contours.jpg'
img = cv.imread(imgPath,0)

print(img.shape)
print("W = {}".format(img.shape[1]))
print("H = {}".format(img.shape[0]))
print(img.dtype)

ret,thresh = cv.threshold(img,127,255,0)
contours,hierarchy = cv.findContours(thresh,1,2)

cnt = contours[0]
M = cv.moments(cnt)

print("---------------------------------")
print(M)

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

print(cx)
print(cy)

print("---------------Contour Area------------------")

area = cv.contourArea(cnt)
print(area)

print("-----------------Contour Perimeter----------------")

perimeter = cv.arcLength(cnt,True)
print(perimeter)

print("---------------------------------")

perimeter = 0.1*perimeter
approx = cv.approxPolyDP(cnt,perimeter,True)
print(approx)

print("---------------------------------")

k = cv.isContourConvex(cnt)
print(k)


print("---------------------------------")


bgimg = cv.imread(imgPath)
x,y,w,h = cv.boundingRect(cnt)

print(x,y,w,h)
cv.rectangle(bgimg,(x,y),(x+w,y+h),(0,255,0),3)

print("---------------------------------")
bgimg2 = cv.imread(imgPath)
re = cv.minAreaRect(cnt)
box = cv.boxPoints(re)
box = np.int0(box)

bgimg2 = cv.drawContours(bgimg2,[box],0,(255,0,0),3)

titles = ['Original','Bounding','Bounding2','Lower_resoM']
imgs = [img,bgimg,bgimg2]



for i in range(len(imgs)):
    plt.subplot(2,3,i+1),plt.imshow(imgs[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
