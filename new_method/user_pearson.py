import csv
from pre_processing import DataProcessing


def read_csv():
    with open('user.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        data_user = [row for row in spamreader]

    user = {}
    for i in data_user:

        if i[0] in user.keys():
            user[i[0]].update({i[1]: i[2]})
        else:
            user[i[0]] = {i[1]: i[2]}
    return user


def transform_matrix():
    matrix = DataProcessing().sum_matrix_class_disc()
    fit = {}
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if i == j:
                fit[matrix[i][0]] = matrix[i]

    print(fit)


transform_matrix()
