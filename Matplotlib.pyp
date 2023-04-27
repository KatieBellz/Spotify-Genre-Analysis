import matplotlib.pyplot as plt

# create a bar chart of average popularity by genre
plt.bar(df_grouped.index, df_grouped['popularity'])

# create a scatter plot of popularity vs. energy
plt.scatter(df['popularity'], df['energy'])

# create a line chart of average danceability by genre
plt.plot(df_grouped.index, df_grouped['danceability'])

# add axis labels and a title
plt.xlabel('Genre')
plt.ylabel('Average Popularity')
plt.title('Average Popularity by Genre')

# display the chart
plt.show()
