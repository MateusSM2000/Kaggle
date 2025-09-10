import pandas as pd

wine_reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)
print(wine_reviews.country, '\n' * 10)
print(wine_reviews['country'], '\n' * 10)
print(wine_reviews['country'][0], '\n' * 10)
print(wine_reviews.iloc[0], '\n' * 10)
print(wine_reviews.iloc[:3], '\n' * 10)
print(wine_reviews.iloc[0, 0], '\n' * 10)
print(wine_reviews.iloc[:, 0], '\n' * 10)
print(wine_reviews.iloc[:3, 0], '\n' * 10)
print(wine_reviews.iloc[[0, 1, 2], 0], '\n' * 10)
print(wine_reviews.iloc[-5:], '\n' * 10)
