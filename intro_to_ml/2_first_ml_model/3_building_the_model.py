from sklearn.tree import DecisionTreeRegressor
import pandas as pd

melbourne_data = pd.read_csv('../melb_data.csv')
melbourne_data = melbourne_data.dropna(axis=0)


y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = melbourne_data[melbourne_features]


melbourne_model = DecisionTreeRegressor(random_state=1)
melbourne_model.fit(X, y)
print(melbourne_model, type(melbourne_model))


print('Making predictions for the following 5 houses: ')
print(X.head())
print('The predictions are: ')
print(melbourne_model.predict(X.head()), type(melbourne_model.predict(X.head())))
print('Comparing to actual data:')
print(y.head())