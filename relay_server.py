
import time
import threading
import socket

class Channel:

    def __init__(self):
        self._sender = None
        self._receivers = []

    def set_sender(self, sender):
        self._sender = sender
    
    def get_sender(self):
        return self._sender

    def add_receiver(self, receiver):
        self._receivers.append(receiver)

    def get_receivers(self):
        return self._receivers
    
    
        


class RelayServer:

    ADDR = '127.0.0.1'
    PORT = 8888
    SENDER   = 0x1
    RECEIVER = 0x2

    def __init__(self):
        print("RelayServer Init")
        self._contable = {}
        self._thtable  = {}

    def _show(self, buffer):
        for b in buffer:
            print("{:02x}".format(b), end=" ")
        print()
    
    def _ask_send(self, conn):
        bout = bytearray()
        bs = "OK".encode("ascii")
        [bout.append(b) for b in bs]
        conn.sendall(bout)

    def _parse(self, conn):
        data = conn.recv(1024)
        print(len(data))
        print(type(data))
        self._show(data)
        
        nlen = data[1]
        name = data[2:nlen+2].decode('ascii')

        print("name={}".format(name))
        _new_channel = False
        _channel = self._contable.get(name)
        if _channel == None:
            print("create channel")
            _channel = Channel()
            _new_channel = True
            self._contable[name] = _channel

        if data[0] == RelayServer.SENDER:
            print("set sender")
            _channel.set_sender(conn)
        elif data[0] == RelayServer.RECEIVER:
            print("add receiver")
            _channel.add_receiver(conn)

        return (_new_channel, name)
    
        

    def _relay(self, ch_name):
        print(ch_name)
        _channel = self._contable[ch_name]        
        print("YES")
        
        while True:
            s_conn = _channel.get_sender()
            if s_conn:
                data = s_conn.recv(1024)
                self._show(data)
                _receivers = _channel.get_receivers()
                for r_conn in _receivers:
                    r_conn.sendall(data)
            else:
                print("no sender yet")
                time.sleep(1)
        

        

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((RelayServer.ADDR, RelayServer.PORT))
            s.listen(1)
            while True:
                conn, addr = s.accept()
                new_chan, chan_name = self._parse(conn)

                self._ask_send(conn)
                if new_chan:
                    print("create thread")
                    th = threading.Thread(target=self._relay, args=(chan_name,))
                    th.setDaemon(True)
                    th.start()





    




if __name__ == "__main__":
    print("relay server")

    rserver = RelayServer()
    rserver.start()
