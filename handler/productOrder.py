#coding=utf-8

'''author:radio
   http://www.github.com/amigoradio
'''

from bson.objectid import ObjectId

from index import BaseHandler

class OrderHandler(BaseHandler):
    def get(self, order_id):
        print 'id=%s'%order_id
        if order_id:
            entry = self.db.productOrder.find_one(ObjectId(order_id))
        else:
            entry = {}
        print 'entry=%s'%entry
        products = self.db.product.find()
        self.render('order.html',entry=entry,products=products)

    def post(self,order_id):
        postPrice = self.get_argument('postPrice')
        salePrice = self.get_argument('salePrice')
        realPrice = self.get_argument('realPrice')
        profit = self.get_argument('profit')
        description = self.get_argument('description')
        products = self.get_argument('products')
        posts = {'postPrice':postPrice,
                 'salePrice':salePrice,
                 'realPrice':realPrice,
                 'profit':profit,
                 'description':description,
                 'products':eval(products),
                 }
        if order_id:
            posts['_id'] = ObjectId(order_id)
        print(posts)
        self.db.productOrder.save(posts)
        self.redirect('/orderList')

class OrderListHandler(BaseHandler):
    def get(self):
        entries = self.db.productOrder.find()
        self.render('orderList.html',entries=entries)

class OrderDelHandler(BaseHandler):
    def get(self,order_id):
        if order_id:
            self.db.productOrder.remove(ObjectId(order_id))
        self.redirect('/orderList')