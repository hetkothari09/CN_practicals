import socket
import time
import sys
import select

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8080

def create_server_socket():
    """Create and configure the server socket."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen()
    print(f"Server started and listening on {SERVER_HOST}:{SERVER_PORT}\n")
    return server_socket

def input_ready():
    """Check if user input is available."""
    return select.select([sys.stdin], [], [], 0)[0]

def handle_client(client_socket):
    try:
        while True:
            # Receive data
            data = client_socket.recv(1024).decode()
            if not data or "connection closed" in data:
                print("Client requested to close the connection.")
                break

            print(f"Received frame: {data}")

            # Simulate ACK or NACK
            print("Press 1 for NACK or any key for ACK within 2 seconds...")
            start_time = time.time()
            user_input = None
            while time.time() - start_time < 2:
                if input_ready():
                    user_input = input().strip()
                    break

            if user_input == "1":
                print("Sending NACK")
                client_socket.send("NACK".encode())
            else:
                print("Sending ACK")
                seq_num = int(data)
                client_socket.send(f"ACK:{seq_num}".encode())

    except ConnectionResetError:
        print("Client disconnected abruptly.")
    except Exception as e:
        print(f"Error in server logic: {e}")
    finally:
        try:
            client_socket.send("connection closed".encode())
        except Exception:
            pass
        client_socket.close()
        print("Connection closed with the client.")


def start_server():
    """Main server logic."""
    server_socket = create_server_socket()
    try:
        while True:
            # Accept new client connections
            client_socket, addr = server_socket.accept()
            print(f"Connection established with {addr}")
            handle_client(client_socket)  # Handle each client connection
    except KeyboardInterrupt:
        print("\nServer is shutting down.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
