import pandas as pd

melbourne_data = pd.read_csv('../melb_data.csv')

print(melbourne_data.columns, '\n')
print(melbourne_data.describe(), '\n' * 10)
print(melbourne_data.head(), '\n' * 10)
print(melbourne_data.__len__())
print(melbourne_data, '\n\n\n')

melbourne_data = melbourne_data.dropna(axis=0)
print(melbourne_data.__len__())