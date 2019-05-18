import simillarity
import sys


def list_interval(list_value, id_ref):
    sim = [i[1] for i in list_value if i[0] == id_ref]
    return sim[0] - 0.1, sim[0] + 0.1


def trace_ep_rating_member(id_ref):
    simillarity_list = simillarity.ep_rating_member()
    v_min, v_max = list_interval(simillarity_list, id_ref)
    return [[ad, sim] for ad, sim in simillarity_list if v_min <= sim <= v_max]


def trace_ep_rating(id_ref):
    simillarity_list = simillarity.ep_rating()
    print(len(simillarity_list))
    v_min, v_max = list_interval(simillarity_list, id_ref)
    return [[ad, sim] for ad, sim in simillarity_list if v_min <= sim <= v_max]


def simillarity_list(matrix, id_ref):
    return matrix[id_ref]


def trace_type_gender(id_ref):
    simillarity_matrix = simillarity.type_gender()
    print(simillarity_matrix[20])
    list_sim = simillarity_list(simillarity_matrix, id_ref)
    list_sim = [i for i in list_sim if i[1] >= 0.4]
    # print(list_sim)


if __name__ == '__main__':
    try:
        id_video = sys.argv[1]
        trace_type_gender(int(id_video))
    except Exception as e:
        print("Argumento inválido")
        exit(404)
