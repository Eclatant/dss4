# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import datetime

from sqlalchemy import create_engine
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from model import Movie, Rating
from connection import Session

class MovieDAO(object):
    def __init__(self):
        pass

    def save_comment(self, id, news_id, content, written_time, sympathy_count, antipathy_count):
        session = Session()
        if not self.get_comment_by_id(id):
            print content
            comment = Comment(id = id, news_id = news_id, content = content,
                            written_time = written_time, sympathy_count = sympathy_count,
                            antipathy_count = antipathy_count, crawl_time = datetime.datetime.now())

            session.add(comment)
            session.commit()

        session.close()
