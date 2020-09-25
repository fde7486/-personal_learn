import numpy as np 
import cv2
img0 = cv2.imread("cat.jpg",-1)
img1 = cv2.resize(img0,(200,200))

img2 = cv2.resize(img1, (800,800),interpolation = cv2.INTER_NEAREST)
img3 = cv2.resize(img1, (800,800),interpolation = cv2.INTER_LINEAR)
img4 = cv2.resize(img1, (800,800),interpolation = cv2.INTER_CUBIC)
cv2.imshow("cat",img0)
cv2.imshow("NN",img2)
cv2.imshow("Linter",img3)
cv2.imshow("Cubic",img4)
cv2.waitKey()