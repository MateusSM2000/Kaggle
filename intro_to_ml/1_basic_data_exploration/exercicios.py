import pandas as pd
from datetime import datetime
home_data = pd.read_csv('../train.csv', index_col=0)

print(home_data.columns)

print(home_data.describe())

avg_lot_size = round(home_data.describe().loc['mean', 'LotArea'])
print(avg_lot_size, '\n\n\n')

newest_home_age = datetime.now().year - home_data.describe().loc['max', 'YearBuilt']
print(newest_home_age)