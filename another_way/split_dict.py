import csv
from pandas import read_csv


def read(file):
    # spamreader = open('rating.csv', 'r')
    # spamreader = csv.reader(spamreader, )
    # for row in spamreader:
    #     print(row)
    # spamreader = read_csv(file)
    # for i in spamreader['user_id']:
    #    print(i)

    with open(file) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        # user[spamreader[0]] = {spamreader[1]: spamreader[2]}
        data_user = [row for row in spamreader]

        # print(data_user)
        # print(1044 in data_user)

    user = {}
    for i in data_user:
        

        # value = i[0].split(',')

        if i[0] in user.keys():
            user[i[0]].update({i[1]: i[2]})
            print('usuário já existe')
        else:
            user[i[0]] = {i[1]: i[2]}
            print('novo usuário')
    print(f'opa: {user}')


read('rating.csv')
