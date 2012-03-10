#coding=utf-8

'''author:radio
   http://www.github.com/amigoradio
'''

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    pass

class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')