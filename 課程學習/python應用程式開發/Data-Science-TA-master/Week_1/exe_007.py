import re # 載入正規表達式

msgs = ["請打給我的秘書，0930-111-532 or 0955-103-221",
        "明天要去吃大餐",
        "明天吃大餐以前請先打給我，0911-532-532"]

def parser_findall_string(string):
    phone_relu = re.compile(r"\d{4}-\d{3}-\d{3}")# 正規表達規則
    phone_number = phone_relu.findall(string)
    print(phone_number)

for msg in msgs:
    parser_findall_string(msg)