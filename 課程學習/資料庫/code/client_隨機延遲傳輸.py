import socket
import time
import random

HOST = '127.0.0.1'
POST = 7830

clientMessage = "Hello, i do not have delay"
clientMessage_d = "I am delay"

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,POST))

tStart = time.time()
time.sleep(random.randint(0,10))
tEnd = time.time()
Total_time = tEnd - tStart
print(Total_time)

if Total_time >3 :
    client.sendall(clientMessage_d.encode())
else:
    client.sendall(clientMessage.encode())

serverMessage = str(client.recv(1024),encoding="utf-8")
print("Sever:",serverMessage)

client.close()