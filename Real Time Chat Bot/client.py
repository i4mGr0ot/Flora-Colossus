import socket
import threading

# Global variables
HOST = '127.0.0.1'
PORT = 55555

# Username
username = None


def receive_messages(client_socket):
    """
    Receives messages from the server and displays them
    :param client_socket: socket object for the client
    """
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
        except:
            # Handle disconnection
            print("Disconnected from the server.")
            break


def send_messages(client_socket):
    """
    Sends messages to the server
    :param client_socket: socket object for the client
    """
    global username
    while True:
        try:
            message = input()
            client_socket.send(message.encode('utf-8'))
        except:
            # Handle disconnection
            print("Disconnected from the server.")
            break


def start_client():
    """
    Starts the client
    """
    global username
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Get username from user
    username = input("Enter your username: ")
    client_socket.send(username.encode('utf-8'))

    # Start threads for sending and receiving messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()


if __name__ == "__main__":
    start_client()
