from django.shortcuts import render
import time
import random

# Create your views here.
def show(request):
    return render(request, 'H1.html',{'data': 'hi',})
def nowtime(request):
    now_time = time.asctime( time.localtime(time.time()) )
    return render(request, 'H2.html',{'data' : now_time,})
def randomnum(request):
    randnum_10 = []
    for i in range(10):
        randnumi = random.randint(0,100)
        randnum_10.append(randnumi)
    return render(request, 'H3.html',{'data' : randnum_10,})
def random_product(request):
    a = random.randint(1,100)
    b = random.randint(1,100)
    ans = a*b
    return render(request, 'H4.html',{'data' : ans,})
        
    
