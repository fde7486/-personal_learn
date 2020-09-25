import numpy as np
import cv2

img = cv2.imread("building.jpg",0)

AverageBlur = cv2.blur(img,(5,5))
GaussianBlur = cv2.GaussianBlur(img,(5,5),0)
MediumBlue = cv2.medianBlur(img,5)

cv2.imshow("01",img)
cv2.imshow("02",AverageBlur)
cv2.imshow("03",GaussianBlur)
cv2.imshow("04",MediumBlue)
cv2.waitKey()