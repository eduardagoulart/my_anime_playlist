import pandas as pd

df = pd.read_csv('rating.csv')
anime_id = []
for i in df['user_id']:
    if i not in anime_id:
        anime_id.append(i)

print(anime_id)
