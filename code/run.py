#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:12:21 2021

@author: zmessai
"""

import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

if len(sys.argv) < 2:
    print('Error: must specify K value for K-means algorithm')
    exit

#getting the data
data = pd.read_csv('movie_preprocessed.csv', index_col=0)

#function to resize and wheigh a numerical column in the dataset
def resize_numerical_data(name_column, dataframe=data, weight=1, sc=StandardScaler()):
    column_values = dataframe[[name_column]].values.reshape((len(dataframe), 1))
    column_values_resized = weight*sc.fit_transform(column_values)
    return pd.DataFrame(column_values_resized, columns=[name_column], index=dataframe.index)

#function to resize and wheigh a categorical columns with the prefix 'prefix_name_column' in the dataset
def resize_categorical_data(prefix_name_column, dataframe=data, weight=1):
    return weight*dataframe.filter(items=[col for col in dataframe.columns if prefix_name_column in col])

#RESIZING NUMERICAL DATA
imdb_score = resize_numerical_data('imdb_score')
duration = resize_numerical_data('duration', weight=0.2)
title_year = resize_numerical_data('title_year', weight=0.1)
budget = resize_numerical_data('budget', weight=0.1)
movie_facebook_likes = resize_numerical_data('movie_facebook_likes', weight=0.1)
cast_total_facebook_likes = resize_numerical_data('cast_total_facebook_likes', weight=0.1)

#RESIZING CATEGORICAL DATA
genres = resize_categorical_data('genre', weight=0.1)
content_rating = resize_categorical_data('content_rating', weight=0.8)
country = resize_categorical_data('country', weight=0.25)
director_name = resize_categorical_data('director_name', weight=0.15)
actors = resize_categorical_data('actor', weight=0.15)

#BUILDING THE DATASET FOR kMEANS
df = pd.concat([imdb_score, genres, content_rating, country, duration, director_name, title_year, actors, budget, movie_facebook_likes, cast_total_facebook_likes], axis=1)

#PREDICTION
kmeans = KMeans(n_clusters = int(sys.argv[1]), init = 'k-means++', random_state = 42)
kmeans.fit(df.values)
result = kmeans.predict(df)

print('\n\n')
for i in range(40):
    print('**********CLUSTER MOVIE NAMES - {}***************'.format(i+1))
    for name in data.index[result==i]:
        print(name)
    print('\n\n')
    input("Press Enter to continue, Ctrl+c to exit")
    print('\n\n')
    