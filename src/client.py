import socket
import threading

SERVER: str = "127.0.0.1"  # Endereço IP do servidor
PORT: int = 12345  # Porta para conexão

def receive_message(sock):
    while True:
        try:
            message = sock.recv(1024).decode("utf-8")
            print(message)
        except OSError:
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER, PORT))

    receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
    receive_thread.start()

    is_first_message: bool = True

    while True:
        if is_first_message:
            message = input("Digite seu apelido: ")
            is_first_message = not is_first_message
        else:
            message = input()
        if message == "/quit":
            break
        client_socket.sendall(message.encode("utf-8"))

    client_socket.close()

main()
