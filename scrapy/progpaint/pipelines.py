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
        # later.. check validity and drop if duplicate
        # valid=True
        # if {condition}
        # raise DropItem("Duplicate ({0})".format(some_data_string))

        if spider.name == 'test':
          # self.model.insert(dict(item))
          print(item)
        return item


# does nothing - just for testing
class TestPipeline(object):
    def process_item(self, item, spider):
        print("test \n " + item["url"])
        return item
