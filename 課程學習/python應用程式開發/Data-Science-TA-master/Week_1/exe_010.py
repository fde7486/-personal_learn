import requests

url = 'https://wiki.biligame.com/blhx/%E9%A6%96%E9%A1%B5'
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    print("取得網頁內容成功")
    print("網頁內容大小 = ", len(htmlfile.text))
else:
    print("取得網頁內容失敗")