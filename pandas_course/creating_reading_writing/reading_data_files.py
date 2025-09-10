import pandas as pd

wine_reviews = pd.read_csv('../winemag-data-130k-v2.csv')
print(type(wine_reviews), '\n')
print(wine_reviews.shape, '\n')  #(records, columns)
print(wine_reviews.head(), '\n') # a coluna unnamed é pra ser o index na vdd, e consertamos assim
wine_reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)
print(wine_reviews.head())