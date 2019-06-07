import pandas as pd
import math
import numpy as np


class DataProcessing:
    def __init__(self):
        self.file = pd.read_csv("anime.csv")
        self.teste = pd.read_csv("base_teste.csv")

    def id_anime(self):
        return self.file["anime_id"]

    @staticmethod
    def cosine_distance(v, w):
        return np.dot(v, w) / (np.linalg.norm(v) * np.linalg.norm(w))

    def anime_type(self):
        types = self.teste["type"]
        print(types[5])
        types = [[1 if referential == video_type else 0 for referential in types] for video_type in types]
        return types

    def ep(self):
        episodes = self.file["episodes"]
        episodes = episodes.copy()
        for i in range(0, len(episodes)):
            try:
                episodes[i] = int(episodes[i])
            except:
                episodes[i] = 0
        standard = episodes.tolist()
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
        return [0 if math.isnan(value) else value for value in ranking]

    def members(self):
        members = self.file["members"]
        popularity = members.copy().tolist()
        max_value = max(popularity)
        popularity = [value / max_value for value in members]
        print(popularity)
        return popularity

    def fit_transform(self):
        gender = self.teste["genre"]
        values = gender.copy().tolist()
        values = [value.split(',') for value in values]
        values = [[va.replace(" ", "") for va in value] for value in values]
        return [[[1 if word in referential else 0 for word in sub_list] for sub_list in values] for referential in
                values]

    def genders(self):
        tri_matrix = self.fit_transform()
        final_list = []
        for two_matrix in tri_matrix:
            sum_list = []
            for internal_list in two_matrix:
                soma = 0
                for values in internal_list:
                    soma += values
                sum_list.append(soma)
            final_list.append(sum_list)
        return final_list

    def normalize_gender(self):
        matrix = self.genders()
        list_max = [max(internal_list) for internal_list in matrix]
        max_value = max(list_max)
        return [[matrix[i][j] / max_value for j in range(0, len(matrix[i]))] for i in range(0, len(matrix))]


if __name__ == '__main__':
    DataProcessing().members()
