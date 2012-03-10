__author__ = 'maxfirecomic'
#coding=utf-8

import tornado.web

class MaterialHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("material")
