# 將圖片分成紅藍綠三色

import numpy as np
import cv2
img = cv2.imread("001.png",-1)
cv2.imshow("img",img)
cv2.waitKey()

cv2.imshow("img_B1",img[:,:,0])  #單層圖層  只會顯示灰階
cv2.imshow("img_G1",img[:,:,1])
cv2.imshow("img_R1",img[:,:,2])
cv2.waitKey()

img_2 = np.zeros([225,225,3],dtype="uint8") #宣告一個空白矩陣 
img_2[:,:,0] = img[:,:,0]  #更改其圖層
img_3 = np.zeros([225,225,3],dtype="uint8")
img_3[:,:,1] = img[:,:,1]
img_4 = np.zeros([225,225,3],dtype="uint8")
img_4[:,:,2] = img[:,:,2]
cv2.imshow("img_B",img_2)  #顯示藍色
cv2.imshow("img_G",img_3)
cv2.imshow("img_R",img_4)
cv2.waitKey()