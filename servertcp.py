from socket import *
from Util.connection import Connection
from Util.msgfiltered import Msgfiltered
from Util.servercontroller import ServerController

msg_filter = Msgfiltered()

s_controller = ServerController()

def handle_new_client(tcp_connection):
    while True:
        connection_socket, client_address = tcp_connection.GetSocket().accept()
        received_message = connection_socket.recv(1024).decode()
        msg = msg_filter.handle_new_client(received_message)
        s_controller.reg_connection(msg, client_address, connection_socket)

def handle_client_send(connection):
    while True:
        s_controller.to_send()