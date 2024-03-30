import socket
import threading
from typing import Dict

HOST = "127.0.0.1"  # Endereço IP do servidor
PORT = 12345  # Porta para conexão
CLIENTS: Dict[str, socket.socket] = {}

def handle_client(client_socket, address):
    nickname = client_socket.recv(1024).decode("utf-8")
    CLIENTS[nickname] = client_socket

    print(f"{nickname} entrou no chat.")
    while True:
        message: str = client_socket.recv(1024).decode("utf-8")
        if message == "/quit":
            break
        elif message.startswith("/msg"):
            parts = message.split(" ", 1)
            if len(parts) == 2:
                recipient, msg = parts[1].split(" ", 1)
                if recipient in CLIENTS:
                    CLIENTS[recipient].sendall(f"{nickname}: {msg}".encode("utf-8"))
                else:
                    client_socket.sendall("Usuário não encontrado.".encode("utf-8"))
        else:
            if not message:
                break
            print(f"Mensagem de {nickname}: {message}")

    print(f"{nickname} saiu do chat.")
    del CLIENTS[nickname]
    client_socket.close()

def main():
    server_socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"Servidor ouvindo em {HOST}:{PORT}")

    while True:
        client_socket, address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()

main()
