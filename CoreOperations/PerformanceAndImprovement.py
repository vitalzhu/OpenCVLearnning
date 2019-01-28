import cv2 as cv

img = cv.imread('../Assets/Pictures/demo.jpg')

e1 = cv.getTickCount()

for i in range(5,49,2):
    img = cv.medianBlur(img,1)

e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()

print(t)

print(cv.useOptimized())
