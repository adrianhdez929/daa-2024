import networkx as nx
from itertools import combinations

def is_connected(subgraph, s, D):

    if s not in subgraph:
        return set()

    reachable_nodes = set(nx.single_source_shortest_path_length(subgraph, s).keys())
    
    return D.intersection(reachable_nodes)

def brute_force_repair(G, s, D, P, B):

    best_priority = 0
    best_repaired_edges = set()
    best_connected_nodes = set()
    all_edges = list(G.edges(data=True))

    for k in range(1, len(all_edges) + 1): 
        for edge_subset in combinations(all_edges, k):
            cost = sum(edge[2]['cost'] for edge in edge_subset)
            if cost > B: 
                continue

            subgraph = nx.Graph()
            subgraph.add_edges_from((u, v) for u, v, _ in edge_subset)

            connected_disasters = is_connected(subgraph, s, D)
            total_priority = sum(P[d] for d in connected_disasters)

            if total_priority > best_priority:
                best_priority = total_priority
                best_repaired_edges = {(u, v) for u, v, _ in edge_subset}
                best_connected_nodes = {s}.union(connected_disasters)  
                best_cost = cost

    return best_repaired_edges, best_connected_nodes, best_priority, best_cost
