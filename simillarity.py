from pre_processing import DataProcessing
import sys

obj = DataProcessing()
type_animes = obj.anime_type()
qt_ep = obj.ep()
grades = obj.grades()
num_members = obj.members()
gender = obj.normalize_gender().copy()


def ep_rating_member():
    sum_values = [qt_ep[i] + grades[i] + num_members[i] for i in range(0, len(num_members))]
    max_value = max(sum_values)
    return [i / max_value for i in sum_values]


def type_gender():
    sum_values = [[type_animes[i][j] + gender[i][j] for j in range(0, len(type_animes[i]))] for i in
                  range(0, len(type_animes))]
    max_value_list = [max(i) for i in sum_values]
    return [[j / max_value_list[i] for j in sum_values[i]] for i in range(0, len(sum_values))]


def all_values():
    matrix, list_values = type_gender(), ep_rating_member()
    final_matrix = [[internal_list[i] + list_values[i] for i in range(0, len(internal_list))] for internal_list in
                    matrix]
    print(f'ep_rating_member: {list_values}')
    print(f'matrix: {matrix[1]}')
    print(f'resultado final: {final_matrix[1]}')


if __name__ == '__main__':
    all_values()
