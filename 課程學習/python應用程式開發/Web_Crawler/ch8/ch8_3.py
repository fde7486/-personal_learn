# ch8_3.py
import requests, bs4
import time

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
ptthtml = requests.get(url, cookies={'over18':'1'})
objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')

articles = []                                           # 本頁面文章
pttdivs = objSoup.find_all('div', 'r-ent')
t = time.localtime(time.time())
for p in pttdivs:
    if p.find('a'):
        title = p.find('a').text
        author = p.find('div', 'author').text
        href = p.find('a')['href']
        f = open('{}_{}_{}_{}.json'.format(t.tm_mon,t.tm_mday,t.tm_hour,t.tm_min),'a',encoding="utf-8")
        f.write('title : {}\n'.format(title))
        f.close()
        f = open("928.txt",'a',encoding="utf-8")
        f.write('author : {}\n'.format(author))
        f.close()
        f = open("928.txt",'a',encoding="utf-8")
        f.write('href : {}\n'.format(href))
        f.close()
        articles.append({'title':title,                 # 文章標題
                         'author':author,               # 文章作者
                         'href':href,                   # 文章超連結
                        })
print('本頁的文章數量 = ', len(articles))
count = 0                                               # 文章編號計數器
for article in articles:
    count += 1
    print('文章編號 : ', count)
    print('文章標題 : ', article['title'])
    print('文章作者 : ', article['author'])
    print('文章連結 : ', article['href'],'\n')
    

















