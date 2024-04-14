import socket

class Connection:

    def __init__(self):
        self.servername = ''
        self.serverport = 0
        self.serversocket = None
        self.protocol = ''
    def SetName(self, servername):
        self.servername = servername
        return self

    def SetPort(self, port):
        self.serverport = port
        return self

    def SetProtocol(self, protocol):
        self.protocol = protocol
        if protocol == 'TCP':
            self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serversocket.bind((self.servername, self.serverport))
            self.serversocket.listen(5)
        elif protocol == 'UDP':
            self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.serversocket.bind((self.servername, self.serverport))
        return self

    def get_socket(self):
        return self.serversocket


