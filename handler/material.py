#coding=utf-8
from bson.objectid import ObjectId

from index import BaseHandler

class MaterialHandler(BaseHandler):
    def get(self, material_id):
        print 'id=%s'%material_id
        if material_id:
            entry = self.db.material.find_one(ObjectId(material_id))
        else:
            entry = {}
        print 'entry=%s'%entry
        self.render('material.html',entry=entry)

    def post(self,material_id):
        name = self.get_argument('name')
        sumPrice = self.get_argument('sumPrice')
        sumNum = self.get_argument('sumNum')
        size = self.get_argument('size')
        description = self.get_argument('description')
        unitPrice = round(float(sumPrice)/int(sumNum),2)
        posts = {'name':name,
                 'sumPrice':sumPrice,
                 'sumNum':sumNum,
                 'size':size,
                 'description':description,
                 'unitPrice':unitPrice,
                 }
        if material_id:
            posts['_id'] = ObjectId(material_id)
        print(posts)
        self.db.material.save(posts)
        self.redirect('/materialList')

class MaterialListHandler(BaseHandler):
    def get(self):
        entries = self.db.material.find()
        self.render('materialList.html',entries=entries)

class MaterialDelHandler(BaseHandler):
    def get(self,material_id):
        if material_id:
            self.db.material.remove(ObjectId(material_id))
        self.redirect('/materialList')