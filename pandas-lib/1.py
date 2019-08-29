import pandas as pd
from collections import Counter

movies = pd.read_csv("movies.csv")

# Extract column year
movies["year"] = movies["title"].apply(lambda x: x[-5:-1])

# Select movie in year 1995
movies_1995 = movies[movies.year == '1995']

pd.options.mode.chained_assignment = None
# See this https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas
genres_list = movies_1995["genres"].apply(lambda x: x.split('|'))


flat_list = [item for sublist in genres_list for item in sublist]
print(Counter(flat_list))