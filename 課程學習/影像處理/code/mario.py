import numpy as np
import cv2
img = cv2.imread("mario.bmp",-1)
cv2.imshow("img",img)


img2 = np.zeros((img.shape[0]*2,img.shape[1]*2),dtype="uint8")
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img2[2*i,2*j] = img[i,j]
        img2[2*i+1,2*j] = img[i,j]
        img2[2*i,2*j+1] = img[i,j]
        img2[2*i+1,2*j+1] = img[i,j]
cv2.imshow("img2",img2)
cv2.waitKey()