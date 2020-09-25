# -*- coding: utf8 -*-

import socket

HOST = '140.134.210.134'
PORT =  9384

address = (HOST, PORT)
socket02 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket02.connect(address)  



print('start send txt file')
#imgFile = open("./Message.txt", "rb")
imgFile = open("84216995_p0_master1200.jpg", "rb")
while True:
    imgData = imgFile.readline(660)
    if not imgData:
        break  
    socket02.send(imgData)
imgFile.close()
print('transmit end')

socket02.close()  
print('client close')
