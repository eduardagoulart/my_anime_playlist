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


def all_values(ref_id):
    obj = DataProcessing()
    type_animes = obj.anime_type()
    qt_ep = obj.ep()
    grades = obj.grades()
    num_members = obj.members()
    gender = obj.normalize_gender().copy()


if __name__ == '__main__':
    type_gender()
