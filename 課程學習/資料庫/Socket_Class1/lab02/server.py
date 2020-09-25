# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:54:36 2020

@author: chris
"""

import socket
HOST = '127.0.0.1'
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)

while True:
    conn, addr = server.accept()
    clientMessage = str(conn.recv(1024), encoding='utf-8')

    print('Client message is:', clientMessage)

    serverMessage = 'I\'m here!'
    
    conn.sendall(serverMessage.encode())
    conn.close()
