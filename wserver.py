import tornado.ioloop
import tornado.web
import tornado.websocket
import signal

cl = []
is_closing=False


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("get is called")
        #self.render('test_ws.html')
        self.render('client.html')

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("open is called")        
        if self not in cl:
            cl.append(self)
 
    def on_message(self, message):
        print("on message")
        for client in cl:
            client.write_message(message)
 
    def on_close(self):
        print("on close")
        if self in cl:
            cl.remove(self)

def signal_handler(signum,frame):
        global is_closing
        is_closing=True

def try_exit():
        global is_closing
        if is_closing:
            # clean up here
            tornado.ioloop.IOLoop.instance().stop()


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/websocket", WebSocketHandler),    
])
if __name__ == "__main__":
    print("main")
    signal.signal(signal.SIGINT,signal_handler)
    application.listen(8888)#port number
    tornado.ioloop.PeriodicCallback(try_exit,100).start()
    tornado.ioloop.IOLoop.instance().start()
    
