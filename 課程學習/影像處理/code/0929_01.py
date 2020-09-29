# 邊緣偵測 一維處理

import numpy as np 
import cv2

def img_do(img):
    sobel_x1 = cv2.Sobel(img,cv2.CV_16S,0,1)
    sobel_x1 = cv2.convertScaleAbs(sobel_x1)
    sobel_x2 = cv2.Sobel(img,-1,1,0)
    return [sobel_x1,sobel_x2]

img1 = cv2.imread("building.jpg")
img2 = cv2.imread("face.jpg")
img3 = cv2.imread("cat.jpg")
AverageBlur = cv2.blur(img1,(5,5))
cv2.imshow("original",img1)
cv2.imshow("cv_16s",img_do(img1)[0])
cv2.imshow("cv_8u",img_do(img1)[1])
# cv2.imshow("original_1",AverageBlur)
# cv2.imshow("cv_16s_1",img_do(AverageBlur)[0])
# cv2.imshow("cv_8u_1",img_do(AverageBlur)[1])
cv2.waitKey()
