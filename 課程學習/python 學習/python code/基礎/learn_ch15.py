# def division(x, y):
#     try:
#         return x/y
#     except ZeroDivisionError:
#         print("分母不能為0")
# print(division(10,5))
# print(division(5,0))

# fn = 'ch15_4.txt'               # 設定欲開啟的檔案
# try:
#     with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
#         data = file_Obj.read()  # 讀取檔案到變數data
# except FileNotFoundError:
#     print("找不到 %s 檔案" % fn)
# else:
#     print(data)         
# fn = 'ch15_5.txt'               # 設定欲開啟的檔案
# try:
#     with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
#         data = file_Obj.read()  # 讀取檔案到變數data
# except FileNotFoundError:
#     print("找不到 %s 檔案" % fn)
# else:
#     print(data)     


def e(n):
    r = 1
    for i in range(1,n):
        x = 1
        for j in range(1, i+1):
            x *= j
        r += 1/x
    return r
assert e(10) < 2.7