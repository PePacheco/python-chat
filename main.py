import threading
import server
from socket import *
from Util.connection import Connection

connection = Connection().SetName('127.0.0.1').SetPort(12345).SetProtocol('TCP')
server_tcp = server.Server()

receive_thread = threading.Thread(target=server_tcp.handle_new_client, args=(connection,))
print("Servidor ativo...")
send_thread = threading.Thread(target=server_tcp.handle_client_send, args=())
receive_thread.start()
send_thread.start()
