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
    return [i for i in list_sim if i[1] >= 0.7]


def playlist(id_ref):
    simillarity_matrix = simillarity.type_gender()
    list_sim = simillarity_list(simillarity_matrix, id_ref)
    list_sim.sort(key=lambda x: x[1], reverse=True)
    playlist_recomendation = [list_sim[i] for i in range(0, 155)]
    print(playlist_recomendation)
    return [list_sim[i] for i in range(0, 155)]


def community(id_ref):
    # :TODO aplicar algoritmo de divisão de comunidade
    print(trace_type_gender(id_ref))
    return


def remove_repet(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l


if __name__ == '__main__':
    try:
        id_video = sys.argv[1]
        # trace_type_gender(int(id_video))
        playlist(int(id_video))
    except:
        print("Argumento inválido")
        exit(404)
