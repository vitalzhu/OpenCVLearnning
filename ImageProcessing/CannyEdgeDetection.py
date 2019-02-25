import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgPath = '../Assets/Pictures/test.jpg'
img = cv.imread(imgPath,0)

edges = cv.Canny(img,200,200)


titles = ['Original','Edge Image']
imgs = [img,edges]



for i in range(len(imgs)):
    plt.subplot(2,2,i+1),plt.imshow(imgs[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
