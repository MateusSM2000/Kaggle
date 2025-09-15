import pandas as pd
reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)


print(reviews.price.dtype, type(reviews.price.dtype), '\n' * 10)