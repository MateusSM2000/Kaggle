import pandas as pd
reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)


print(reviews.groupby('points'), type(reviews.groupby('points')))
print(reviews.groupby('points').points, type(reviews.groupby('points').points))
print(reviews.groupby('points').points.count(), type(reviews.groupby('points').points.count()), '\n' * 10)

print(reviews.groupby('points').price.min(), '\n' * 10) # cheapest wine in each point value category

print(reviews.groupby('winery').apply(lambda df: df.title.iloc[0]),
      type(reviews.groupby('winery').apply(lambda df: df.title.iloc[0])), '\n' * 10)

print(reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()]),
      type(reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])), '\n')
print(reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()]).loc[:, ['points', 'price']],
      '\n')
print(reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()]).loc[['Argentina', 'Uruguay'], ['points', 'price']])