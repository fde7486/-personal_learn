# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:54:53 2020

@author: chris
"""

import socket
import time
HOST = '127.0.0.1'
PORT = 8000
clientMessage = 'Hello, how are you!'
num = 0

while num < 10:
    num += 1
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    Hello = input("Please input what you want to say to sever:")
    Hello = "第"+str(num)+"句 : "+ Hello
    client.sendall(Hello.encode())
    serverMessage = str(client.recv(1024), encoding='utf-8')
    print('Server:', serverMessage)
    #time.sleep(2)
    

client.close()
