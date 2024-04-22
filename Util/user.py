import threading
from Util.msgfiltered import Msgfiltered
from socket import *
msg_filter = Msgfiltered()

class User:
    def __init__(self, user_id, username, client_address, socket):
        self.user_id = user_id
        self.username = username
        self.online = True
        self.client_address = client_address
        self.socket = socket
        self.messages  = []
        self.message   = []
        self.threading = threading.Thread(target=self.rec_message)
        self.threading.start()

    def rec_message(self):
        while self.online:
            message = ''
            if self.socket.type == SOCK_STREAM:
                message = msg_filter.process_message(self.socket.recv(1024).decode())
            else:
                msg, clientAddres = self.socket.recvfrom(1024)
                message = msg_filter.process_message(msg.decode())
            print(message.param1, message.param2, message.param3)
            if message:
                self.messages.append(message)
            
        self.threading.join()

    def next_msg_filtered(self):
        if len(self.messages) == 0:
            return
        self.message = self.messages.pop(0)

    def disconnect(self):
        self.threading.join()

