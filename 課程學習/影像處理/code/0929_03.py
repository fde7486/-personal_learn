import numpy as np
import cv2
import math

img1 = cv2.imread("building.jpg",-1)
img2 = img1.copy()
gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=5,maxRadius=20)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(img2,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(img2,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow("Original",img1)
cv2.imshow("circle",img2)
cv2.waitKey()