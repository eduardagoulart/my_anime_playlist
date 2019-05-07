import pandas as pd


class NewFile:

    def procces(self):
        df = pd.read_csv("anime.csv")
        gender = df["genre"]
        file = gender.copy().tolist()
        for value in range(0, len(gender)):
            # print(type(df["genre"][i]))
            # print(type(value))
            if type(file[value]) is str:
                print("OPPPA PASSANDO AQUI")
                # file.append(type(value))
                # print(f'df[] -> {value}')

            #     print(df[i])
            #     df[i] = df[i]
        # print(df)


if __name__ == "__main__":
    NewFile().procces()