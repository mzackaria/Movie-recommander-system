import pandas as pd
import numpy as np

# Importing the dataset
data = pd.read_csv('movie_metadata.csv')

##dropping duplicates
data = data.drop_duplicates(subset='movie_title', keep='last')

movie_title = data.movie_title

#replacing nan values by 0
num_critic_for_reviews = data.num_critic_for_reviews.fillna(0)
director_facebook_likes = data.director_facebook_likes.fillna(0)
actor_3_facebook_likes = data.actor_3_facebook_likes.fillna(0)
actor_1_facebook_likes = data.actor_1_facebook_likes.fillna(0)
num_voted_users = data.num_voted_users.fillna(0)
cast_total_facebook_likes = data.cast_total_facebook_likes.fillna(0)
facenumber_in_poster = data.facenumber_in_poster.fillna(0)
num_user_for_reviews = data.num_user_for_reviews.fillna(0)
actor_2_facebook_likes = data.actor_2_facebook_likes.fillna(0)
movie_facebook_likes = data.movie_facebook_likes.fillna(0)

#replacing nan values by mean
gross = data.gross.fillna(data.gross.mean())
budget = data.budget.fillna(data.budget.mean())
title_year = data.title_year.fillna(data.title_year.mean())
imdb_score = data.imdb_score.fillna(data.imdb_score.mean())
aspect_ratio = data.aspect_ratio.fillna(data.aspect_ratio.mean())
duration = data.duration.fillna(data.duration.mean())
ratio_gross_budget =  gross/budget

#create director name dataframe with more then 10 films
director_name = pd.get_dummies(data[['director_name']]).groupby(level=0).sum()
directors_index = np.argwhere(sum(director_name.values == 1) > 10)[:,0]
director_name = director_name.iloc[:,directors_index]

#create actor name dataframe with more then 25 films
actors = pd.concat([data.actor_1_name, data.actor_2_name, data.actor_3_name], axis =1).fillna('')
cleaned = actors.stack().reset_index(level=1, drop=True).to_frame('actors'); 
actors = pd.get_dummies(cleaned).groupby(level=0).sum()
actors_index = np.argwhere(sum(actors.values == 1) > 25)[:,0]
actors = actors.iloc[:,actors_index]

#get genres dataframe
data.genres = data.genres.fillna('')
cleaned = data.set_index(data.index).genres.str.split(r'|', expand=True).stack().reset_index(level=1, drop=True).to_frame('genre'); 
genres = pd.get_dummies(cleaned).groupby(level=0).sum()

#get countries dataframe
country = pd.get_dummies(data.country).groupby(level=0).sum()
country_index = np.argwhere(sum(country.values == 1) > 10)[:,0]
country = country.iloc[:,country_index]

#get color dataframe
color = data.color.replace("Col", "Color")
color = pd.get_dummies(color).groupby(level=0).sum()

content_rating = pd.get_dummies(data[['content_rating']]).groupby(level=0).sum()

#congregate all important data to one dataframe
preprocessed_data = pd.concat([color,\
num_critic_for_reviews,\
director_facebook_likes,\
actor_3_facebook_likes,\
actor_1_facebook_likes,\
num_voted_users,\
cast_total_facebook_likes,\
facenumber_in_poster,\
num_user_for_reviews,\
actor_2_facebook_likes,\
movie_facebook_likes,\
duration,\
gross,\
budget,\
title_year,\
imdb_score,\
aspect_ratio,\
director_name,\
actors,\
genres,\
country,\
content_rating,\
ratio_gross_budget], axis = 1)

preprocessed_data = values.set_index(movie_title.values)

values.to_csv('movie_preprocessed.csv')


