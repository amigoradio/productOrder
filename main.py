#coding=utf-8

import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
import handler.product
import handler.material
import handler.index
from tornado.options import define,options
from setting import *
from pymongo import Connection

define('port',default=8888,help='run server on 8888 port',type=int)

conn = Connection('localhost')
db = conn.shaw

def main():
    tornado.options.parse_command_line()
    all_handler = [
        (r'/',handler.index.IndexHandler,dict(db=db)),
        (r'/product$',handler.product.ProductHandler,dict(db=db)),
        (r'/material/(\w*)',handler.material.MaterialHandler,dict(db=db)),
        (r'/materialList',handler.material.MaterialListHandler,dict(db=db)),
        (r'/materialDel/(\w+)',handler.material.MaterialDelHandler,dict(db=db)),
    ]
    application = tornado.web.Application(all_handler, **setting)
    server = tornado.httpserver.HTTPServer(application)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if  __name__=="__main__":
    main()