import numpy as np
import cv2
img = cv2.imread("001.png",-1)
cv2.imshow("img",img)
cv2.waitKey()

print(img.shape) #檢查資料的長,高,彩色OR黑白