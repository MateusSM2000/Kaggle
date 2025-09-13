import pandas as pd
reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)


countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
print(type(countries_reviewed.index), '\n' * 2)

print(countries_reviewed.reset_index())