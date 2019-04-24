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
        return ranking

    def members(self):
        members = self.file["members"]
        popularity = members.copy().tolist()
        max_value = max(popularity)
        popularity = [value / max_value for value in members]
        return popularity

    def genders(self):
        gender = self.file["genre"]
        values = gender.copy().tolist()
        values = [value.split(',') for value in values if type(value) is str]
        # print(values)
        print(values[0])
        print(type(values[500]))
        '''
        f = open("teste.txt", 'w')
        for i in values:
            if type(i) is not 'str':
                # print(f'i: {i} -> type: {type(i)}')
                x = str(type(i))
                y = str(i)
                f.write(y)
                f.write(x)
                f.write('\n')
                '''
        # print(type(value))
        # print(value)


if "__main__" == __name__:
    DataProcessing().genders()