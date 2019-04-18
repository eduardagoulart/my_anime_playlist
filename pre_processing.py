import pandas as pd


class DataProcessing:
    def __init__(self):
        self.file = pd.read_csv("anime.csv")

    def anime_type(self):
        types = self.file["type"]
        types = [[1 if referential == video_type else 0 for referential in types] for video_type in types]
        # print(types)
        return types


if "__main__" == __name__:
    DataProcessing().anime_type()