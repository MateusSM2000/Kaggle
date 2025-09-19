import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

iowa_data = pd.read_csv('../train.csv', index_col='Id')

y = iowa_data.SalePrice
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

X = iowa_data[features]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

iowa_model = DecisionTreeRegressor()
iowa_model.fit(X_train, y_train)

predictions = iowa_model.predict(X_test)
mae = mean_absolute_error(predictions, y_test)
print(mae)
print(predictions[:5])
print(y_test.head())