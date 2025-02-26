import networkx as nx
import itertools
from collections import deque

def bfs_connected_nodes(G, s):
    visited = set()
    queue = deque([s])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor in G.neighbors(node):
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited

def brute_force_solution(G, s, D, P, B):
    edge_list = list(G.edges(data='cost'))
    best_priority = -1
    best_edges = None
    best_nodes = None

    for r in range(1, len(edge_list) + 1):
        for subset in itertools.combinations(edge_list, r):
            total_cost = sum(edge[2] for edge in subset)
            if total_cost > B:
                continue

            H = nx.Graph()
            H.add_nodes_from(G.nodes())
            for u, v, cost in subset:
                H.add_edge(u, v)

            connected = bfs_connected_nodes(H, s)
            benefit = sum(P.get(node, 0) for node in connected if node in D)
            if benefit > best_priority:
                best_priority = benefit
                best_edges = {tuple(sorted((u, v))) for u, v, cost in subset}
                best_nodes = connected
                best_cost = cost

    return best_edges, best_nodes, best_priority,best_cost

