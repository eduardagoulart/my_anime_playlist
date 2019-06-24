import pandas as pd
import numpy as np
import math


class DataProcessing:

    def __init__(self):
        self.file = pd.read_csv("anime.csv")
        self.test = pd.read_csv("teste.csv")

    @staticmethod
    def amplitute(first, last, sturges_size=5):
        return (last - first) / sturges_size

    def anime_validation(self):
        gender = self.test["genre"]
        id_anime = self.test["anime_id"]
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
        gender = self.test["genre"]
        id_anime = self.test["anime_id"]

        list_gender = [gender[i].split(",") for i in range(0, len(gender)) if id_anime[i] in valid_animes]
        list_gender = [[va.replace(" ", "") for va in value] for value in list_gender]

        tri_matrix = [[[1 if word in referential else 0 for word in sub_list] for sub_list in list_gender] for
                      referential in list_gender]

        final_list = {}
        for i in range(0, len(tri_matrix)):
            final_list[id_anime[i]] = []
            for j in range(0, len(tri_matrix[i])):
                soma = 0
                for k in range(0, len(tri_matrix[i][j])):
                    soma += tri_matrix[i][j][k]
                if id_anime[j] in valid_animes:
                    final_list[id_anime[i]].append((id_anime[j], soma))

        return final_list

    # @TODO: analisar se esta informação é útil e como testar
    def anime_type(self):
        types = self.test["type"]
        types = [[1 if referential == video_type else 0 for referential in types] for video_type in types]
        return types

    def ep(self):
        episodes = self.file["episodes"]
        id_anime = self.file["anime_id"]
        valid_animes = self.anime_validation()
        eps = []
        for i in range(0, len(episodes)):
            if id_anime[i] in valid_animes:
                try:
                    eps.append((id_anime[i], int(episodes[i])))
                except:
                    eps.append((id_anime[i], 0))

        print(self.similarity_all_for_all(self.discretization(eps)))

        return

    def grades(self):
        grade = self.test['rating']
        id_anime = self.test['anime_id']
        valid_animes = self.anime_validation()
        ranking = []
        for i in range(0, len(grade)):
            if id_anime[i] in valid_animes:
                try:
                    ranking.append((id_anime[i], int(grade[i])))
                except:
                    ranking.append((id_anime[i], 0))

        return self.similarity_all_for_all(self.discretization(ranking))

    def members(self):
        members = self.test["members"]
        id_anime = self.test['anime_id']
        valid_animes = self.anime_validation()
        members_qtd = []
        for i in range(0, len(members)):
            if id_anime[i] in valid_animes:
                members_qtd.append((id_anime[i], members[i]))

        return self.similarity_all_for_all(self.discretization(members_qtd))

    def discretization(self, all_values):
        all_values.sort(key=lambda x: x[1])
        class_size = self.amplitute(all_values[0][1], all_values[-1][1])
        lower_value = all_values[0][1]
        class_division = []

        for i in all_values:
            if lower_value <= i[1] <= lower_value + class_size:
                class_division.append((i[0], 1))
            elif lower_value + class_size < i[1] <= lower_value + (class_size * 2):
                class_division.append((i[0], 2))
            elif lower_value + (class_size * 2) < i[1] <= lower_value + (class_size * 3):
                class_division.append((i[0], 3))
            elif lower_value + (class_size * 3) < i[1] <= lower_value + (class_size * 4):
                class_division.append((i[0], 4))
            elif lower_value + (class_size * 4) < i[1] <= lower_value + (class_size * 5):
                class_division.append((i[0], 5))

        return class_division

    @staticmethod
    def similarity_all_for_all(matrix):
        return [[(j[0], round(1 - ((abs(i[1] - j[1])) / 5), 2)) for j in matrix] for i in matrix]


if __name__ == '__main__':
    DataProcessing().ep()
