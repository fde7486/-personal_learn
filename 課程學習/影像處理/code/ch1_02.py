"""
import numpy as np
a = np.array([[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14]])
print(a[1])
print(a[1:])
print(a[1,2:])
print(a[:2,2:])
print(a[:,2:4])
"""


'''
import numpy as np
import cv2
y = np.zeros([500,500],dtype="uint8")
for i in range(5):
    for j in range(5):
        if ((i+j) % 2 == 0):
            y[i*100:i*100+100,j*100:j*100+100] = 255
cv2.imshow("test",y)
# cv2.waitKey()
z = y.reshape(100,2500)
cv2.imshow("test_reshape",z)
# cv2.waitKey()
cv2.imshow("test_resize",cv2.resize(y,(500,100)))
cv2.imshow("test_resize_2",cv2.resize(y,(100,100)))
cv2.waitKey()
'''


# import numpy as np
# a = np.random.randint(1,100,20)
# print(a)
# a.sort()
# print(a)
# print(np.unique(a))
# b = np.array([[2,1,-1,3,0],[4,2,3,4,1]])
# print(b)
# b.sort()
# print(b)
# print(np.unique(b))


# import numpy as np
# import cv2
# img = np.zeros([500,500,3],dtype="uint8") #np.zeros([a,b,c] a,b 圖片範圍, c 維度 )
# cv2.rectangle(img,(100,100),(200,200),(255,255,255),-1)
# cv2.imshow("01",img)
# cv2.waitKey()

# cv2.rectangle(img,(100,200),(300,400),(255,0,0),-1)
# cv2.imshow("02",img)
# cv2.waitKey()


# import numpy as np
# import cv2
# img = np.zeros([500,500],dtype="uint8")
# for i in range(5):
#     for j in range(5):
#         if ((i+j) % 2 == 0):
#             cv2.rectangle(img,(i*100,j*100),(i*100+100,j*100+100),(255,255,255),-1)
# cv2.imshow("test",img)
# cv2.waitKey()

import numpy as np
import cv2
img = np.zeros([100,100,3],dtype="uint8")
a = np.array([80,97,89,65,90])
b = np.array([50,77,100,91,20])
c = np.array([78,60,56,75,79])
z = [a, b, c]
z_mean = []
z_std = []
color = [(0,0,255),(0,255,0),(255,0,0)]
for i in range(len(z)):
    z_mean.append(int(np.mean(z[i])))
    z_std.append(int(np.std(z[i])))
print(z_mean,z_std)

for i in range(len(z)):
    cv2.rectangle(img, (i*20, 100-z_mean[i]),(i*20+10, 100),color[(i%3)],-1)
    cv2.rectangle(img, (i*20+4,(100-z_mean[i]-int(z_std[i]/2))),(i*20+6,100-z_mean[i]+int(z_std[i]/2)),(255,255,255),-1)

cv2.imshow("test",img)
cv2.waitKey()


# a_sum = 100 - int(np.mean(a))
# a_std = int(np.std(a))
# b_sum = 100 - int(np.mean(b))
# b_std = int(np.std(b))
# c_sum = 100 - int(np.mean(c))
# c_std = int(np.std(c))
# cv2.rectangle(img,(20,a_sum),(30,100),(0,0,255),-1)
# cv2.rectangle(img,(24,(a_sum- a_std)),(26,a_sum + a_std),(255,255,255),-1)
# cv2.rectangle(img,(40,b_sum),(50,100),(0,255,0),-1)
# cv2.rectangle(img,(44,b_sum- b_std),(46,b_sum + b_std),(255,255,255),-1)
# cv2.rectangle(img,(60,c_sum),(70,100),(255,0,0),-1)
# cv2.rectangle(img,(64,c_sum- c_std),(66,c_sum + c_std),(255,255,255),-1)
# cv2.imshow("test",img)
# cv2.waitKey()
