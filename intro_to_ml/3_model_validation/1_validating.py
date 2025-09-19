#The Problem with "In-Sample" Scores
# The measure we just computed can be called an "in-sample" score. We used a single "sample" of houses for both building the model and evaluating it. Here's why this is bad.
# Imagine that, in the large real estate market, door color is unrelated to home price.
# However, in the sample of data you used to build the model, all homes with green doors were very expensive.
# The model's job is to find patterns that predict home prices, so it will see this pattern, and it will always predict high prices for homes with green doors.
# Since this pattern was derived from the training data, the model will appear accurate in the training data.
# But if this pattern doesn't hold when the model sees new data, the model would be very inaccurate when used in practice.
# Since models' practical value come from making predictions on new data, we measure performance on data that wasn't used
# to build the model. The most straightforward way to do this is to exclude some data from the model-building process, and
# then use those to test the model's accuracy on data it hasn't seen before. This data is called validation data.

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


melbourne_data = pd.read_csv('../melb_data.csv')
melbourne_data = melbourne_data.dropna(axis=0)

y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]
melbourne_model = DecisionTreeRegressor()

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

melbourne_model.fit(train_X, train_y)

val_predictions = melbourne_model.predict(val_X)

val_mae = mean_absolute_error(val_predictions, val_y)
print(f'Validation MAE: {val_mae}')