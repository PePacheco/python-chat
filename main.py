from socket import *
from Util.connection import Connection
from Util.msgfiltered import Msgfiltered
from Util.servercontroller import ServerController
import servertcp

connection = Connection().SetName('127.0.0.1').SetPort(12345).SetProtocol('TCP')
server_tcp = servertcp.ServerTCP()


server_tcp.handle_new_client(connection)

# if connection.protocol == 'TCP':
#  receive_thread = threading.Thread(target=server_tcp.handle_new_client, args=(connection))
#    send_thread = threading.Thread(target=handle_client_send, args=(client_socket))
#    receive_thread.start()
#    send_thread.start()