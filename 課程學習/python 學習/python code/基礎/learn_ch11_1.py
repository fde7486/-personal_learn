# def a():
#     print("123")
#     print("456")
#     print("789")
# for i in range(6):
#     a()
    
# def 加法運算(x1,x2):
#     result = x1+x2
#     return(result)
# a,b = eval(input("請輸入要相加的兩個數字"))
# x = 加法運算(a,b)
# print(x)
# def subtract(x1, x2):
#     """ 減法設計 """
#     result = x1 - x2
#     print(result)               # 輸出減法結果
# print("本程式會執行 a - b 的運算")     
# a = int(input("a = "))
# b = int(input("b = "))
# print("a - b = ", end="")       # 輸出a-b字串,接下來輸出不跳行
# subtract(a, b)
# def 除法運算(x1,x2):
#     if x2 == 0:
#         result = "分母不能為0"
#     else:
#         result = x1/x2
#     return(result)
# a,b = eval(input("請輸入要相除的兩個數字"))
# print(除法運算(a,b))


# def interest(interest_type, subject):
#     print("我的興趣是",interest_type)
#     print("在",interest_type,"中,最喜歡的是",subject)
# interest('旅遊','敦煌')
# interest("寫程式",'ptyhon')
# interest(interest_type = '旅遊', subject = '敦煌')  # 位置正確
# interest(subject = '敦煌', interest_type = '旅遊')  # 位置更動

# def greeting(name):
#     """Python函數需傳遞名字name"""
#     print("Hi, ", name, " Good Morning!")
# ret_value = greeting('Nelson')
# print("greeting( )傳回值 = ", ret_value)
# print(ret_value, " 的 type  = ", type(ret_value))
# def is_None(string, x):
#     if x is None:
#         print("%s = None" % string)
#     elif x:
#         print("%s = True" % string)
#     else:
#         print("%s = False" % string)

# is_None("空串列", [])                 # 空串列
# is_None("空元組", ())                 # 空元組
# is_None("空字典", {})                 # 空字典
# is_None("空集合", set())              # 空集合
# is_None("None  ", None)
# is_None("True  ", True)
# is_None("False ", False)

# def addition(x1,x2):
#     result = x1 + x2
#     return(result)
# def subtract(x1,x2):
#     result = x1 - x2
#     return(result)
# def multiplication(x1,x2):
#     result = x1 * x2
#     return(result)
# def division(x1,x2):
#     if x2 == 0:
#         result = "分母不能為0"
#     else:
#         result = x1/x2
#     return(result)
# print("請輸入你要做的運算")
# print("1.加法(a+b)")
# print("2.減法(a-b)")
# print("3.乘法(a*b)")
# print("4.除法(a/b)")
# op = int(input("輸入1/2/3/4:"))
# a = int(input("a="))
# b = int(input("b="))
# if op == 1:
#     print("{}+{}={}".format(a,b,addition(a,b)))
# elif op == 2:
#     print("{}-{}={}".format(a,b,subtract(a,b)))
# elif op == 3:
#     print("{}*{}={}".format(a,b,multiplication(a,b)))
# elif op == 4:
#     print("{}/{}={}".format(a,b,division(a,b)))
# else:
#     print("輸入錯誤")

# def bmi(weight,height):
#     result = weight/(height**2)
#     return(result)
# w, h = eval(input("請輸入體重(單位:KG),身高(單位:M):"))
# print("你的BMI值為{0:2.2f}".format(bmi(w,h)))
# bMI = bmi(w,h)
# if (bMI < 18.5):
#     print("體重過輕」，需要多運動，均衡飲食，以增加體能，維持健康！")
# elif(18.5<= bMI <24):
#     print("恭喜！「健康體重」，要繼續保持！")
# elif(24<= bMI <27):
#     print("哦！「體重過重」了，要小心囉， 趕快力行「健康體重管理」！")
# else :
#     print("啊～「肥胖」，需要立刻力行「健康體重管理」囉！")

# def guest_info(firstname, middlename, lastname, gender):
#     """ 整合客戶名字資料 """
#     if gender == "M":
#         welcome = lastname + middlename + firstname + '先生歡迎你'
#     else:
#         welcome = lastname + middlename + firstname + '小姐歡迎妳'
#     return welcome

# info1 = guest_info('煒', '達', '鄭', 'M')
# print(info1)

# def build_vip(id, name):
#     """ 建立VIP資訊 """
#     vip_dict = {'VIP_ID':id, 'Name':name}
#     return vip_dict
# member = build_vip('101', 'Nelson')
# print(member)
# def build_vip(id, name, tel = ''):
#     """ 建立VIP資訊 """
#     vip_dict = {'VIP_ID':id, 'Name':name}
#     if tel:
#         vip_dict['Tel'] = tel
#     return vip_dict
# member1 = build_vip('101', 'Nelson')
# member2 = build_vip('102', 'Henry', '0952222333')
# print(member1)
# print(member2)

# def build_vip(id, name, tel = ''):
#     vip_dict = {'vip':id, 'Name':name}
#     if tel:
#         vip_dict['tel'] = tel
#     return vip_dict
# while True:
#     print("建立VIP資訊系統")
#     idnum = input("請輸入ID: ")
#     name = input("請輸入姓名: ")    
#     tel = input("請輸入電話號碼: ")
#     member = build_vip(idnum, name, tel)
#     print(member,'\n')
#     repeat = input("是否繼續(y/n)? 輸入非y字元可結束系統: ")
#     if repeat != 'y':
#         break
# print("歡迎下次再使用")

def product_msg(customers):
    str1 = '親愛的: '
    str2 = '本公司將在2020年12月20日北京舉行產品發表會'
    str3 = '總經理:深石敬上'
    for customer in customers:
        msg = str1 + customer + '\n' + str2 + '\n' + str3
        print(msg, '\n')
name = open(file="name.txt",,mode="r", encoding='utf-8')