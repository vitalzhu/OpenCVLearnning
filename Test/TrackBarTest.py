import cv2 as cv

cv.namedWindow('Image')

value = None

def trackUpdate(x):
    global value
    value = x
    print('Update Value,value = {}'.format(value))


cv.createTrackbar('TrackBar','Image',126,255,trackUpdate)
cv.setTrackbarPos('TrackBar','Image',100)

cv.waitKey(0)

cv.destroyAllWindows()
