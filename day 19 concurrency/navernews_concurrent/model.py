# -*- coding: utf-8 -*-

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, CHAR, Date, String, Time, Index, DateTime, TIMESTAMP, func
from sqlalchemy.dialects.mysql import INTEGER, BIT, TINYINT, TIME, DOUBLE, TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# News table과 mapping될 객체
class News(Base):
    __tablename__ = 'news'

    link            = Column(String(200), primary_key = True, nullable = False)
    title           = Column(String(100), nullable = False)
    content         = Column(TEXT, nullable = False)
    crawl_time      = Column(DateTime, nullable = False)
