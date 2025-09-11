import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)

# subtraindo os pontos de cada row de um objeto series pela média dos pontos (esse map é um metodo de series)
print(wine_reviews.points.map(lambda r: r - wine_reviews.points.mean()), '\n' *10)

# fazendo a msm coisa mas usando um metodo do objeto dataframe
mapped_reviews = wine_reviews.apply(lambda r: r.points - wine_reviews.points.mean(), axis=1) # axix=1 aplica a função em cada row, axis=0 aplica em cada coluna
print(mapped_reviews)
print(type(mapped_reviews), '\n' * 10)

# mas agr fazendo retornar um objeto dataframe
def subtract_mean(row):
    row.points = row.points - wine_reviews.points.mean()
    return row

mapped_reviews = wine_reviews.apply(subtract_mean, axis=1)
print(mapped_reviews)
print(type(mapped_reviews), '\n' * 10)

# ambos metodos retornam novos objetos de dataframe ou series sem modificar o wine_reviews original

# agr um jeito bem mais simples de fazer um .map()

print(wine_reviews.points - wine_reviews.points.mean(), '\n' * 10)

# However, they are not as flexible as map() or apply(), which can do more advanced things, like applying conditional
# logic, which cannot be done with addition and subtraction alone.