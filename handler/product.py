#coding=utf-8
from bson.objectid import ObjectId

from index import BaseHandler

class ProductHandler(BaseHandler):
    def get(self, product_id):
        print 'id=%s'%product_id
        if product_id:
            entry = self.db.product.find_one(ObjectId(product_id))
        else:
            entry = {}
        print 'entry=%s'%entry
        materials = self.db.material.find()
        self.render('product.html',entry=entry,materials=materials)

    def post(self,product_id):
        name = self.get_argument('name')
        salePrice = self.get_argument('salePrice')
        description = self.get_argument('description')
        material = self.get_argument('needMaterial')
        posts = {'name':name,
                 'salePrice':salePrice,
                 'description':description,
                 'material':material,
                 }
        if product_id:
            posts['_id'] = ObjectId(product_id)
        print(posts)
        self.db.product.save(posts)
        self.redirect('/productList')

class ProductListHandler(BaseHandler):
    def get(self):
        entries = self.db.product.find()
        self.render('productList.html',entries=entries)

class ProductDelHandler(BaseHandler):
    def get(self,product_id):
        if product_id:
            self.db.product.remove(ObjectId(product_id))
        self.redirect('/productList')