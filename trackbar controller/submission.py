import cv2

# Create a window to display results
cv2.namedWindow("Resize Image", cv2.WINDOW_AUTOSIZE)
im = cv2.imread('truth.png')

# Callback functions
def scaleImage(*args):
    global scaleType
    global scaleFactor
    pos = cv2.getTrackbarPos('scale', 'Resize Image')
    if scaleType == 0:
        scaleFactor = 1 + pos/100
        x = cv2.resize(im, None, fx = scaleFactor, fy = scaleFactor)
    else:
        scaleFactor = 1 - pos/100
        if scaleFactor == 0:
            return
        x = cv2.resize(im, None, fx = scaleFactor, fy = scaleFactor)
    cv2.imshow('Resize Image', x)

# Callback functions
def scaleTypeImage(*args):
    global scaleType
    scaleType = args[0]

scaleType = 0
cv2.createTrackbar("scale", 'Resize Image', 1, 100, scaleImage)
cv2.createTrackbar("Type: \n 0: Scale up, \n 1: Scale down",'Resize Image', 0, 1, scaleTypeImage)

cv2.imshow("Resize Image", im)
c = cv2.waitKey(0)

cv2.destroyAllWindows()