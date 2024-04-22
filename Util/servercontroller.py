from Util.user import User
from Util.msgfiltered import Msgfiltered
import threading
from Util.commands import Commands
from socket import *

cmds = Commands()

msg_filter = Msgfiltered()

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
    
                if user.message.param3:
                    msg = f'\n\n{user.username}: {msg.param2} {msg.param3}'
                else:
                    msg = f'\n\n{user.username}: {msg.param2}'

                if other.socket.type == SOCK_STREAM:
                    other.socket.send(msg.encode())
                else:
                    other.socket.sendto(msg.encode(), other.client_address)

                user.next_msg_filtered()

    def send_pv_msg(self, user):
        if user.message.param1 != cmds.PV:
            return

        for other in self.users:
            if other.username == user.message.param2:
                msg = user.message
                msg = f'\n\n{user.username}: {msg.param3}'
                if other.socket.type == SOCK_STREAM:
                    other.socket.send(msg.encode())
                else:
                    other.socket.sendto(msg.encode(), other.client_address)
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