import pandas as pd
from sklearn.ensemble import RandomForestRegressor


iowa_data = pd.read_csv('train.csv', index_col='Id')
y = iowa_data.SalePrice
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = iowa_data[features]

rf_model_on_full_data = RandomForestRegressor(random_state=1)
rf_model_on_full_data.fit(X, y)

test_data = pd.read_csv('test.csv')
test_X = test_data[features]
predictions = rf_model_on_full_data.predict(test_X)
print(predictions, type(predictions))