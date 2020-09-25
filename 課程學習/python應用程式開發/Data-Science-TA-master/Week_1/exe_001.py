def Taiwan_mobile_number(string):
    '''輸入一個字串進行比對，找出符合台灣電話號碼的格式'''
    
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
    
print(Taiwan_mobile_number("0912-333-601"))
print(Taiwan_mobile_number("xk3-454-45c"))