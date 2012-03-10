__author__ = 'maxfirecomic'
#coding=utf-8

import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
import handler.product
import  handler.material
from tornado.options import define,options

define('port',default=8888,help='run server on 8888 port',type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello world")

application = tornado.web.Application([
    (r"/",MainHandler),
])

def main():
    tornado.options.parse_command_line()
    all_handler = [
        (r'/',MainHandler),
        (r'/product',handler.product.ProductHandler),
        (r'/material',handler.material.MaterialHandler),
    ]
    application = tornado.web.Application(all_handler)
    server = tornado.httpserver.HTTPServer(application)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if  __name__=="__main__":
    main()