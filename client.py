from socket import *

serverName = '192.168.2.107'
serverPort1 = 12000
serverPort2 = 12001

serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

port1: bool = True

while True:
    message = input('Input lowercase sentence:')

    if port1:
        serverPort = serverPort1
    else: 
        serverPort = serverPort2
    
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress =  clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())

    port1 = not port1

clientSocket.close()