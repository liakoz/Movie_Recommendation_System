import numpy as np
import wget
import zipfile
import pandas as pd
import os
from collections import OrderedDict
os.chdir('C:\Python\Python37\ml-1m')

def get_movie_similarity(movie_title):
    
    favoured_movie_index = list(movie_index).index(movie_title)

    P = corr_matrix[favoured_movie_index]

    return P

def get_movie_recommendations(user_movies):
    
    movies_similarities= np.zeros(corr_matrix.shape[0])

    for movie in user_movies:
        movies_similarities= movies_similarities + get_movie_similarity(movie)

    similarities_df = pd.DataFrame( { 'movies_title' : movie_index , 'sum_similarity' : movies_similarities })

    similarities_df=similarities_df[~(similarities_df.movies_title.isin(user_movies))]
    similarities_df= similarities_df.sort_values(by='sum_similarity', ascending=False)

    return similarities_df
    

ratings_df= pd.read_table('ratings.dat',header=None, sep='::',names=['user_id','movies_id','rating','timestamp'],engine='python')


movies_df= pd.read_table('movies.dat',header=None, sep='::', names=['movies_id','movies_title','movies_genre'],engine='python')

ratings_df = pd.merge(ratings_df, movies_df, on='movies_id')[['user_id', 'movies_title', 'movies_id','rating']]

ratings_mtx_df= ratings_df.pivot_table(values='rating', index='user_id', columns='movies_title', fill_value=0)
movie_index= ratings_mtx_df.columns

corr_matrix = np.corrcoef(ratings_mtx_df, rowvar=False)

user_movies= ['Aladdin (1992)',
 "Bug's Life, A (1998)",
 'Groundhog Day (1993)',
 'Lion King, The (1994)']

movies_recom = get_movie_recommendations(user_movies)
print(movies_recom.movies_title.head(15))




