#coding=utf-8

from index import BaseHandler

class MaterialHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('material.html')

    def post(self, *args, **kwargs):
        name = self.get_argument('name')
        sumPrice = self.get_argument('sumPrice')
        sumNum = self.get_argument('sumNum')
        size = self.get_argument('size')
        description = self.get_argument('description')
        unitPrice = round((sumPrice)/int(sumNum),2)
        print('name=%s'%name)
        print('sumPrice=%s'%sumPrice)
        print('sumNum=%s'%sumNum)
        print('size=%s'%size)
        print('desc=%s'%description)
        posts = {'name':name,
                 'sumPrice':sumPrice,
                 'sumNum':sumNum,
                 'size':size,
                 'description':description,
                 'unitPrice':unitPrice,
                 }
        self.db.material.save(posts)
        self.redirect('/materialList')

class MaterialListHandler(BaseHandler):
    def get(self, *args, **kwargs):
        entries = self.db.material.find()
#        for i in entries:
#            print(i.get('name'))
        self.render('materialList.html',entries=list(entries))