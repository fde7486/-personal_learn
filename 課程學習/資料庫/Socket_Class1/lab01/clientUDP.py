# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:54:53 2020

@author: chris
"""

import socket

HOST = '127.0.0.1'
PORT = 8000
clientMessage = 'Hello, how are you!'

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(clientMessage.encode(),(HOST,PORT))

data, addr = client.recvfrom(1024)
data = data.decode()#解碼訊息
print('Server message is:', data)

client.close()

