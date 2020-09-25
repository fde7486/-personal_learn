import numpy as np
import cv2

a = []
for k in range(18):
    img = cv2.imread("PDFtoImage\page_" + str(k) +".png",-1)
    for i in range(3):
        for j in range(3):
            img1 = img[i*750+90:i*750+750,j*520+70:j*520+540]
            a.append(img1)
for i in range(len(a)):
    cv2.imwrite( 'img_' + str(i)+".bmp",a[i])
# img1_1 = img1[90:800,70:540]
# img1_2 = img1[840:1550,70:540]
# img1_3 = img1[90:800,590:]
# cv2.imshow("Cubic",img1_1-2)
# cv2.waitKey()