import pandas as pd
import _pickle as pickle


data = pd.read_csv('rating.csv')
anime_id = []
for i in data['user_id']:
    if i not in anime_id:
        anime_id.append(i)

df = pd.DataFrame(data, index=['user_id', 'anime_id', 'rating'])

df_filter = {}
for i in anime_id:
    df_filter[i] = [(df.user_id == i)]

print(df_filter)

with open('file.txt', 'w') as file:
    file.write(pickle.dumps(df_filter))

