# x = range(10)
# print(x)

# total = 0
# for i in range(1,11):
#     total +=i
#     print(i, total)

# x='*'
# for i in range(1,6):
#      print(i*x)
# for i in range(5,0,-1):
#     print(i*x)

# names = ['james', 'nick', 'jonathan']
# eng = [12,23,90]
# math = [100,99,98]
# phy = [54,66,88]
# for i in range(len(names)):
#     n,e,m,p = names[i],eng[i],math[i],phy[i]
#     av = round((e+m+p)/3,2)
#     print("{}:{},{},{},平均={}".format(n,e,m,p,av))
# eng_av = round(sum(eng)/len(eng),2)
# math_av = round(sum(math)/len(math),2)
# phy_av = round(sum(phy)/len(phy),2)
# print ('Eng average:',eng_av)
# print ('math average:',math_av)
# print ('phy average:',phy_av)
# subject = 'eng math phy'.split(' ')
# g =[eng, math, phy]
# for i in range(len(subject)):
#     sub, av = subject[i], round(sum(g[i])/len(g[i]),2)
#     print ('{} average: {}'.format(sub.title(), av))

# c = [30, 32, 35, 45, 73, 72]
# f = []
# fno = []
# for i in c:
#     fi=i*9/5+32
#     if fi > 100:
#         f.append(fi)
#     else :
#         fno.append(fi)
# print(f, fno)
# c = [30, 32, 35, 45, 73, 72]
# f = {f*9/5+32 for f in c  if f*9/5+32 >100}
# print(f)

# for i in range(1,10):
#     for j in range(1,10):
#         s = "{}*{} = {}".format(i,j,i*j)
#         print(s)

# fruits1 = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
# fruits2 = ['香蕉', '芭樂', '西瓜']
# print("目前fruita2串列:",fruits2)
# for fruit in fruits2[:]:
#     if fruit in fruits1:
#         fruits2.remove(fruit)
#         print("刪除{}".format(fruit))
# print("最後fruits2串列", fruits2)

# p = "34,6,73,34,65,7,54,9,64".split(",")
# a = "a b c d".split()
# pa = [[x,y]  for x in p for y in a]
# print(pa,len(pa))

# for i in range(0,11):
#     if i == 5:
#         print("結束")
#         break
#     print(i)
# for i in range(0,11):
#     if i == 5:
#         print("?")
#         continue
#     print(i)

# num = int(input("請輸入大於一的整數"))
# if num == 2:
#     print("{}是質數".format(num))
# else:
#     for n in range(2, num):
#         if num%n == 0:
#             print("{}不是質數".format(num))
#             break
#     else :
#         print("{}是質數".format(num)

# score = []
# g = int(input("請輸入成績"))
# t = 0
# while (g>0):
#     t+=g
#     score.append(g)
#     g = int(input("請輸入成績"))
# average = t/len(score)
# print(score,t,average,len(score))

# money = int(input("請輸入學費:"))
# year = 0
# if (money<0):
#     print("學費不為負")
# else:
#     while (money<60000):
#         money = int(money*(1+0.05))
#         year+=1
# print("經過{}年後,學費會大於等於60000,學費是{}".format(year,money))

# c = [30, 32, 35, 38]
# city = ["台北","新北","台中","高雄"]
# cf = []
# for c,i in enumerate(c):
#     f = i*9/5+32
#     print(city[c],f)   
#     cf.append([city[c],f])
# print(cf)

# sc = [[1, '洪錦魁', 80, 95, 88, 0, 0, 0],
#       [2, '洪冰儒', 98, 97, 96, 0, 0, 0],
#       [3, '洪雨星', 91, 93, 95, 0, 0, 0],
#       [4, '洪冰雨', 92, 94, 90, 0, 0, 0],
#       [5, '洪星宇', 92, 97, 80, 0, 0, 0],
#      ]
# import random as r
# for st in sc:
#     st[2] = r.randint(20,80)
#     st[3] = r.randint(30,90)
#     st[4] = r.randint(40,100)
#     st[5] = st[2]+st[3]+st[4]
#     st[6] = round(st[5]/3,1)
# print(sc)
# sc.sort(key=lambda sc:sc[5],reverse=True)
# for st in sc:
#     st[-1] = sc.index(st)+1
# print(st)

# import random as x
# x = x.randint(1,100)
# your_ans = int(input("請輸入你猜的數字:"))
# index = 1
# while your_ans != x :
#     index+=1
#     if your_ans < x:
#         your_ans = int(input("猜大一點:"))
#     elif your_ans > x:
#         your_ans = int(input("猜小一點:"))
    
# print("答對了,猜了{}次".format(index))

# import random as x
# x = x.randint(1,100)

import random as x
x = x.randint(1,100)
your_ans = int(input("請輸入你猜的數字:"))
index = 1
ans = [your_ans]
while (your_ans != x and index <= 4):
    if your_ans < x:
        your_ans = int(input("猜大一點:"))
    else:
        your_ans = int(input("猜小一點:"))
    index+=1
    ans.append(your_ans)
if your_ans == x:
    print("答對了,猜了{}次,你猜的過程為{}".format(index,ans))
else:
    print("答錯了,答案是{},你猜的過程為{}".format(x,ans))    