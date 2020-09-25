# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:54:53 2020

@author: chris
"""

import socket

HOST = '140.134.27.90'
PORT = 3701
clientMessage = 'Hello, how are youhaha!'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(clientMessage.encode())

serverMessage = str(client.recv(1024), encoding='utf-8')
print('Server:', serverMessage)

client.close()

