import pandas as pd


df_reviews = pd.read_csv('reviews.csv')
df_movie_titles = pd.read_csv('movies.csv', index_col=False)

df_users = []
df_items = []

df = pd.merge(df_users, df_movie_titles, on='movieId')

movie_matrix = df.pivot_table(index='userId', columns='title', values='rating')

Avatar_user_rating = movie_matrix['Avatar (2009)']
Avatar_user_rating = Avatar_user_rating.dropna()
Avatar_user_rating.head()

similar_to_Avatar = movie_matrix.corrwith(Avatar_user_rating)
corr_Avatar = pd.DataFrame(similar_to_Avatar, columns=['correlation'])
corr_Avatar.dropna(inplace=True)
corr_Avatar = corr_Avatar.join(df_ratings['number_of_ratings'])
corr_Avatar.head()
