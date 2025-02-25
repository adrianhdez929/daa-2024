import networkx as nx
import heapq

'''
Input:
    G: Grafo que representa la red de calles
    s: Nodo central (origen de distribución)
    D: Conjunto de nodos que son zonas de desastre (por ejemplo, {'a', 'b', 'c'})
    P: Diccionario con las prioridades asignadas a cada zona de desastre,
    por ejemplo, {'a': 5, 'b': 3, 'c': 8}  
    B: Presupuesto total disponible para reparar calles

Output:
    E_repaired: Conjunto de aristas reparadas
    Z: Conjunto de nodos que quedaron conectados a s luego de reparar las calles
'''
def bfs_simulation(start_node, candidate_edge, D, E_repaired, Z, G):
    """
    Realiza un BFS en el subgrafo formado por las aristas ya reparadas
    junto con la arista candidata (que se asume "reparada" para la simulación)
    """
    u, v = candidate_edge
    # Para simular la reparación de la arista candidata, se agrega al conjunto temporalmente
    simulated_edges = E_repaired.union({tuple(sorted(candidate_edge))})
    visited = set()
    queue = [v]
    reachable = set()

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            reachable.add(node)
            for neighbor in G.neighbors(node):
                edge = tuple(sorted((node, neighbor)))
                if edge in simulated_edges:
                    queue.append(neighbor)
    # También se incluye el nodo v si es zona de desastre
    if v in D and v not in Z:
        reachable.add(v)
    return reachable

def greedy_repair_algorithm(G, s, D, P, B):
    """
    - Se inicia con Z = {s} y un presupuesto B.
    - Se construye una cola de prioridad con las aristas de "frontera" 
    evaluadas por la razón (beneficio marginal / costo).
    - Se selecciona la arista de mayor razón
    - Se actualiza E_repaired, Z, y el presupuesto; luego se agregan
    nuevas aristas de frontera.
    - El proceso se repite hasta agotar la frontera o el presupuesto.
    """
    Z = {s}                   # Nodos conectados
    E_repaired = set()        # Aristas reparadas 
    budget_remaining = B
    frontier = []             # Cola de prioridad: ( -razon, costo, (u,v), nodos alcanzados)    
    # Inicializa la frontera para todas las aristas que salen de s
    for v in G.neighbors(s):
        if v in Z:
            continue
        cost = G[s][v]['cost']
        if cost > budget_remaining:
            continue
        # Simula el resultado de reparar la arista (s, v)
        reachable = bfs_simulation(s, (s, v), E_repaired, Z, G)
        benefit = sum(P.get(node, 0) for node in reachable if node in D and node not in Z)
        ratio = benefit / cost if cost != 0 else float('inf')
        heapq.heappush(frontier, (-ratio, cost, (s, v), reachable))

    while frontier and budget_remaining > 0:
        neg_ratio, cost, edge, reachable = heapq.heappop(frontier)
        u, v = edge
        # Si ambos extremos ya se encuentran en Z, descartar la arista
        if u in Z and v in Z:
            continue
        new_node = v if v not in Z else u
        if cost > budget_remaining:
            continue

        # Repara la arista y actualiza presupuesto
        E_repaired.add(tuple(sorted(edge)))
        budget_remaining -= cost
        # Actualiza el conjunto de nodos conectados Z usando la simulación
        Z.update(reachable)
        Z.add(new_node)

        # Agrega a la frontera las aristas que salen de los nuevos nodos
        for node in list(reachable.union({new_node})):
            for neighbor in G.neighbors(node):
                if neighbor in Z:
                    continue
                candidate_edge = (node, neighbor)
                candidate_cost = G[node][neighbor]['cost']
                if candidate_cost > budget_remaining:
                    continue
                # Simula la reparación de candidate_edge(arista candidata)
                candidate_reachable = bfs_simulation(node, candidate_edge, E_repaired, Z, G)
                candidate_benefit = sum(
                    P.get(n,0) for n in candidate_reachable 
                    if n in D and n not in Z
                )
                candidate_ratio = candidate_benefit / candidate_cost 
                if candidate_cost == 0:
                    candidate_ratio = float('inf')
                heapq.heappush(
                    frontier, 
                    (-candidate_ratio, candidate_cost, candidate_edge, candidate_reachable)
                )
                
    return E_repaired, Z
