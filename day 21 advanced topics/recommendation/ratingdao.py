# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import datetime
import numpy as np

from sqlalchemy import desc, func
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from model import Rating, Movie, Similarity
from connection import Session

class RatingDAO(object):
    def __init__(self):
        pass

    def get_topn_higly_rated_movies(self, n):
        session = Session()
        try:
            result = session.query(Rating.movie_id, func.avg(Rating.rating) \
                    .label('avgrating')) \
                    .group_by(Rating.movie_id) \
                    .order_by('avgrating desc') \
                    .limit(n) \

            return [(row[0], row[1]) for row in result]
        except Exception as e:
            print e
        finally:
            session.close()

    def get_rating_array_fast(self, user_ids, movie_id):
        session = Session()
        try:
            result = session.query(Rating.rating) \
                            .filter(Rating.movie_id == movie_id) \
                            .filter(Rating.user_id.in_(user_ids)) \
                            .order_by(Rating.user_id) \
                            .all()
        except Exception as e:
            print e
        finally:
            session.close()

        return np.array([float(row[0]) for row in result])

    def get_rating_array(self, user_ids, movie_id):
        ratings = []
        for uid in user_ids:
            rating  = self.get_rating(uid, movie_id)
            ratings.append(float(rating))
        return np.array(ratings)

    def get_rating(self, user_id, movie_id):
        session = Session()
        try:
            result = session.query(Rating.rating) \
                            .filter(Rating.user_id == user_id) \
                            .filter(Rating.movie_id == movie_id) \
                            .one()

            return result[0]

        except Exception as e:
            print e

        finally:
            session.close()

    def get_unrated_movies(self, user_id):
        '''
        select movie_id
        	from movies
        	where movie_id not in
        	(select movie_id
        	from ratings where user_id = 1)
        '''
        session = Session()
        try:
            subquery = session.query(Rating.movie_id) \
                                .filter(Rating.user_id == user_id) \
                                .subquery()

            result = session.query(Movie.movie_id) \
                            .filter(Movie.movie_id.notin_(subquery)) \
                            .all()

            return [int(row[0]) for row in result]

        except Exception as e:
            print e

        finally:
            session.close()

    def get_user_average_rating(self, user_id):
        session = Session()
        try:
            result = session.query(func.avg(Rating.rating)) \
                            .filter(Rating.user_id == user_id) \
                            .one()

            return result[0]

        except Exception as e:
            print e

        finally:
            session.close()

    def get_user_vectors(self):
        user_vectors = {}
        session = Session()
        try:
            result = session.query(Rating) \
                            .order_by(Rating.user_id, Rating.movie_id) \
                            .all()
            prev_user = None
            for row in result:
                cur_user = row.user_id
                movie_id = row.movie_id
                rating = row.rating

                if prev_user == None or prev_user != cur_user:
                    uv = {}
                    uv[movie_id] = rating
                    user_vectors[cur_user] = uv
                else:
                    user_vectors[cur_user][movie_id] = rating

                prev_user = cur_user

            return user_vectors

        except Exception as e:
            print e
            return {}

        finally:
            session.close()

if __name__ == '__main__':
    ratingdao = RatingDAO()
    print ratingdao.get_user_average_rating(2)
    print len(ratingdao.get_unrated_movies(1))
