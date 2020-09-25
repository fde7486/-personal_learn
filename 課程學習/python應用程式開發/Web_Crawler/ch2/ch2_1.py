# ch2_1.py
import csv

fn = '臺中市百大名攤名產_1.csv'
with open(fn,encoding="utf-8") as csvFile:               # 開啟csv檔案
    csvReader = csv.reader(csvFile)     # 讀檔案建立Reader物件
    listReport = list(csvReader)        # 將資料轉成串列    
print(listReport)                       # 列印串列方法



