# grade = {
#     "a":100,
#     "b":90,
#     "c":45,
#     "d":[50,63,62],
#     "e":(45,89)
# }
# print(grade["a"],grade["d"],grade["e"])

# grade ={
#     'd001': {'eng':90,'ch' :60,'math':74},
#     'd002': {'eng':86,'ch' :80,'math':85},
#     'd003': {'eng':56,'ch' :64,'math':34},
#     'd004': {'eng':98,'ch' :95,'math':96},
# }
# number = input("請輸入你的學號")
# if number in list(grade.keys()):
#     sub = input("請輸入你要查詢科目的成績")
#     if sub in list(grade[number].keys()):
#         print(grade[number][sub])
#     else:
#         print("查無科目")
# else:
#     print("查無學號")

# ch_en = {
#     "蘋果" : "apple",
#     "香蕉" : "banana",
#     "水蜜桃" : "Peach"
# }
# fruit = input("請輸入你要查詢的水果:")
# if fruit in ch_en.keys():
#     print(ch_en[fruit])
# else :
#     print("查無資料")

# dealerA = {1:'Nissan', 2:'Toyota', 3:'Lexus'}
# dealerB = {11:'BMW', 12:'Benz'}
# dealerA.update(dealerB) #將B字典和並進A裡
# print(dealerA)

# nation = [['日本','東京'],['泰國','曼谷'],['英國','倫敦']]
# nationDict = dict(nation)
# print(nation)
# print(nationDict)

# x = zip("abcdef",range(6))
# print(x)
# print(list(x))
# x = dict(zip("abcdef",range(6)))
# print(x)

# players = {'Stephen Curry':'Golden State Warriors',
#            'Kevin Durant':'Golden State Warriors',
#            'Lebron James':'Cleveland Cavaliers',
#            'James Harden':'Houston Rockets',
#            'Paul Gasol':'San Antonio Spurs'}
# for name in sorted(players.keys( )):
#     print(name)
#     print("Hi! %s 我喜歡看你在 %s 的表現" % (name, players[name]))

# noodles = {'牛肉麵':100, '肉絲麵':80, '陽春麵':60,
#            '大滷麵':90, '麻醬麵':70}
# print(noodles)
# noodles = sorted(noodles.items(),key=lambda item:item[1],reverse=True)
# print(noodles)
# noodles_1 = []
# for n,m in noodles.items():
#     if m > 70:
#         noodles_1.append((n,m))
# print(noodles_1)
# noodles_2 = [(n,m) for n,m in noodles.items() if m > 70]
# print(noodles_2)


# song = "Are you sleeping, are you sleeping, Brother John, Brother John?\
# Morning bells are ringing, morning bells are ringing.\
# Ding ding dong, Ding ding dong."
# mydict = {}                         # 空字典未來儲存單字計數結果
# print("原始歌曲")
# print(song)

# # 以下是將歌曲大寫字母全部改成小寫
# songLower = song.lower()            # 歌曲改為小寫
# print("小寫歌曲")
# print(songLower)

# # 將歌曲的標點符號用空字元取代
# for ch in songLower:                
#         if ch in ".,?":
#             songLower = songLower.replace(ch,'')
# print("不再有標點符號的歌曲")    
# print(songLower)

# # 將歌曲字串轉成串列
# songList = songLower.split()        
# print("以下是歌曲串列")
# print(songList)                     # 列印歌曲串列

# # 方法一: 將歌曲串列處理成字典 
# for wd in songList:                 
#         if wd in mydict:            # 檢查此字是否已在字典內
#             mydict[wd] += 1         # 累計出現次數
#         else:
#             mydict[wd] = 1          # 第一次出現的字建立此鍵與值
    
# print("以下是最後執行結果")
# print(mydict)                       # 列印字典


# # 方法二: 將歌曲串列處理成字典 
# mydict = {wd:songList.count(wd) for wd in songList}
# print("以下是最後執行結果")
# print(mydict)   

# a = ['1','2','3','4']
# b = ['2','5','6','7']
# c = ['1','2','6','8']
# # a_and_b =[]
# for i in a:
#     if i in b:
#         a_and_b.append(i)
# print(a_and_b)
# a = set(a)
# print(a)
# print(set(a)&set(b)) #找出a跟b的相同資料(交集)
# print(set(a).intersection(set(b)))
# print(set(a)^set(b))
# print(set(a)|set(b))
# print(set(a)-set(b))


# ans = "abcdefghijklmnopqrstuvwxyz"  #加密
# encry_dict = {}
# front5 = ans[:5]
# end21 = ans[5:]
# subtext = end21 + front5
# encry_dict = dict(zip(subtext, ans))

# msgtext = "answer"
# msg = list(msgtext)
# cipher = []
# for i in msgtext:
#     v = encry_dict[i]
#     cipher.append(v)
# ciphertext = ''.join(cipher)
# print(msgtext,ciphertext)


n = []
name = input("請輸入名字")
movie = input("請輸入喜歡的電影")
while int(name) != -1:
    n_1= n.append([name,movie])
    name = input("請輸入名字")
    movie = input("請輸入喜歡的電影")
x = dict(n)
ans = input("請問是要列出全部資料還是查詢?")
if (ans == "查詢"):
    ans_1 = input("輸入想查詢的名字")
    if ans_1 in x.keys():
        print(x[ans_1])
    else:
        print("查無資料")
else:
    print(x)