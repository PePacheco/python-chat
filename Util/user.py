import threading
from Util.msgfiltered import Msgfiltered

msg_filter = Msgfiltered()


class User:
    def __init__(self, user_id, username, client_address, socket):
        self.user_id = user_id
        self.username = username
        self.client_address = client_address
        self.socket = socket
        self.threading = None
        self.messages  = []
        self.message   = []

    def rec_message(self):
        message = msg_filter.process_message(self.socket.recv(1024).decode())
        self.messages.append(message)
        print(f'A thread do {self.username} recebeu a msg')

    def next_msg_filtered(self):
        if len(self.messages) == 0:
            return
        self.message = self.messages.pop(0)

    def disconnect(self):
        self.stop_thread()
        
   