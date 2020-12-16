import tornado.ioloop
import tornado.web
import tornado.websocket

cl = []

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


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/websocket", WebSocketHandler),    
])
if __name__ == "__main__":
    print("main")
    application.listen(8080)
    tornado.ioloop.IOLoop.current().start()