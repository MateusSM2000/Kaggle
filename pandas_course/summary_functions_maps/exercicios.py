import pandas as pd
reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)

# 1
median_points = reviews.points.median()
print(median_points, '\n' * 10)

# 2
unique_countries = reviews.country.unique()
print(unique_countries)
print(type(unique_countries), '\n' * 10)

# 3
reviews_per_country = reviews.country.value_counts()
print(reviews_per_country, '\n' * 10)

# 4
centered_price = reviews.price.map(lambda x: x - reviews.price.mean())
print(centered_price, '\n' * 10)

# 5
reviews['points_price_ratio'] = reviews.points / reviews.price
print(reviews.loc[:, ['title', 'points', 'price', 'points_price_ratio']], '\n')
bargain_wine_index = reviews.points_price_ratio.idxmax()
print(reviews.iloc[bargain_wine_index], '\n' * 10)
bargain_wine = reviews.title[bargain_wine_index]

# 6
tropical_count_serie = reviews.description.str.count('tropical') #total de ocorrências (inclui repetições na mesma linha)
tropical_total_sum = tropical_count_serie.sum()
fruity_count_serie = reviews.description.str.count('fruit')
fruity_total_sum = fruity_count_serie.sum()
descriptor_counts = pd.Series([tropical_total_sum, fruity_total_sum], index=['tropical', 'fruity'], name='count_includes_repetition')
print(descriptor_counts, '\n')

n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum() #número de linhas que mencionam o termo ao menos uma vez
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'], name='count_excludes_repetition')
print(descriptor_counts, '\n' * 10)

# 7
def points_to_stars(row) -> pd.DataFrame:
    if row.country == 'Canada':
        row.points = '***'
        return row
    if row.points >= 95:
        row.points = '***'
        return row
    elif row.points >= 85:
        row.points = '**'
        return row
    else:
        row.points = '*'
        return row

star_ratings = reviews.apply(points_to_stars, axis=1).loc[:, 'points']
print(star_ratings, '\n')
print(reviews.apply(points_to_stars, axis=1).loc[(reviews.country == 'Canada') & ((reviews.points == '**') | (reviews.points == '*')), ['points', 'country']])