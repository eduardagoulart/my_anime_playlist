import pandas as pd


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
        print(ranking)
        return ranking


if "__main__" == __name__:
    DataProcessing().grades()