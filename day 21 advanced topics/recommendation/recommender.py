# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import numpy as np
from similaritydao import SimilarityDAO
from ratingdao import RatingDAO

class Recommender(object):
    def recommend(id):
        pass

class PopularityRecommender(object):
    def __init__(self, ratingdao, nrec):
        self.ratingdao = ratingdao
        self.nrec = nrec

    def recommend(self, user_id):
        print self.ratingdao.get_topn_higly_rated_movies(self.nrec)





# User based collaborative filtering recommender
class UserBasedCFRecommender(object):
    def __init__(self, ratingdao, similaritydao, nneighbors = 10, nrec = 5):
        self.ratingdao = ratingdao
        self.similaritydao = similaritydao
        self.nneighbors = nneighbors
        self.nrec = nrec

    def recommend(self, user_id):
        return self.scoring_by_weighted_sum(user_id, self.nneighbors, self.nrec)

    def scoring_by_weighted_sum(self, user_id, nneighbors = 10, nrec = 5):
        predicted_rating_dict = {}
        unrated_movies = self.ratingdao.get_unrated_movies(user_id)

        for movie_id in unrated_movies:
            similar_user_tuple = self.similaritydao
                            .get_similar_users_who_rated(user_id, movie_id, nneighbors)

            similar_user_ids = np.array(sorted([su[0] for su in similar_user_tuple]))
            similarities = np.array([float(su[1]) for su in similar_user_tuple])
            ratings = self.ratingdao.get_rating_array_fast(similar_user_ids, movie_id)

            predicted_rating = ratings.dot(similarities) / np.sum(similarities)

            if len(predicted_rating_dict) >= nrec:
                mid = min(predicted_rating_dict, key = predicted_rating_dict.get)
                if predicted_rating_dict[mid] < predicted_rating:
                    del predicted_rating_dict[mid]
                    predicted_rating_dict[movie_id] = predicted_rating

            print movie_id, predicted_rating
            predicted_rating_dict[movie_id] = predicted_rating

            print predicted_rating_dict


    def scoring_by_adjusted_average(self, user_id, nneighbors = 10, nrec = 5):
        # 평가 되지 않은 영화의 평점을 예측
        ratings = {}

        user_avg_rating = self.ratingdao.get_user_average_rating(user_id)
        unrated_movies = self.ratingdao.get_unrated_movies(user_id)

        for movie_id in unrated_movies:
            similar_user_tuple = self.similaritydao.get_similar_users_who_rated(user_id, movie_id, nneighbors)

            similarities = np.array([float(su[1]) for su in similar_user_tuple])
            similarity_sum = np.sum(similarities)

            similar_user_ids = np.array([su[0] for su in similar_user_tuple])
            similar_user_avg_ratings = np.array([self.ratingdao.get_user_average_rating(uid)
                                                    for uid in similar_user_ids])

            similar_user_ratings_on_movie  = np.array([float(self.ratingdao.get_rating(uid, movie_id))
                                                    for uid in similar_user_ids])

            print similar_user_ratings_on_movie
            print similar_user_avg_ratings

            weighted_similarity_sum = similarities.dot(similar_user_ratings_on_movie - similar_user_avg_ratings)

            predicted_rating = user_avg_rating + float(weighted_similarity_sum) / similarity_sum
            ratings[movie_id] = predicted_rating
            print movie_id, predicted_rating

        ratings = sorted(ratings.items(), key = lambda x : x[1], reverse = True)
        return ratings[:nrec]


if __name__ == '__main__':
    ratingdao = RatingDAO()
    similaritydao = SimilarityDAO()

    recommender = UserBasedCFRecommender(ratingdao, similaritydao)
    recommender.recommend(2)

    recommender = PopularityRecommender(ratingdao, 5)
    #recommender.recommend(2)
