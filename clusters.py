import simillarity
import sys


def list_interval(list_value, id_ref):
    sim = [i[1] for i in list_value if i[0] == id_ref]
    return sim[0] - 0.1, sim[0] + 0.1


def trace_list(param, id_ref):
    if param == "ep_member":
        list_simillarity = simillarity.ep_rating_member()
    elif param == "ep_rating":
        list_simillarity = simillarity.ep_rating()
    elif param == "ep_rating_member":
        list_simillarity = simillarity.ep_rating_member()
    elif param == "ep_member":
        list_simillarity = simillarity.ep_member()
    else:
        list_simillarity = simillarity.rating_member()
        
    v_min, v_max = list_interval(list_simillarity, id_ref)
    return [[ad, sim] for ad, sim in list_simillarity if v_min <= sim <= v_max]


def simillarity_list(matrix, id_ref):
    return matrix[id_ref]


def trace_type_gender(id_ref):
    simillarity_matrix = simillarity.type_gender()
    list_sim = simillarity_list(simillarity_matrix, id_ref)
    return [i for i in list_sim if i[1] >= 0.9]


if __name__ == '__main__':
    try:
        id_video = sys.argv[1]
        trace_type_gender(int(id_video))
    except Exception as e:
        print("Argumento inválido")
        exit(404)
