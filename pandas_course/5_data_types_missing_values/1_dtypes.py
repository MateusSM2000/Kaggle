import pandas as pd
reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)


print(reviews.price.dtype, type(reviews.price.dtype), '\n')
print(reviews.dtypes, type(reviews.dtypes), '\n' * 10)

print(reviews.points.dtype, '\n')
print(reviews.points.astype('float64'), '\n' * 10)

print(reviews.index.dtype)