# -*- coding: utf8 -*-

import socket


HOST = '127.0.0.1'
PORT = 8000

address = (HOST, PORT)

socket01 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket01.bind(address)  
socket01.listen(10)  

print('Socket Startup')
conn, addr = socket01.accept()
print('Connected by', addr)


DataFile = open('./Message1.txt', 'wb+')
#DataFile = open('./1.PNG', 'wb+')
while True:
    DataRead = conn.recv(512)  
    if not DataRead:
        break  
    DataFile.write(DataRead)
DataFile.close()
print('data save')


conn.close()
socket01.close()
print('server close')
