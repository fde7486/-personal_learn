from bs4 import BeautifulSoup
import requests

html = requests.get("http://www.fcu.edu.tw/wSite/mp?mp=1")
# print(html.text)

bsObj = BeautifulSoup(html.content, "html.parser")
# print(bsObj)

images = bsObj.find_all("img")
for image in images:
    print(image['src'])