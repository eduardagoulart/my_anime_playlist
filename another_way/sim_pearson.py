from math import sqrt


def sim(users, p1, p2):
    # p1, p2 = int(p1), int(p2)
    
    print(users[p1])
    print(users[p2])
    si = {}
    for item in users[p1]:
        if item in users[p2]:
            si[item] = 1

    qtd_sim = len(si)

    if qtd_sim == 0:
        return 0
    print(f'Dicionário de similaridade: {si}')
    try:
        sum1 = sum([users[p1][item] for item in si])
        sum2 = sum([users[p2][item] for item in si])
    except:
        sum1 = users[p1][1]
        sum2 = users[p2][1]
    squares_sum1 = sum([pow(users[p1][item], 2) for item in si])
    squares_sum2 = sum([pow(users[p2][item], 2) for item in si])

    product_sum = sum([users[p1][item] * users[p2][item] for item in si])

    num = product_sum - (sum1 * sum2 / qtd_sim)
    den = sqrt((squares_sum1 - pow(sum1, 2) / qtd_sim) * (squares_sum2 - pow(sum2, 2) / qtd_sim))
    if den == 0:
        return 0

    return num / den
