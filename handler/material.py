#coding=utf-8

from index import BaseHandler

class MaterialHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('material.html')

    def post(self, *args, **kwargs):
        print('name=%s'%self.get_argument('name'))
        print('sumPrice=%s'%self.get_argument('sumPrice'))
        print('sumNum=%s'%self.get_argument('sumNum'))
        print('size=%s'%self.get_argument('size'))
        print('desc=%s'%self.get_argument('description'))
        self.redirect('/materialList')

class MaterialListHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('materialList.html')