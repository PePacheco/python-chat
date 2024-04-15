import sys
import threading
import socket
from Util.msgfiltered import Msgfiltered

serverName = '127.0.0.1'
serverPort = 12345
msg_filter = Msgfiltered()

def enviar_dados(client_socket, message):
    while True:
        # Aguarda entrada do usuário
        entrada = input("Digite uma mensagem para enviar (ou EXIT para sair): ")
        if entrada.upper() == "EXIT":
            break
        client_socket.send(entrada.encode())

def receber_dados(client_socket):
    while True:
        # Recebe dados do servidor
        message = client_socket.recv(1024)
        if message:
            print(message.decode())

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

message = input('Adicione um username para entrar no chat :> ')

msg = msg_filter.process_message(message)

if msg.param1 != "\\REG" and msg.param3 != None:
    sys.exit()

clientSocket.send(message.encode())

enviar_thread = threading.Thread(target=enviar_dados, args=(clientSocket, None))
receber_thread = threading.Thread(target=receber_dados, args=(clientSocket,))

enviar_thread.start()
receber_thread.start()


