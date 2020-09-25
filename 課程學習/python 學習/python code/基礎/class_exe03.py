# a = list(input("請輸入數字(用空白隔開):").split(' '))
# a.reverse()
# b = ' '
# print(b.join(a))

# def build_vip(id, name, tel = ''):
#     """ 建立VIP資訊 """
#     vip_dict = {'VIP_ID':id, 'Name':name}
#     if tel:
#         vip_dict['Tel'] = tel
#     return vip_dict

# while True:
#     print("建立VIP資訊系統")
#     idnum = input("請輸入ID: ")
#     name = input("請輸入姓名: ")    
#     tel = input("請輸入電話號碼: ")        # 如果直接按Enter可不建立此欄位
#     member = build_vip(idnum, name, tel)   # 建立字典
#     print(member, '\n')
#     repeat = input("是否繼續(y/n)? 輸入非y字元可結束系統: ")
#     if repeat != 'y':
#         break

# print("歡迎下次再使用")

def comp(x, y):
   x = x - 1
   return (x, y) 

p, q = 10, 10
comp(p, q)

print(p, q)