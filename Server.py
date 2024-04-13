from socket import *

servername = '192.168.2.107'

FLAG_EXIT='EXIT'

received_message = ''

serverPort = 13000

serverSocket = socket(AF_INET, SOCK_DGRAM)
#TCP :
##serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind((servername, serverPort))

print('The server is ready to receive')

while received_message != FLAG_EXIT:
    message, clientAddress = serverSocket.recvfrom(2048)
    received_message = message.decode()

    modifiedMessage = received_message.upper()
    print('Mensagem recebida: ', received_message)
    serverSocket.sendto(modifiedMessage.encode(),
    clientAddress)

serverSocket.sendto('servidor fechado'.encode(), clientAddress)

serverSocket.close()