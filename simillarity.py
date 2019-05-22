from pre_processing import DataProcessing

obj = DataProcessing()
type_animes = obj.anime_type()
qt_ep = obj.ep()
grades = obj.grades()
num_members = obj.members()
gender = obj.normalize_gender().copy()
id_anime = obj.id_anime()


def normalize_list(sum_values):
    max_value = max(sum_values)
    return [i / max_value for i in sum_values]


def add_id_list(list_values):
    return [[int(id_anime[i]), list_values[i]] for i in range(0, len(list_values))]


def ep_rating_member():
    return [qt_ep[i] + grades[i] + num_members[i] for i in range(0, len(num_members))]


def ep_rating():
    return [qt_ep[i] + grades[i] for i in range(0, len(num_members))]


def ep_member():
    sum_values = [qt_ep[i] + num_members[i] for i in range(0, len(num_members))]
    return add_id_list(normalize_list(sum_values))


def rating_member():
    sum_values = [grades[i] + num_members[i] for i in range(0, len(num_members))]
    return add_id_list(normalize_list(sum_values))


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


def all_values():
    matrix, list_values = type_gender(), ep_rating_member()
    final_matrix = [[internal_list[i] + list_values[i] for i in range(0, len(internal_list))] for internal_list in
                    matrix]
    max_value_list = [max(i) for i in final_matrix]
    return [[j / max_value_list[i] for j in final_matrix[i]] for i in range(0, len(final_matrix))]


def all_values_with_id():
    values = all_values()
    return add_id_matrix(values)


def write_file_weigth_matrix():
    values = all_values_with_id()
    weight = open("weight.txt", "w")
    for ref in range(0, len(values)):
        for ultimo in values[ref]:
            pass
            # print(ultimo)
            # print(ultimo[ref])
            weight.write(str(values[ref][ref][0]))
            weight.write(" ")
            weight.write(str(ultimo[0]))
            weight.write(str(" "))
            weight.write(str(ultimo[1]))
            weight.write("\n")
    weight.close()


if __name__ == '__main__':
    write_file_weigth_matrix()
