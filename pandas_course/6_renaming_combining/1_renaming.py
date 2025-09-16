import pandas as pd
reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)


renamed_points = reviews.rename(columns={'points': 'rating'})
print(renamed_points.rating, '\n' * 10)


renamed_index = reviews.rename(index={0: 'first_entry', 1: 'second_entry'})
print(renamed_index, '\n' * 10)


renamed_axes = reviews.rename_axis('wines', axis='index').rename_axis('fields', axis='columns')
print(renamed_axes, '\n' * 10)