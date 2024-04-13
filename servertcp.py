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
            received_message = connection_socket.recv(1024).decode()
            msg = msg_filter.process_message(0, received_message)
            s_controller.reg_connection(msg_filter, client_address, connection_socket)

    def handle_client_send(self, connection):
        while True:
            s_controller.to_send()