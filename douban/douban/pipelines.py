# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
#from douban.douban.settings import mongo_host,mongo_port,mongo_db_name,mongo_db_collection

mongo_host = '127.0.0.1'
mongo_port = 27017
mongo_db_name = 'douban'
mongo_db_collection = 'douban_movie'

class DoubanPipeline(object):

    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        sheetname = mongo_db_collection
        client = pymongo.MongoClient(host=host,port=port)
        mydb = client[dbname]
        self.post = mydb[sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item

