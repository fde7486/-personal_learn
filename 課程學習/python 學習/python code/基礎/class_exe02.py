
p = '妙蛙種子 妙蛙草 妙蛙花 小火龍'.split()
j = 'フシギダネ フシギソウ フシギバナ ヒトカゲ'.split()
pro = '草 草 毒 火'.split()
tall = (20, 50, 10, 70)

x = tuple(zip(j, pro, tall))
pokamo = dict(zip(p, x))
print(pokamo)
pokamo_tall = sorted(list(pokamo.values()),key=lambda x:x[2],reverse = True)
print(pokamo_tall)


# import csv

# fn = 'csvReport.csv'
# with open(fn) as csvFile:               # 開啟csv檔案
#     csvReader = csv.reader(csvFile)     # 讀檔案建立Reader物件
#     listReport = list(csvReader)        # 將資料轉成串列    

# title = listReport[0]
# listReport = listReport[1:]

# for i in range(0, len(listReport)):
#     listReport[i][3] = int(listReport[i][3])
#     listReport[i][4] = int(listReport[i][4])
#     listReport[i][5] = int(listReport[i][5])
#     for j in range(len(title)):        
#        print ("{}: {}".format(title[j], listReport[i][j]), end=', ')
#     print ()   

# listReport.sort(key = lambda x: x[-2])

# print(listReport)  

# import csv
# fn = 'movie_evaluatein.csv'
# with open(fn) as csvFile:               # 開啟csv檔案
#     csvReader = csv.reader(csvFile)     # 讀檔案建立Reader物件
#     movies = list(csvReader)        # 將資料轉成串列    
# print(movies)
# p = movies[0][1:]
# movies = movies[1:]

# like = {}
# for i in range(len(p)):
#     v = []
#     for m in movies:
#         v.append(int(m[i+1]))
#     print (v)    
#     like[p[i]] = tuple(v)

# def dist(a, b):
#     # print (like[a], like(b))
#     leng = len(like[a])
#     t = 0
#     for i in range (leng):
#         t += (like[a][i]-like[b][i])**2
#     return t**0.5    
        
# a = 'a'
# b = 'b'
# c = 'c'
# d = 'd'
# print (dist(a, b))    
# print (dist(a, d))    
# print (dist(c, d))    
# print (dist(a, c))

# def likeme(people, like, x):
#     closest = 100
#     for y in people:
#         if (y == x):
#             continue
#         d = dist(x, y)
#         if d < closest:
#             closest = d
#             r = y
#     return (r)        


# print (likeme(p, like, a))
# print (likeme(p, like, b))
# print (likeme(p, like, c))
# print (likeme(p, like, d))