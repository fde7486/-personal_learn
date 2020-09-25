# 選取想要的圖片位子並輸出

import numpy as np
import cv2


img = cv2.imread("001.png",-1)
cv2.imshow("img",img)
img2 = img[25:70,80:135]
cv2.imshow("img2",img2)
img3 = cv2.resize(img2,(130, 110))
cv2.imshow("img3",img3)
cv2.waitKey()
