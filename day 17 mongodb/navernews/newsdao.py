# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import datetime
from sqlalchemy import create_engine
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.orm import sessionmaker
from model import News

server = '127.0.0.1'
connection_string = 'mysql+mysqldb://root:test1234@{}:3306/test'.format(server)
engine = create_engine(connection_string, pool_recycle = 3600, encoding='utf-8')
Session = sessionmaker(bind=engine)

# DAO
'''
Data Acess Object
실제로 data를 다루는 모듈을 dao라 함
save_neww(), get_news_by_id() 와 같이 인터페이스를 정의하여
데이터를 사용하는 쪽에서는 실제 db에 접근하는 코드를 최소화 함
'''

class NewsDAO(object):
    def __init__(self):
        pass

    def save_news(self, news_id, title, content):
        session = Session()
        if not self.get_news_by_id(news_id):
            print news_id
            news = News(link = news_id, title = title, content = content, crawl_time = datetime.datetime.now())
            session.add(news)
            session.commit()
        session.close()

    def get_news_by_id(self, news_id):
        try:
	    session = Session()
            row = session.query(News).filter(News.link == news_id).first()
            return row
        except Exception as e:
            print e
        finally:
            session.close()

    def get_news_by_keyword_in_title(self, keyword):
        pass

    def get_news_by_keyword_in_content(self, keyword):
        data = []
        session = Session()
        result = session.query(News).filter(News.content.like('%' + keyword + '%')).all()
        for row in result:
            news = {}
            news['link'] = row.link
            news['title'] = row.title
            news['content'] = row.content

            data.append(news)
        return data
