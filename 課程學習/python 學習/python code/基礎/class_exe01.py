# for i in range(1,10):
#     for j in range(1,10):
#         ans = i*j
#         print("{0:3d}".format(ans),end=" ")
#     print()

'''
x = int(input("請輸入一個整數"))
for i in range(x):
    if (i%2 == 0 and i%3 == 0 and i%5 !=0):
        print(i)

x = eval(input('the value?'))
v = 0
while True:
    if (v > x):
        break
    if (v%3 == 0 and v%2 == 0 and v%5 != 0):
        print (v)
    v += 1;    
    
    
def m(a, b, c):
   v = 0 
   while True:
      if (v%a == 0 and v%b == 0 and v%c != 0):
         break
      v += 1; 
   return v
'''   

"""
a = 0
b = 1
print(a, b, end=" ")
while True:
    c = a + b
    print(c, end=' ')
    if c > 100:
        break
    a = b
    b = c
print('\n',b)

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)        
n = 0    
while True:
    if (f(n)>100):
        break
    n+=1
print ('f({})={}'.format(n-1, f(n-1)))
"""


"""
ans = input("請輸入密碼")
ans = list(ans)

lengthOK = False
upperLetter = lowerLetter = False
decimalOK = False

if len(ans)>=6 and len(ans)<=12:
    lengthOK = True
for p in ans:
    if p.isdecimal():
        decimalOK = True
    elif p.islower():
        lowerLetter = True
    elif p.isupper():
        upperLetter =True
if (lengthOK and upperLetter and lowerLetter and decimalOK):
    print('密碼設定完成')
else :
    print("密碼設定不符合規定")
"""


# a, b = eval(input("請輸入兩個正整數"))
# c = abs(a*b)
# while (a > 0 and b > 0):
#     if (a > b):
#         a = a%b
#     else :
#         b = b%a
# if a == 0:
#     print("最大公因數為{},最小公倍數為{}".format(b,c/b))
# else:
#     print("最大公因數為{},最小公倍數為{}".format(a,c/a))
# def gcd(a, b):
#    x = min(a, b)
#    for i in range(1, x+1):
#        if (a % i ==0 and b % i ==0):
#            g = i
#    return g        
# print ('gcd of {}, {} is {}'.format(5,7,gcd(5,7)))
# print ('gcd of {}, {} is {}'.format(4,8,gcd(4,8)))
# print ('gcd of {}, {} is {}'.format(91,7,gcd(91,7)))
# def lcm(a, b):    
#     return int(a*b/gcd(a,b))
# print ('lcm of {}, {} is {}'.format(5,7,lcm(5,7)))
# print ('lcm of {}, {} is {}'.format(4,8,lcm(4,8)))
# print ('lcm of {}, {} is {}'.format(91,7,lcm(91,7)))



# monster_list = ['地精', '狼人', '熊貓人']
# attack_list = [80, 90, 20]
# defense_list = [70, 92, 75]
# leng = len(monster_list)
# a = {}  
# for i in range(leng):
#     a[monster_list[i]] = (attack_list[i], defense_list[i])
# a = zip(monster_list, zip(attack_list, defense_list))
# a = dict(a)
# monster = input('要呼喚誰? ')
# print (a[monster])   



# student_set = set()
# for i in range(1,51):
#     student = "S"+str(i)
#     student_set.add(student)
# st_list = list(student_set)
# import random as r
# gt = set(r.sample(student_set,10))
# print("參加吉他社的:",gt)
# cp = set(r.sample(student_set,10))
# print("參加電腦社的:",cp)
# print("都參加的：",gt &cp)
# print("參加吉他沒有參加電腦社的：",gt - cp)
# print("參加電腦社，沒參加吉他社的：",cp - gt)


# ch2eng = {'貓': 'cat',
#          '狗': 'dog'}
# def gen_eng2ch(d):
#     d2 = {}
#     for ch, eng in d.items():
#         d2[eng] = ch
#     print (d2)    
#     return d2    
# eng2ch = gen_eng2ch(ch2eng)    
# while True:
#     r = input('please select 1) eng2ch 2) ch2eng 3) exit')
#     if r == '3':
#         break
#     elif r == '1':
#         w = input('Please input a eng: ')
#         print ('The ch of {} is {}'.format(w, eng2ch[w]))
#     elif r == '2':
#         w = input('Please input a ch: ')
#         print ('The eng of {} is {}'.format(w, ch2eng[w]))
#     else:
#         print ('error input')


rank = {'Nick': {'Coco': 1, 'Joker': 5},
        'John': {'Coco': 5, 'Joker': 1}}
# for name in rank.keys():
#     print(name)
#     for movie, evaluatein in rank[name].items():
#         print("     {0:4s} {1:2}".format(movie,evaluatein))

for name in rank.keys():
    print(name, end=" ")
print()
for movie, evaluatein in rank[name].items():
    print(movie,end=" ")