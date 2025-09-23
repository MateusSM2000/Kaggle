import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

melbourne_data = pd.read_csv('../melb_data.csv')
melbourne_data = melbourne_data.dropna(axis=0)

y = melbourne_data.Price
features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = melbourne_data[features]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)

predictions = forest_model.predict(val_X)
mae = mean_absolute_error(predictions, val_y)
print(mae)