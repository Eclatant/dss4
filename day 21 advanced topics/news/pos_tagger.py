# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from konlpy.tag import Kkma
from konlpy.utils import pprint
from pymongo import MongoClient

kkma = Kkma()

mongo = MongoClient(host='54.149.163.97', port=27017)
news = mongo.data2.news

doc = news.find_one()

content = doc['content'].decode('utf-8')

pprint(kkma.pos(u'오류보고는 실행환경, 에러메세지와함께 설명을 최대한상세히!^^'))
pprint(kkma.pos(content))
