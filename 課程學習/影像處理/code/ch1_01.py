# a = [[1, 2], [3, 4]]
# b = [[0, 4], [1, 1]]
# for i in range(len(a)):
#     c1 = 0
#     c2 = 0
#     for j in range(len(a[i])):
#         d1 = a[i][j] * b[j][i]
#         c1 += d1
#         d2 = a[j][i] * b[j][i]
#         c2 += d2
#     print(c1,c2)

# import numpy as np 
# a = np.floor(4.5)
# b = np.floor(-4.5)
# print(a+b)
# c = np.ceil(4.5)
# d = np.ceil(-4.5)
# print(c+d)
# e = np.arctan(1/7)
# f = np.arctan(3/79)
# print(20*e+8*f)
# x = 0
# for i in range(1,1001):
#     x += 1/(i**2)
# print(np.sqrt(6*x))

# import numpy as np 
# a = np.array([[1,2],[3,4]])
# b = np.array([[5,6],[7,8]])
# # print(a+b)
# # print(a-1)
# # print(a-b)
# # print(a*b)
# print(np.dot(a,b))
# print(np.matmul(a,b))

# import numpy as np 
# a = np.array([1,2,3,4,5,6,7,8,9,10])
# print(np.mean(a))
# print(np.std(a))
# print(np.max(a))
# print(a[a<4])

# import numpy as np 
# a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(np.mean(a))
# print(np.mean(a[0]))
# print(np.mean(a[1]))
# print(np.std(a))
# print(np.max(a))
# print(a[a>6])
# print(a.sum(axis=0))
# print(a.sum(axis=1))

# import numpy as np 
# import cv2
# img1 = np.zeros([512,512],dtype="uint8")
# img2 = np.ones([512,512],dtype="float32")
# cv2.imshow("test1",img1)
# cv2.imshow("test2",img2)
# cv2.waitKey()

# import numpy as np 
# import cv2
# img1 = np.ones([500,500],dtype="uint8")
# for i in range(5):
#     for j in range(5):
#         if i%2 == 1 and j%2 == 0:
#             for k in range(i*100,i*100+100):
#                 for l in range(j*100,j*100+100):
#                     img1[k][l] *=255
#         elif i%2 == 0 and j%2 == 1:
#             for k in range(i*100,i*100+100):
#                 for l in range(j*100,j*100+100):
#                     img1[k][l] *=255
# cv2.imshow("test1",img1)
# cv2.waitKey()


# import numpy as np 
# import cv2
# img1 = np.ones([500,500],dtype="float32")
# for x in range(1,500):   
#     y = int(x*2/3)    
#     if y >500:
#         break
#     img1[x][y] *= 0
# cv2.imshow("test1",img1)
# cv2.waitKey()



# import numpy as np
# import cv2
# def f(x,y):
#     c = np.sin(0.02*x+0.03)+np.sin(0.08*y+0.07)
#     return c
# img = np.ones([512,512],dtype="uint8")
# for x in range(1,512):
#     for y in range(1,512):
#         img[x][y] = f(x,y)
# cv2.imshow("test1",img)
# cv2.waitKey()


# import numpy as np
# import cv2
# empty = np.empty(10)
# print(empty)
# x = np.array([[1,2,3,4,5,6],[6,7,8,9,10,11]])
# print(x.reshape(3,4))
# print(x.T)
# print(x[0])
# print(x[1,2:5])

import numpy as np
import cv2
img = np.zeros([500,500],dtype="uint8")
for i in range(5):
    for j in range(5):
        if ((i+j) % 2 == 0):
            img[i*100:i*100+100,j*100:j*100+100] = 255
for x in range(1,500):   
    y = int((x**2)**(1/3))    
    if y >500:
        break
    if img[x][y] == 0:
        img[x][y] = 255
    elif img[x][y] == 255:
        img[x][y] = 0
cv2.imshow("test",img)
cv2.waitKey()