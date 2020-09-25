# b = (12,34,67) #tuple無法修改資料

# a = list(b)
# print(b,a)
# c = tuple(a)
# print(c)

# drinks = ["coffee", "tea", "wine"]
# enumerate_drinks = enumerate(drinks)                # 數值初始是0
# lst = list(enumerate_drinks)
# print("轉成串列輸出, 初始索引值是 0 = ", lst)
# print(type(lst[0]))

# a = (12,56,78,35)
# for i in enumerate(a):
#     print(i)

# fields = ['Name', 'Age', 'Hometown']
# info = ['Peter', '30', 'Chicago']
# zipData = zip(fields, info)         # 執行zip
# print(type(zipData))                # 列印zip資料類型
# player = list(zipData)              # 將zip資料轉成串列
# print(player)                       # 列印串列

# drinks = ["coffee", "tea", "wine"]
# enumerate_drinks = enumerate(drinks)                # 數值初始是0
# lst = list(enumerate_drinks)
# print("轉成串列輸出, 初始索引值是 0 = ", lst)
# print(type(lst[0]))

# Tuple 比較省
# li_grade = [11, 22, 99, 35, 59] # list
# tu_grade = (11, 22, 99, 35, 59) # tuple

# import sys
# print (sys.getsizeof(li_grade))
# print (sys.getsizeof(tu_grade))

# Tuple 比較快
# import timeit
# do_list = timeit.timeit(stmt = '[1,2,3,4,5]',
#                         number = 10000000)
# do_tupl = timeit.timeit(stmt = '(1,2,3,4,5)',
#                         number = 10000000)
# print(do_list)
# print(do_tupl)

sc = (45,68,93,56,82)
mean = sum(sc)/len(sc)
var = 0
for v in sc:
    var+=(v-mean)**2
var = var/(len(sc)-1)
dev = var**0.5
print("平均值:{0:2.2f},變異數:{1:2.4f},標準差:{2:2.4f}".format(mean,var,dev))