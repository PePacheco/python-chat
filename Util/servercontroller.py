from Util.user import User
from Util.msgfiltered import Msgfiltered
import threading
from Util.commands import Commands

cmds = Commands()

msg_filter = Msgfiltered()

def send_message(user):
        t = user.socket.recv(1024).decode()
        print(t)
        message = msg_filter.process_message(t)
        user.messages.append(message)
        print(f'A thread do {user.username} recebeu a msg')

class ServerController:

    lock = threading.Lock()

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
        if user.message.param1 != cmds.ALL:
            return

        for other in self.users:
            if other.username != user.username:
                msg = user.message
                msg = f'\n\n{user.username}: {msg.param2}'
                other.socket.send(msg.encode())
                user.next_msg_filtered()

    def send_pv_msg(self, user):
        if user.message.param1 != cmds.PV:
            return

        for other in self.users:
            if other.username == user.message.param2:
                msg = user.message
                msg = f'\n\n{user.username}: {msg.param3}'
                other.socket.send(msg.encode())
                user.next_msg_filtered()
                break

    def reg_connection(self, msg_filter, client_address, c_socket):

        if msg_filter.param1 != cmds.REG:
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

        print(f"Usuario {newUser.username} adicionado!!!")
        return user

    def user_thread_receive(user, connection_socket):
        message = msg_filter.process_message(connection_socket.recv(1024).decode())
        user.messages(message)