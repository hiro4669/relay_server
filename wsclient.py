
import sys
from websocket import create_connection



if __name__ == "__main__":
    ws = create_connection("ws://localhost:8080/websocket")
    message = "Hello World"
    print("send {}".format(message))
    ws.send(message)
    
    
    #print ws.send(message)
    #print ws.recv()
    
    ws.close()