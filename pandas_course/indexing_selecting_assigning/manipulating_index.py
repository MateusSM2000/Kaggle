import pandas as pd

wine_reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)
wine_reviews.set_index('title', inplace=True)
print(wine_reviews, '\n' * 10)
print(wine_reviews.loc['Citation 2004 Pinot Noir (Oregon)'], '\n' * 10)