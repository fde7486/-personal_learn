import numpy as np
import cv2
import math

img1 = cv2.imread("building.jpg",-1)
img2 = img1.copy()
edges = cv2.Canny(img1,50,200)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 80, minLineLength=30, maxLineGap=10)

for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(img2,(x1,y1),(x2,y2),(0,0,255),1)

cv2.imshow("Original",img1)
cv2.imshow("Canny Edge Detection",edges)
cv2.imshow("Hough Line Detection",img2)
cv2.waitKey()