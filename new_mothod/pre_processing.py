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
        # standard = episodes.tolist()

        # occurrence = {}
        # for i in standard:
        #     occurrence[i] = standard.count(i)

        # occurrence = [occurrence[i] for i in occurrence.keys()]

        # plt.plot(standard)
        # plt.show()
        class_division = {"A": [], "B": [], "C": [], "D": [], "E": []}
        print(f'eps: {eps}')

        for i in eps.keys():
            if 0 <= eps[i][1] <= 50:
                class_division["A"].append(eps[i])
            elif 51 <= eps[i][1] <= 110:
                class_division["B"].append(eps[i])
            elif 111 <= eps[i][1] <= 800:
                class_division["C"].append(eps[i])
            elif 801 <= eps[i][1] <= 1200:
                class_division["D"].append(eps[i])
            else:
                class_division["E"].append(eps[i])
        print(class_division)
        return

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


if __name__ == '__main__':
    DataProcessing().ep()
