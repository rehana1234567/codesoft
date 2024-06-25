import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

data = {
    'user_id': [1, 1, 1, 2, 2],
    'movie_id': ['M1', 'M2', 'M3', 'M2', 'M3'],
    'rating': [5, 4, 2, 3, 5]
}

df = pd.DataFrame(data)
print(df)
avg_ratings = df.groupby('movie_id')['rating'].mean().reset_index()
print(avg_ratings)
user_item_matrix = df.pivot_table(index='user_id', columns='movie_id', values='rating', fill_value=0)
print(user_item_matrix)

item_similarity = cosine_similarity(user_item_matrix.T)
item_similarity_df = pd.DataFrame(item_similarity, index=user_item_matrix.columns, columns=user_item_matrix.columns)
print(item_similarity_df)
def recommend_movies(user_id, top_n=5):
    watched_movies = df[df['user_id'] == user_id]['movie_id'].tolist()
    

    avg_user_ratings = df[df['user_id'] == user_id]['rating'].mean()

    movie_scores ={}
    for movie in watched_movies:
        similar_scores = item_similarity_df[movie]
        
        user_ratings = new_func1(user_id)
        
        for other_movie, similarity in similar_scores.iteritems():
            if other_movie not in watched_movies:
                if other_movie not in movie_scores:
                    movie_scores[other_movie] = {
                        'score': 0,
                        'similarity_sum': 0
                    }
                movie_scores[other_movie]['score'] += similarity * user_ratings[other_movie]
                movie_scores[other_movie]['similarity_sum'] += similarity
    
    
    final_scores = [(movie, score['score'] / score['similarity_sum']) for movie, score in movie_scores.items()]
    final_scores.sort(key=lambda x: x[1], reverse=True)
    
    recommended_movies = [movie for movie, _ in final_scores[:top_n]]
    
    return recommended_movies

def new_func1(user_id):
    user_ratings =user_item_matrix(user_id)
    return user_ratings

def new_func(user_id):
    user_ratings = user_item_matrix[user_id]
    return user_ratings


recommended_movies = recommend_movies(1)
print("Recommended Movies:", recommended_movies)


