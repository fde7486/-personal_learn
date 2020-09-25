#  影像位子抓取


import cv2

global img 

def onMouse(event,x,y,flags,param):
    x,y = y,x
    if img.ndim != 3:
        print("(x,y)={},{}".format(x,y),end="  ")
        print("Gray-Level = {:3d}".format(img[x,y]))
    else:
        print("(x,y)={},{}".format(x,y),end="  ")
        print("R,G,B = ({},{},{})".format(img[x,y,2],img[x,y,1],img[x,y,0]))
        
img = cv2.imread("02.jpg",-1)
cv2.namedWindow("onMouse")
cv2.setMouseCallback("onMouse",onMouse)
cv2.imshow("onMouse",img)
cv2.waitKey()