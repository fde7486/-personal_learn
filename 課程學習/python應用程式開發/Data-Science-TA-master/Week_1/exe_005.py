import re # 載入正規表達式

msgs = ["請打給我的秘書，0930-111-532 or 0955-103-221",
        "明天要去吃大餐",
        "明天吃大餐以前請先打給我，0911-532-532"]

def parser_string(string):
    phone_relu = re.compile(r"\d\d\d\d-\d\d\d-\d\d\d")# 正規表達規則
    phone_number = phone_relu.search(string)
    if phone_number != None:
        print("not Group:{}".format(phone_number))
        print("電話號碼:{}".format(phone_number.group()))
    else:
        print("沒有包含電話號碼")

for msg in msgs:
    parser_string(msg)