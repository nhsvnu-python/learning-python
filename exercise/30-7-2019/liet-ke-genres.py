import pandas as pd
from collections import Counter

df = pd.read_csv("movies.csv")
df_genres = df['genres'].apply(lambda x: x.split('|'))
flat_list = [item for sublist in df_genres for item in sublist]
counter_genres = Counter(flat_list)

print(counter_genres)
