import numpy as np
import cv2

def f(img):
    img_list = []
    img_w_d = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for i in range(len(img_w_d[:,0])):
        for j in range(len(img_w_d[0,:])):
            if img_w_d[i][j] == 0 :
                img_list.append([i,j])
    return img_w_d,img_list

face_cascade = cv2.CascadeClassifier('C:\opencv\opencv\data\haarcascades\haarcascade_frontalface_default.xml')

img1 = cv2.imread("image.jpg",-1)
effect = cv2.imread("effect.jpg",-1)

effect_w_d,effect_list = f(effect)
effect_x1 ,effect_y1 = effect_list[0]
effect_x2 ,effect_y2 = effect_list[-1]

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    ew = round(w / (effect_x2 - effect_x1),2)
    eh = round(h / (effect_y2 - effect_y1),2)


effect_resize = cv2.resize(effect, (0,0), fx = ew, fy = eh)
effect_resize_w_d,effect_resize_list = f(effect_resize)
effect_resize_x1, effect_resize_y1 = effect_resize_list[0]
for i in range(len(effect_resize[:,0])):
    for j in range(len(effect_resize[0,:])):
        if x - effect_resize_x1 + i < 0 or y - effect_resize_y1 + j < 0:
            continue
        elif effect_resize_w_d[i][j] > 220 or effect_resize_w_d[i][j] < 20:
            continue
        else:
            img1[y - effect_resize_x1 + i][x - effect_resize_y1 + j] = effect_resize[i][j]

cv2.imshow('img',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
