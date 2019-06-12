import pandas as pd
import math
import numpy as np


class DataProcessing:
    def __init__(self):
        self.file = pd.read_csv("anime.csv")
        self.teste = pd.read_csv("base_teste.csv")

    def id_anime(self):
        return self.teste["anime_id"]

    def anime_validation(self):
        gender = self.teste["genre"]
        id_anime = self.id_anime()
        values = gender.copy().tolist()
        list_gender = []
        for i in range(0, len(values)):
            try:
                list_gender.append((id_anime[i], gender[i].split(",")))
            except:
                pass

        return [value[0] for value in list_gender]

    def ep(self):
        episodes = self.teste["episodes"]
        episodes = episodes.copy()
        for i in range(0, len(episodes)):
            try:
                episodes[i] = int(episodes[i])
            except:
                episodes[i] = 0
        standard = episodes.tolist()
        # max_value = max(standard)
        return standard

    def rating(self):
        grade = self.teste['rating']
        ranking = grade.copy().tolist()
        max_value = max(ranking)
        # ranking = [value / max_value for value in grade]
        return [0 if math.isnan(value) else value for value in ranking]

    def members(self):
        members = self.teste["members"]
        popularity = members.copy().tolist()
        max_value = max(popularity)
        return popularity

    def fit_transform(self):
        gender = self.teste["genre"]
        values = gender.copy().tolist()
        values = [value.split(',') for value in values]
        values = [[va.replace(" ", "") for va in value] for value in values]
        return [[[1 if word in referential else 0 for word in sub_list] for sub_list in values] for referential in
                values]

    def anime_validation(self):
        gender = self.teste["genre"]
        id_anime = self.teste["anime_id"]
        values = gender.copy().tolist()
        list_gender = []
        for i in range(0, len(values)):
            try:
                list_gender.append((id_anime[i], gender[i].split(",")))
            except:
                pass

        return [value[0] for value in list_gender]

    def genders(self):
        valid_animes = self.anime_validation()
        gender = self.teste["genre"]
        id_anime = self.teste["anime_id"]

        # gender_id = [(id_anime[i], gender[i].split(",")) for i in range(0, len(gender)) if id_anime[i]
        # in valid_animes]
        list_gender = [gender[i].split(",") for i in range(0, len(gender)) if id_anime[i] in valid_animes]
        # gender_id = [[(value[0], va.replace(" ", "")) for va in value[1]] for value in gender_id]
        list_gender = [[va.replace(" ", "") for va in value] for value in list_gender]

        tri_matrix = [[[1 if word in referential else 0 for word in sub_list] for sub_list in list_gender] for
                      referential in list_gender]

        final_list = []
        for i in range(0, len(tri_matrix)):
            final_list[id_anime[i]] = []
            for j in range(0, len(tri_matrix[i])):
                soma = 0
                for k in range(0, len(tri_matrix[i][j])):
                    soma += tri_matrix[i][j][k]
                if id_anime[j] in valid_animes:
                    final_list[i].append((id_anime[j], soma))

        class_division = {}
        for i in final_list.keys():
            class_division[i] = {1: [], 2: [], 3: [], 4: [], 5: []}
            for j in final_list[i]:
                if 0 <= j[1] <= 2:
                    class_division[i][1].append(j)
                elif 2 < j[1] <= 4:
                    class_division[i][2].append(j)
                elif 4 < j[1] <= 6:
                    class_division[i][3].append(j)
                elif 6 < j[1] <= 8:
                    class_division[i][4].append(j)
                else:
                    class_division[i][5].append(j)

        return final_list

    def gender(self):
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

    def anime_type(self):
        types = self.teste["type"]
        types = [[1 if referential == video_type else 0 for referential in types] for video_type in types]
        return types


if __name__ == '__main__':
    obj = DataProcessing()
    print(obj.rating())
