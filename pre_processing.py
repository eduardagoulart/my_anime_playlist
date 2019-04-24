import pandas as pd
import numpy as np


class DataProcessing:
    def __init__(self):
        self.file = pd.read_csv("anime.csv")

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
    def cosine_similarity(v, w):
        return np.dot(v, w) / (np.linalg.norm(v) * np.linalg.norm(w))

    # @TODO: cada lista será um vocabulário em determinado momento
    def gender_simillarity(self):
        pass

    def genders(self):
        gender = self.file["genre"]
        values = gender.copy().tolist()
        values = [value.split(',') for value in values if type(value) is str]
        # lista = [[[1 if valor in referential else 0 for valor in sub_lista] for sub_lista in values] for referential in
        #          values]
        # print(lista[0][0])
        # print(lista[0][1])
        a = []
        for referential in values:
            for sub_lista in values:
                for v in sub_lista:
                    if v in referential:
                        a.append([referential, sub_lista, v])
        print(a[0])
        '''
        soma = 0
        for i in values:
            for j in values:
                for k in j:
                    if k in i:
                        soma += 1
                        print(f'lista: {j} -> valor: {k} -> referencial: {i}')
                lista.append(soma)
                soma = 0
        print(soma)
        '''


if "__main__" == __name__:
    DataProcessing().genders()
