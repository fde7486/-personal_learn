# 月份 = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
星期 = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
day = {
    "1":3, "2":6, "3月":0, "4":3,
    "5":5, "6":1, "7":3, "8":6,
    "9":2, "10":4, "11":0, "12":2}

m = input("請輸入月份")
if m in day :    
    if m == "1" or m == "3" or m == "5" or m == "7" or m == "8" or m == "10" or m == "12":
        d = int(input("請輸入幾號"))
        if d == 1:
            print("2020/{}/{} 是{}".format(m,d,星期[day[m]-1]))
        elif 1 < d < 32:
            t = (d-1+day[m])%7
            t -=1
            print("2020/{}/{} 是{}".format(m,d,星期[t]))
        else:
            print("輸入日期錯誤")
    elif m == "2":
        d = int(input("請輸入幾號"))
        if d == 1:
            print("2020/{}/{} 是{}".format(m,d,星期[day[m]-1]))
        elif 1 < d < 30:
            t = (d-1+day[m])%7
            t -=1
            print("2020/{}/{} 是{}".format(m,d,星期[t]))
        else:
            print("輸入日期錯誤")
    else:
        d = int(input("請輸入幾號"))
        if d == 1:
            print("2020/{}/{} 是{}".format(m,d,星期[day[m]-1]))
        elif 1 < d < 31:
            t = (d-1+day[m])%7
            t -=1
            print("2020/{}/{} 是{}".format(m,d,星期[t]))
        else:
            print("輸入日期錯誤")        
else:
    print("輸入月份錯誤")
