import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class DataProcessing:

    def __init__(self):
        self.file = pd.read_csv("anime.csv")

    def fit_transform(self):
        gender = self.file["genre"]
        id_anime = self.file["anime_id"]
        values = gender.copy().tolist()
        list_gender = []
        for i in range(0, len(values)):
            try:
                list_gender.append((id_anime[i], values[i].split(",")))
            except:
                pass

        return [[(value[0], va.replace(" ", "")) for va in value[1]] for value in list_gender], [value[0] for value in
                                                                                                 list_gender]

    # @TODO: testar a saída dessa função: killed
    def genders(self):
        gender_list, _ = self.fit_transform()
        tri_matrix = [[[1 if word in referential else 0 for word in sub_list] for sub_list in gender_list] for
                      referential in
                      gender_list]
        final_list = []
        for two_matrix in tri_matrix:
            sum_list = []
            for internal_list in two_matrix:
                soma = 0
                for values in internal_list:
                    soma += values
                sum_list.append(soma)
            final_list.append(sum_list)
        print(final_list)
        return final_list

    # @TODO: analisar se esta informação é útil e como testar
    def anime_type(self):
        types = self.file["type"]
        types = [[1 if referential == video_type else 0 for referential in types] for video_type in types]
        return types

    def ep(self):
        episodes = self.file["episodes"]
        id_anime = self.file["anime_id"]
        _, valid_animes = self.fit_transform()
        eps = {}
        for i in range(0, len(episodes)):
            if id_anime[i] in valid_animes:
                try:
                    eps[i] = (id_anime[i], int(episodes[i]))
                except:
                    eps[i] = (id_anime[i], 0)

        class_division = {1: [], 2: [], 3: [], 4: [], 5: []}

        for i in eps.keys():
            if 0 <= eps[i][1] <= 50:
                class_division[1].append(eps[i])
            elif 51 <= eps[i][1] <= 110:
                class_division[2].append(eps[i])
            elif 111 <= eps[i][1] <= 800:
                class_division[3].append(eps[i])
            elif 801 <= eps[i][1] <= 1200:
                class_division[4].append(eps[i])
            else:
                class_division[5].append(eps[i])
        print(class_division)
        return class_division

    def grades(self):
        grade = self.file['rating']
        id_anime = self.file['anime_id']
        _, valid_animes = self.fit_transform()
        ranking = {}
        for i in range(0, len(grade)):
            if id_anime[i] in valid_animes:
                try:
                    ranking[i] = (id_anime[i], int(grade[i]))
                except:
                    ranking[i] = (id_anime[i], 0)

        class_division = {1: [], 2: [], 3: [], 4: [], 5: []}

        for i in ranking.keys():
            if 0 <= ranking[i][1] <= 2:
                class_division[1].append(ranking[i])
            elif 2 < ranking[i][1] <= 4:
                class_division[2].append(ranking[i])
            elif 4 < ranking[i][1] <= 6:
                class_division[3].append(ranking[i])
            elif 6 < ranking[i][1] <= 8:
                class_division[4].append(ranking[i])
            elif 8 < ranking[i][1] <= 10:
                class_division[5].append(ranking[i])
        print(class_division)
        return class_division

    def members(self):
        members = self.file["members"]
        id_anime = self.file['anime_id']
        _, valid_animes = self.fit_transform()
        members_qtd = {}
        for i in range(0, len(members)):
            if id_anime[i] in valid_animes:
                members_qtd[i] = (id_anime[i], members[i])

        class_division = {1: [], 2: [], 3: [], 4: [], 5: []}

        for i in members_qtd.keys():
            if 5 <= members_qtd[i][1] <= 1000:
                class_division[1].append(members_qtd[i])
            elif 1000 < members_qtd[i][1] <= 50000:
                class_division[2].append(members_qtd[i])
            elif 50000 < members_qtd[i][1] <= 100000:
                class_division[3].append(members_qtd[i])
            elif 100000 < members_qtd[i][1] <= 500000:
                class_division[4].append(members_qtd[i])
            else:
                class_division[5].append(members_qtd[i])

        # plt.plot(members)
        # plt.ylabel("Quantidade de membros")
        # plt.xlabel("Quantidade de animes")
        # plt.show()
        print(class_division)
        return class_division


if __name__ == '__main__':
    DataProcessing().members()
