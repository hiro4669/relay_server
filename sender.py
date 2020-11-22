import socket
import time
from relay_server import RelayServer

CHANNEL = "abc"

def _create_header():
    global CHANNEL
    bout = bytearray()
    bout.append(RelayServer.SENDER)
    bs = CHANNEL.encode('ascii')
    bout.append(len(bs))
    [bout.append(b) for b in bs]
    return bout


def show(buffer):
    for b in buffer:
        print("{:02x}".format(b), end=" ")
    print()

def run_sender():
    buffer = _create_header()
    show(buffer)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #s.connect((IPADDR, PORT))
        s.connect((RelayServer.ADDR, RelayServer.PORT))
        s.sendall(buffer)
        ack = s.recv(1024)        
        msg = ack[0:2]
        if msg.decode("ascii") == "OK":
            msg = "hello".encode("ascii")
            buffer = bytearray()
            [buffer.append(b) for b in msg]
            show(buffer)
            while True:
                s.sendall(buffer)                
                time.sleep(2)
                #print("sleep")

if __name__ == "__main__":
    print("sender")
    run_sender()