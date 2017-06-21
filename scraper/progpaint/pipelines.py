# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import hashlib
from urllib.parse import quote
import pymongo
from scrapy.conf import settings # this will allow to access settings like 'settings['MONGODB_PORT']'
from scrapy.exceptions import DropItem


# stores item in a mongodb
class MongoPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.model = db[settings['MONGODB_COLLECTION_MODEL']]
        self.profile = db[settings['MONGODB_COLLECTION_PROFILE']]


    def process_item(self, item, spider):
        if item['img'] is None:
          raise DropItem("Empty item ({0})".format(item['img']))
        else:
          print(item)
        
        # if spider.name == 'complete':
          # self.model.insert(dict(item))
          
        return item
