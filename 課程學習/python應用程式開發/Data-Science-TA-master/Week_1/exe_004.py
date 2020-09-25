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

def Japan_mobile_number(string):
    '''輸入一個字串進行比對，找出符合日本電話號碼的格式'''    
    if len(string) != 13:
        return False
    # 電話號碼格式 string = "XXX-XXXX-XXXX"    
    for i, s in enumerate(string):
        
        if i == 3 or i == 8:
            if s != '-': # 如果第4個字和第9個字不是"-"
                return False 
        else:
            if not s.isdecimal(): # 如果 s不是數字(0~9)
                return False        
    return True

def parse_Japan_mobile_number_string(string):
    '''尋找字串中的電話號碼'''
    for i in range(len(string)):
        msg = string[i:i+13]
        if Japan_mobile_number(msg):
            print("日本門號:{}".format(msg))
            return False
    return True



strings = ["你好，我是王三，我日本的門號是080-1968-3552，台灣門號為0912-145-856",\
           "你好，我是王老吳，我的電話號碼是0911-165-123",\
           "你好，我是王老吳，我的電話號碼是080-1919-3555", \
           "你好，我是王老吳，我明天要去逛夜市"]

for i, string in enumerate(strings):
    taiwan = parse_Taiwan_mobile_number_string(string)
    japan = parse_Japan_mobile_number_string(string)
        
    if taiwan and japan:
        print("{} : 沒有日本或台灣門號".format(string))