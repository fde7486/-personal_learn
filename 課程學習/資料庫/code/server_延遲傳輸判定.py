import socket
import time
HOST = '127.0.0.1'
PORT = 7830

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)
while True:   

    conn, addr = server.accept()
    tStart = time.time()
    clientMessage = str(conn.recv(1024), encoding='utf-8')
    tEnd =time.time()
    total_time = tEnd-tStart
    print('Client message is:', clientMessage)
    print(total_time)
    serverMessage1 = 'Client is not delay'
    serverMessage2 = 'Client is delay'
    if total_time <5:
        conn.sendall(serverMessage1.encode())
    else:
        conn.sendall(serverMessage2.encode())
    conn.close()
