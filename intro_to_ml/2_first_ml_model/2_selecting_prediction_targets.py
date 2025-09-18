import pandas as pd

melbourne_data = pd.read_csv('../melb_data.csv')
melbourne_data = melbourne_data.dropna(axis=0)


y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = melbourne_data[melbourne_features]



print(X.describe(), '\n')
print(X.head())