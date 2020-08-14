import numpy as np
import wget
import zipfile
import pandas as pd
import os
from collections import OrderedDict

##Movie Recommendator based on user's preferences given as input to the programm

def ComputeMovieScores(user_preferences,movies_df):##Computes the likeness score(of the user) for each movie in the dataset
    movies_scores=OrderedDict()
    for movie in range(1,3884):
        movie_score=0
        for x in range(0,18):
            movie_score=movie_score + user_preferences[movies_categories[x]]*int(movies_df.loc[movie-1][movies_categories][x])
        movies_scores[movies_df.movies_title[movie-1]]= movie_score
    return movies_scores

def DownloadData(file_path):##Downloads movielens dataset
    url= 'http://files.grouplens.org/datasets/movielens/ml-1m.zip'
    filename= wget.download(url)
    with zipfile.ZipFile('C:\Python\Python37\ml-1m.zip','r') as zip_ref:
         zip_ref.extractall('C:\Python\Python37')


os.chdir('C:\Python\Python37\ml-1m')

movies_df= pd.read_table('movies.dat',header=None, sep='::', names=['movies_id','movies_title','movies_genre'],engine='python')
movies_df= pd.concat([movies_df,movies_df.movies_genre.str.get_dummies()],axis=1)
movies_categories= movies_df.columns[3:]

def UserPreferences(movies_categories):##Asks the user to rate 18 genres and makes his profile
    user_preferences= OrderedDict()
    print("From a scale 1-5 please rate the following genres:\n")
    for x in range(0,18):
       print(movies_categories[x])
       user_input= int(input())
       user_preferences[movies_categories[x]]= user_input
    return user_preferences
   
  
user_pref= UserPreferences(movies_categories)
print('Please wait while we process your preferences :) ')
movie_scores= ComputeMovieScores(user_pref,movies_df)
sort_movie_scores= sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)

x=0
print('Recommended Movies \n')
for i in sort_movie_scores:
    print(i[0],i[1])
    x=x + 1
    if x==5:
        break

    


    
