import random

def phone_number(number):
    
    phone_list = []
    for i in range(number):
        phone = ""
        for j in range(12):
            if j == 4 or j == 8:
                phone += '-'
            else:
                phone += str(chr(random.randint(0,9)))
        phone_list.append(phone)
    return phone_list

def Taiwan_mobile_number(string):       
    if len(string) != 12:
        return False
    # 電話號碼格式 string = "XXXX-XXX-XXX"    
    for i, s in enumerate(string):        
        if i == 4 or i == 8:
            if s != '-': # 如果第5個字和第9個字不是"-"
                return False 
        else:
            if not s.isdecimal(): # 如果 s不是數字(0~9)
                return False        
    return True

phone_number_list = phone_number(5)
for i in range(len(phone_number_list)):
    n = Taiwan_mobile_number(phone_number_list[i])
    print(phone_number_list[i],n)
    