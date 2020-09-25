# ch5_3.py
import bs4

htmlFile = open('csc1.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
print("物件類型  = ", type(objSoup.title))
print("列印title = ", objSoup.title)











