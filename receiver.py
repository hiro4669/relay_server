import socket
import time
from relay_server import RelayServer

def _create_header():    
    bout = bytearray()
    bout.append(RelayServer.RECEIVER)

    s = "abc"
    bs = s.encode('ascii')
    slen = len(bs)
    bout.append(slen)

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
        s.connect(('127.0.0.1', 8888))
        s.sendall(buffer)
        ack = s.recv(1024)
        print(len(ack))
        print(type(ack))
        print("----")
        ok = ack[0:2]
        if ok.decode("ascii") == "OK":
            print("Receive Start")
            while True:
                data = s.recv(1024)
                show(data)


    

if __name__ == "__main__":
    print("receiver")
    run_receiver()
    