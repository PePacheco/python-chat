from Util.user import User
from Util.msgfiltered import Msgfiltered
import threading

msg_filter = Msgfiltered()

def send_message(user):
        t = user.socket.recv(1024).decode()
        print(t)
        message = msg_filter.process_message(t)
        user.messages.append(message)
        print(f'A thread do {user.username} recebeu a msg')

class ServerController:

    ALL = "\\ALL"
    REG = "\\REG"
    PV  = "\\PV"

    def __init__(self):
        self.users = []
        self.id = 1

    def to_send(self):
        for user in self.users:
            if len(user.messages) != 0:
                user.next_msg_filtered()
                self.send_to_all(user)
                self.send_pv_msg(user)

    def send_to_all(self, user):
        if user.message.param1 != self.ALL:
            return

        for other in self.users:
            if other.username != user.username:
                msg = user.message
                msg = f'{user.username}: {msg.param2}'
                other.socket.send(msg.encode())
                user.next_msg_filtered()

    def send_pv_msg(self, user):
        if user.message.param1 != self.PV:
            return

        for other in self.users:
            if other.username == user.message.param2:
                msg = user.message
                msg = f'{user.username}: {msg.param3}'
                other.socket.send(msg.encode())
                user.next_msg_filtered()
                break

    def reg_connection(self, msg_filter, client_address, c_socket):
        
        if msg_filter.param1 != self.REG:
            return

        user = User(self.id, msg_filter.param2, client_address, c_socket)

        users_set = set(self.users)
        finded_user = user.username in users_set

        if finded_user == True:
            print(f"Nome de usuário já existe")
            return

        self.users.append(user)
        newUser = self.users[self.id-1]
        self.id += 1
        
        #newUser.threading = threading.Thread(target=send_message, args=(user))
        #newUser.threading.start()

        print(f"Usuario {newUser.username} adicionado!!!")
    
    def user_thread_receive(user, connection_socket):
        message = msg_filter.process_message(connection_socket.recv(1024).decode())
        user.messages(message)