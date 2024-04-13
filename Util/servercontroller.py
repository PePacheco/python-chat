from Util.user import User

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
        if user.message.primary_command != self.ALL:
            return

        for other in self.users.items():
            if other.name != user.name:
                user.send_message(other.client_address)

    def send_pv_msg(self, user):
        if user.message.primary_command != self.PV:
            return

        for other in self.users.items():
            if other.name == user.message.second_command:
                user.send_message(other.client_address)

    def reg_connection(self, msg_filter, client_address, c_socket):
        if msg_filter.primary_command != self.REG:
            return
        user = User(self.id, msg_filter.message_content, client_address, c_socket)
        self.users.append(user)
        id += 1