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

def parse_Taiwan_mobile_number_string(string):
    '''尋找字串中的電話號碼'''
    for i in range(len(string)):
        msg = string[i:i+12]
        if Taiwan_mobile_number(msg):
            print("台灣門號:{}".format(msg))
            return False
    return True

string1 = "你好，我是王老吳，我的電話號碼是0911-165-123"
string2 = "你好，我是王老吳，我明天要去逛夜市"
if parse_Taiwan_mobile_number_string(string1):
    print("內文中沒有電話號碼")
if parse_Taiwan_mobile_number_string(string2):
    print("內文中沒有電話號碼")