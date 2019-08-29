import pandas as pd
from collections import Counter

movies = pd.read_csv("movies.csv")

# Extract column year
movies["year"] = movies["title"].apply(lambda x: x[-5:-1])

# Select movie in year 1995
movies_1995 = movies[movies.year == '1930']

pd.options.mode.chained_assignment = None
# See this https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas
genres_list = movies_1995["genres"].apply(lambda x: x.split('|'))


flat_list = [item for sublist in genres_list for item in sublist]
'''
#https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
flat_list = []
for sublist in l:
    for item in sublist:
        flat_list.append(item)
'''

# Count genres element
counter_genres = Counter(flat_list)

print(counter_genres)
# Print most common genres
print(counter_genres.most_common(1))