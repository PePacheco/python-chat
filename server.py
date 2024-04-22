import socket
from Util.connection import Connection
from Util.msgfiltered import Msgfiltered
from Util.servercontroller import ServerController
import threading

msg_filter = Msgfiltered()
s_controller = ServerController()

port = 12346

class Server:

    def handle_new_client(self, connection):
        while True:
            if(connection.protocol == 'TCP'):
                connection_socket, client_address = connection.get_socket().accept()
                print("Conexão aceita")
                th = threading.Thread(target=self.reg_client, args=(connection_socket, client_address,))
                th.start()
            else:
                message, client_address = connection.get_socket().recvfrom(1024)
                th = threading.Thread(target=self.reg_client_udp, args=(connection,client_address, message,))
                th.start()
                

    def handle_client_send(self):
        while True:
            s_controller.to_send()

    def reg_client(self, connection_socket, client_address):
        received_message = connection_socket.recv(1024).decode()
        msg = msg_filter.process_message(received_message)
        print(f"{msg.param1} - {msg.param2} - {msg.param3}")
        user = s_controller.reg_connection(msg, client_address, connection_socket)

    def reg_client_udp(self,connection,client_address, message):
        global port
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        serversocket.bind((connection.servername, port))
        serversocket.sendto(str(port).encode(), client_address)
        port += 1
        msg = msg_filter.process_message(message.decode())
        print(f"{msg.param1} - {msg.param2} - {msg.param3}")
        user = s_controller.reg_connection(msg, client_address, serversocket)
