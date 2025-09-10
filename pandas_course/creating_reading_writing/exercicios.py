import pandas as pd

#1
fruits = pd.DataFrame({'Apples': [30], 'Bananas': [21]})
print(fruits, '\n')

#2
fruit_sales = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index=['2017 Sales', '2018 Sales'])
print(fruit_sales, '\n')

#3
ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')
print(ingredients, '\n')

#4
wine_reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)
print(wine_reviews.head(), '\n')

#5
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22,19]}, index=['Year 1', 'Year 2'])
print(animals, '\n')
animals.to_csv('animals.csv', index=False)