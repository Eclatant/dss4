# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import numpy as np
from ratingdao import RatingDAO
from similaritydao import SimilarityDAO

def cosine(x, y):
    ndx = np.array(x.values())
    ndy = np.array(y.values())

    norm_product = float(np.sqrt(np.sum(ndx ** 2)) * np.sqrt(np.sum(ndy ** 2)))
    dot_product = float(np.sum([x[movie_id] * y[movie_id] for movie_id in
                                            x.keys() if movie_id in y.keys()]))

    return dot_product / norm_product



class BatchSimilarity(object):
    def __init__(self, ratingdao, similaritydao):
        self.ratingdao = ratingdao
        self.similaritydao = similaritydao

    def calculate(self, sim_method = cosine):
        user_vectors = self.ratingdao.get_user_vectors()
        user_ids = user_vectors.keys()

        for user_id1 in user_ids:
            for user_id2 in user_ids:
                if user_id1 == user_id2: continue

                uv1 = user_vectors[user_id1]
                uv2 = user_vectors[user_id2]

                similarity = sim_method(uv1, uv2)
                print user_id1, user_id2, similarity

                if similarity > 0.0:
                    similaritydao.store_similarity(user_id1, user_id2, similarity)

if __name__ == '__main__':
    ratingdao = RatingDAO()
    similaritydao = SimilarityDAO()

    batch = BatchSimilarity(ratingdao, similaritydao)
    batch.calculate(cosine)
