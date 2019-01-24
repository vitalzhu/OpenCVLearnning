import cv2 as cv
import numpy as np

def nothing(x):
    pass

img_name = "image"
img = np.zeros((300,512,3),np.uint8)
cv.namedWindow(img_name)

cv.createTrackbar('R',img_name,0,255,nothing)
cv.createTrackbar('G',img_name,0,255,nothing)
cv.createTrackbar('B',img_name,0,255,nothing)

switch = '0 : OFF \n 1 : ON'
cv.createTrackbar(switch,img_name,0,1,nothing)

while(1):
    cv.imshow(img_name,img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    r = cv.getTrackbarPos('R',img_name)
    g = cv.getTrackbarPos('G',img_name)
    b = cv.getTrackbarPos('B',img_name)
    s = cv.getTrackbarPos(switch,img_name)

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]


cv.destroyAllWindows()
