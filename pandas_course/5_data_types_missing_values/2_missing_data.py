import pandas as pd
reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)


print(reviews[pd.notnull(reviews.country)], '\n')
print(reviews[pd.notnull(reviews.country)].country.dtype, '\n' * 10)

print(reviews[pd.isnull(reviews.country)], '\n')
print(reviews[pd.isnull(reviews.country)].country.dtype, '\n' * 10)


print(reviews.region_2.fillna('Unknown'), '\n' * 10)


print(reviews.taster_twitter_handle.replace('@kerinokeefe', '@kerino'))