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
        first_arg = entry_split[0]
        second_arg = entry_split[1]
        if len(entry_split) == 3:
            third_arg = entry_split[2]
        if first_arg == '\\ALL':
            abs_path = os.path.abspath(second_arg)
        elif first_arg == '\\PV':
            abs_path = os.path.abspath(third_arg)
        else:
                abs_path = ''
        if os.path.isfile(abs_path):
            with open(abs_path, 'rb') as file:
                file_data = file.read()
                print(file_data)
                message_to_send = f"{entry} ".encode() + file_data
                client_socket.sendall(message_to_send)
            client_socket.send(entry.encode())
        else:
            client_socket.send(entry.encode())

def receive_data(client_socket):
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

enviar_thread = threading.Thread(target=send_data, args=(clientSocket, None))
receber_thread = threading.Thread(target=receive_data, args=(clientSocket,))

enviar_thread.start()
receber_thread.start()
