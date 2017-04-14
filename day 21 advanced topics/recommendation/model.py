# -*- coding: utf-8 -*-

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, CHAR, Date, String, Time, Index, DateTime, TIMESTAMP, func
from sqlalchemy.dialects.mysql import INTEGER, BIT, TINYINT, TIME, DOUBLE, TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import PrimaryKeyConstraint

Base = declarative_base()

class Rating(Base):
    __tablename__ = 'ratings'

    user_id         = Column(Integer, nullable = False)
    movie_id        = Column(Integer, nullable = False)
    rating          = Column(DOUBLE, nullable = False)
    timestamp       = Column(TIMESTAMP, nullable = False)

    __table_args__ = (
        PrimaryKeyConstraint('user_id', 'movie_id'),
        {},
    )


class Movie(Base):
    __tablename__ = 'movies'

    movie_id        = Column(Integer, primary_key = True, nullable = False)
    title           = Column(String(100), nullable = False)
    genre           = Column(String(255), nullable = True)


class Similarity(Base):
    __tablename__ = 'similarity'

    user_id1         = Column(Integer, nullable = False)
    user_id2         = Column(Integer, nullable = False)
    similarity       = Column(DOUBLE, nullable = False)

    __table_args__ = (
        PrimaryKeyConstraint('user_id1', 'user_id2'),
        {},
    )
