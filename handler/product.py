__author__ = 'maxfirecomic'
#coding=utf-8

import tornado.web

class ProductHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("product")