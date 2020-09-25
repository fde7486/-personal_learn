##设置一定的点击次数
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re

browser = webdriver.Firefox(executable_path="geckodriver.exe")

# 去豆瓣
browser.get('https://movie.douban.com/tag/#/?sort=T&range=0,10&tags=')

#瀏覽器解釋JS腳本是需要時間的，但實際上這個時間並不好確定，如果我們手動設定時間間隔的話，設置多了浪費時間，設置少了又會丟失數據
#implictly_wait函數則完美解決了這個問題，給他一個時間參數，它會只能等待，當js完全解釋完畢就會自動執行下一步。
browser.implicitly_wait(3)

#讓程式休息3毫秒
time.sleep(3)

#選擇勵志電影類型
browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/ul[4]/li[6]/span').click()


for i in range(5):
    #找到加载更多這個按鈕並按下去
    browser.find_element_by_link_text("加载更多").click()
    
    ###如果網頁沒有完全加載，會出現點擊錯誤，會點擊到某個電影頁面，所以加了一個睡眠時間。
    time.sleep(5)
    
    ##browswe.page_source是點擊5次後的源碼，用Beautiful Soup解析源碼
    soup = BeautifulSoup(browser.page_source, 'html.parser')

items = soup.find('div', class_=re.compile('list-wp'))
for item in items.find_all('a'):
    
    #將標題抓下來
    Title = item.find('span', class_='title').text
    
    #將評分抓下來
    Rate = item.find('span', class_='rate').text
    print(Title,Rate)

#關閉瀏覽器
browser.close()