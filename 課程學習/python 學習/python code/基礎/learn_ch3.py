
#  x= 106
#  print(chr(x))  #印出輸入述職的字元
'''
x="鄭"
print(x)   
print(ord(x))  #輸出字元X的Unicode(10進位)碼值
print(hex(ord(x)))  #輸出字元'鄭'的Unicode(16進位)碼值
'''

'''
for i in range(254):
    print(chr(i),end=" ")  # 取消換行(end=" ")  
'''
"""
for i in range(ord('一'), ord("一")+20):
    print(chr(i),end="")          #chr(number): 印出 number 的字碼; chr: character (字元)
    print(chr(i) +str(i),end="")   #ord(c): 印出 c 的 unicode
    print(chr(i).encode('utf-8'))  #.encode(‘utf-8’): 用 utf-8 編碼
"""
'''
dist=384400
seep=1225
total_hours=dist//seep
days,hours=divmod(total_hours,24)
print("耗時",days,"天")
print("耗時",hours,"時")
'''

# x1,y1=(1,8)
# x2,y2=(3,10)
# dist=((x1-x2)**2+(y1-y2)**2)**0.5
# print(dist)


# x1,y1=eval(input('請輸入第一點的座標(用，分隔)'))
# z=x+y
# print(z)

x1=int(input('請輸入座標x1:'))
y1=int(input('請輸入座標y1:'))
x2=int(input('請輸入座標x2:'))
y2=int(input('請輸入座標y2:'))
dist=((x1-x2)**2+(y1-y2)**2)**0.5
#dist=round(dist,3) 
#print("兩點間的距離",round(dist,3)) #rond(X,n) 將幅點數取道小數第n位
print("({},{})和({},{})的距離是{}".format(x1,y1,x2,y2,dist))

