# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from konlpy.tag import Kkma
from collections import defaultdict
from pymongo import MongoClient, DESCENDING
import numpy as np

def run_batch():
    try:
        kkma = Kkma()

        mongo = MongoClient(host='54.149.163.97', port=27017)
        news = mongo.data2.news

        for doc in news.find():
            try:
                news_id = doc['_id']
                category = doc['category']
                doc_content = doc['content']
                doc_keyword = kkma.nouns(doc_content.decode('utf-8'))
                doc_keyword_dict = defaultdict(int)

                for kw in doc_keyword:
                    kw = kw.encode('utf-8')
                    cnt = doc_content.count(kw)
                    doc_keyword_dict[kw] = cnt

                doc_norm = np.sum(np.array(doc_keyword_dict.values()) ** 2)

                max_similarity = -1
                most_similar_doc = None

                for n in news.find({'category' : category}):
                    if n['_id'] == news_id:
                        continue

                    content = n['content']
                    keyword = kkma.nouns(content.decode('utf-8'))
                    keyword_dict = defaultdict(int)

                    for kw in keyword:
                        kw = kw.encode('utf-8')
                        cnt = content.count(kw)
                        keyword_dict[kw] = cnt

                    dot_product = sum([v * doc_keyword_dict[k] \
                                                    for k, v in keyword_dict.items() \
                                                    if k in doc_keyword_dict])

                    norm = np.sum(np.array(keyword_dict.values()) ** 2)

                    similarity = dot_product / float(doc_norm * norm)
                    print n['_id'], similarity, dot_product

                    if similarity > max_similarity:
                        max_similarity = similarity
                        most_similar_doc = n['_id']

                print news_id, max_similarity, most_similar_doc
                news.update_one({'_id' : news_id}, {'$set' : {'similar_doc_id' : most_similar_doc}})
            except Exception, e:
                print e
                continue

    except Exception, e:
        print e
    finally:
        mongo.close()


if __name__ == '__main__':
    run_batch()
