'''
# .format
x1=int(input('請輸入座標x1:'))
y1=int(input('請輸入座標y1:'))
x2=int(input('請輸入座標x2:'))
y2=int(input('請輸入座標y2:'))
dist=((x1-x2)**2+(y1-y2)**2)**0.5
#print("({0},{1})和({2},{3})的距離是{4}".format(x1,y1,x2,y2,dist))
print("({0:4d},{1:4d})和({2:4d},{3:4d})的距離是{4:5.1f}".format(x1,y1,x2,y2,dist))
# d= decimal;f=float

'''
"""
x1,x2,x3,x4=eval(input("請輸入四個數字:"))
y=(x1+x2)*(x3+x4)
print("({}+{})*({}+{})={}".format(x1,x2,x3,x4,y))
"""

# text = open(file="text.txt",mode="r")
# aLine = text.readline()
# x1,y1,x2,y2 = eval(aLine)
# dist=((x1-x2)**2+(y1-y2)**2)**0.5
# print("({0:4d},{1:4d})和({2:4d},{3:4d})的距離是{4:5.1f}".format(x1,y1,x2,y2,dist))
# text.close()

# text = open(file="text.txt",mode="a")
# text.write("9,3,6,24\n")
# print("9,45,23,8\n",file=text)
# text.close()

'''
c=float(input("請輸入想要轉換的攝氏溫度:"))
華氏溫度=c*(9/5)+32
print("你要的華氏溫度為",華氏溫度)

f=float(input("請輸入想要轉換的華氏溫度:"))
攝氏溫度=(f-32)*5/9
print("你要的攝氏溫度為",攝氏溫度)
'''
"""
score = open(file="score.txt",mode="r", encoding='utf-8')
aScore=score.readline()
name1=aScore.replace("\n","")  #用replace()將自動換行取代
#name1=aScore.strip()          #Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
aScore=score.readline()
x1,x2,x3=eval(aScore)
aScore=score.readline()
name2=aScore.strip()
aScore=score.readline()
y1,y2,y3=eval(aScore)
dist1=(x1+x2+x3)/3
dist2=(y1+y2+y3)/3
print("{0}的國英數是:{1:4d},{2:4d},{3:4d},平均為:{4:4.2f}".format(name1,x1,x2,x3,dist1))
print("{0}的國英數是:{1:4d},{2:4d},{3:4d},平均為:{4:4.2f}".format(name2,y1,y2,y3,dist2))
"""

score = open(file="score1.txt",mode="r", encoding='utf-8')
aScore=score.readline()
name1=aScore.split()[0]
x1,x2,x3=eval(aScore.split()[1])
aScore=score.readline()
name2=aScore.split()[0]
y1,y2,y3=eval(aScore.split()[1])
dist1=(x1+x2+x3)/3
dist2=(y1+y2+y3)/3
print("{0}的國英數是:{1:4d},{2:4d},{3:4d},平均為:{4:4.2f}".format(name1,x1,x2,x3,dist1))
print("{0}的國英數是:{1:4d},{2:4d},{3:4d},平均為:{4:4.2f}".format(name2,y1,y2,y3,dist2))