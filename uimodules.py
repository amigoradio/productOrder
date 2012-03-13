#coding=utf-8

'''author:radio
   http://www.github.com/amigoradio
'''
from bson.objectid import ObjectId

import tornado.web


class RealPriceModule(tornado.web.UIModule):
    def render(self,entries):
        price = 0.0
        for entry in entries:
            material = entry['material']
            mNumber = entry['mNumber']
            print material
            price += round(material['unitPrice']/mNumber,2)
            print(price)
        return self.render_string('modules/realPrice.html',price=price)

class ProductMaterials(tornado.web.UIModule):
    def render(self, entries):
        return self.render_string('modules/productMaterials.html',entries=entries)