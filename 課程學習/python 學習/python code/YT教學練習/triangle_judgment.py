import random

def triangle_judgment(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        if a==b and b==c:
            ans = "正三角形"
        elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
            if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (a**2 + b**2 == c**2):
                ans = "等腰直角三角形"             
            else: 
                ans = "等腰三角形"
        elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (a**2 + b**2 == c**2):
            ans = "直角三角形"
        else:
            ans = "三角形"
    else:
        ans = "非三角形"
    return ans

def random_try(n):
    for i in n:
        