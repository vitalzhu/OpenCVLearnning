import cv2 as cv

imgPath = '../Assets/Pictures/'
# img01 = cv.imread(imgPath+'airplane02.png')
# img02 = cv.imread(imgPath+'airplane.png')
# dst = cv.addWeighted(img01,0.1,img02,0.9,0)
#
# cv.imshow('dst',dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

# ------------------------------


img = cv.imread(imgPath+'blackboard.png')
img01 = cv.imread(imgPath+'logo.png')

rows,cols,channels = img01.shape
roi = img[0:rows,0:cols]

img01gray =  cv.cvtColor(img01,cv.COLOR_BGR2GRAY)
ret,mask = cv.threshold(img01gray,10,255,cv.THRESH_BINARY)
print(mask)
mask_inv = cv.bitwise_not(mask)
print(mask_inv)

img_bg = cv.bitwise_and(roi,roi,mask = mask_inv)

img01_fg = cv.bitwise_and(img01,img01,mask = mask)

dst = cv.add(img_bg,img01_fg)
img[0:rows,0:cols] = dst

cv.imshow('res',img)
cv.waitKey(0)
cv.destroyAllWindows()
