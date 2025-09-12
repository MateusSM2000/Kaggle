import pandas as pd

wine_reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)
print(wine_reviews.country == 'Italy', '\n' * 10)
print(wine_reviews.loc[wine_reviews.country == 'Italy'], '\n' * 10)
print(wine_reviews.loc[(wine_reviews.country == 'Italy') & (wine_reviews.points >= 90)], '\n' * 10)
print(wine_reviews.loc[(wine_reviews.country == 'Italy') | (wine_reviews.points >= 90)], '\n' * 10)
print(wine_reviews.loc[wine_reviews.country.isin(['Italy', 'France'])], '\n' * 10) # itália ou frança
print(wine_reviews.loc[wine_reviews.price.notnull()], '\n' * 10) # retorna rows cujo price n é nulo
print(wine_reviews.loc[wine_reviews.price.isnull()]) # retorna rows cujo price é nulo