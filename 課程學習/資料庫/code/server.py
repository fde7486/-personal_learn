import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 7830
s.bind((HOST,PORT))
s.listen(3)

while True:
    for i in range(10):
        conn,addr = s.accept()
        cliemtMessage = str(conn.recv(1024),encoding="utf-8")

        print("Client message is:",cliemtMessage)

        serverMessage = str(input("sever:"))
        conn.sendall(serverMessage.encode())
    conn.close()
