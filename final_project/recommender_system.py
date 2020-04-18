import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def compare_gender(df):
    return cosine_similarity(df)


if __name__ == "__main__":
    df = pd.read_csv("anime.csv")
    df["type"] = df["type"].replace("nan", np.nan)
    print(len(df))
    try:
        df["genre"] = df["genre"].str.split()
    except:
        pass
    df["episodes"] = df["episodes"].replace("Unknown", np.nan)
    df = df.dropna(subset=["type", "episodes", "rating", "members"])
    print(compare_gender(df[["anime_id", "genre"]]))