#coding=utf-8

from index import BaseHandler

class ProductHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write("product")