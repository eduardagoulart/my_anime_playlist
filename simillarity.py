from pre_processing import DataProcessing
import numpy as np
from scipy.spatial import distance

obj = DataProcessing()
type_animes = obj.anime_type()
qt_ep = obj.ep()
grades = obj.rating()
num_members = obj.members()
gender = obj.gender()
id_anime = obj.id_anime()

nodes = open('nodes.txt', 'w')
for i in id_anime:
    nodes.write(str(i))
    nodes.write('\n')


def cosine_distance(v, w):
    return np.dot(v, w) / (np.linalg.norm(v) * np.linalg.norm(w))


def ep_mem_rating():
    anime_value = [[qt_ep[i], num_members[i], grades[i]] for i in range(0, len(qt_ep))]
    return [[1 - distance.cosine(ref, actual) for actual in anime_value] for ref in anime_value]


def add_id_matrix(list_values):
    return [[(int(id_anime[j]), list_values[i][j]) for j in
             range(0, len(list_values[i]))] for i in range(0, len(list_values))]


def type_gender():
    return [[type_animes[i][j] + gender[i][j] for j in range(0, len(type_animes[i]))] for i in
            range(0, len(type_animes))]


def all_values():
    mem_ep_rating = ep_mem_rating()
    final_matrix = [[type_animes[i][j] + gender[i][j] + mem_ep_rating[i][j] for j in range(0, len(gender[i]))] for i in
                    range(0, len(gender))]
    max_value_list = [max(i) for i in final_matrix]
    max_value = max(max_value_list)
    return [[j / max_value for j in final_matrix[i]] for i in range(0, len(final_matrix))]


def write_file_weigth_matrix():
    values = add_id_matrix(all_values())
    # print(values)
    # values = type_gender_id()

    weight = open("type_gender.txt", "w")
    for ref in range(0, len(values)):
        for ultimo in values[ref]:
            if ultimo[1] >= 0.9:
                t = f'{str(values[ref][ref][0]): <6}{str(ultimo[0]): <6}1'
                weight.write(t)
                weight.write('\n')

            '''weight.write(str(values[ref][ref][0]))
            weight.write(" ")
            weight.write(str(ultimo[0]))
            weight.write(str(" "))
            weight.write(str(ultimo[1]))
            weight.write("\n")'''
    weight.close()

write_file_weigth_matrix()