import socket
import time

def join_socket():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 8080
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print(f"Connected to server at {SERVER_HOST}:{SERVER_PORT}")
    return client_socket

def client_logic(client_socket):
    base = 0
    window_size = 4
    next_seq_num = 0
    data_list = [i for i in range(1, 11)]
    CUSTOM_TIMER = 3  # Timer for retransmission
    retransmit_flag = False
    start_time = None

    try:
        while base < len(data_list):
            # Send frames within the window
            while next_seq_num < base + window_size and next_seq_num < len(data_list):
                frame = f"{data_list[next_seq_num]}"
                try:
                    client_socket.send(frame.encode())
                    print(f"Sent frame: {frame}")
                    next_seq_num += 1
                except Exception as e:
                    print(f"Error while sending frame: {e}")
                    return
            
            # Start retransmission timer
            if not retransmit_flag:
                start_time = time.time()
                retransmit_flag = True
            
            # Wait for ACKs
            try:
                client_socket.settimeout(2)
                response = client_socket.recv(1024).decode()

                if response.startswith("ACK:"):
                    ack_num = int(response.split(":")[1])
                    print(f"Received ACK for frame {ack_num}")
                    while base <= ack_num and base < len(data_list):
                        base += 1
                    retransmit_flag = False
                elif response.startswith("NACK:"):
                    nack_num = int(response.split(":")[1])
                    print(f"Received NACK for frame {nack_num}. Retransmitting.")
                    next_seq_num = nack_num  # Restart from the NACK frame
                    retransmit_flag = False

            except socket.timeout:
                print("Timeout occurred, resending window...")
                next_seq_num = base

            # Check if retransmission timer expired
            if retransmit_flag and time.time() - start_time >= CUSTOM_TIMER:
                print(f"Retransmitting from frame {base}")
                next_seq_num = base
                retransmit_flag = False

        print("All frames sent successfully.")

    except Exception as e:
        print(f"Error in client logic: {e}")
    finally:
        try:
            client_socket.send("connection closed".encode())
        except Exception:
            pass
        client_socket.close()
        print("Connection closed.")

def start_client():
    client_socket = join_socket()
    client_logic(client_socket)

if __name__ == "__main__":
    start_client()
