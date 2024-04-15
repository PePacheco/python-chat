from socket import *
from Util.connection import Connection
from Util.msgfiltered import Msgfiltered
from Util.servercontroller import ServerController
import threading

msg_filter = Msgfiltered()
s_controller = ServerController()

class ServerTCP:
    def handle_new_client(self, tcp_connection):
        while True:
            connection_socket, client_address = tcp_connection.get_socket().accept()
            print("Conexão aceita")
            th = threading.Thread(target=self.reg_client, args=(connection_socket, client_address, threading,))
            th.start()
            
    def handle_client_send(self):
        while True:
            s_controller.to_send()

    def reg_client(self, connection_socket, client_address, threading):
        received_message = connection_socket.recv(1024).decode()
        msg = msg_filter.process_message(received_message)
        print(f"{msg.param1} - {msg.param2} - {msg.param3}")
        user = s_controller.reg_connection(msg, client_address, connection_socket)