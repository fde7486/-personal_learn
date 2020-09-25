import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
HOST = "127.0.0.1"
PORT = 5830
for i in range(10):
    clientMassage = str(input("Client:"))
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((HOST,PORT))
    client.sendall(clientMassage.encode())

    serverMassage = str(client.recv(1024),encoding="utf-8")

    print('Server:',serverMassage)
client.close()