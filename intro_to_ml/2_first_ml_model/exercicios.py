from sklearn.tree import DecisionTreeRegressor
import pandas as pd

iowa_data = pd.read_csv('../train.csv', index_col='Id')
print(iowa_data, '\n')

print(iowa_data.columns, '\n\n\n\n')

y = iowa_data.SalePrice

features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

X = iowa_data[features]
print(X.head(), '\n\n', X.describe(), '\n\n\n\n')

iowa_model = DecisionTreeRegressor(random_state=1)
iowa_model.fit(X, y)
print(iowa_model, type(iowa_model), '\n\n\n')


predictions = iowa_model.predict(X)
print(predictions, type(predictions), '\n')
print(iowa_data.SalePrice)