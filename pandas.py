import pandas as pd

# read data from CSV file
df = pd.read_csv('spotify_data.csv')

# select columns
df_subset = df[['genre', 'artist', 'track_name', 'popularity', 'danceability', 'energy']]

# filter by genre
df_filtered = df_subset[df_subset['genre'] == 'pop']

# group by genre and calculate mean popularity, danceability, and energy
df_grouped = df_subset.groupby('genre')[['popularity', 'danceability', 'energy']].mean()

# merge dataframes on common column
df_merged = pd.merge(df_grouped, other_dataframe, on='column_name')
