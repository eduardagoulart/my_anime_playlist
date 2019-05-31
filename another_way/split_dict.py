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
        # data_user = [row for row in spamreader]
        for row in spamreader:
            print(row)
        # print(data_user)
        # print(1044 in data_user)
    '''

    user = {}
    for i in data_user:
        print(i)

        value = i[0].split(',')
        if len(value) == 3:
            if value[0] in user.keys():
                user[value[0]].update({value[1]: value[2]})
            else:
                user[value[0]] = {value[1]: value[2]}
                '''


                # print(user.keys())


read('rating.csv')
