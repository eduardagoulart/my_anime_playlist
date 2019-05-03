import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances


class DataProcessing:
    def __init__(self):
        self.file = pd.read_csv("anime.csv")
        self.teste = pd.read_csv("base_teste.csv")

    def anime_type(self):
        types = self.file["type"]
        types = [[1 if referential == video_type else 0 for referential in types] for video_type in types]
        return types

    def ep(self):
        episodes = self.file["episodes"]
        for i in range(0, len(episodes)):
            try:
                episodes[i] = int(episodes[i])
            except:
                episodes[i] = 0
        standard = episodes.copy()
        standard = standard.tolist()
        standard.sort(reverse=True)
        max_value = standard[0]
        standard = [value / max_value for value in episodes]
        return standard

    def grades(self):
        grade = self.file['rating']
        ranking = grade.copy().tolist()
        ranking.sort(reverse=True)
        max_value = ranking[0]
        ranking = [value / max_value for value in grade]
        return ranking

    def members(self):
        members = self.file["members"]
        popularity = members.copy().tolist()
        max_value = max(popularity)
        popularity = [value / max_value for value in members]
        return popularity

    @staticmethod
    def vocabulary(vector):
        return np.array(list(vector))

    @staticmethod
    def validation(text, words):
        return [1 if word in text else 0 for word in words]

    @staticmethod
    def cosine_distancy(v, w):
        return np.dot(v, w) / (np.linalg.norm(v) * np.linalg.norm(w))

    def fit_transform(self):
        gender = self.teste["genre"]
        values = gender.copy().tolist()
        values = [value.split(',') for value in values if type(value) is str]
        values = [[va.replace(" ", "") for va in value] for value in values]
        return [[[1 if word in referential else 0 for word in sub_list] for sub_list in values] for referential in
                values]

    def genders(self):
        # @TODO: definir uma equação matemática para a distância entre dois vetores de tamanhos diferentes
        tri_matrix = self.fit_transform()
        matrix = [[euclidean_distances(referential, internal_list) for referential in two_matrix for internal_list in
                   two_matrix] for two_matrix in tri_matrix]
        print(matrix[0])
        return


if "__main__" == __name__:
    # DataProcessing().genders()
    o = DataProcessing()
    o.genders()
