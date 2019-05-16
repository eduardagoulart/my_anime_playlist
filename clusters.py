import simillarity


def ep_rating_member_cluster():
    id_anime = simillarity.obj.id_anime()
    simillarity_list = simillarity.ep_rating_member()
    return [[id_anime[i], simillarity_list[i]] for i in range(0, len(simillarity_list))]


if __name__ == '__main__':
    ep_rating_member_cluster()
