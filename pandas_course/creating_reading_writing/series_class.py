import pandas as pd

s1 = pd.Series([1, 2, 3, 4, 5])
print(s1, '\n')
print(s1.__dict__, '\n')
print(dir(s1), '\n')

s2 = pd.Series([2000, 1250, 1565], index=[2023, 2024, 2025], name='Product A production each year')
print(s2)