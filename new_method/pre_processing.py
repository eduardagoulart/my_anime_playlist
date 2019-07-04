import pandas as pd
import numpy as np


class DataProcessing:

    def __init__(self):
        self.file = pd.read_csv("anime.csv")
        self.test = pd.read_csv("teste.csv")

    @staticmethod
    def amplitute(first, last, sturges_size=5):
        return (last - first) / sturges_size

    @staticmethod
    def max_tuple(list_tuple):
        return max(list_tuple, key=lambda item: item[1])

    @staticmethod
    def cosine_distance(v, w):
        return round(np.dot(v, w) / (np.linalg.norm(v) * np.linalg.norm(w)), 4)

    def normalize_matrix(self, matrix):
        max_in_list = [self.max_tuple(i) for i in matrix]
        max_value = self.max_tuple(max_in_list)
        return [[(j[0], round(j[1] / max_value[1], 2)) for j in i] for i in matrix]

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

        final_list = [[(id_anime[j], sum(i[j])) for j in range(0, len(i)) if id_anime[j] in valid_animes] for i in
                      tri_matrix]

        return self.normalize_matrix(final_list)

    def anime_type(self):
        types = self.test["type"]
        id_anime = self.test["anime_id"]
        valid_animes = self.anime_validation()
        types = [[(id_anime[i], 1) if types[i] == video_type else (id_anime[i], 0) for i in range(0, len(types)) if
                  id_anime[i] in valid_animes] for video_type in types]
        return types

    def ep(self):
        episodes = self.test["episodes"]
        id_anime = self.test["anime_id"]
        valid_animes = self.anime_validation()
        eps = []
        for i in range(0, len(episodes)):
            if id_anime[i] in valid_animes:
                try:
                    eps.append((id_anime[i], int(episodes[i])))
                except:
                    eps.append((id_anime[i], 0))

        return self.discretization(eps)

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

        return self.discretization(ranking)

    def members(self):
        members = self.test["members"]
        id_anime = self.test['anime_id']
        valid_animes = self.anime_validation()
        members_qtd = []
        for i in range(0, len(members)):
            if id_anime[i] in valid_animes:
                members_qtd.append((id_anime[i], members[i]))

        return self.discretization(members_qtd)

    def discretization(self, all_values):
        original_matrix = all_values.copy()
        all_values.sort(key=lambda x: x[1])
        class_size = self.amplitute(all_values[0][1], all_values[-1][1])
        lower_value = all_values[0][1]
        class_division = []

        for i in original_matrix:
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

    def similarity_cosine(self):
        membs = self.members()
        eps = self.ep()
        rating = self.grades()
        animes = [[membs[i], eps[i], rating[i]] for i in range(0, len(membs))]
        animes_without_id = [[j[1] for j in i] for i in animes]
        sim = [[self.cosine_distance(ref, actual) for actual in animes_without_id] for ref in animes_without_id]
        gender = self.genders()
        types = self.anime_type()
        sum_matrix = [
            [(animes[j][0][0], sim[i][j] + gender[i][j][1] + types[i][j][1]) for j in range(0, len(sim[i]))] for i in
            range(0, len(sim))]
        return self.normalize_matrix(sum_matrix)

    @staticmethod
    def similarity_all_for_all(matrix):
        return [[(j[0], round(1 - ((abs(i[1] - j[1])) / 5), 2)) for j in matrix] for i in matrix]

    def sum_matrix_class_disc(self):
        types = self.anime_type()
        gend = self.genders()
        eps = self.similarity_all_for_all(self.discretization(self.ep()))
        membs = self.similarity_all_for_all(self.discretization(self.members()))
        rating = self.similarity_all_for_all(self.discretization(self.grades()))
        return self.sum_matrix(gend, types, eps, membs, rating)

    def sum_matrix(self, gend, types, eps, membs, rating):
        matrix_sum = [
            [(gend[i][j][0], round(types[i][j][1] + gend[i][j][1] + eps[i][j][1] + membs[i][j][1] + rating[i][j][1], 2))
             for j in range(0, len(types[i]))] for i in range(0, len(types))]
        return self.normalize_matrix(matrix_sum)

    def write_file_weigth_matrix(self):
        # values = self.sum_matrix_class_disc()
        values = self.similarity_cosine()
        weight = open("cosine_distance.txt", "w")
        for ref in range(0, len(values)):
            for ultimo in values[ref]:
                if ultimo[1] >= 0.9:
                    t = f'{str(values[ref][ref][0]): <6}{str(ultimo[0]): <6}1'
                    weight.write(t)
                    weight.write('\n')
        weight.close()


if __name__ == '__main__':
    obj = DataProcessing()
    obj.write_file_weigth_matrix()
