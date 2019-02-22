import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgPath = '../Assets/Pictures/j.png'
img = cv.imread(imgPath)


crows = 5
kernel = np.ones((crows,crows),np.uint8)
erosion = cv.erode(img,kernel,iterations=1)

dilation = cv.dilate(img,kernel,iterations=1)

imgPath = '../Assets/Pictures/opening.png'
openingImg = cv.imread(imgPath)

opening = cv.morphologyEx(openingImg,cv.MORPH_OPEN,kernel)
openinged = cv.dilate(cv.erode(openingImg,kernel,iterations=1),kernel,iterations=1)

gradient = cv.morphologyEx(img,cv.MORPH_GRADIENT,kernel)

tophat = cv.morphologyEx(img,cv.MORPH_TOPHAT,kernel)

blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

titles = ['Original','Erosion','Dilation','OpeningImg','Opening','Openinged','Gradient','Tophat','Blackhat']
imgs = [img,erosion,dilation,openingImg,opening,openinged,gradient,tophat,blackhat]



for i in range(len(imgs)):
    plt.subplot(3,3,i+1),plt.imshow(imgs[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
