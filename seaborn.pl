import seaborn as sns

# create a scatter plot of popularity vs. energy with regression line
sns.regplot(x='popularity', y='energy', data=df)

# create a box plot of danceability by genre
sns.boxplot(x='genre', y='danceability', data=df)

# create a heatmap of correlation between audio features
sns.heatmap(df[['popularity', 'danceability', 'energy']].corr(), cmap='YlGnBu')

# create a pair plot of audio features
sns.pairplot(df[['popularity', 'danceability', 'energy']])

# set plot style and context
sns.set_style('darkgrid')
sns.set_context('paper')

# display the plot
plt.show()
