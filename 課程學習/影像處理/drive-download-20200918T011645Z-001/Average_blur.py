import cv2
import numpy as np

img1 = cv2.imread("2020-09-19_09-29-49_031.jpg")
img2 = cv2.imread("penguin_noise.png")

ave1 = cv2.blur(img1,(3,3))
med1 = cv2.medianBlur(img1,3)
# ave2 = cv2.blur(img2,(3,3))
# med2 = cv2.medianBlur(img2,3)

cv2.imshow("img0", img1)
cv2.imshow("img1", ave1)
cv2.imshow("img2", med1)
# cv2.imshow("img3", ave2)
# cv2.imshow("img4", med2)
cv2.waitKey()