import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compare_gender(df):
    vectorizer = TfidfVectorizer()
    corpus = [df.genre[1], df.genre[2]]
    print(corpus)
    trsfm=vectorizer.fit_transform(corpus)
    print(cosine_similarity(trsfm[0:1], trsfm))


if __name__ == "__main__":
    df = pd.read_csv("anime.csv")
    df["type"] = df["type"].replace("nan", np.nan)
    df["genre"] = df["genre"].replace(" ", "")
    print(len(df))
    df["episodes"] = df["episodes"].replace("Unknown", np.nan)
    df = df.dropna(subset=["type", "episodes", "rating", "members"])
    aux = compare_gender(df[["anime_id", "genre"]])
