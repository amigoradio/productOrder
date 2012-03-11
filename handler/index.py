#coding=utf-8

'''author:radio
   http://www.github.com/amigoradio
'''

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self,db):
        self.db = db

class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')