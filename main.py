import threading
import servertcp
from socket import *
<<<<<<< HEAD
from Util.connection        import Connection
from Util.msgfiltered       import Msgfiltered
from Util.servercontroller  import ServerController
=======
from Util.connection import Connection
>>>>>>> origin/Pedrao

connection = Connection().SetName('127.0.0.1').SetPort(12345).SetProtocol('TCP')
server_tcp = servertcp.ServerTCP()

if connection.protocol == 'TCP':
    receive_thread = threading.Thread(target=server_tcp.handle_new_client, args=(connection,))
    print("Servidor ativo...")
    send_thread = threading.Thread(target=server_tcp.handle_client_send, args=())
    receive_thread.start()
<<<<<<< HEAD
    send_thread.start()
    handle_rec = threading.Thread(target=server_tcp.handle_messages, args=())
    handle_rec.start()
=======
    send_thread.start()
>>>>>>> origin/Pedrao
