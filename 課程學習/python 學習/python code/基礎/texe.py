#CH2練習 2
# 本金=int(input("請輸入本金"))
# 年=int(input("請問要存幾年"))
# 年利率=0.0085
# 利息=本金*年利率*年
# print("您的本金為{0},存了{1}年,這{2}年的利息為{3:1.2f}".format(本金,年,年,利息))

#ch2練習 4
# apple = 100
# student = 23
# day_enough = apple//student
# day_insufficient = day_enough+1
# insufficient = student-apple%student
# print("可以吃{}天,在第{}天會不足,缺少{}顆".format(day_enough,day_insufficient,insufficient))

# x = int(input("請輸入第一個數字:"))
# y = int(input("請輸入第二個數字:"))

# while (x > 0 and y > 0):
#     if (x > y):
#         x = x%y
#     else :
#         y = y%x
# if (x == 0):
#     print("最大公因數為:{}".format(str(y)))
# else :
#     print("最大公因數為:{}".format(str(x)))

# m, n = eval(input("請輸入m, n兩個整數(m>n):"))
# sum1 = 0
# for i in range(n,m+1):
#     sum1 +=i
# print(sum1)

e = 1
factorial=1
for i in range(1,4):
    factorial*=(i+1)
    print(factorial)
