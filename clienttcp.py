import socket

serverName = '127.0.0.1'

serverPort = 12345

while True:
    message = input('Input lowercase sentence:')
    
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    clientSocket.send(message.encode())
    modifiedMessage = clientSocket.recv(1024)
    print (modifiedMessage.decode())
    clientSocket.close()

