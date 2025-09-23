import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=1)
    model.fit(train_X, train_y)
    predictions = model.predict(val_X)
    mae = mean_absolute_error(predictions, val_y)
    return mae


iowa_data = pd.read_csv('../train.csv', index_col='Id')
y = iowa_data.SalePrice
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = iowa_data[features]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

mae_results = []
max_leaf_nodes_list = [5, 25, 50, 100, 250, 500]
for max_leaf_nodes in max_leaf_nodes_list:
    mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    mae_results.append(mae)
    print(f'Max leaf nodes: {max_leaf_nodes}, MAE: {mae}')
best_tree_size = max_leaf_nodes_list[mae_results.index(min(mae_results))]
print(f'Best tree size: {best_tree_size}')





final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=1)
final_model.fit(X, y)