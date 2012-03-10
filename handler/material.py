#coding=utf-8

from index import BaseHandler

class MaterialHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('material.html')

    def post(self, *args, **kwargs):
        self.redirect('/material')