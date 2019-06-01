import csv


def read(file='rating.csv'):
    with open(file) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        data_user = [row for row in spamreader]

    user = {}
    for i in data_user:

        if i[0] in user.keys():
            user[i[0]].update({i[1]: i[2]})
            print('usuário já existe')
        else:
            user[i[0]] = {i[1]: i[2]}
            print('novo usuário')
    return user