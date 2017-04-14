# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import datetime

from sqlalchemy import desc
from model import Rating, Movie, Similarity
from connection import Session

class SimilarityDAO(object):
    def __init__(self):
        pass

    def get_similar_users_who_rated(self, user_id, movie_id, nneighbors):
        session = Session()
        try:
            result = session.query(Similarity) \
                            .join(Rating, Similarity.user_id2 == Rating.user_id) \
                            .filter(Similarity.user_id1 == user_id) \
                            .filter(Rating.movie_id == movie_id) \
                            .order_by(desc(Similarity.similarity)) \
                            .limit(nneighbors) \
                            .all()

            return [(row.user_id2, row.similarity) for row in result]

        except Exception as e:
            print e
        finally:
            session.close()


    def store_similarity(self, user_id1, user_id2, similarity):
        session = Session()
        try:
            sim = Similarity(user_id1 = user_id1,
                            user_id2 = user_id2,
                            similarity = similarity)
            session.add(sim)
            session.commit()

        except Exception as e:
            print e
            session.rollback()

        finally:
            session.close()
