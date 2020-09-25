# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:54:36 2020

@author: chris
"""

import socket
HOST = '127.0.0.1'
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))
Count = 0
while Count < 1:
    data, addr = server.recvfrom(1024)
    data = data.decode()
    print('Client message is:', data)
    print('The message comes from IP[%s]'%(str(addr[0])))
    serverMessage = 'I\'m here!'
    
    server.sendto(serverMessage.encode(),addr)
    Count += 1
server.close()
