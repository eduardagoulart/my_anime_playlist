import csv


def read_file(file):
    user = {}
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        # user[spamreader[0]] = {spamreader[1]: spamreader[2]}
        data_user = [row for row in spamreader]
        for i in data_user:
            value = i[0].split(',')
            if len(value) == 3:
                user[value[0]] = {value[1]: value[2]}

    print(user)


read_file('rating.csv')
