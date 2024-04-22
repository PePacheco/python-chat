import sys
import threading
import os
import socket
from Util.msgfiltered import Msgfiltered

serverName = '127.0.0.1'
serverPort = 12345
msg_filter = Msgfiltered()

def send_data(client_socket, message):
    while True:
        # Aguarda entrada do usuário
        entry = input("Digite uma mensagem para enviar (ou EXIT para sair): ")
        if entry.upper() == "EXIT":
            break
        entry_split= entry.split(' ')
        print(entry_split)
        first_arg = entry_split[0]
        second_arg = entry_split[1]
        if len(entry_split) == 3:
            third_arg = entry_split[2]
        else:
            third_arg = ''
        if first_arg == '\\ALL':
            abs_path = os.path.abspath(second_arg)
        elif first_arg == '\\PV':
            abs_path = os.path.abspath(third_arg)
        else:
            abs_path = ''

        if os.path.isfile(abs_path):
            with open(abs_path, 'rb') as arquivo:
                while True:
                    dados = arquivo.read(1024)  # Lê 1024 bytes do arquivo
                    if not dados:
                        break  # Se não houver mais dados, termina o loop
                    print(dados)
                    if third_arg == '':
                        clientSocket.sendto((first_arg + " " + second_arg + " ").encode() + dados, (serverName, serverPort))
                    else:
                        clientSocket.sendto((first_arg + " " + second_arg + " " + third_arg + " ").encode() + dados, (serverName, serverPort))
        else:
            clientSocket.sendto(entry.encode(), (serverName, serverPort))

def receive_data(client_socket):
    global serverPort 
    serverPort = int(client_socket.recv(1024).decode())
    print("Recaminhaou a porta", serverPort)
    while True:
        # Recebe dados do servidor
        message = client_socket.recv(1024)
        if message:
           print(message.decode())

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input('Adicione um username para entrar no chat :> ')

msg = msg_filter.process_message(message)

if msg.param1 != "\\REG" and msg.param3 != None:
    sys.exit()

clientSocket.sendto(message.encode(), (serverName, serverPort))

enviar_thread = threading.Thread(target=send_data, args=(clientSocket, None))
receber_thread = threading.Thread(target=receive_data, args=(clientSocket,))

enviar_thread.start()
receber_thread.start()