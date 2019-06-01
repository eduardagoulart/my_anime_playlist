from split_dict import read
from math import sqrt


def sim(users, p1, p2):
    si = {}
    for item in users[p1]:
        if item in users[p2]:
            si[item] = 1

    qtd_sim = len(si)
    print(qtd_sim)
