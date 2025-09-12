import pandas as pd

wine_reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)
print(wine_reviews.columns, '\n')
wine_reviews['critic'] = 'everyone'
print(wine_reviews.columns, '\n')
print(wine_reviews.critic, '\n' * 10)
wine_reviews['backwards_index'] = range(len(wine_reviews) - 1, -1, -1)
print(wine_reviews.backwards_index, '\n' * 10)