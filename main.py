#coding=utf-8

from pymongo.errors import ConnectionFailure
import sys
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
from handler.index import *
from handler.productOrder import *
from handler.product import *
from handler.material import *
from tornado.options import define,options
from setting import *
from pymongo import Connection
from uimodules import RealPriceModule,ProductMaterials
from pymongo.son_manipulator import AutoReference,NamespaceInjector

define('port',default=8888,help='run server on 8888 port',type=int)

try:
    conn = Connection('localhost')
except ConnectionFailure:
    print "not connect mongodb on localhost:27017"
    sys.exit(1)

db = conn.shaw
db.add_son_manipulator(NamespaceInjector())
db.add_son_manipulator(AutoReference(db))

def main():
    tornado.options.parse_command_line()
    all_handler = [
        (r'/',IndexHandler,dict(db=db)),
        (r'/order/(\w*)',OrderHandler,dict(db=db)),
        (r'/orderList',OrderListHandler,dict(db=db)),
        (r'/orderDel/(\w+)',OrderDelHandler,dict(db=db)),
        (r'/product/(\w*)',ProductHandler,dict(db=db)),
        (r'/productList',ProductListHandler,dict(db=db)),
        (r'/productDel/(\w+)',ProductDelHandler,dict(db=db)),
        (r'/material/(\w*)',MaterialHandler,dict(db=db)),
        (r'/materialList',MaterialListHandler,dict(db=db)),
        (r'/materialDel/(\w+)',MaterialDelHandler,dict(db=db)),
    ]
    setting['ui_modules']={"realPrice":RealPriceModule,"productMaterials":ProductMaterials}
    application = tornado.web.Application(all_handler, **setting)
    server = tornado.httpserver.HTTPServer(application)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if  __name__=="__main__":
    main()