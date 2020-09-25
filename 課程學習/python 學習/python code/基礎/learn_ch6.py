# math = [5,6,3,8,2,0,9,1,7]
# print(math[2:5])

# grades = [0]*12
# import random as r
# for i in range(12):  
#     grades[i]=r.randint(0,100) #產生亂數
# print(grades)
# grades.sort()  #將list裡的由小到大資料排序
# print(grades)
# print(grades[0:4])
# # print(grades[0:11:3])
# print(max(grades))
# print(min(grades))
# print(sum(grades))

# james = [23, 19, 22, 31, 18]        # 定義james的5場比賽得分
# print("舊的James比賽分數", james)
# james[4] = 28
# print("新的James比賽分數", james)

# math=[23,56,34,67,2,57,97,65,45,5,23,55,98,533]
# math.sort()
# print(math)
# del math[2]
# print(math)
# del math[3:5]
# print(math)
# math*=3
# print(math)

# uni = '  feng chia uni     '
# print(uni.lstrip())
# print(uni.rstrip())
# print(uni.upper())

# ans = input("請問你喜歡籃球嗎(yes or no)?")
# ans = ans.strip().lower()
# answer = ['yes','y']
# if ans in answer:
#     print("歡迎來到籃球世界")
# else :
#     print("去找到你的興趣")

# a = [12,23]
# a.append(34) #在串列末端增加元素 append(
# print(a)
# a.append([45,56])  # 串列B將接在串列A末端
# print(a)
# a.extend([67,78]) #串列B將分解成元素插入串列A末端
# print(a)
# a.insert(0,100) #insert(索引, 元素內容) # 索引是插入位置，元素內容是插入內容
# print(a)
# a.pop() #沒有索引是刪除串列末端元素
# print(a) 
# a.pop(0) #是刪除指定索引值i位置的串列元素
# print(a)


# with open("score2.txt",mode="r",encoding="utf-8") as file:
#     st =[]
#     aline = file.readline().split(' ')
#     st.append(aline)
#     aline = file.readline().split(' ')
#     st.append(aline)
#     aline = file.readline().split(' ')
#     st.append(aline)
# st[0][1] = int(st[0][1])
# st[0][2] = int(st[0][2])
# st[0][3] = int(st[0][3])
# st[1][1] = int(st[1][1])
# st[1][2] = int(st[1][2])
# st[1][3] = int(st[1][3])
# st[2][1] = int(st[2][1])
# st[2][2] = int(st[2][2])
# st[2][3] = int(st[2][3])
# print(st)

# love = 'go go go'
# x = love.split(' ')
# print(x)

learn = 'learn ch5'
x = list(learn)
y = x[:]
for i in range(len(x)):
    y[i] = chr(ord(x[i])+5)
y = ''.join(y)
print(y)