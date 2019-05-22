import simillarity
import sys
import igraph


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


def playlist(id_ref=20):
    simillarity_matrix = simillarity.type_gender()
    list_sim = simillarity_list(simillarity_matrix, id_ref)
    list_sim.sort(key=lambda x: x[1], reverse=True)
    return [list_sim[i] for i in range(0, 155)]


def trace_route():
    file = open('weight.txt', 'r')
    file = file.read().split("\n")
    file = [i.split(" ") for i in file]
    file.pop()

    adj_list = [(adj[0], adj[1], float(adj[2])) for adj in file if
                float(adj[2]) >= 0.9 and adj[0] != adj[1]]

    return remove_repet(adj_list)


def clustering_multilevel():
    graph = igraph.Graph.TupleList(trace_route(), weights=True)
    # graph.vs["label"] = list(map(lambda x: x, open('nodes.txt', 'r')))
    visual_style = {"vertex_size": 20, "bbox": (600, 600), "margin": 20}
    member = graph.community_multilevel(weights=None, return_levels=False)
    print(member)
    igraph.plot(member, **visual_style)
    # graph.add_vertices('nodes.txt')
    # graph.add_edges(trace_route())


def remove_repet(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l


if __name__ == '__main__':
    clustering_multilevel()
    '''
    try:
        id_video = sys.argv[1]
        # trace_type_gender(int(id_video))
        community()
    except:
        print("Argumento inválido")
        exit(404)
        '''
