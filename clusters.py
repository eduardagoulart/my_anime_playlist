import simillarity


def ep_rating_member_id():
    id_anime = simillarity.obj.id_anime()
    simillarity_list = simillarity.ep_rating_member()
    return [[int(id_anime[i]), simillarity_list[i]] for i in range(0, len(simillarity_list))]


def trace_ep_rating_member():
    simillarity_list = ep_rating_member_id()
    final_cluster = [[ad, sim] for ad, sim in simillarity_list if 0.6 <= sim <= 1.0]
    print(final_cluster)
    for i in simillarity_list:
        if i[0] == 24:
            print(f'24: {i}')


if __name__ == '__main__':
    trace_ep_rating_member()
