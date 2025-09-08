import pandas as pd

#DataFrame class
df1 = pd.DataFrame({'x': [50, 30], 'y': [10, 20]})
print(df1, '\n')
print(type(df1), '\n')
print(df1.__dict__, '\n')
print(dir(df1), '\n')

df2 = pd.DataFrame({'Mateus': ['sim', 'nao', 'sim'], 'Marcinha': ['nao', 'sim', 'nao']})
print(df2, '\n')

df3 = pd.DataFrame({'Mateus': ['sim', 'nao', 'sim'], 'Marcinha': ['nao', 'sim', 'nao']}, index= ['Produto A', 'Produto B', 'Produto C'])
print(df3, '\n')