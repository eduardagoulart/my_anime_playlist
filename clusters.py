import simillarity


def list_interval(list_value, id_ref):
    sim = [i[1] for i in list_value if i[0] == id_ref]
    return sim[0] - 0.15, sim[0] + 0.15


def trace_ep_rating_member():
    simillarity_list = simillarity.ep_rating_member()
    v_min, v_max = list_interval(simillarity_list, 20)
    return [[ad, sim] for ad, sim in simillarity_list if v_min <= sim <= v_max]


if __name__ == '__main__':
    x = trace_ep_rating_member()
    print(x)