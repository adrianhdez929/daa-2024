import sys
from scipy.sparse.csgraph import floyd_warshall
from itertools import combinations, product
from typing import List, Tuple, Dict, Set


def brute_force_hfvrp(F: List[List[Tuple[int, int]]], D: List[int], M: List[List[int]]) -> Tuple[Dict[int, Set[int]], bool]:
    num_depots = len(F)
    num_clients = len(D)
    best_solution = None
    best_cost = float('inf')
    
    def calculate_total_cost(depot_assignments: Dict[int, Set[int]]) -> float:
        total_cost = 0
        
        for depot, clients in depot_assignments.items():
            if not clients:
                continue
                
            depot_needs = sum(D[client - num_depots] for client in clients)
            
            fleet = F[depot]
            total_capacity = sum(cap for cap, _ in fleet)
            if depot_needs > total_capacity:
                return float('inf')
            
            distance_cost = sum(M[depot][client] for client in clients)
            total_cost += distance_cost
            
        return total_cost
    
    for partition_size in range(1, num_depots + 1):
        for client_groups in combinations(range(num_clients), partition_size):
            depot_indices = range(num_depots)
            for depot_assignment in product(depot_indices, repeat=len(client_groups)):
                current_assignment = {i: set() for i in range(num_depots)}
                
                for group_idx, depot_idx in enumerate(depot_assignment):
                    client_idx = client_groups[group_idx]
                    current_assignment[depot_idx].add(client_idx + num_depots)
                
                cost = calculate_total_cost(current_assignment)
                
                if cost < best_cost:
                    best_cost = cost
                    best_solution = current_assignment
    
    return best_solution or {}, best_solution is not None

'''
Input
F: conjunto de flotas: F[i] = (c, d), asumimos que F[i] esta ordenado bajo 
el criterio de F[i] >= F[j] si y solo si ci/di >= cj/dj, o sea, la capacidad es mayor que el consumo 
D: conjunto de zonas: D[i] = q
M: matriz de distancia, donde los primeros k nodos representan las sucursales 
y los restantes las zonas de desastre, con k = len(F)

Output
A: diccionario de asignacion, donde las llaves son las sucursales y el valor es la asignacion de los caminos de dicha sucursal
b: bool que representa si se existe una asignacion válida o no
'''

def assign_routes(F, D, M):
    # se calculan las distancias minimas entre los nodos, 
    # asi como las rutas y fuentes de los caminos de costo minimo utilizando 
    # floyd_warshall
    distances, predecessors = floyd_warshall(csgraph=M, directed=False, return_predecessors=True)
    # key = zona
    # value = sucursal
    depot_assign = {}
    # dict que contiene las rutas de cada asignacion
    paths = {}
    # dict que contiene el costo de las demandas de las zonas de la ruta
    path_cost = {}
    # lista que contiene la suma para cada sucursal, la suma de los valores de su respectiva flota
    depot_fleet = [(sum([v[0] for v in f]), sum([v[1] for v in f])) for f in F]
    # a cada zona se le asocia su sucursal mas cercana

    for i in range(len(F), len(F) + len(D)):
        min_dist = sys.float_info.max
        closest_depot = 0

        for s in range(len(F)):
            dist = distances[s][i]
            if dist < min_dist:
                min_dist = dist
                closest_depot = s
        depot_assign[i - len(F)] = closest_depot

    # formamos los conjuntos de zonas que debe proveer cada sucursal para calcular el costo
    p = [[] for _ in range(len(F))]
    
    for i, j in depot_assign.items():
        p[j].append(i)
    
    for i, path in enumerate(p):
        paths[i] = path

    # por cada ruta se le calcula el costo total y se verifica si su sucursal 
    # puede encargarse de proveer dicha demanda
    for depot, path in paths.items():
        path_cost[depot] = sum([D[i] if i >= len(F) else 0 for i in path])    
        # si el costo de la ruta es mayor que la capacidad de la flota de la sucursal 
        # entonces se cambia con la sucursal mas cercana que tenga una flota capaz de 
        # encargarse de la demanda
        if path_cost[depot] > depot_fleet[depot][0]:
            closest_depots = [i for i in range(len(F))]
            closest_depots.sort(key=lambda x: distances[depot, x])

            valid_depot = False

            for closest in closest_depots:
                if depot_fleet[closest][0] >= path_cost[depot]:
                    temp = paths[depot]
                    paths[depot] = paths[closest]
                    paths[closest] = temp
                    break
            if not valid_depot:
                return {}, False
    return paths, True
