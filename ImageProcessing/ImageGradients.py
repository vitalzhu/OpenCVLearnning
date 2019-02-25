import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgPath = '../Assets/Pictures/test.jpg'
img = cv.imread(imgPath,0)

laplacian = cv.Laplacian(img,cv.CV_64F)
sobelX = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
sobelY = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)

titles = ['Original','Laplacian','Sobel X','Sobel Y']
imgs = [img,laplacian,sobelX,sobelY]



for i in range(len(imgs)):
    plt.subplot(2,2,i+1),plt.imshow(imgs[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
