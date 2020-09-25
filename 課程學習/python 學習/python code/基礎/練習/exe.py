# r = 0.0
# x = int(input("請輸入數字"))
# for i in range(x+1):
#     r += (-1)**i/(2*i+1)
    
#     print(4*r)
# print(4*r)

# name = "Python 王者歸來"
# print(len(name))
# nameBytes = name.encode('utf-8')
# print(len(nameBytes))
# print(nameBytes)

# x = int(input("請輸入一個整數"))
# ans = (x//10)*10
# print(ans)

# x1, x2, x3 = eval(input("請輸入三個不同的整數"))
# if x1 > x2:
#     if x1 > x3:
#         if x2 > x3:
#             print(x1, x2, x3)
#         else:
#             print(x1, x3, x2)
#     else:
#         print(x3, x1, x2)
# else:
#     if x1 > x3:
#        print(x2, x1, x3)
#     else:
#         if x2 > x3:
#             print(x2, x3, x1)
#         else:
#             print(x3, x2, x1)

# fields = ['Name', 'Age', 'Hometown']
# info = ['Peter', '30', 'Chicago']
# zipData = zip(fields, info)         # 執行zip
# print(zipData)                # 列印zip資料類型
# player = list(zipData)              # 將zip資料轉成串列
# print(player)          

fruits = {'Apple':20, 'Orange':25}
ret_value = fruits.setdefault('Orange')
print("Value = ", ret_value)
print("fruits字典", fruits)
ret_value = fruits.setdefault('Orange',100)
print("Value = ", ret_value)
print("fruits字典", fruits)