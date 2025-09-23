import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    predictions = model.predict(val_X)
    mae = mean_absolute_error(predictions, val_y)
    return mae


melbourne_data = pd.read_csv('../melb_data.csv')
melbourne_data = melbourne_data.dropna(axis=0)


y = melbourne_data.Price
features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = melbourne_data[features]
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)


for max_leaf_nodes in [5, 50, 500, 5000]:
    mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print(f'Max leaf nodes: {max_leaf_nodes} \t\t Mean absolute error: {mae}')