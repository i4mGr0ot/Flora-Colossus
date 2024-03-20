import socket
import threading

# Global variables
HOST = '127.0.0.1'
PORT = 55555

# List to store connected clients and their usernames
clients = {}


def handle_client(client_socket, username):
    """
    Handles individual client connection
    :param client_socket: socket object for the client
    :param username: username of the client
    """
    # Broadcast new user joined message
    broadcast(f'{username} joined the chat!', username)

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                broadcast(message, username)
        except:
            # Remove client and close socket upon disconnection
            del clients[username]
            broadcast(f'{username} left the chat!', username)
            client_socket.close()
            break


def broadcast(message, sender):
    """
    Broadcasts message to all connected clients
    :param message: message to be broadcasted
    :param sender: username of the sender
    """
    for username, client_socket in clients.items():
        if username != sender:
            try:
                client_socket.send(message.encode('utf-8'))
            except:
                # Remove client upon error
                del clients[username]


def start_server():
    """
    Starts the server
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server is running on {HOST}:{PORT}")

    while True:
        client_socket, address = server.accept()
        print(f"Connected with {address}")

        # Request username from the client
        client_socket.send("Enter your username: ".encode('utf-8'))
        username = client_socket.recv(1024).decode('utf-8')

        # Add client to the list
        clients[username] = client_socket

        # Start thread to handle client
        thread = threading.Thread(target=handle_client, args=(client_socket, username))
        thread.start()


if __name__ == "__main__":
    start_server()
