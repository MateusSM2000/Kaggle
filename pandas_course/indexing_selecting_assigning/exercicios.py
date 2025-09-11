import pandas as pd
reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)

# 1
desc = reviews.description
print(desc, '\n' * 10)

# 2
first_description = reviews.description.iloc[0]
print(first_description, '\n' * 10)

# 3
first_row = reviews.iloc[0]
print(first_row, '\n' * 10)

# 4
first_descriptions = reviews.description.iloc[:10]
print(first_descriptions, '\n' * 10)

# 5
sample_reviews = reviews.iloc[[1, 2, 3, 5, 8]]
print(sample_reviews, '\n' * 10)

# 6
df = reviews.loc[[0, 1, 10, 100], ['country', 'province', 'region_1', 'region_2']]
print(df, '\n' * 10)

# 7
df = reviews.loc[:99, ['country', 'variety']]
print(df, '\n' * 10)

# 8
italian_wines = reviews.loc[reviews.country == 'Italy']
print(italian_wines, '\n' * 10)

# 9
top_oceania_wines = reviews.loc[(reviews.points >= 95) & (reviews.country.isin(['Australia', 'New Zealand']))]
#top_oceania_wines = reviews.loc[(reviews.points >= 95) & ((reviews.country == 'Australia') | (reviews.country == 'New Zealand'))]
print(top_oceania_wines, '\n' * 10)