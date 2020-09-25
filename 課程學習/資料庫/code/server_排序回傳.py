import socket

def list_word(list1):
    word = " "
    for i in range(len(list1)):
        list1[i] = str(list1[i])
    word = " ".join(list1)
    return word
def word_list(word1):
    list1 = word1.split(" ")
    for i in range(len(list1)):
        list1[i] = int(list1[i])
    return list1

HOST = '127.0.0.1'
PORT = 7830

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)

while True:
    conn, addr = server.accept()
    clientMessage = str(conn.recv(1024), encoding='utf-8')
    print('Client message is:',clientMessage)
    a = word_list(clientMessage)
    
    a.sort()
    serverMessage = list_word(a) 
    
    conn.sendall(serverMessage.encode())
    conn.close()
