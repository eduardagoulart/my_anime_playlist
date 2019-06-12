from pre_processing import DataProcessing
import numpy as np

obj = DataProcessing()
type_animes = obj.anime_type()
qt_ep = obj.ep()
grades = obj.rating()
num_members = obj.members()
gender = obj.normalize_gender().copy()
id_anime = obj.id_anime()
'''
nodes = open('nodes.txt', 'w')
for i in id_anime:
    nodes.write(str(i))
    nodes.write('\n')'''


def cosine_distance(v, w):
    return np.dot(v, w) / (np.linalg.norm(v) * np.linalg.norm(w))


def ep_mem_rating():
    anime_value = [[qt_ep[i], num_members[i], grades[i]] for i in range(0, len(qt_ep))]
    anime_distance = [[cosine_distance(ref, actual) for actual in anime_value] for ref in anime_value]
    print(anime_value)


ep_mem_rating()
'''------------------------------ MATRIX -----------------------------------------------------------'''


def normalize_matrix(sum_values):
    max_value_list = [max(i) for i in sum_values]
    return [[j / max_value_list[i] for j in sum_values[i]] for i in range(0, len(sum_values))]


def add_id_matrix(list_values):
    return [[(int(id_anime[j]), list_values[i][j]) for j in
             range(0, len(list_values[i]))] for i in range(0, len(list_values))]


def type_gender():
    return [[type_animes[i][j] + gender[i][j] for j in range(0, len(type_animes[i]))] for i in
            range(0, len(type_animes))]


def type_gender_id():
    values = type_gender()
    return add_id_matrix(values)


def all_values():
    matrix, list_values = type_gender(), ep_rating_member()
    final_matrix = [[internal_list[i] + list_values[i] for i in range(0, len(internal_list))] for internal_list in
                    matrix]
    max_value_list = [max(i) for i in final_matrix]
    max_value = max(max_value_list)
    return [[j / max_value for j in final_matrix[i]] for i in range(0, len(final_matrix))]


def all_values_with_id():
    values = all_values()
    return add_id_matrix(values)


def write_file_weigth_matrix():
    values = all_values_with_id()
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
