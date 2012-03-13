#coding=utf-8

from pymongo.errors import ConnectionFailure
import sys
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
        (r'/',handler.index.IndexHandler,dict(db=db)),
        (r'/product/(\w*)',handler.product.ProductHandler,dict(db=db)),
        (r'/productList',handler.product.ProductListHandler,dict(db=db)),
        (r'/productDel/(\w+)',handler.product.ProductDelHandler,dict(db=db)),
        (r'/material/(\w*)',handler.material.MaterialHandler,dict(db=db)),
        (r'/materialList',handler.material.MaterialListHandler,dict(db=db)),
        (r'/materialDel/(\w+)',handler.material.MaterialDelHandler,dict(db=db)),
    ]
    setting['ui_modules']={"realPrice":RealPriceModule,"productMaterials":ProductMaterials}
    application = tornado.web.Application(all_handler, **setting)
    server = tornado.httpserver.HTTPServer(application)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if  __name__=="__main__":
    main()