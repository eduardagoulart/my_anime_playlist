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
        episodes = episodes.copy()
        for i in range(0, len(episodes)):
            try:
                episodes[i] = int(episodes[i])
            except:
                episodes[i] = 0
        standard = episodes.tolist()
        print(standard)
        '''
        x = np.random.randn(len(standard))
        plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)
        plt.axis(len(standard))
        plt.xlabel("Número do anime")
        plt.ylabel('Quantidade de epsódios')
        plt.grid(True)'''

        plt.plot(standard)
        plt.show()
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
