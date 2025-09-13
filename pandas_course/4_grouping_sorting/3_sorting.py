import pandas as pd
reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)


countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
countries_reviewed = countries_reviewed.reset_index()
countries_reviewed = countries_reviewed.sort_values(by='len', ascending=False)
print(countries_reviewed, '\n' * 10)

countries_reviewed = countries_reviewed.sort_index()
print(countries_reviewed, '\n' * 10)

countries_reviewed = countries_reviewed.sort_values(by=['country', 'len'])