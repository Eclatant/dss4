# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import datetime
from pymongo import MongoClient

class NewsDAO(object):
    def __init__(self):
        self.mongo = MongoClient('localhost', 27017)
        self.news = self.mongo.data.news_concurrent

    def save_news(self, news_id, title, content):
        if not self.get_news_by_id(news_id):
            print news_id

            doc = {}
            doc['_id'] = news_id
            doc['title'] = title
            doc['content'] = content
            doc['crawl_time'] = datetime.datetime.now()
            self.news.insert_one(doc)

    def get_news_by_id(self, news_id):
        return self.news.find_one({'_id' : news_id}) != None

    def get_news_by_keyword_in_title(self, keyword):
        pass
