import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgPath = '../Assets/Pictures/test.jpg'
img = cv.imread(imgPath,0)

edges = cv.Canny(img,200,200)

lower_reso = cv.pyrDown(img)

lower_resoM = lower_reso

for i in range(2):
    lower_resoM = cv.pyrDown(lower_resoM)


titles = ['Original','Edge Image','Lower_reso','Lower_resoM']
imgs = [img,edges,lower_reso,lower_resoM]



for i in range(len(imgs)):
    plt.subplot(2,2,i+1),plt.imshow(imgs[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
