import cv2
import numpy as np

def calcAndDrawHist(image, color):
    hist= cv2.calcHist([image], [0], None, [256], [0.0,255.0])
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
    histImg = np.zeros([256,256,3], np.uint8)
    hpt = int(0.9* 256)

    for h in range(256):
        intensity = int(hist[h]*hpt/maxVal)
        cv2.line(histImg,(h,256), (h,256-intensity), color)

    return histImg

img = cv2.imread("penguin.png",0)
eqimg = cv2.equalizeHist(img)

his = calcAndDrawHist(img,(255,255,255))
his2 = calcAndDrawHist(eqimg,(255,255,255))

cv2.imshow("img1",img)
cv2.imshow("img2",eqimg)
cv2.imshow("img3",his)
cv2.imshow("img4",his2)
cv2.waitKey()