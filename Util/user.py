import threading

class User:
    def __init__(self, user_id, username, client_address, socket):
        self.user_id = user_id
        self.username = username
        self.client_address = client_address
        self.socket = socket
        self.messages = None
        self.message  = None

    def set_thread(self, thread):
        self.thread = thread

    def send_message(self, client_address):
        self.socket.send(client_address, message.message_content.encode())

    def next_msg_filtered(self):
        self.message = messages.pop(0)

    def disconnect(self):
        self.stop_thread()
   