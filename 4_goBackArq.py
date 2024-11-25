import time 
import random

windowSize = int(input("Enter the window size: "))
totalFrames = int(input("Enter the total number of frames: "))
# timeout = int(input("Enter the timeout: "))

def sending_frame(frameNumber):
    print(f"Sending Frame {frameNumber}")
    return random.choice([True, False])

def recieveAck(frameNumber):
    # print(f"Received Acknowledgement of Frame {frameNumber}")
    time.sleep(1)
    return random.choice([frameNumber, None])

def goBackArq():
    base = 0
    next_frame = 0
    ack_recieved = -1

    while base < totalFrames:
        while next_frame < base + windowSize and next_frame < totalFrames:
            if sending_frame(next_frame):
                print(f"Frame {next_frame} sent successfully")
            else:
                print(f"Frame {next_frame} send unsuccessfully")
            next_frame += 1
        ack = recieveAck(base)

        if ack is not None:
            print(f"Acknowledgement received for frame {ack}")
            base = ack + 1
        else:
            print(f"ACK lost or error occured, resending from the base frame.")
            next_frame = base

if __name__ == "__main__":
    goBackArq()