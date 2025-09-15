import pandas as pd
reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)


# 1
dtype = reviews.points.dtype
print(dtype, '\n' * 10)


# 2
point_strings = reviews.points.astype(str)
print(point_strings, '\n' * 10)


# 3
n_missing_prices = reviews.price.isnull().sum()
print(n_missing_prices, '\n')
n_missing_prices_df = reviews[pd.isnull(reviews.price)]
print(n_missing_prices_df, '\n' * 10)


# 4
reviews_per_region = reviews.region_1.fillna('Unknown')
reviews_per_region = reviews_per_region.value_counts()
print(reviews_per_region, '\n' * 10)