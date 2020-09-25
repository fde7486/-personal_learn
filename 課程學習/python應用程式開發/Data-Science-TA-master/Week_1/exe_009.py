import requests

url = 'http://www.fcu.edu.tw'  # 給定網址
htmlfile = requests.get(url)
try:
    htmlfile.raise_for_status()                 # 異常處理
    print("下載成功")
except Exception as err:                        # err ==> 系統自訂的錯誤訊息
    print("網頁下載失敗: %s" % err)
print("程式結束")