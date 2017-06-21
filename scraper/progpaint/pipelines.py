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
        self.posts = db[settings['MONGODB_COLLECTION_POSTS']]


    def process_item(self, item, spider):
        if len(item['image_urls']) is 0:
          raise DropItem("Dropping empty item.")
        else:
          # print(item) # looks good 
          self.posts.insert(dict(item))
          
        return item
