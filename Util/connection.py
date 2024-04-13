import socket

class Connection:
    
    def __init__(self,name, port):
        self.servername   = name
        self.serverport   = port

    def SetProtocol(self, protocol):
        if protocol == 'TCP':
            self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serversocket.bind((self.servername, self.serverport))
            self.serversocket.listen(5)
        if protocol == 'UDP':
            self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.serversocket.bind((self.servername, self.serverport))
        return self

    def get_socket():
        return self.serversocket


