import pandas as pd

wine_reviews = pd.read_csv('../winemag-data-130k-v2.csv', index_col=0)
print(wine_reviews.loc[0, 'country'], '\n' * 10)
print(wine_reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']])
print(wine_reviews.loc[:10, ['taster_name', 'taster_twitter_handle', 'points']]) #no loc[x:y], y é incluído

#iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one
# excluded. So 0:10 will select entries 0,...,9. loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.

#Why the change? Remember that loc can index any stdlib type: strings, for example. If we have a DataFrame with index
# values Apples, ..., Potatoes, ..., and we want to select "all the alphabetical fruit choices between Apples and Potatoes",
# then it's a lot more convenient to index df.loc['Apples':'Potatoes'] than it is to index something like df.loc['Apples', 'Potatoet'] (t coming after s in the alphabet).

#This is particularly confusing when the DataFrame index is a simple numerical list, e.g. 0,...,1000. In this case
# df.iloc[0:1000] will return 1000 entries, while df.loc[0:1000] return 1001 of them! To get 1000 elements using loc, you will need to go one lower and ask for df.loc[0:999].
#Otherwise, the semantics of using loc are the same as those for iloc.