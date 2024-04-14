from socket import *
from Util.connection import Connection
from Util.msgfiltered import Msgfiltered
from Util.servercontroller import ServerController

msg_filter = Msgfiltered()
s_controller = ServerController()

class ServerTCP:
    def handle_new_client(self, tcp_connection):
        while True:
            connection_socket, client_address = tcp_connection.get_socket().accept()
            print("Conexão aceita")
            received_message = connection_socket.recv(1024).decode()
            msg = msg_filter.process_message(received_message)
            print(f"{msg.param1} - {msg.param2} - {msg.param3}")
            s_controller.reg_connection(msg, client_address, connection_socket)

    def handle_messages(self):
        while True:
            for user in s_controller.users:
                user.rec_message()

    def handle_client_send(self):
        while True:
            s_controller.to_send()