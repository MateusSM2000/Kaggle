import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)

print(wine_reviews.points.describe(), '\n' * 10)
print(wine_reviews.taster_name.describe(), '\n' * 10)
print(wine_reviews.points.mean(), '\n' * 10)
print(wine_reviews.taster_name.unique(), '\n' * 10)
print(wine_reviews.taster_name.value_counts(), '\n' * 10)