import random
import time
window_size= int(input("Number of frames that can be sent before needing an ACK:"))
total_frames= int(input ("Total number of frames to send:"))
timeout= int(input("Timeout in seconds:"))

def send_frame(frame_number):
    print(f"Sending frame {frame_number}")
    return random.choice([True, False])  
def receive_ack(expected_frame):
    time.sleep(1) 
    return random.choice([expected_frame, None])  
def go_back_n_arq():
    base = 0  
    next_frame_to_send = 0  
    ack_received = -1  
    while base < total_frames:
        while next_frame_to_send < base + window_size and next_frame_to_send < total_frames:
            if send_frame(next_frame_to_send):
                print(f"Frame {next_frame_to_send} sent successfully.")
            else:
                print(f"Frame {next_frame_to_send} lost.")
            next_frame_to_send += 1
        ack = receive_ack(base)
        if ack is not None:
            print(f"Received ACK for frame {ack}")
            base = ack + 1
        else:
            print("ACK lost or timeout occurred, resending from base frame")
            next_frame_to_send = base  
if __name__== "__main__":
    go_back_n_arq()
