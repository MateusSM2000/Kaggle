import pandas as pd
reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)



# 1
reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()
print(reviews_written, '\n' * 10)


# 2
best_rating_per_price = reviews.groupby('price').points.agg(max)
# ou
best_rating_per_price = reviews.groupby('price').apply(lambda df: df.loc[df.points.idxmax()]).loc[:, 'points']
print(best_rating_per_price, '\n' * 10)


# 3
price_extremes = reviews.groupby('variety').price.agg([min, max])
print(price_extremes, '\n' * 10)


# 4
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)
print(sorted_varieties, '\n' * 10)

# 5
reviewer_mean_ratings = reviews.groupby('taster_name').apply(lambda df: df.points.mean())
print(reviewer_mean_ratings, '\n' * 10)


# 6
country_variety_counts = reviews.groupby(['country', 'variety']).variety.value_counts().sort_values(ascending=False)
print(country_variety_counts, '\n' * 10)