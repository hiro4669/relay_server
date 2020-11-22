import socket
import time
from relay_server import RelayServer

CHANNEL = "abc"

def _create_header():
    global CHANNEL
    bout = bytearray()
    bout.append(RelayServer.RECEIVER)
    bs = CHANNEL.encode('ascii')
    bout.append(len(bs))
    [bout.append(b) for b in bs]    
    return bout

def show(buffer):
    for b in buffer:
        print("{:02x}".format(b), end=" ")
    print()

def run_receiver():
    buffer = _create_header()
    show(buffer)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #s.connect(('127.0.0.1', 8888))
        s.connect((RelayServer.ADDR, RelayServer.PORT))
        s.sendall(buffer)
        ack = s.recv(1024)
        #print(len(ack))
        #print(type(ack))
        #print("----")
        msg = ack[0:2]
        if msg.decode("ascii") == "OK":
            print("Receive Start")
            while True:
                data = s.recv(1024)
                show(data)


    

if __name__ == "__main__":
    print("receiver")
    run_receiver()
    