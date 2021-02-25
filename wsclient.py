
import sys
from websocket import create_connection



if __name__ == "__main__":
    //Enter IP address & port number
    ws = create_connection("ws://180.235.234.95:8888/websocket")
    message = "Hello World"
    print("send {}".format(message))
    ws.send(message)
    
    
    #print ws.send(message)
    #print ws.recv()
    
    ws.close()
