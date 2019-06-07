import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt


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
        id_anime = self.id_anime()
        eps = {}
        for i in range(0, len(episodes)):
            try:
                eps[i] = (id_anime[i], int(episodes[i]))
            except:
                eps[i] = (id_anime[i], 0)

        # occurrence = {}
        # for i in standard:
        #     occurrence[i] = standard.count(i)

        # occurrence = [occurrence[i] for i in occurrence.keys()]

        # plt.plot(standard)
        # plt.show()
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
        return class_division

    def grades(self):
        grade = self.file['rating']
        id_anime = self.id_anime()
        ranking = {}
        for i in range(0, len(grade)):
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

        class_division = {1: [], 2: [], 3: [], 4: [], 5: []}

        for i in members.keys():
            if 5 <= members[i] <= 1000:
                class_division[1].append(members[i])
            elif 1000 < members[i] <= 50000:
                class_division[2].append(members[i])
            elif 50000 < members[i] <= 100000:
                class_division[3].append(members[i])
            elif 100000 < members[i] <= 500000:
                class_division[4].append(members[i])
            else:
                class_division[5].append(members[i])

        plt.plot(members)
        plt.ylabel("Quantidade de membros")
        plt.xlabel("Quantidade de animes")
        plt.show()
        return class_division


if __name__ == '__main__':
    DataProcessing().grades()
